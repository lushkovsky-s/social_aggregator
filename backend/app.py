from pymongo import MongoClient
from flask import Flask, jsonify

from settings import MONGO_DB, MONGO_COLLECTION

app = Flask(__name__)

mongo_client = MongoClient()
mongo_db = mongo_client[MONGO_DB]
mongo_posts_collection = mongo_db[MONGO_COLLECTION]

@app.route('/posts')
def hello_world():
    recent_posts = list(mongo_posts_collection.find({}))

    result = []

    for post in recent_posts:
        video = None

        if len(post['videos']) > 0:
            video = post['videos'][0]

        image = None

        if len(post['images']) > 0:
            image = post['images'][0]
            
        result.append({
            'post_text': post['text'],
            'post_image': image,
            'post_video': video,
            'date': post['date'],
            'social': post['social'],
            'fullname': post['fullname'],
            'username': post['username'],
            'user_photo': post['user_photo']
        })
    
    resp = jsonify(result)
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp