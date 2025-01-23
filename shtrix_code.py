import cv2
import numpy as np
from pyzbar.pyzbar import decode

def process_barcode_data(barcode_data, barcode_type):
    print(f"Штрих-код: {barcode_data}, Тип: {barcode_type}")
    # Пример анализа типа данных
    if barcode_type == "EAN13":
        print("Это штрих-код товара (EAN-13).")
        # Вы можете добавить здесь запрос к базе данных товаров или API
    elif barcode_type == "QRCODE":
        print("Это QR-код.")
        if barcode_data.startswith("http"):
            print(f"Ссылка: {barcode_data}")
        else:
            print(f"Текст: {barcode_data}")
    else:
        print(f"Неизвестный тип данных: {barcode_type}")

def read_barcode_from_camera():
    # Открываем веб-камеру
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Распознаем штрих-коды на текущем кадре
        barcodes = decode(frame)

        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Обрабатываем данные штрих-кода
            process_barcode_data(barcode_data, barcode_type)

            # Рисуем прямоугольник вокруг штрих-кода
            points = barcode.polygon
            if points:
                pts = [(point.x, point.y) for point in points]
                pts = np.array(pts, dtype=np.int32)
                cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

            # Добавляем текст с данными штрих-кода
            cv2.putText(frame, f"{barcode_data} ({barcode_type})",
                        (barcode.rect.left, barcode.rect.top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Отображаем кадр
        cv2.imshow("Barcode Scanner", frame)

        # Нажмите "q" для выхода
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Пример использования
read_barcode_from_camera()
