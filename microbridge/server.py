
from threading import Thread
import socket
from client import Client


class Server(object):
    # Server socket for the TCP connection
    server_socket = None

    # Set of connected clients
    clients = set()

    # Set of event listeners for this server
    listeners = set()

    # Indicates that the main server loop should keep running
    keep_alive = True

    def __init__(self, port=4567):
        self.port = port
        self.host = "0.0.0.0"

    def is_running(self):
        # Returns true if server is running
        return (self.listen_thread != None) and (self.listen_thread.is_alive())

    def get_client_count(self):
        # Returns number of connected clients
        return len(self.clients)

    def start(self):
        # Configures server and starts main thread
        self.keep_alive = True

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.settimeout(1)
        self.server_socket.listen(5)

        self.listen_thread = Thread(target=self.thread_loop, args=(self, ))
        self.listen_thread.start()

        for listener in self.listeners:
            listener.on_server_started(self)

    def thread_loop(self, *args):
        # Main thread method
        try:
            while self.keep_alive:
                try:
                    (client_socket, address) = self.server_socket.accept()
                    client = Client(self, client_socket)
                    self.clients.add(client)

                    for listener in self.listeners:
                        listener.on_client_connect(self, client)
                except socket.timeout, e:
                    pass
                except socket.error, e:
                    self.keep_alive = False
        except Exception, e:
            # TODO
            pass

    def stop(self):
        # Stops server
        self.keep_alive = False
        if self.server_socket:
            try:
                self.server_socket.close()
            except Exception, e:
                # TODO
                pass

        for client in self.clients:
            client.close()

        for listener in self.listeners:
            listener.on_server_stopped(self)

    def disconnect_client(self, client):
        # Disconnects client
        self.clients.discard(client)

        for listener in self.listeners:
            listener.on_client_disconnect(self, client)

    def receive(self, client, data):
        # Notify listeners about receive event
        for listener in self.listeners:
            listener.on_receive(client, data)

    def add_listener(self, listener):
        # Adds a listener to the server
        self.listeners.add(listener)

    def remove_listener(self, listener):
        # Removes a server listener
        self.listeners.discard(listener)

    def send(self, string):
        # Send string to all clients
        for client in self.clients:
            client.send(string)
