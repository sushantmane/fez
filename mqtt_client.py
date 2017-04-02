import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc))

	client.publish("/sushant", payload="ON", qos=1, retain=True)

def on_message(client, userdata, msg):
	print(msg.topic + " " + str(msg.payload))
	print("OKK!")

client = mqtt.Client(client_id="PUB-SUSHANT-YU", clean_session=False, userdata=None)
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.56.198", 1883, 60)
client.loop_forever()
client.disconnect()
