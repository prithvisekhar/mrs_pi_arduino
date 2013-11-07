// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>

#define SLAVE_ADDRESS 0x04

char recData[10];
int i;
int recBytes = 0 ;
int b1 =0; int b2=0 ;int b3=0 ;
char c1, c2,c3 ;
void setup()
{
  Wire.begin(SLAVE_ADDRESS);                // join i2c bus with address #4
  Wire.onReceive(receiveEvent); // register event
  Wire.onRequest(sendData);     // Send data on request
  Serial.begin(9600);           // start serial for output
  
  Serial.println("I2C ready!");
}

void loop()
{
  delay(100);
  
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany)
{
  Serial.print("data received: ");
  int index = 0;
  while(1 < Wire.available()) // loop through all but the last
  {
    char c = Wire.read(); // receive byte as a character
    recData[index]=c;
    index ++;
    b1=c;
    Serial.print(c);         // print the character
    Serial.print(b1);
  }
  char ct = Wire.read();    // receive byte as an integer 
  b2 =ct;
  recData[index]=ct;
    Serial.print(ct);         // print the character
    Serial.print(b2);
  Serial.println("data stored: ");
  Serial.println(b1); Serial.println(b2);  
  for (int ind=0;ind<sizeof(recData);ind++){
                Serial.print(ind); Serial.print("::");
                Serial.println(recData[ind]);
                }
}

// callback for sending data
void sendData(){  
  c1=b1 ; c2=b2 ; 
  Serial.println(c1); Serial.println(c2);
  //Wire.write(recData[0]); Wire.write(recData[1]); Wire.write(recData[2]);
  //Serial.print(recData[0]); Serial.print(recData[1]); Serial.print(recData[2]);
  recData[0]=0;recData[1]=0;recData[2]=0;recData[3]=0;
  }
