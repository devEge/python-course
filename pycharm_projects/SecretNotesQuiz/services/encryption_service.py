from cryptography.fernet import Fernet
import base64


class EncryptionService:
    @staticmethod
    def save_and_encrypt_notes(secret_data: str, master_key: str) -> str:
        key = master_key.ljust(32)[:32]
        key = base64.urlsafe_b64encode(key.encode())
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(secret_data.encode()).decode()
        return encrypted_data

    @staticmethod
    def decrypt_notes(encrypted_text, master_key) -> str:
        key = master_key.ljust(32)[:32]
        key = base64.urlsafe_b64encode(key.encode())
        fernet = Fernet(key)
        plain_text = fernet.decrypt(encrypted_text.encode()).decode()
        return plain_text