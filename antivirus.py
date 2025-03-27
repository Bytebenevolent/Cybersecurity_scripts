import hashlib
import os
import re


def calculate_sha256(file_path):
    """Вычисляет SHA-256 hash файла."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b''):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as exception:
        print(f"Ошибка при обработке {file_path}: {exception}")
        return None


def check_hash_against_blacklist(file_hash, blacklist):
    """Проверяет hash в чёрном списке."""
    return file_hash in blacklist


def static_analysis(file_path):
    """Простейший статический анализ-поиск подозрительных строк."""
    suspicious_patterns = [
        r"(?i)cmd\.exe",
        r"(?i)system\(",
        r"(?i)powershell",
        r"(?i)base64",
        r"(?i)import os",
        r"(?i)eval\(",
    ]
    # Обработка возможных ошибок.
    try:
        with open(file_path, 'r', errors = 'игнорирование') as file:
            content = file.read()
            for pattern in suspicious_patterns:
                if re.search(pattern, content):
                    return True
    except Exception as exception:
        print(f"Ошибка анализа {file_path}: {exception}")
    return False


def scan_directory(directory, blacklist):
    """Сканирует папку на предмет зараженных файлов."""
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_sha256(file_path)
            if file_hash and check_hash_against_blacklist(file_hash, blacklist):
                print(f"ОБНАРУЖЕН ВРЕДОНОСНЫЙ ФАЙЛ: {file_path}")
            elif static_analysis(file_path):
                print(f"ПОДОЗРИТЕЛЬНЫЙ ФАЙЛ: {file_path}")

# Пример использования.
blacklisted_hashes = {
    "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",  # Hash.
    "d41d8cd98f00b204e9800998ecf8427e"  # Еще один hash.
}
directory_to_scan = "./test_folder"
scan_directory(directory_to_scan, blacklisted_hashes)
