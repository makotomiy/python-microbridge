#include <SPI.h>
#include <Adb.h>

const int ledPin = 3;

int ledState = 1;

// Adb connection.
Connection * connection;

// Elapsed time for ADC sampling
long lastTime;

// Event handler for the shell connection. 
void adbEventHandler(Connection * connection, adb_eventType event, uint16_t length, uint8_t * data)
{
  if (event == ADB_CONNECTION_RECEIVE)
  {
    int8_t num = data[0];
    // Check if data received is an 'a' (0x61)
    if (num == 97) {
      digitalWrite(ledPin, ledState);
      ledState = !ledState;
    }
  }
}

void setup()
{

  // Initialize serial port
  Serial.begin(57600);
  
  // Note start time
  lastTime = millis();
  
  pinMode(ledPin, OUTPUT);

  // Initialize the ADB subsystem.  
  ADB::init();

  // Open an ADB stream to the phone's shell. Auto-reconnect
  connection = ADB::addConnection("tcp:4567", true, adbEventHandler);  
}

void loop()
{
  if ((millis() - lastTime) > 100)
  {
    // Read analog pin and send data to arduino
    uint16_t data = analogRead(A0);
    connection->write(2, (uint8_t*)&data);
    lastTime = millis();
  }

  // Poll the ADB subsystem.
  ADB::poll();
}

