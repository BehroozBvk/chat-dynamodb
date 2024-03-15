from dotenv import load_dotenv
from boto3 import resource
from boto3.dynamodb.conditions import Attr, Key
from datetime import datetime
import os
import uuid

load_dotenv() 

HOST=os.getenv('WS_HOST')
PORT=int(os.getenv('WS_PORT'))

chat_table = resource('dynamodb').Table('chats')



from websocket_server import WebsocketServer

def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])

def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])

def message_received(client, server, message):
    print("Client(%d) sent: %s" % (client['id'], message))
    parts = message.split(':', 1)
    if len(parts) == 2:
        target_id, private_message = parts
        target_client = next((c for c in server.clients if c['id'] == int(target_id)), None)
        if target_client:
            save(client['id'],target_client['id'],private_message)
            server.send_message(target_client, f"{target_client['id']}: {private_message}")
    else:
        server.send_message_to_all(message)


def save(sender_id,receiver_id,message):
    
    response = chat_table.put_item(
        Item={
                'id': str(uuid.uuid4()),
                'sender_id' : sender_id,
                'receiver_id' : receiver_id,
                'message' : message,
                'status': 'sent',
                'created_at' : datetime.now().isoformat()
            }
        )
    print(f'Save response: {response}') 


server = WebsocketServer(HOST,PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
