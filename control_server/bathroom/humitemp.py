import paho.mqtt.client as mqtt
from pymongo import MongoClient
from datetime import datetime
from gpiozero import LED
from time import sleep

hitter = LED(27)
aircon = LED(17)
airdry = LED(22)

# DB연결
mongodb = MongoClient("mongodb://192.168.0.87:27017/")
db = mongodb.full_house

# 브로커 접속 시도 결과 처리 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    if rc == 0:
        client.subscribe("home/bathroom/#") # 연결 성공시 토픽 구독 신청
    else:
        print('연결 실패 : ', rc)
        
# 관련 토픽 메시지 수신 콜백 함수
def on_message(client, userdata, msg):
    value = float(msg.payload.decode())
    print(f" {msg.topic} {value}")
  
    
    # MongoDB에 데이터 저장하는 코드가 여기에서 이루어짐
    if msg.topic == "home/bathroom/humi":
        h = value
        if h > 38:
            airdry.on()
        else:
             airdry.off()   
    
    else :
        t = value
     
        if t > 28:
            hitter.off()
            aircon.on()
            
        elif t < 22:
            hitter.on()
            aircon.off()
            
            
        else:
            hitter.off()
            aircon.off()
           
        
    

        
    
# 1. MQTT 클라이언트 객체 인스턴스화
client = mqtt.Client()

# 2. 관련 이벤트에 대한 콜백 함수 등록
client.on_connect = on_connect
client.on_message = on_message

try :
    # 3. 브로커 연결 / 브로커아이피 입력
    client.connect("192.168.0.93")
    
    # 4. 메시지 루프 - 이벤트 발생시 해당 콜백 함수 호출됨
    client.loop_forever()

    # client.loop_start()
    # 새로운 스래드를 가동해서 운영 - daemon 스레드  Thread.setDaemon(True)
except Exception as err:
	print('에러 : %s'%err)
    
print("--- End Main Thread ---")