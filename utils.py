from config import RUSSIAN_ALPHABET, LATIN_ALPHABET, GROUP_SIZE


def clean_text(text: str) -> str:
    """
    Предобрабатывает текст для шифрования:
    - Заменяет Ё на Е
    - Удаляет всё, что не буква
    - Приводит к нижнему регистру
    """
    # Замена ё → е
    text = text.replace('ё', 'е').replace('Ё', 'Е')
    
    # Оставляем только буквы
    text = ''.join(char for char in text if char.isalpha())
    
    # Приводим к нижнему регистру
    return text.lower()


def group_text(text: str, group_size: int = GROUP_SIZE) -> str:
    """
    Разбивает текст на группы по group_size символов.
    Нужно для вывода зашифрованного текста (по заданию — по 5 символов).
    """
    return ' '.join(
        text[i:i + group_size] 
        for i in range(0, len(text), group_size)
    )


def detect_alphabet(text: str) -> str:
    """
    Определяет алфавит по первому буквенному символу.
    Возвращает RUSSIAN_ALPHABET или LATIN_ALPHABET.
    """
    for char in text:
        if char.isalpha():
            if char in RUSSIAN_ALPHABET:
                return RUSSIAN_ALPHABET
            elif char in LATIN_ALPHABET:
                return LATIN_ALPHABET
    
    # Если букв не нашли — по умолчанию русский
    return RUSSIAN_ALPHABET


def get_valid_key(prompt: str) -> int:
    """
    Запрашивает у пользователя ключ шифрования.
    Принимает ЛЮБОЕ целое число (отрицательное, ноль, огромное положительное).
    """
    while True:
        try:
            # Пытаемся превратить ввод пользователя в целое число
            key = int(input(prompt))
            return key  # Если получилось, сразу возвращаем число и выходим из цикла
            
        except ValueError:
            # Если пользователь ввёл буквы, дробное число или символы
            print("Ошибка: введите целое число (например, 5, -3 или 100)")