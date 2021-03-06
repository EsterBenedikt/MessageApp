from src.message import Message
from src.message_db import message_db
from config import *

class MessageList:

    @staticmethod
    def add_new_message(message):
        try:
            app_id=message['application_id']
            session_id = message['session_id']
            message_id = message['message_id']
            participants=message['participants']
            content=message['content']
        except:
            raise Exception("data not correct")
        new_message=Message(app_id,session_id,message_id,participants,content)

        conn=message_db.create_connection(DATABASE)
        with conn:
            try:
                message = (new_message.application_id, new_message.session_id, new_message.message_id,",".join(new_message.participants), new_message.content)
                message_db.insert_message(conn, message)
            except:
                raise Exception("message_id is alredy exist")

    @staticmethod
    def get_messages(id,value):
        conn = message_db.create_connection(DATABASE)
        with conn:
            res=message_db.select_specific_messages(conn,id,value=value)
        if res:
            for item in res:
                item["participants"]=list(item["participants"].split(','))
        return res

    @staticmethod
    def delete_messages(id,value):
        conn = message_db.create_connection(DATABASE)
        with conn:
            res = message_db.delete_message(conn, id, value=value)
        return  res
