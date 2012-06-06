
from server import Server
from server_listener import ServerListener
import android


class DemoMicroBridge(ServerListener):
    def __init__(self):
        self.droid = android.Android()
        self.droid.webViewShow('file:///sdcard/sl4a/scripts/microbridge/demo.html')

        # Start server
        self.server = Server()
        self.server.add_listener(self)
        self.server.start()

    def on_server_started(self, server):
        print "Server Started!"

    def on_client_connect(self, server, client):
        print "Client Connected!"

    def on_client_disconnect(self, server, client):
        print "Client Disconnected!"

    def on_receive(self, client, string):
        # print "Received " + string

        # Received data from ADC
        # Arduino uses little-endian format
        data = 0
        for d in string[::-1]:
            data = data << 8 | ord(d)
        self.droid.eventPost("ADC", str(data))

demo = DemoMicroBridge()
while True:
    result = demo.droid.eventWaitFor('LedButton', 10).result
    if result:
        # Sending an 'a' to light the LED
        demo.server.send('a')
        demo.droid.eventClearBuffer()
