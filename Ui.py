import PySimpleGUI as sg
import File
import Encryption


class Window:
    __keep_going = True
    window = None
    __event = ''
    __file = None
    __encrypt = None
    __font = ("Arial", 11)

    def __init__(self):
        self.__create_window()
        return

    def __create_window(self):
        """
        Initializes the main graphic window
        :return: None
        """
        if self.__event == '':
            sg.set_options(font=self.__font)
            sg.theme('DarkAmber')  # Add a touch of color
            # All the stuff inside your window.
            layout = [[sg.Multiline(reroute_stdout=True, autoscroll=True, size=(70, 5))],
                      [sg.Input(key='_FILEBROWSE_', enable_events=True, visible=False)],
                      [sg.FileBrowse(button_text="Choose File", enable_events=True, target='_FILEBROWSE_')],
                      [sg.Button('Encrypt'), sg.Button('Decrypt')],
                      [sg.Button('Close')]]
            self.window = sg.Window('Encryption', layout)

        # elif self.__event == 'Encrypt':
        #     sg.set_options(font=self.__font)
        #     sg.theme('DarkAmber')  # Add a touch of color
        #     # All the stuff inside your window.
        #     layout = [[sg.Button('Close')]]
        #     self.window = sg.Window('File encrypted successfully!', layout)
        #
        # elif self.__event == 'Decrypt':
        #     sg.set_options(font=self.__font)
        #     sg.theme('DarkAmber')  # Add a touch of color
        #     # All the stuff inside your window.
        #     layout = [[sg.Button('Close')]]
        #     self.window = sg.Window('File decrypted successfully!', layout)

        return

    def show(self):
        """
        Event Loop to process "events" and get the "values" of the inputs, while also handling events
        :return: None
        """

        while self.__keep_going:
            self.__event, values = self.window.read()
            self.__event_handler(values)
        self.window.close()
        return

    def __event_handler(self, values):
        """
        Handling the events received from the window
        :param values: The values the event returns
        :return: False if the window should be closed, True otherwise
        """
        if self.__event == sg.WIN_CLOSED or self.__event == 'Close':  # if user closes window or clicks close
            self.__keep_going = False
            return
        elif self.__event == 'Encrypt':
            self.__file.write(self.__encrypt.encrypt(self.__file.read()))
            print('File encrypted successfully')
        elif self.__event == 'Decrypt':
            self.__file.write(self.__encrypt.decrypt(self.__file.read()))
            print('File decrypted successfully')
        elif self.__event == '_FILEBROWSE_':
            self.__file = File.File(values['Choose File'])
            print(values['Choose File'])
            self.__encrypt = Encryption.Encryption()

        self.__event = ''
        self.__keep_going = True
        return
