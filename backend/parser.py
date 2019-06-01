import sys
import os

from pymongo import MongoClient

import socials.vk.parser as vk

from settings import PUBLICS_LIST_FILE, MONGO_DB, MONGO_COLLECTION 

PARSERS = {
    'vk': vk
}

mongo_client = MongoClient()
mongo_db = mongo_client[MONGO_DB]
mongo_posts_collection = mongo_db[MONGO_COLLECTION]


def load_publics_list(filename):
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            try:
                social, public = line.split(':')
            except ValueError:
                raise Exception(f'Incorrect publics list file format at line {i}')

            social, public = social.strip(), public.strip()

            yield (social, public) 

def save_post(social, date, text, images, videos, links, fullname, username, user_photo): 
    mongo_posts_collection.insert_one({
        'social': social, 
        'date': date,
        'text': text,
        'images': images,
        'videos': videos,
        'links': links,
        'fullname': fullname,
        'username': username,
        'user_photo': user_photo
    })

def clean_old_posts():
    mongo_posts_collection.delete_many({})

if __name__ == '__main__':
    publics_list = load_publics_list(PUBLICS_LIST_FILE)

    clean_old_posts()

    for social, public in publics_list:
        try:
            parser = PARSERS[social]
        except KeyError:
            raise Exception(f'No parser for social: {social}')

        public_info = parser.get_public_info(public)
        posts = parser.get_posts(public)

        for post in posts:
            text, date, images, links, videos = post['text'], post['date'], post['images'], post['links'], post['videos']
            fullname = public_info['name']
            username = public_info['username']
            user_photo = public_info['photo']

            if len(images) != 0 or len(videos) != 0:
                save_post(
                    social=social,
                    text=text,
                    date=date,
                    images=images,
                    videos=videos,
                    links=links,
                    fullname=fullname,
                    username=username,
                    user_photo=user_photo
                )
                
    