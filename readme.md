# BÀI THỰC HÀNH 1 — LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

## 1. Thông tin sinh viên

| STT | Họ tên | MSSV |
|---|---|---|
| 1 | Trương Đình Hoàng Vũ | B23DCCN949 |
| 2 | Dương Đức Thành | B23DCCN767 |
| 3 | Vũ Minh Quang | B23DCCN697 |

| Thông tin | Nội dung |
|---|---|
| Lớp | B23DCCN |
| Môn | IoT |
| Buổi thực hành | Buổi 1 — Python với MQTT |

## 2. Môi trường

- Python 3.x
- Thư viện: `paho-mqtt`

Cài đặt:

```bash
pip install paho-mqtt
```

## 3. MQTT Broker sử dụng

| Thông số | Giá trị |
|---|---|
| Broker | `broker.hivemq.com` |
| Port | `1883` |
| Giao thức | MQTT (không TLS) |

Đây là broker public, không cần cài đặt hay đăng ký.
Có thể đổi sang `test.mosquitto.org` hoặc `broker.emqx.io` nếu broker chính bị chậm.

## 4. Cấu trúc thư mục

```
Code/
├── publisher_bai1.py            # Bài 1 — Publisher
├── subscriber_bai1.py           # Bài 1 — Subscriber
├── sensor_publisher_bai2.py     # Bài 2 — Sensor publisher
├── monitor_subscriber_bai2.py   # Bài 2 — Monitoring subscriber
├── device_bai3.py               # Bài 3 — Smart light device
├── controller_bai3.py           # Bài 3 — Controller app
└── README.md
```

## 5. Cách chạy từng chương trình

### Bài 1 — Gửi và nhận thông điệp MQTT cơ bản

Topic sử dụng: `iot/lab/message`

**Terminal 1 — Subscriber:**
```bash
python subscriber_bai1.py
```

**Terminal 2 — Publisher:**
```bash
python publisher_bai1.py
```

Publisher gửi thông điệp mỗi 5 giây, subscriber in ra Topic / Payload / Time.
Subscriber chạy liên tục đến khi nhấn `Ctrl+C`.

### Bài 2 — Mô phỏng cảm biến nhiệt độ và độ ẩm

Topic sử dụng: `iot/lab/sensor01/data`, `iot/lab/sensor02/data`

**Terminal 1 — Monitoring subscriber:**
```bash
python monitor_subscriber_bai2.py
```

**Terminal 2 — Sensor publisher:**
```bash
python sensor_publisher_bai2.py
```

Publisher gửi dữ liệu JSON mỗi 3 giây cho `sensor01` và `sensor02`.
Subscriber lắng nghe topic `iot/lab/+/data`, in dữ liệu và cảnh báo:

- Nhiệt độ > 35°C → `CANH BAO: Nhiet do cao`
- Độ ẩm < 40% → `CANH BAO: Do am thap`

### Bài 3 — Điều khiển đèn thông minh qua MQTT

Topic sử dụng:

| Topic | Vai trò |
|---|---|
| `iot/lab/light01/cmd` | Controller gửi lệnh ON / OFF |
| `iot/lab/light01/status` | Device phản hồi trạng thái |

**Terminal 1 — Device (chạy trước):**
```bash
python device_bai3.py
```

**Terminal 2 — Controller:**
```bash
python controller_bai3.py
```

Nhập `ON`, `OFF` để điều khiển đèn. Nhập `EXIT` để thoát.

#### 5.3.1. Mở rộng — Mô phỏng nhiều thiết bị

Để mô phỏng nhiều thiết bị như `light01`, `fan01`, `pump01`, làm theo các bước:

**Bước 1:** Copy file `device_bai3.py` thành nhiều file, mỗi file tương ứng một thiết bị:
```
device_bai3_light01.py
device_bai3_fan01.py
device_bai3_pump01.py
```

**Bước 2:** Trong mỗi file, đổi biến `DEVICE_ID` cho đúng thiết bị:
- `DEVICE_ID = "light01"`
- `DEVICE_ID = "fan01"`
- `DEVICE_ID = "pump01"`

**Bước 3:** Mở nhiều terminal, mỗi terminal chạy một device:
```bash
python device_bai3_light01.py
python device_bai3_fan01.py
python device_bai3_pump01.py
```

**Bước 4:** Sửa `controller_bai3.py` để điều khiển nhiều thiết bị:
- Cho phép nhập lệnh theo cú pháp `<device> <ON|OFF>`, ví dụ: `light01 ON`, `fan01 OFF`.
- Subscribe topic `iot/lab/+/status` để nhận trạng thái của tất cả thiết bị.

**Bước 5:** Chạy controller và nhập lệnh theo cú pháp mới:
```
Nhap lenh: light01 ON
Nhap lenh: fan01 OFF
Nhap lenh: pump01 ON
```

## 6. Kết quả đạt được

### Bài 1

Publisher:
```
Da ket noi toi MQTT broker
Da gui: Xin chao tu client Python MQTT - B23DCCN949 - Truong Dinh Hoang Vu
```

Subscriber:
```
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN949 - Truong Dinh Hoang Vu
Time: 10:15:20
```

### Bài 2

Publisher:
```
[iot/lab/sensor01/data] Da gui: {"device_id": "sensor01", "temperature": 28.5, "humidity": 65.2}
[iot/lab/sensor02/data] Da gui: {"device_id": "sensor02", "temperature": 36.1, "humidity": 38.7}
```

Subscriber:
```
Device: sensor02
Temperature: 36.1 C
Humidity: 38.7 %
CANH BAO: Nhiet do cao
CANH BAO: Do am thap
Time: 10:16:05
```

### Bài 3

Controller:
```
Nhap lenh: ON
Da gui lenh ON toi light01
Trang thai nhan duoc: {"device_id": "light01", "status": "ON"}
```

Device:
```
Nhan lenh: ON
Da gui trang thai: {"device_id": "light01", "status": "ON"}
```

### Bài 3 — Mở rộng nhiều thiết bị

Controller:
```
Nhap lenh: light01 ON
Da gui lenh ON toi light01
Trang thai nhan duoc: {"device_id": "light01", "status": "ON"}

Nhap lenh: fan01 OFF
Da gui lenh OFF toi fan01
Trang thai nhan duoc: {"device_id": "fan01", "status": "OFF"}
```

## 7. Ghi chú

- Tất cả chương trình đều dùng chung broker public `broker.hivemq.com`, port `1883`.
- Nếu broker public bị chậm hoặc mất kết nối, đổi sang `test.mosquitto.org` ở cả 2 file tương ứng.
- Thứ tự chạy: **Subscriber / Device trước, Publisher / Controller sau** để tránh mất message.
- Với Bài 3 mở rộng nhiều thiết bị, topic sử dụng wildcard `iot/lab/+/status` ở controller để nhận trạng thái của tất cả thiết bị.