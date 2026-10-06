import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi toi MQTT broker")
        client.subscribe(TOPIC)
        print("Dang lang nghe topic:", TOPIC)
    else:
        print("Ket noi that bai, ma loi:", rc)


def on_message(client, userdata, msg):
    now = datetime.now().strftime("%H:%M:%S")
    payload = msg.payload.decode("utf-8")

    print("Nhan duoc message:")
    print("Topic:", msg.topic)
    print("Payload:", payload)
    print("Time:", now)
    print("-" * 40)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDung chuong trinh")
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()