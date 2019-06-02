# System packages installation

## Python and pip

[CentOS7](https://janikarhunen.fi/how-to-install-python-3-6-1-on-centos-7)

## Node and npm/yarn

[Install Node on Ubuntu/Debian/CentOS/macOS/Windows and other](https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions-enterprise-linux-fedora-and-snap-packages) 

## MongoDB

[Install on Ubuntu/Debian/CentOS/macOS/Windows](https://docs.mongodb.com/v4.0/installation/#mongodb-community-edition-installation-tutorials)

## Chorme and chromedriver

Open /etc/yum.repos.d/google-chrome.repo (e.g. with vim) and add: 
```
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
```

Run:
```
yum install -y google-chrome-stable
```

Install chromedriver:
```
cd ~
wget https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_linux64.zip 
unzip chromedriver_linux64.zip
mv chromedriver /usr/local/bin/
```


The solution is getted from [this gist](https://gist.github.com/xiaol825/625b94f97c0580c0586ded2b8f0d76e2)

