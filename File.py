class File:

    filename = ''
    file = None
    filetype = ''

    def __init__(self, name):
        self.filename = name

    def __open(self, mode):
        """
        Opens the file either to read or to write.
        :param mode: Either read or write
        :return: None
        """
        self.file = open(self.filename, mode)
        return

    def __close(self):
        """
        Closes the file.
        :return: None
        """
        self.file.close()
        return

    def read(self):
        """
        Reads the content of the file.
        :return: content of the file
        """
        self.__open('r')
        content = self.file.read()
        self.__close()
        return content

    def write(self, text):
        """
        Writes content of 'text' variable to the file.
        :param text: string
        :return: None
        """
        self.__open('w')
        self.filetype = 't'
        if isinstance(text, bytes):
            self.filetype = 'b'
        self.file.write(text)
        self.__close()
        return
