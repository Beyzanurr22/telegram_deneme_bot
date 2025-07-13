import requests
import time

TOKEN = "7696415713:AAGbHJKYEZVUNtSdMD95Mv7DU4WbiLZVONk"  # Buraya BotFather'dan aldığın tokeni yaz

API_URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    params = {'timeout': 5, 'offset': offset}
    try:
        response = requests.get(API_URL + 'getUpdates', params=params)
        data = response.json()
        print("Gelen API cevabı:", data)
        return data
    except requests.exceptions.RequestException as e:
        print("İstek hatası:", e)
        return None

def send_message(chat_id, text):
    params = {'chat_id': chat_id, 'text': text}
    try:
        requests.post(API_URL + 'sendMessage', data=params)
    except requests.exceptions.RequestException as e:
        print("Mesaj gönderme hatası:", e)

def main():
    offset = None
    print("Bot çalışıyor...")
    while True:
        updates = get_updates(offset)
        if updates and 'result' in updates:
            for update in updates['result']:
                offset = update['update_id'] + 1
                message = update.get('message')
                if message:
                    chat_id = message['chat']['id']
                    text = message.get('text')
                    print(f"Gelen mesaj: {text}")
                    send_message(chat_id, f"Mesajınız alındı: {text}")
        time.sleep(1)

if __name__ == "__main__":
    main()