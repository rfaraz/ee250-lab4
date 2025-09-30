"""EE 250L Lab 04 Starter Code
Starter code taken from vm_sub.py"""

# Team Members: Rida Faraz, Leyaa George
# Github Repo: https://github.com/rfaraz/ee-250-lab3.git

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """
def on_connect(client, userdata, flags, rc):
    client.subscribe("faraz/ping")
    client.message_callback_add("faraz/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
    num = int(message.payload.decode())
    print("Ping callback - Num: ", num)

    # Increment and send back to pong subscriber
    time.sleep(1)
    client.publish("faraz/pong", str(num + 1))
    print("Ping callback - Sent pong")

if __name__ == '__main__':

    #create a client object
    client = mqtt.Client()
    
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect
    """Connect using the following hostname, port, and keepalive interval (in 
    seconds). We added "host=", "port=", and "keepalive=" for illustrative 
    purposes. You can omit this in python.
        
    The keepalive interval indicates when to send keepalive packets to the 
    server in the event no messages have been published from or sent to this 
    client. If the connection request is successful, the callback attached to
    `client.on_connect` will be called."""

    client.connect(host="172.20.10.2", port=1883, keepalive=60)

    """ask paho-mqtt to spawn a separate thread to handle
    incoming and outgoing mqtt messages."""
    client.loop_forever()
