import serial
import time

# Налаштування серійного порту
SERIAL_PORT = "COM6"  # Замініть на ваш порт, наприклад, /dev/ttyUSB0 для Linux
BAUD_RATE = 115200    # Швидкість передачі даних

def read_serial_data():
    try:
        # Підключення до серійного порту
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
            
            # Безкінечний цикл для зчитування даних
            while True:
                if ser.in_waiting > 0:
                    # Зчитуємо рядок даних
                    data = ser.readline().decode('utf-8').strip()
                    print(f"Received: {data}")
                time.sleep(0.1)
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Terminated by user.")

if __name__ == "__main__":
    read_serial_data()
