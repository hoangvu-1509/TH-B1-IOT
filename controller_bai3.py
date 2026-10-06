import paho.mqtt.client as mqtt
import json

BROKER = "broker.hivemq.com"
PORT = 1883
DEVICE_ID = "light01"

TOPIC_CMD = f"iot/lab/{DEVICE_ID}/cmd"
TOPIC_STATUS = f"iot/lab/{DEVICE_ID}/status"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Da ket noi toi MQTT broker")
        client.subscribe(TOPIC_STATUS)
        print("Dang lang nghe trang thai:", TOPIC_STATUS)
    else:
        print("Ket noi that bai, ma loi:", rc)


def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print("Trang thai nhan duoc:", payload)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("Nhap lenh ON / OFF (go EXIT de thoat)")

    try:
        while True:
            cmd = input("Nhap lenh: ").strip().upper()

            if cmd == "EXIT":
                print("Ket thuc chuong trinh")
                break

            if cmd not in ("ON", "OFF"):
                print("Lenh khong hop le, chi chap nhan ON / OFF")
                continue

            client.publish(TOPIC_CMD, cmd)
            print(f"Da gui lenh {cmd} toi {DEVICE_ID}")

    except KeyboardInterrupt:
        print("\nDung chuong trinh")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()