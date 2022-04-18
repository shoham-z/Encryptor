class File:
    filename = ''
    __file = None
    filetype = ''

    def __init__(self, name):
        self.filename = name

    def __open(self):
        """
        Opens the file either to read or to write.
        :param: "mode" Either read or write
        :return: None
        """
        self.__file = open(self.filename, self.filetype)
        return

    def __close(self):
        """
        Closes the file.
        :return: None
        """
        self.__file.close()
        return

    def read(self):
        """
        Reads the content of the file.
        :return: content of the file
        """
        self.filetype = 'r'
        content = ''
        try:
            self.__open()
            content = self.__file.read()
        except UnicodeDecodeError:
            self.filetype = 'rb'
            self.__open()
            content = self.__file.read()
        self.__close()
        return content

    def write(self, text):
        """
        Writes content of 'text' variable to the file.
        :param: "text" string
        :return: None
        """
        self.filetype = 'w'
        if isinstance(text, bytes):
            self.filetype = 'wb'
        self.__open()
        self.__file.write(text)
        self.__close()
        return
