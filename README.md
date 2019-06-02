# Twitter client (aiFactory hometask) 

1. [Install](#Install)
2. [Configuration](#Configuration)
3. [Running](#Running)
4. [Console tools](#Console-tools)
4. [Solution description](#Solution-description)

## Install 

### Systsem packages

Prerequirements:
* python (3.6+) and pip 
* nodejs (8+) and yarn/npm  
* mongodb
* chrome and chromedriver

You can check the packages existance using the command:
```
python --version && node --version && mongo --version
```

If something is miseed see [INSTALLL_PREREQUIREMENTS.md](INSTALL_PREREQUIREMENTS.md)

### Packages from npm and pip

Install and requirements:
* using yarn/npm in frontend 
* using pip in backend

See details in [INSTALL_DEPENDENCIES.md](INSTALL_DEPENDENCIES.md)

--- 

# Configuration

Create/edit `backend/publics_list.txt` using the format: "SOCIAL_NAME: PUBLIC_NAME_OR_ID"  
For example:  
```
vk: bon
vk: abiturient_mgmu
vk: buffrussia
```

---

## Running

### Frontend

```
cd frontend  
yarn start # or: npm start
```

The frontend will be stared at [localhost:8080](http://localhost:8080)

Otherwise, the frontend could be staticly built:
```
cd frontend
export API_URL="api.mywebpage.com"
yarn build # or: npm run build
```
Replace "api.mywebpage.com" with your api URL. By default "http://localhost:5000" will be used. 

### Backend
Test server:
```
python app.py
```

Otherwise you can run the backend using uWSGI or gunicorn. Flask app is fully compatible with both of them.

### Parser
To parse recent posts, run:
```
python parser.py
```

Or if you want to do it periodicly - configure cron (type `crontab -e`) by adding the row:
```
* * * * * /path/to/python /path/to/parsepy/file
```

For example:
```
* 2 * * * /usr/bin/python /var/www/posts/backend/parse.py
```
This configuration will trigger the parser run every day at 2 AM

You can find the complete guide on cron [here (ru)](https://www.shellhacks.com/ru/crontab-format-cron-job-examples-linux/)

---

## Console tools

You can use social parsers by it's own, using console interface (see [CONSOLE_USAGE.md](CONSOLE_USAGE.md))

---

## Solution description

### Frontend

The app is created using the [angular-1.5-cli](https://www.npmjs.com/package/angular-1.5-cli) and contains principals: the mail component (app), post directive and api integration service  

### Backend

Technologies: python3.6, flask, mongo
All posts are stored in database "posts" inside the "recent_posts" collection

### Parser

The current version of the app supports the networks: 

**VK**   
The quite all parsing does by using of [VK API](https://vk.com/dev/manuals).  
But except for getting the video iframe url (for some reason [that method](https://vk.com/dev/video.get) requires user-level access key (as so requires to pass the OAuth proccedure every day)).  
As so, it's been done by using of webpage automation by selenium.   

### What to improve

* Disable chromedriver logging (messages like "DevTools started on..."). Somehow couldn't be disabled with command line arguments or desired capabilities
* Parser logging
* Version-aware chromedriver install guide