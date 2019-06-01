# Parsers console usage

## VK

### Resolve community ID

Resolve community username to id

**Run**:
```
cd backend
python -m socials.vk.parser resolve_username YOUR_PUBLIC_USERNAME
```

**Result** (example):
```
69062504
```

### Get community posts

Get community posts (print JSON to console)

**Run**:
```
cd backend 
python -m socials.vk.parser get_posts YOUR_PUBLIC_USERNAME_OR_ID
```

**Result** (example):
```
[..., {"date": 1295293112, "text": "Jimm Beamm \u043f\u0440\u0438\u0433\u043b\u0430\u0448\u0430\u0435\u0442...", "images": ["https://..."], "links": ["https://..."], "counters": {"comments": 2, "likes": 5}}... 
```

### Get public info

Get public name, username, photo

**Run**:
```
cd backend
python -m socials.vk.parser public_info PUBLIC_USERNAME
```

**Result** (example):
```
{'name': 'Абитуриенты Первого МГМУ им.И.М. Сеченова',
 'photo': 'https://sun1-23.userapi.com/c850620/v850620109/113595/1qoM45fldIo.jpg?ava=1',
 'usernmae': 'abiturient_mgmu'}
```