import socket

from sms_client.http_request import HttpRequest
from sms_client.http_response import HttpResponse
from sms_client.config import UserConfig, ServerConfig
from sms_client.utils import auth_encoding


class Client:
    def __init__(self, req: HttpRequest, resp: HttpResponse, usr_conf: UserConfig, serv_conf: ServerConfig):
        self.request = req
        self.response = resp
        self.user_config = usr_conf
        self.server_config = serv_conf

    def send_sms(self, sender: str, recipient: str, message: str) -> HttpResponse:
        """Отправление сообщения"""
        host = self.server_config.host
        port = self.server_config.port
        username = self.user_config.username
        password = self.user_config.password

        logpass = auth_encoding(username, password)
        url = f'{host}:{port}'

        # Формирование запроса
        self.request.build_request(logpass,
                                   sender,
                                   recipient,
                                   message,
                                   url)

        # Отправка запроса
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, int(port)))
            s.sendall(self.request.to_bytes())

            # Получение ответа в "кусочками"
            response_data = b''
            while True:
                chunk = s.recv(4096)
                if not chunk:
                    break
                response_data += chunk

        self.response.from_bytes(response_data)
        return self.response
