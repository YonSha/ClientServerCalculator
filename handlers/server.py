from handlers.connectionHandler import ConnectionHandler
from utils.logger import enter_exit_wrapper


class Server(ConnectionHandler):

    def __init__(self):
        super().__init__()

    @enter_exit_wrapper
    def __receive_data_from_client(self, conn):
        data = conn.recv(1024).decode()
        return data

    @enter_exit_wrapper
    def __send_data_to_client(self, data, conn):
        try:
            conn.send(("Answer: " + str(eval(data))).encode())
        except (NameError, SyntaxError, ZeroDivisionError) as e:
            self.log.logging_error(e)
            conn.send("Invalid input".encode())

    @enter_exit_wrapper
    def run_server(self):
        conn, address = self.connect_server()
        self.log.logging_info("Connection from: " + str(address))

        while True:
            data = self.__receive_data_from_client(conn)
            if not data:
                break
            self.__send_data_to_client(data, conn)
