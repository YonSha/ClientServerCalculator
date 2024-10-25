import socket

from utils import logger
from utils.logger import enter_exit_wrapper


class ConnectionHandler:

    def __init__(self):
        self.log = logger.Logger()

    @enter_exit_wrapper
    def connect_server(self, port=8080):
        host = socket.gethostname()

        server_socket = socket.socket()
        server_socket.bind((host, port))

        server_socket.listen(2)
        return server_socket.accept()

    @enter_exit_wrapper
    def connect_client(self, port=8080):
        host = socket.gethostname()  #

        client_socket = socket.socket()
        client_socket.connect((host, port))
        return client_socket

    @enter_exit_wrapper
    def close_connection(self, run_socket):
        run_socket.close()
