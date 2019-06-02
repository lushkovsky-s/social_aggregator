import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .settings import VIDEO_PAGE_LOADING_TIMEOUT
from . import exceptions as exc

def get_embed_youtube(driver):
    youtube_iframe = driver.find_elements_by_xpath('//iframe[contains(@class, "video_yt_player")]')

    iframe_src = youtube_iframe[0].get_attribute('src')
    return iframe_src 

def is_youtube_embed(driver):
    return len(driver.find_elements_by_xpath('//iframe[contains(@class, "video_yt_player")]')) > 0

def is_vk_embed(driver):
    return len(driver.find_elements_by_css_selector('[data-action=copy_embed_code]')) > 0

def get_embed_vk(driver):
    iframe_code = driver.execute_async_script('''
        var done = arguments[0]
        document.addEventListener('DOMNodeInserted', (ev) => {
            done(ev.target.value); 
        })
        document.querySelector('[data-action=copy_embed_code]').click()
    ''')

    iframe_src = re.search(r'src="([^ ]+)"', iframe_code).group(1)

    return iframe_src

def get_embed_src(video_url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu') 
    options.add_argument('--no-sandbox') # Required to run the script as a root

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(video_url)

    time.sleep(VIDEO_PAGE_LOADING_TIMEOUT)

    if is_youtube_embed(driver):
        src = get_embed_youtube(driver)
    elif is_vk_embed(driver):
        src = get_embed_vk(driver)
    else:
        driver.close()
        raise exc.VideoParsingError(f'Unsupported video embedding: {video_url}')

    driver.close()

    return src     
