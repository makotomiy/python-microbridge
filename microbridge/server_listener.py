

class ServerListener:

    def on_server_started(self, server):
        # Called when server has started
        pass

    def on_server_stopped(self, server):
        # Called when server has stopped
        pass

    def on_client_connect(self, server, client):
        # Called when a new client connects to the server
        pass

    def on_client_disconnect(self, server, client):
        # Called when a client disconnects from the server
        pass

    def on_receive(self, client, string):
        # Called when string is received from the client
        pass
