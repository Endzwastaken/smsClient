import sys
import json

from sms_client.logger import setup_logger
from sms_client.config import UserConfig, ServerConfig
from sms_client.http_request import HttpRequest
from sms_client.http_response import HttpResponse
from sms_client.client import Client
from sms_client.utils import print_response_result

def main() -> None:
    # если кол-во аргументов не 4, то выходим
    # if len(sys.argv) != 4:
    #     print('Аргументов командной строки не 3.')
    #     return

    usr_config = UserConfig()
    serv_config = ServerConfig()
    req = HttpRequest()
    resp = HttpResponse()
    client = Client(req, resp, usr_config, serv_config)

    # создаём словарь для логирования параметров командной строки
    log = {
        'Номер отправителя': sys.argv[1],
        'Номер получателя': sys.argv[2],
        'Сообщение': sys.argv[3]
    }

    logger = setup_logger("sms_client.log")
    logger.info(f"Параметры командной строки: {log}")

    # отправляем сообщение
    client.send_sms(sys.argv[1], sys.argv[2], sys.argv[3])

    logger.info(f"Ответ от сервиса: {json.dumps(client.response.to_bytes().decode())}")
    # печатаем ответ от сервиса
    print_response_result(client.response)


if __name__ == "__main__":
    main()
