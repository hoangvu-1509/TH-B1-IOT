import paho.mqtt.client as mqtt
import json
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/+/data"


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

    try:
        data = json.loads(payload)
        device_id = data.get("device_id")
        temperature = data.get("temperature")
        humidity = data.get("humidity")

        print("Device:", device_id)
        print("Temperature:", temperature, "C")
        print("Humidity:", humidity, "%")

        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")

        print("Time:", now)
        print("-" * 40)

    except json.JSONDecodeError:
        print("Payload khong phai JSON hop le:", payload)


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