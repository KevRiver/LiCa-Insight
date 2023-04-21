import paho.mqtt.client as mqtt

# MQTT subscriber 생성
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# subscriber 실행
subscriber.connect("localhost", 1883)
subscriber.loop_forever()