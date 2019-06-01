import sys
import os
import json
from pprint import pprint

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests

from .settings import API_VERSION, ACCESS_TOKEN, WALL_PARSE_POSTS_COUNT

def parse_post(post):
    text = post['text']
    date = post['date']

    attachments = post.get('attachments', [])

    counters = {}

    if 'comments' in post:
        counters['comments'] = post['comments']['count']

    if 'likes' in post:
        counters['likes'] = post['likes']['count']

    if 'reports' in post:
        counters['reposts'] = post['reposts']['count']

    if 'views' in post:
        counters['views'] = post['views']['count']

    images = []
    links = []
    videos = []

    for attachment in attachments:
        type = attachment['type']

        if type == 'photo':
            if 'sizes' in attachment['photo']: 
                for variation in attachment['photo']['sizes']:
                    if variation['type'] == 'x': # The largest image
                        images.append(variation['url'])
            else:
                images.append(attachment['photo']['photo_604'])

        elif type == 'link': 
            links.append(attachment['link']['url'])

        elif type == 'video':
            owner_id = attachment['video']['owner_id']
            video_id = attachment['video']['id']

            video_url = f'https://vk.com/video{owner_id}_{video_id}'

            embed_src = get_embed_src(video_url)

            if embed_src:
                videos.append(embed_src)

    return {
        'date': date,
        'text': text,
        'images': images,
        'videos': videos,
        'links': links,
        'counters': counters
    }

def api_get(uri, params=None):
    if params is None:
        params = {}

    params['access_token'] = ACCESS_TOKEN
    params['v'] = API_VERSION

    resp = requests.get(f'https://api.vk.com/method/{uri}', params=params)
    resp.raise_for_status()

    resp = resp.json()

    if 'error' in resp:
        pprint(resp)
        raise Exception('VK API Error')

    if not 'response' in resp: 
        pprint(resp)
        raise Exception('Unexpected VK API response: "response" field not found')

    return resp['response']

def get_embed_src(video_url):
    driver = webdriver.Chrome()
    driver.get(video_url)

    youtube_iframe = driver.find_elements_by_xpath('//iframe[contains(@class, "video_yt_player")]')

    if len(youtube_iframe) > 0:
        iframe_src = youtube_iframe[0].get_attribute('src')
        driver.close()

        return iframe_src 

    driver.close()
    return None
    
    import time
    time.sleep(5)

    # Store embed code in clipboard
    copy_btn = driver.find_element_by_css_selector('[data-action=copy_embed_code]')
    driver.execute_script('arguments[0].click()', copy_btn)
    driver.execute_script('var el = document.createElement("input"); el.focus(); document.execCommand("paste"); console.log(el.value);')
    import pyperclip
    s = pyperclip.paste()
    print(s)

    import time
    time.sleep(10)
    assert False

    driver.close()

def resolve_username(username):
    resp = api_get('utils.resolveScreenName', params={'screen_name': username})

    return resp['object_id']

def get_public_info(public):
    resp = api_get('groups.getById', params={'group_id': public})

    name = resp[0]['name']
    username = resp[0]['screen_name']
    photo = resp[0]['photo_200']

    return {
        'name': name,
        'username': username,
        'photo': photo
    }

def get_posts(public):
    try:
        public_id = int(public)
    except ValueError:
        public_id = -int(resolve_username(public))

    resp = api_get('wall.get', params={'owner_id': public_id, 'count': WALL_PARSE_POSTS_COUNT})

    items = resp['items']

    for item in items:
        try:
            yield parse_post(item)
        except Exception as e:
            pprint(item)
            raise e


if __name__ == '__main__':
    assert len(sys.argv) >= 2, f'Using: python {sys.argv[0]} <resolve_username|get_posts|public_info>'
    _, command, *_ = sys.argv

    if command == 'resolve_username':
        assert len(sys.argv) == 3, f'Using: python {sys.argv[0]} {sys.argv[1]} USERNAME'
        _, _, username = sys.argv

        public_id  = resolve_username(username)
        print(public_id)
    
    elif command == 'get_posts':
        assert len(sys.argv) == 3, f'Using: python {sys.argv[0]} {sys.argv[1]} PUBLIC'
        _, _, public = sys.argv

        posts = get_posts(public)
        json_version = json.dumps(list(posts))
        print(json_version)

    elif command == 'public_info':
        assert len(sys.argv) == 3, f'Using: python {sys.argv[0]} {sys.argv[1]} PUBLIC'
        _, _, public = sys.argv

        info = get_public_info(public)
        pprint(info)
