from handlers.connectionHandler import ConnectionHandler
from utils.logger import enter_exit_wrapper


class Client(ConnectionHandler):

    def __init__(self):
        super().__init__()

    def close_server(self,server_socket):
        server_socket.close()

    @enter_exit_wrapper
    def __send_data_to_server(self, client_socket):
        message = input(" -->: ")
        if message.strip() == '':
            message = "Invalid input"
        client_socket.send(message.encode())
        return message

    @enter_exit_wrapper
    def __receive_data_from_server(self, client_socket):
        return client_socket.recv(1024).decode()

    @enter_exit_wrapper
    def run_client(self):

        client_socket = self.connect_client()

        while True:
            message =  self.__send_data_to_server(client_socket)
            if message == "quit":
                self.connect_server.close()
                client_socket.close()
            data = self.__receive_data_from_server(client_socket)
            print('Received from server: ' + data)

