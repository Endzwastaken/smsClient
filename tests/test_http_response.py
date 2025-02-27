# test_http_response.py
from sms_client.http_response import HttpResponse


def test_response_serialization():
    response = HttpResponse()
    response.status_code = 200
    response.headers = {"Content-Type": "application/json"}
    response.body = b'{"status": "ok"}'

    bytes_data = response.to_bytes()
    assert b"HTTP/1.1 200" in bytes_data
    assert b"Content-Type: application/json" in bytes_data
    assert b'{"status": "ok"}' in bytes_data


def test_response_deserialization():
    raw_response = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/json\r\n"
        b"\r\n"
        b'{"status": "success"}'
    )

    response = HttpResponse().from_bytes(raw_response)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.body == b'{"status": "success"}'