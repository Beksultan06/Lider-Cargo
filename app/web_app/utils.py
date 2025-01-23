import requests

def process_barcode_data(barcode_data, barcode_type):
    print(f"Штрих-код: {barcode_data}, Тип: {barcode_type}")
    if barcode_type == "QRCODE":
        print("Это QR-код.")
        try:
            server_url = f"http://127.0.0.1:8000/web_app/redirect/{barcode_data}/"
            response = requests.get(server_url)
            if response.status_code == 200:
                print("Данные успешно отправлены на сервер.")
            else:
                print(f"Ошибка при отправке: {response.status_code}")
        except Exception as e:
            print(f"Ошибка соединения с сервером: {e}")
