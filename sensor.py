import json
import random
import time
import boto3
from datetime import datetime


STREAM_NAME = 'heat_sensor'  
REGION_NAME = 'us-east-1'        


kinesis_client = boto3.client('kinesis', region_name=REGION_NAME)


daily_max_temp = -float('inf')
last_reset_day = datetime.now().day

def generate_weather_data():
    """Hava durumu ve günlük maksimum sıcaklık verisi üretir."""
    global daily_max_temp, last_reset_day
    
    now = datetime.now()
    

        if now.day != last_reset_day:
        daily_max_temp = -float('inf')
        last_reset_day = now.day


    current_temp = round(random.uniform(15.0, 35.0), 2)
    humidity = random.randint(30, 70)
    

    if current_temp > daily_max_temp:
        daily_max_temp = current_temp
    

    data = {
        "sensor_id": "ANK_CANKAYA_WS_01",
        "timestamp": now.isoformat(),
        "metrics": {
            "current_temperature_c": current_temp,
            "daily_max_temperature_c": daily_max_temp,
            "humidity_percentage": humidity
        },
        "status": "HEAT_WAVE_ALERT" if current_temp > 32 else "NORMAL"
    }
    return data

def send_to_kinesis(data):
    """Veriyi AWS Kinesis'e paket olarak gönderir."""
    try:
        response = kinesis_client.put_record(
            StreamName=STREAM_NAME,
            Data=json.dumps(data),
            PartitionKey=data['sensor_id']
        )
        return response
    except Exception as e:
        print(f"AWS Hatası: {e}")
        return None

if __name__ == "__main__":
    print(f"--- {STREAM_NAME} Akisi Baslatildi (Bolge: {REGION_NAME}) ---")
    print("Durdurmak için Ctrl+C tuslarina basin.\n")
    
    try:
        while True:

            weather_data = generate_weather_data()
            

            result = send_to_kinesis(weather_data)
            
            if result:
                seq_no = result.get('SequenceNumber')
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Veri başarıyla gönderildi.")
                print(f"Sıcaklık: {weather_data['metrics']['current_temperature_c']}°C | "
                      f"Günlük Max: {weather_data['metrics']['daily_max_temperature_c']}°C")
                print(f"Sequence No: {seq_no[-10:]}... (başarıyla ulaştı)\n")
            
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nSimülasyon kullanıcı tarafından durduruldu.")
