#coding=utf-8

import itchat
# tuling plugin can be get here:
# https://github.com/littlecodersh/EasierLife/tree/master/Plugins/Tuling
from tuling import get_response

@itchat.msg_register('Text')
def text_reply(msg):
    if u'����' in msg['Text'] or u'����' in msg['Text']:
        return u'������������˽�����https://github.com/littlecodersh'
    elif u'Դ����' in msg['Text'] or u'��ȡ�ļ�' in msg['Text']:
        itchat.send('@fil@main.py', msg['FromUserName'])
        return u'��������ڻ����˺�̨�Ĵ��룬�ǲ��Ǻܼ��أ�'
    elif u'��ȡͼƬ' in msg['Text']:
        itchat.send('@img@applaud.gif', msg['FromUserName']) # there should be a picture
    else:
        return get_response(msg['Text']) or u'�յ���' + msg['Text']

@itchat.msg_register(['Picture', 'Recording', 'Attachment', 'Video'])
def atta_reply(msg):
    return ({ 'Picture': u'ͼƬ', 'Recording': u'¼��',
        'Attachment': u'����', 'Video': u'��Ƶ', }.get(msg['Type']) +
        u'�����ص�����') # download function is: msg['Text'](msg['FileName'])

@itchat.msg_register(['Map', 'Card', 'Note', 'Sharing'])
def mm_reply(msg):
    if msg['Type'] == 'Map':
        return u'�յ�λ�÷���'
    elif msg['Type'] == 'Sharing':
        return u'�յ�����' + msg['Text']
    elif msg['Type'] == 'Note':
        return u'�յ���' + msg['Text']
    elif msg['Type'] == 'Card':
        return u'�յ�������Ϣ��' + msg['Text']['Alias']

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
    if msg['isAt']:
        return u'@%s\u2005%s' % (msg['ActualNickName'],
            get_response(msg['Text']) or u'�յ���' + msg['Text'])

@itchat.msg_register('Friends')
def add_friend(msg):
    itchat.add_friend(**msg['Text'])
#   itchat.send_msg(u'��Ŀ��ҳ��github.com/littlecodersh/ItChat\n'
#        + u'Դ����  ���ظ�Դ����\n' + u'ͼƬ��ȡ���ظ���ȡͼƬ\n'
#        + u'��ӭStar�ҵ���Ŀ��ע���£�', msg['RecommendInfo']['UserName'])

itchat.auto_login(True, enableCmdQR=True)
itchat.run()