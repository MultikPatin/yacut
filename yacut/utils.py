from datetime import datetime
from hashlib import blake2b

from .models import URLMap


def generate_link_end(byte_size: int = 3) -> str:
    """
    Функция генерирует последовательность из byte_size байт
    состоящую из букв и цифр на основе hashlib.blake2b
    :param byte_size: Количество байт в сгенерированном ответе
    :return: Сгенерированная последовательность
    """
    sequence = ""
    exists = True
    h = blake2b(digest_size=byte_size)
    while exists:
        date = str(datetime.now())
        h.update(bytes(date, "utf-8"))
        sequence = h.hexdigest()
        if not URLMap.query.filter_by(short=sequence).first():
            exists = False
    return sequence
