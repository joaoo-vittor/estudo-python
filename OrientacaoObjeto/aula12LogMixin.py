class LogMixin:
    @staticmethod
    def writer(msg):  # Metodo Estatico não passe self por parametro
        with open('aula12log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        aux = 'INFO: ' + msg
        self.writer(aux)

    def log_error(self, msg):
        aux = 'ERROR: ' + msg
        self.writer(aux)
