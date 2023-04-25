import paho.mqtt.client as mqtt
import time

publisher = mqtt.Client()
publisher.connect("70.12.247.164", 1883)

while True:
    publisher.publish("test/topic", "[{}]jigun gae chu maryeopne...".format(time.time()))
    time.sleep(3)
