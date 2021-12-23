import socket

class App:
    __conf = {
        'URL': 'http://' + socket.gethostbyname(socket.gethostname()),
        'IP_ADDR': socket.gethostbyname(socket.gethostname()),
        'PORT': 80,
        'OUTPUTFILEPATH': 'C:\\Users\\Calin\\Bureaublad\\output.txt',
        'KEYLOGGERFILE': 'key_log.txt'
    }

    __setters = ['OUTPUTFILEPATH']

    @staticmethod
    def config(name):
        return App.__conf[name]

    @staticmethod
    def set(name, value):
        if name in App.__setters:
            App.__conf[name] = value
        else:
            raise NameError('Error: This property cannot be set.')