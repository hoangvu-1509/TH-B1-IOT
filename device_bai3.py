import paho.mqtt.client as mqtt
import json

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = "light01"

TOPIC_CMD = f"iot/lab/{DEVICE_ID}/cmd"
TOPIC_STATUS = f"iot/lab/{DEVICE_ID}/status"

status = "OFF"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi toi MQTT broker")
        client.subscribe(TOPIC_CMD)
        print("Dang lang nghe lenh:", TOPIC_CMD)
        publish_status(client)
    else:
        print("Ket noi that bai, ma loi:", rc)


def publish_status(client):
    data = {
        "device_id": DEVICE_ID,
        "status": status
    }
    payload = json.dumps(data)
    client.publish(TOPIC_STATUS, payload)
    print("Da gui trang thai:", payload)


def on_message(client, userdata, msg):
    global status
    payload = msg.payload.decode("utf-8").strip().upper()
    print("Nhan lenh:", payload)

    if payload == "ON":
        status = "ON"
        publish_status(client)
    elif payload == "OFF":
        status = "OFF"
        publish_status(client)
    else:
        print("Lenh khong hop le:", payload)


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