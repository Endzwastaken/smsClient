import json


class HttpRequest:
    method: str
    path: str
    headers: dict[str:str]
    body: bytes

    def build_request(self, logpass: str, sender: str, recipient: str, message: str, url: str):
        data = {'sender': sender, 'recipient': recipient, 'message': message}
        self.body = json.dumps(data).encode()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {logpass}',
            'Host': f'{url}',
            'Content-length': f'{len(self.body)}'
        }

        self.method = 'POST'
        self.path = '/send_sms'
        self.headers = headers

    def to_bytes(self) -> bytes:
        """Преобразование запроса в байты."""
        request_line = f"{self.method} {self.path} HTTP/1.1\r\n"
        headers_str = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        request_str = f"{request_line}{headers_str}\r\n\r\n"
        return request_str.encode() + self.body

    def from_bytes(self, binary_data: bytes):
        """Разбор байтов запроса в атрибуты класса."""
        raw_request = binary_data.decode().split('\r\n\r\n')
        body = raw_request[1].encode()
        self.body = body

        header = raw_request[0]
        status = header.split('\r\n')[0]
        self.method = status.split(' ')[0]
        self.path = status.split(' ')[1]

        header_lst = header.split('\r\n')[1:]
        header_dict = dict()
        for line in header_lst:
            line_lst = line.split(': ')
            header_dict[line_lst[0]] = line_lst[1]
        self.headers = header_dict
        return self
