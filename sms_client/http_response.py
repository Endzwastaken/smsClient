class HttpResponse:
    status_code: int
    headers: dict[str:str]
    body: bytes

    def to_bytes(self) -> bytes:
        """Преобразование ответа в байты."""
        status_line = f"HTTP/1.1 {self.status_code}\r\n"
        headers_str = "\r\n".join(f"{key}: {value}" for key, value in self.headers.items())
        response_str = f"{status_line}{headers_str}\r\n\r\n"
        return response_str.encode() + self.body

    def from_bytes(self, binary_data: bytes):
        """Разбор байтов ответа в атрибуты класса."""
        raw_response = binary_data.decode().split('\r\n\r\n')
        body = raw_response[1].encode()
        self.body = body

        header = raw_response[0]
        status = header.split('\r\n')[0]
        self.status_code = int(status.split(' ')[1])

        header_lst = header.split('\r\n')[1:]
        header_dict = dict()
        for line in header_lst:
            line_lst = line.split(': ')
            header_dict[line_lst[0]] = line_lst[1]
        self.headers = header_dict
        return self
