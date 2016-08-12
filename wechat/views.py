from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

#disable csrf protection for this view
from django.views.decorators.csrf import csrf_exempt

#Import wechatpy dependencies
#from __future__ import absolute_import, unicode_literals
import os
from wechatpy.crypto import WeChatCrypto
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.exceptions import InvalidAppIdException

from django.conf import settings
TOKEN = settings.WECHAT_TOKEN
EncodingAESKey = settings.WECHAT_ENCODING_AES_KEY
AppId = settings.WECHAT_APP_ID


# Create your views here.
def index(request):
    return HttpResponse("Wechat index.")

#use csrf_exempt to disable csrf protection for this view
@csrf_exempt
def echo(request):
    signature = request.GET.get('signature','') + request.POST.get('signature', '')
    timestamp = request.GET.get('timestamp','') + request.POST.get('timestamp', '')
    nonce = request.GET.get('nonce','') + request.POST.get('nonce', '')
    echo_str = request.GET.get('echostr','') + request.POST.get('echostr', '')
    encrypt_type = request.GET.get('encrypt_type','') + request.POST.get('encrypt_type', '')
    msg_signature = request.GET.get('msg_signature','') + request.POST.get('msg_signature', '')


    print('signature:', signature)
    print('timestamp: ', timestamp)
    print('nonce:', nonce)
    print('echo_str:', echo_str)
    print('encrypt_type:', encrypt_type)
    print('msg_signature:', msg_signature)

    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        raise PermissionDenied
    if request.method == 'GET':
        return HttpResponse(echo_str)
    else:
# use request.data in flask
#        print('Raw message: \n%s' % request.data)
# use request.body in django
        print('Raw message: \n%s' % request.body)
        crypto = WeChatCrypto(TOKEN, EncodingAESKey, AppId)
        try:
            msg = crypto.decrypt_message(
                request.body,
                msg_signature,
                timestamp,
                nonce
            )
            print('Descypted message: \n%s' % msg)
        except (InvalidSignatureException, InvalidAppIdException):
            raise PermissionDenied
        msg = parse_message(msg)
        if msg.type == 'text':
            reply = create_reply(msg.content, msg)
        else:
            reply = create_reply('Sorry, can not handle this for now', msg)
        return HttpResponse(crypto.encrypt_message(
            reply.render(),
            nonce,
            timestamp
        ))
