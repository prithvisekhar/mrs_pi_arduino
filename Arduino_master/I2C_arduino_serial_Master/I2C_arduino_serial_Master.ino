/*
  Serial Event recive user input 
  Transmit over I2C and recieve bytes
  Testing code
 
 */
#include <Wire.h>
int reading = 0;
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete
char inCmd[4] ;
void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  Wire.begin(); // join i2c bus (address optional for master)
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString); 
    // clear the string:
    inputString.toCharArray(inCmd,4);
    inputString = "";
    stringComplete = false;
    Wire.beginTransmission(4); // transmit to device #4
    for (int index=0;index<sizeof(inCmd);index++){
                Serial.print(index); Serial.print("::");
                Serial.println(inCmd[index]);
                Wire.write(inCmd[index]);}
    Wire.endTransmission();    // stop transmitting
    Serial.println("Transmission Complete");
    delay(500);
  
    // step 4: request reading from sensor
  Wire.requestFrom(4, 3);    // request 2 bytes from slave device #4
  delay(25);
  // step 5: receive reading from sensor
  if(3 <= Wire.available())    // if two bytes were received
  {
    reading = Wire.read();  // receive high byte (overwrites previous reading)
    Serial.println(reading);
    //reading = reading << 8;    // shift high byte to be high 8 bits
    reading = Wire.read(); // receive low byte as lower 8 bits
    Serial.println(reading);   // print the reading
    reading = Wire.read();
    Serial.println(reading); 
  }

                    // wait a bit since people have to read the output :)


  }
  

  delay(250);
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
