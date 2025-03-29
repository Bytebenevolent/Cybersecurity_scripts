import argparse
import whois
import socket
import requests


def safe_get(value):
    """Возвращает значение, если оно есть, иначе 'Не удалось выяснить'."""
    return value if value else "Не удалось выяснить"


def save_to_file(target, data):
    """Сохраняет результаты в файл."""
    filename = f"{target}_report.txt"
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write(data + "\n")
    print(f"Данные сохранены в {filename}")


def get_whois_info(target):
    """Получает Whois-информацию о домене и сохраняет в файл."""
    try:
        w = whois.whois(target)
        whois_data = {
            "Домен зарегистрирован": w.name,
            'Оранизация': w.org,
            'Страна': w.country,
            "Электронная почта администратора:": w.email,
            "Дата создания": w.creation_date,
            "Дата истечения": w.expiration_date
        }
        print("[WHOIS Информация]")
        for key, value in whois_data.items():
            print(f"{key}: {safe_get(value)}")
    except Exception as exception:
        print(f"Oшибка: {exception}")


def find_subdomains(target):
    """Ищет поддомены через DNS-запросы."""
    subdomains = ['www', 'mail', 'ftp', 'test', 'dev', 'staging', 'admin', 'api']
    found_subdomains = []
    print("[Поиск поддоменов]")
    for sub in subdomains:
        subdomain = f"{sub}.{target}"
        try:
            # Попытка получить IP-адрес поддомена.
            ip = socket.gethostbyname(subdomain)
            print(f"Найден поддомен: {subdomain} ({ip})")
            found_subdomains.append(subdomain)
        except socket.gaierror:
            pass  # Если поддомен не найден, то ошибка игнорируется.
    if not found_subdomains:
        print("Поддомены не найдены")


def get_http_headers(target):
    """Получает HTTP-заголовки сайта и сохраняет в файл."""
    url = f"http://{target}"  # Использование HTTP, чтобы не возникли проблемы с SSL.
    result = "[HTTP Заголовки сервера]\n"
    try:
        response = requests.get(url, timeout = 5)
        print("HTTP-заголовки сервера")
        # Список интересующих заголовков.
        headers_of_interest = [
            'Server', 
            "Content-Type", 
            "Set-Cookie",
            "Strict-Transport-Security", 
            "X-Frame-Options", 
            "X-Content-Type-Options", 
            "Content-Security-Policy"
        ]
        # Прохождение циклом по списку заголовков.
        for header in headers_of_interest:
              value = response.headers.get(header, 'Неизвестно')
              result += f"{header}: {value}\n"
    except requests.RequestException as request_exception:
        result += f"Ошибка при получении HTTP-заголовков: {request_exception}\n"

    print(result)
    save_to_file(target, result)


def main():
    parser = argparse.ArgumentParser(description = "OSINT-инструмент для сбора информации о домене")
    parser.add_argument('target', help = "Домен или IP-aдрес")
    args = parser.parse_args()
    target = args.target
    print(f"Начинаем разведку для {target}")
    get_whois_info(target)
    find_subdomains(target)
    get_http_headers(target)


if __name__ == '__main__':
    main()