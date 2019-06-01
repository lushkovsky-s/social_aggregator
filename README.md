# Twitter client (aiFactory hometask) 

1. [Установка](#Установка)
2. [Запуск](#Запуск)
3. [Как сделано](#Как-сделано)

## Установка 

### Системные пакеты

Исходим из того, что установлены:
* python (3.6+) и pip 
* nodejs (8+) и yarn/npm  
* mongodb

Проверить наличие пакетов и их версии можно выполнив:
```
python --version && node --version && mongo --version
```

При отсутствии см. [INSTALLL_PREREQUIREMENTS.md](INSTALL_PREREQUIREMENTS.md)

### Пакеты npm и pip

Установить зависимости:
* при помощи yarn/npm в frontend 
* при помощи pip в backend.

см. подробнее в [INSTALL_DEPENDENCIES.md](INSTALL_DEPENDENCIES.md)

--- 

## Запуск

### Фронтенд

```
cd frontend  
yarn start # or: npm start
```

Фронтенд будет запущен на [localhost:8080](http://localhost:8080)

Кроме того, фротенд можно собрать статически:
```
cd frontend
yarn build # or: npm run build
```

### Бекенд
Тестовый сервер:
```
python app.py
```

---

## Console usage

You can use social parsers by it's own, using console interface (see [CONSOLE_USAGE.md](CONSOLE_USAGE.md))

---

## Как сделано

### Фронтенд

Приложение создано при помощи [angular-1.5-cli](https://www.npmjs.com/package/angular-1.5-cli)  
Состоит из: главного компонента (app), директивы поста и сервиса взаимодействия с api  

### Backend

Стек: python3.6, flask, mongo

### Что можно сделать иначе 

* Метод Twitter API GET statuses/oembed может возвращать html для отображения поста (т.е. его можно не верстать руками) 