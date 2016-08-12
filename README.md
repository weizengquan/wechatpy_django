# wechatpy_django

一个用wechatpy包与微信平台接口进行交互的基于Django的平台。
A Django based  project communicating with Wechat platform by using wechatpy package.

## Introduction(介绍)
It's a backend system communicating with Wechat platform.
It uses django as framework and use wechatpy package which encapsulates the Wechat API.

## Installation(安装说明)
1  clone the project source codes into your own folder

```bash
git clone https://github.com/weizengquan/wechatpy_django.git
```
2  in the project, set up python virtual environment, and activate it.(if you did not have virtualenv, install it first)

```bash
cd wechatpy_django    
virtualenv env
source env/bin/activate
```
3  install the dependencies.
```bash
pip install -r requirements.txt
```
4  clone the mysite/settings_secret.py.template and save it as mysite/settings_secret.py
```bash
cd mysite
cp settings_secret.py.template settings_secret.py
then modify the Wechat parameters in this file according to your information.
vi settings_secret.py
```
5  run it with sudo mode (you have to run the server in 80 port, as Wechat platform only allow 80 port to communicate.
```bash
sudo env/bin/python manage.py runserver 0:80
```
6  now you can test it in the Wechat testing platform. By now this system only support text echo.
