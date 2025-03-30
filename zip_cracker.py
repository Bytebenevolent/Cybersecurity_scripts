import zipfile  
import time    


ZIP_FILE = "file.zip"
PASSWORD_FILE = "pass.txt"


def crack_zip():
    """Перебирает пароли из файла и пробует открыть архив."""
    start_time = time.time()  # Засекание времени работы.    
    try:
        # Открытие ZIP-архива.
        with zipfile.ZipFile(ZIP_FILE, 'r') as archive:
            with open(PASSWORD_FILE, 'r', encoding = 'utf-8') as file:
                for password in file:
                    password = password.strip()
                    try:
                        # Попытка извлечь файлы с текущим паролем.
                        archive.extractall(pwd = password.encode())
                        print(f"Пароль найден: {password}")
                        print(f"Время работы: {time.time() - start_time:.2f} секунд")
                        return
                    except:
                        pass  # Если пароль не подошёл, пробуется следующий.
            print("Пароль не найден в словаре")
    except FileNotFoundError:
        print("Файл архива или словарь паролей не найден")


if __name__ == "__main__":
    crack_zip()
