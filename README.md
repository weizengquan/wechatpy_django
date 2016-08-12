# wechatpy_django

一个用wechatpy包与微信平台接口进行交互的基于Django的平台。
A Django based  project communicating with Wechat platform by using wechatpy package.

## Usage(使用说明)
1. git clone https://github.com/weizengquan/wechatpy_django.git
2. cd wechatpy_django    
3. virtualenv env   (if you did not have virtualenv, install it first)
4. source env/bin/activate
5. pip install -r requirements.txt
6. clone the mysite/settings_secret.py.template and save it as mysite/settings_secret.py
   then modify the Wechat parameters in this file according to your information.
7. run it with sudo mode (you have to run the server in 80 port, as Wechat platform only allow 80 port to communicate.
   sudo env/bin/python manage.py runserver 0:80
8. now you can test it in the Wechat testing platform. By now this system only support text echo.
