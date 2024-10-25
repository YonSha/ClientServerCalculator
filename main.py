import threading

from handlers.client import Client
from handlers.server import Server

if __name__ == '__main__':
    c = Client()
    s = Server()

    serv = threading.Thread(target=s.run_server)
    cli = threading.Thread(target=c.run_client)

    serv.start()
    cli.start()
