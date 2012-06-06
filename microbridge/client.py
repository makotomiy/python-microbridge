
from threading import Thread
import socket


class Client:

    keep_alive = True

    def __init__(self, server, socket):
        # Initialize client and starts main thread
        self.server = server
        self.socket = socket
        self.socket.settimeout(1)

        self.comm_thread = Thread(target=self.communication_thread, args=(self, ))
        self.comm_thread.start()

    def communication_thread(self, *args):
        # Main thread
        while self.keep_alive:
            try:
                # You can set it to receive more bytes
                data = self.socket.recv(2)
                if not data:
                    self.keep_alive = False
                else:
                    self.server.receive(self, data)
            except socket.timeout, e:
                pass
            except Exception, e:
                self.keep_alive = False
        self.server.disconnect_client(self)

    def close(self):
        # Close connection
        self.keep_alive = False

        try:
            self.socket.close()
        except Exception, e:
            pass

    def send(self, string):
        # Send string to client
        try:
            self.socket.sendall(string)
        except Exception, e:
            self.close()
            self.server.disconnect_client(self)
