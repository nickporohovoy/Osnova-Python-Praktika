# Задача 1. Логирование с использованием нескольких файлов
import logging

# Настройка логгеров
logging.basicConfig(level=logging.DEBUG)
debug_info_handler = logging.FileHandler("debug_info.log")
debug_info_handler.setLevel(logging.DEBUG)
warnings_errors_handler = logging.FileHandler("warnings_errors.log")
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger = logging.getLogger("multi_logger")
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Пример логирования
logger.debug("Это сообщение уровня DEBUG")
logger.info("Это сообщение уровня INFO")
logger.warning("Это сообщение уровня WARNING")
logger.error("Это сообщение уровня ERROR")
logger.critical("Это сообщение уровня CRITICAL")

# Задача 2. Работа с текущим временем и датой
from datetime import datetime

# Получение текущей даты и времени
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
day_of_week = current_datetime.strftime('%A')
week_number = current_datetime.isocalendar()[1]

print(f"Текущая дата и время: {formatted_datetime}")
print(f"День недели: {day_of_week}")
print(f"Номер недели в году: {week_number}")

# Задача 3. Планирование задач
from datetime import timedelta

def get_future_date(days_from_now):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_from_now)
    return future_date.strftime('%Y-%m-%d')

# Пример использования
future_date = get_future_date(10)
print(f"Дата через 10 дней: {future_date}")

# Задача 4. Опции и флаги
import argparse

def task_with_flags():
    parser = argparse.ArgumentParser(description="Скрипт для работы с числом и строкой с опциями.")
    parser.add_argument("number", type=int, help="Число для обработки.")
    parser.add_argument("text", type=str, help="Строка для вывода.")
    parser.add_argument("--verbose", action="store_true", help="Вывод дополнительной информации о процессе.")
    parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки в выводе (по умолчанию 1).")

    args = parser.parse_args()

    if args.verbose:
        print("Включен режим подробного вывода.")
        print(f"Получено число: {args.number}")
        print(f"Получена строка: {args.text}")
        print(f"Количество повторений: {args.repeat}")

    for _ in range(args.repeat):
        print(args.text)

# Задача 5. Запуск из командной строки
import os
from collections import namedtuple

def collect_directory_info(directory_path):
    FileInfo = namedtuple("FileInfo", ["name", "extension", "is_directory", "parent"])

    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь не является директорией: {directory_path}")

    directory_contents = []

    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        name, extension = os.path.splitext(entry)

        info = FileInfo(
            name=name,
            extension=extension.lstrip(".") if not os.path.isdir(entry_path) else "",
            is_directory=os.path.isdir(entry_path),
            parent=os.path.basename(directory_path),
        )

        logging.info(f"Обработан объект: {info}")
        directory_contents.append(info)

    return directory_contents

def main_task5():
    parser = argparse.ArgumentParser(description="Скрипт для сбора информации о содержимом директории.")
    parser.add_argument("directory", type=str, help="Путь до директории.")
    args = parser.parse_args()

    try:
        contents = collect_directory_info(args.directory)
        print("Информация о содержимом директории:")
        for item in contents:
            print(item)
    except Exception as e:
        logging.error(f"Ошибка при обработке директории: {e}")
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    # Вызовы задач
    print("--- Задача 1 выполнена ---")
    print("--- Задача 2 выполнена ---")
    print(f"Дата через 10 дней (Задача 3): {future_date}")
    print("--- Для выполнения Задачи 4 и 5 используйте командную строку ---")