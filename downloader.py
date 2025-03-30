import requests


def download_file(target_file, filename):
    """Скачивает файл"""
    with requests.get(target_file, stream = True) as request:
        if request.status_code == 200:
            with open(filename, 'wb') as file:
                for chunk in request.iter_content(chunk_size = 5_000):
                    file.write(chunk)
            print("Файл успешно скачан")
        else:
            print(f"Ошибка со статус кодом: {request.status_code}")


def main():
    """Выполняет код всего script'a."""
    while True:
        target_url = input("Введите целевой URL: ")
        if target_url == 'выход':
            print('Выход')
            break
        local_filename = input("Введите название для скачиваемого файла: ").lower()
        download_file(target_url, local_filename)


if __name__ == '__main__':
    main()