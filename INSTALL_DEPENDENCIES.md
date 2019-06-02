# Dependencies istall

## Fronend

**Yarn** 

```
cd frontend 
yarn install
```

**NPM**
```
cd frontend 
npm install
```

## Backend

**Without virtualenv** (in global environment)
```
cd backend
pip install -r requirements.txt
```

**virtualenv**
```
cd backend
python3.6 -m venv .venv
source .venv/bin/activate
pip3.6 install -r requirements.txt
```

**virtualenvwrapper**
```
cd backend
mkvirtualenv posts-parser
workon posts-parser
pip3.6 install -r requirements.txt
```
