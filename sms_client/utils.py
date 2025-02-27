from base64 import b64encode

from sms_client.http_response import HttpResponse


def auth_encoding(username: str, password: str) -> str:
    """кодирование логина:пароля в base64"""
    logpass_bytes = f'{username}:{password}'.encode('ascii')
    base64_bytes = b64encode(logpass_bytes)
    base64_logpass = base64_bytes.decode('ascii')
    return base64_logpass


def print_response_result(response: HttpResponse) -> None:
    """Вывод ответа в стандартный поток"""
    print(f'Код ответа - {response.status_code}')
    print(f'Тело ответа - {response.body.decode()}')
