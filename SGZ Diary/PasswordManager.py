from argon2 import PasswordHasher, exceptions

class PasswordManager:
    def __init__(self):
        self.ph = PasswordHasher()
        self.hashed_password = None

    def set_password(self, plain_password: str):
        self.hashed_password = self.ph.hash(plain_password)

    def verify_password(self, plain_password: str) -> bool:
        if not self.hashed_password:
            raise ValueError("No password set.")
        try:
            return self.ph.verify(self.hashed_password, plain_password)
        except exceptions.VerifyMismatchError:
            return False
