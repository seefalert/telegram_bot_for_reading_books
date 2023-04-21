BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    text = text[start:start + size + 1]
    end_string = 0
    for marks in ',.!:;?':
        if text.rfind(marks) > end_string:
            end_string = text.rfind(marks)
    text = text[:end_string + 1]
    end_string = 0
    if len(text) > size:
        text = text[:end_string - 3]
        for marks in '.,!:;?':
            if text.rfind(marks) > end_string:
                end_string = text.rfind(marks)
        text = text[:end_string + 1]
    return text, len(text)


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
        start = 0
        page_num = 1
        while start < len(text):
            page_text, chars = _get_part_text(text, start, PAGE_SIZE)
            book[page_num] = page_text.lstrip()
            page_num += 1
            start += chars
    return book


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
