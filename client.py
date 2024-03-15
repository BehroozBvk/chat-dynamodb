from dotenv import load_dotenv
import websocket
import threading
import os

load_dotenv() 

HOST = os.getenv('WS_HOST')
PORT = int(os.getenv('WS_PORT'))


def on_message(ws, message):
    print("\nReceived: " + message)

def on_error(ws, error):
    print("Error: " + str(error))

def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    def run():
        while True:
            target_id = input("Enter target client ID (or -1 for broadcasting): ")
            message = input("Enter message: ")
            if message:
                if target_id.strip() == '-1':
                    ws.send(message)
                else:
                    ws.send(target_id.strip() + ':' + message)
    threading.Thread(target=run).start()

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"ws://{HOST}:{PORT}/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
