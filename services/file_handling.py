BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

end_simbols = [',', '.', '!', ':', ';', '?']

def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]: 
    text = text[start:size]
    i = -1
    size = len(text)
    if text[i] not in end_simbols:
        i -= 1
        if text[i] not in end_simbols:
            s = ''
            while s != '':
                i -= 1
                s = text[i]
            size += i
            text = text[0:size]
    page = [text, len(text)]
    return page


def prepare_book(path) -> None:
    pass


text = 'Да? Вы точно уверены? Может быть, вам это показалось?.. Ну, хорошо, приходите завтра, тогда и посмотрим, что можно сделать. И никаких возражений ! Завтра, значит, завтра!'

print(*_get_part_text(text, 22, 145), sep='\n')  

# print(text[22:123])


prepare_book(BOOK_PATH)