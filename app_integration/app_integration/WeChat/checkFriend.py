# coding: utf-8

import itchat


CHATROOM_NAME = 'friend'
CHATROOM = None
HELP_MSG = u'''\����״̬���
* ������Ƭ���᷵�غ���״̬
* ��ȷ����Ϊ%s��δʹ�õ�Ⱥ��
* ������Ⱥ�ı��浽ͨѶ¼
* ����Ƶ�ʴ���һ������\
''' % CHATROOM_NAME
CHATROOM_MSG = u'''\
�޷��Զ�����Ⱥ�ģ����ֶ�����
ȷ��Ⱥ������Ϊ%s
�벻Ҫʹ���Ѿ�ʹ�ù���Ⱥ��
�������뽫Ⱥ�ı��浽ͨѶ¼\
''' % CHATROOM_NAME

def get_chatroom():
    global CHATROOM
    if CHATROOM is None:
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(CHATROOM_NAME)
        if chatrooms:
            return chatrooms[0]
        else:
            r = itchat.create_chatroom(itchat.get_friends()[1:4], topic=CHATROOM_NAME)
            if r['BaseResponse']['ErrMsg'] == '':
                CHATROOM = {'UserName': r['ChatRoomName']}
                return CHATROOM
    else:
        return CHATROOM


def get_friends_status(friend):
    ownAccount = itchat.get_friends(update=True)[0]
    if friend['UserName'] == ownAccount['UserName']:
        return u'��⵽�����˺š�'
    elif itchat.search_friends(userName=friend['UserName']) is None:
        return u'���û�������ĺ����б��С�'
    else:
        chatroom = CHATROOM or get_chatroom()
        if chatroom is None: return CHATROOM_MSG
        r = itchat.add_member_into_chatroom(chatroom['UserName'], [friend])
        if r['BaseResponse']['ErrMsg'] == '':
            status = r['MemberList'][0]['MemberStatus']
            itchat.delete_member_from_chatroom(chatroom['UserName'],[friend])
            return { 3: u'�ú����Ѿ���������������', 4: u'�ú����Ѿ�����ɾ����', }.get(status, u'�ú����Ծ������Ǻ��ѹ�ϵ��')
        else:
            return u'�޷���ȡ����״̬��Ԥ���Ѿ��ﵽ�ӿڵ������ơ�'


@itchat.msg_register(itchat.content.CARD)
def get_friend(msg):
    if msg['ToUserName'] != 'filehelper': return
    friendStatus = get_friends_status(msg['RecommondInfo'])
    itchat.send(friendStatus, 'filehelper')


itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()