#! /usr/bin/env python
import smbus
import time
import rospy
# From the GPIO towards the SD card corner 
# scl sda 3.3v
# GND --- 5v
# Connect :
# SDA -SDA(A4-uno/20-Mega) 
# SCL-SCL(A5-uno/21-Mega) 
# for RPI version 1, use "bus = smbus.SMBus(0)"

class I2CInterface():
# Constant values
  
    
  address = 0x04 # DEFAULT Slave address 

   # Initialise interface
  def __init__(self, pi_version = 1):
    self.bus = smbus.SMBus(pi_version)

  def writeNumber(self, value):
    self.bus.write_byte(self.address, value)
   # bus.write_byte_data(address, 0, value)
    return 0

  def readNumber(self):
    number = self.bus.read_byte(self.address)
    # number = bus.read_byte_data(address, 1)
    return number

  def execute(self):
    while True:
        #var = []
        var = raw_input("Enter Slave Address 1-9: ")
        if not var:
            continue
        self.address=var
        writeNumber(var)
        print "RPI: Hi Arduino, I sent you ", var
        # sleep one second
        time.sleep(1)
    
        number = readNumber()
        print "Arduino: Hey RPI, I received a digit ", number
        print
  
  #~ def get_addresses(self):
    #~ for strip in xrange(self.max_strips):
      #~ for sensor in xrange(self.max_sensors):
        #~ # Calculate the address
        #~ address = (strip << 4) + 2 * sensor
  
  
if __name__ == '__main__':
  rospy.init_node('read_Motornode')
  interface = I2CInterface()
  interface.execute()
