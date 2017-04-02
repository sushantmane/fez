import paho.mqtt.publish as publish


topic = "/MOTOR"
payload = "ON"
qos = 0
retain = False
hostname = "192.168.56.198"
port = 1883
client_id = "PUB-SUSHANT_YU"
keepalive = 60
will = {'topic': '/MOTOR', 'payload': "Take care!", 'qos': 0}
auth = None
tls = None
protocol = "mqtt.MQTTv311"
transport = "tcp"

publish.single(topic, payload, qos, retain, hostname, port, client_id, keepalive, will, auth, tls, protocol, transport)
