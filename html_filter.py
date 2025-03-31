import re
from bs4 import BeautifulSoup


def clean_html(html_content):
    """Удаляет HTML-разметку из текста."""
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()


def find_keywords(text, keywords):
    """Находит ключевые слова в тексте."""
    found = [word for word in keywords if re.search(rf"\b{word}\b", text, re.IGNORECASE)]
    return found


def replace_words(text, replacements):
    """Заменяет слова в тексте по словарю замен."""
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def process_text(input_text):
    """Основной процесс обработки текста."""
    cleaned_text = clean_html(input_text)  # Убираем HTML
    keywords = find_keywords(cleaned_text, ['Python', 'automation', 'data']) 
    replaced_text = replace_words(cleaned_text, {'Java': 'Python'})  # Заменa слов.   
    return replaced_text, keywords


if __name__ == "__main__":
    # Пример входных данных.
    sample_text = "<p>I love Java. Java is great for automation!</p>"
    # Обработка текста.
    final_text, found_keywords = process_text(sample_text)
    output_filename = input("Enter output filename: ").lower()
    # Сохранение результата в файл.
    with open(output_filename, 'w', encoding = 'utf-8') as file:
        file.write(f"Processed Text:\n{final_text}\n\n")
        file.write(f"Found Keywords: {', '.join(found_keywords)}\n")
    print(f"Текст обработан и сохранён в '{output_filename}'")
