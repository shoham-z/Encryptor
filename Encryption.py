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
        try:
            key_file = File.File('key.txt')
            self.__key = key_file.read()
            if len(self.__key) != 44:
                self.__key = Fernet.generate_key()
                key_file.write(str(self.__key.decode('utf-8')))
        except FileNotFoundError:
            self.__key = Fernet.generate_key()
            key_file = File.File('key.txt')
            key_file.write(self.__key.decode('utf-8'))
        return

    def __del__(self):
        return

    def encrypt(self, text):
        """
        Uses the key to encrypt the text, and returns it.
        :param text: To encrypt
        :return: The encrypted text
        """
        tmp = text
        fernet = Fernet(self.__key)
        if not isinstance(text, bytes):
            encrypted = fernet.encrypt(text.encode())
            text = str(encrypted.decode())
        else:
            encrypted = fernet.encrypt(text)
            text = str(encrypted)
        return text

    def decrypt(self, text):
        """
        Uses the key to decrypt the text, and returns it.
        :param text: To decrypt
        :return: The decrypted text
        """
        tmp = text
        fernet = Fernet(self.__key)
        nop = tmp[1:]
        if not isinstance(text, bytes):
            decrypted = fernet.decrypt(text.encode())
            text = str(decrypted.decode())
        else:
            decrypted = fernet.decrypt(text)
            text = str(decrypted)
        return text
