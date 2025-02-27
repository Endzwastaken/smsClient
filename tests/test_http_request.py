# test_http_request.py
from sms_client.http_request import HttpRequest


def test_request_building():
    request = HttpRequest()
    request.build_request(
        logpass="dGVzdDp0ZXN0",
        sender="79001234567",
        recipient="79007654321",
        message="Test message",
        url="localhost:4010"
    )

    assert request.method == "POST"
    assert request.path == "/send_sms"
    assert request.headers["Content-Type"] == "application/json"
    assert request.headers["Authorization"] == "Basic dGVzdDp0ZXN0"
    assert "Test message" in request.body.decode()


def test_request_serialization():
    request = HttpRequest()
    request.build_request("auth", "sender", "recipient", "msg", "host")
    bytes_data = request.to_bytes()

    assert b"POST /send_sms HTTP/1.1" in bytes_data
    assert b"Content-Type: application/json" in bytes_data
    assert b"Authorization: Basic auth" in bytes_data


def test_request_deserialization():
    raw_request = (
        b"POST /send_sms HTTP/1.1\r\n"
        b"Content-Type: application/json\r\n"
        b"Authorization: Basic dGVzdA==\r\n"
        b"\r\n"
        b"test body"
    )

    request = HttpRequest().from_bytes(raw_request)
    assert request.method == "POST"
    assert request.headers["Content-Type"] == "application/json"
    assert request.body == b"test body"