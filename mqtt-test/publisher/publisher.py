import paho.mqtt.client as mqtt
import time

publisher = mqtt.Client()
publisher.connect("localhost", 1883)

while True:
    publisher.publish("test/topic", "test/topic", "[{}]jigun gae chu maryeopne...".format(time.time()))
    time.sleep(3)