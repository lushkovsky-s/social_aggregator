# Установка зависимостей

## Фронтенд

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

## Бекенд

**Без virtualenv** (в глобальное окружение)
```
cd backend
pip install -r requirements.txt
```

**virtualenv**
```
cd backend
python3.6 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**virtualenvwrapper**
```
cd backend
mkvirtualenv twitter-client
workon twitter-client
pip install -r requirements.txt
```
