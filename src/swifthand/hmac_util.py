import secrets
import hmac
from hashlib import sha256


class HMACUtill:
    def __init__(self) -> None:
        self.secret_key = None
        self.curr_hmac = None

    def generate_secret_key(self):
        self.secret_key = secrets.token_bytes(32).hex()

    def calculate_hmac(self, computer_move: str):
        _hmac = hmac.new(self.secret_key.encode(), computer_move.encode(), sha256)
        self.curr_hmac = _hmac.hexdigest()
