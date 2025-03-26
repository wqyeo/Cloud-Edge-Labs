import paho.mqtt.client as mqtt
import base64
import cv2
import numpy as np

MQTT_BROKER = "192.168.254.106"
TOPIC_PUBLISH = "capture/image"
TOPIC_SUBSCRIBE = "image/data"

# MQTT Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    client.subscribe(TOPIC_SUBSCRIBE)
    client.publish(TOPIC_PUBLISH, "capture")

def on_message(client, userdata, msg):
    print("Image received!")
    
    # Decode image
    image_data = base64.b64decode(msg.payload)
    np_arr = np.frombuffer(image_data, dtype=np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    
    # Show Image
    cv2.imshow("Received Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# MQTT Client Setup
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER, 1883, 60)

client.loop_forever()
