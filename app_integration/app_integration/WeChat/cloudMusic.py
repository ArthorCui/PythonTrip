#coding: utf-8

import os, itchat
from NetEaseMusicApi import interact_select_song


HELP_MSG = u'''\
��ӭʹ��΢������������
������ ��ʾ����
�رգ� �رո���
������ ����������������\
'''

with open('stop.mp3', 'w') as f: pass
def close_music():
    os.startfile('stop.mp3')


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] ==u'�ر�':
        close_music()
        itchat.send(u'�����ѹر�', 'filehelper')
    if msg['Text'] == u'����':
        itchat.send(HELP_MSG, 'filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')


itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()