import paho.mqtt.client as mqtt
import time

client = mqtt.Client("Publisher")
client.connect("192.168.254.106", 1883)

while True:
    client.publish("test/topic", "Hello, MQTT!")
    time.sleep(5)
