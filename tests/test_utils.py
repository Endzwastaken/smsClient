# test_utils.py
from sms_client.utils import auth_encoding

def test_auth_encoding():
    encoded = auth_encoding("user", "pass")
    assert encoded == "dXNlcjpwYXNz"