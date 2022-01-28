from cryptography.fernet import Fernet
import File


class Encryption:
    __key = 0
    text = ''

    def __init__(self):
        """
        Tries to read the key from file in the same directory.
        If unsuccessful, it generates a key and saves it to file.
        """
        key_file = File.File('key.txt')
        try:
            self.key = key_file.read()
            if len(self.key) != 44:
                self.key = Fernet.generate_key()
                key_file.write(self.key)
        except Exception:
            self.key = Fernet.generate_key()
            key_file.write(self.key)
        return

    def __del__(self):
        return

    def encrypt(self, text):
        """
        Uses the key to encrypt the text, and returns it.
        :param text: To encrypt
        :return: The encrypted text
        """
        fernet = Fernet(self.key)
        encrypted = fernet.encrypt(text.encode())
        text = str(encrypted.decode())
        return text

    def decrypt(self, text):
        """
        Uses the key to decrypt the text, and returns it.
        :param text: To decrypt
        :return: The decrypted text
        """
        fernet = Fernet(self.key)
        text = str(fernet.decrypt(text.encode()).decode())
        return text
