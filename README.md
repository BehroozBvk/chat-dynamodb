## Installation

**_Step 1:_**

```bash
python3 -m venv .venv
```

**_Step 2:_**

```bash
source ./.venv/bin/active
```

**_Step 3:_**

```bash
pip3 install -r requrements.txt -t ./.venv/lib/python3.11/site-packages
```

**_Step 4:_**

```bash
python3 server.py
```


## run multiply client:

**client1:**

```bash
python3 client.py
```

**client2:**

```bash
python3 client.py
```
**Demo**
![image](https://github.com/BehroozBvk/chat-dynamodb/assets/17563730/f0eb13de-9657-469e-8987-fe01c8e5ae77)


Finally, enter the ID of the client you want to send a message to and then type and send your message.


<br>

>Note: If you want to send a message to all existing users, just enter the value -1 and the message will be sent to all users.
