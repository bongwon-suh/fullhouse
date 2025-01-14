import paho.mqtt.client as mqtt
import time
from pymongo import MongoClient
from datetime import datetime
from gpiozero import LED
import RPi.GPIO as GPIO

mongodb = MongoClient("mongodb://192.168.0.85:27017/")
db = mongodb.full_house

led = LED(16)
SERVO_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
blind = GPIO.PWM(SERVO_PIN, 50)
blind.start(0)

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    if rc == 0:
        client.subscribe("iot/livingroom/illu") # 연결 성공시 토픽 구독 신청
    else:
        print('연결 실패 : ', rc)

# 관련 토픽 메시지 수신 콜백 함수
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f" {msg.topic} {value}")
    
    # 블라인드 동작 제어
    if value < 15: # 어두울 때
        led.on()
        blind.ChangeDutyCycle(7.5) # 90도
    elif value >= 30: # 밝을 때
        led.off()
        blind.ChangeDutyCycle(12.5) # 180도

    

# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try :
    # 3. 브로커 연결
    client.connect("192.168.0.92")
    
    # 4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
    client.loop_forever()
    # client.loop_start()  # 데몬 스레드(새로운 스레드를 가용)
except Exception as err:
    print('에러 : %s'%err)

print("... end Main Thread")


# 서브를 할때 동작이 제어되는 부분은 17번 라인 on_message를 어떻게 정의하느냐에 따라
# db등록 또는 led제어 코드 구성
# 브로커 서버가 localhost -> 라즈베리파이ip
