import paho.mqtt.client as mqtt
import time
import json
import random

BROKER = "broker.hivemq.com"
PORT = 1883

DEVICES = ["sensor01", "sensor02"]


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
            for device_id in DEVICES:
                topic = f"iot/lab/{device_id}/data"
                temperature = round(random.uniform(20.0, 40.0), 1)
                humidity = round(random.uniform(30.0, 90.0), 1)

                data = {
                    "device_id": device_id,
                    "temperature": temperature,
                    "humidity": humidity
                }
                payload = json.dumps(data)

                client.publish(topic, payload)
                print(f"[{topic}] Da gui:", payload)

            time.sleep(3)
    except KeyboardInterrupt:
        print("\nDung chuong trinh")
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()