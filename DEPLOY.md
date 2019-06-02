# Deploy

Deploy scheme: app <=> uWSGI <=(socket)=> nginx <=> client

## Create service file
```
sudo vim /etc/systemd/system/posts_parser_backend.service
```
You can use nano/emacs or whatever editor your prefrere

```
[Unit]
Description=Posts parser backend service (flask<=>uwsgi)

[Service]
User=your-user
Group=your-group
WorkingDirectory=/path/to/project/backend/
ExecStart=/path/to/project/backend/.env/bin/uwsgi --ini uwsgi.ini
```

Run the service:
```
systemctl start posts_parser_backend
```

## Create nginx configuration

Add the new configuration:
```
server {
    server_name your.api.domain;
    
    location / {
        include uwsgi_params;
        uwsgi_pass unix:/path/to/project/backend/uwsgi.sock
    }
}
```

Check on errors:
```
nginx -t
```

Restart nginx (and apply changes):
```
systemctl restart nginx
```