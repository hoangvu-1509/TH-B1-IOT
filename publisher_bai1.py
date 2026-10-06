import paho.mqtt.client as mqtt
import time
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

HO_TEN = "Trương Đình Hoàng Vũ"
MSSV = "B23DCCN949"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi toi MQTT broker")
    else:
        print("Ket noi that bai, ma loi:", rc)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()
    time.sleep(1)

    try:
        while True:
            payload = f"Xin chao tu client Python MQTT - {MSSV} - {HO_TEN}"
            client.publish(TOPIC, payload)
            print("Da gui:", payload)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nDung chuong trinh")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()