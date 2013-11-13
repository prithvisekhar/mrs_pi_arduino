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

  def writeNumber(self, slave, command):
    self.bus.write_i2c_block_data(slave,command[0],command[1:len(command)])
    #self.bus.write_byte(self.address, value)
   
    return 0

  def readNumber(self,slave,command,numByte):
    number = self.bus.read_i2c_block_data(slave, command)[:numByte]
    #self.bus.read_byte()
    # number = bus.read_byte_data(address, 1)
    return number

  def execute(self):
    while True:
        #var = []
        self.cmd=[]
        self.address = 4
        #~ input("Slave Address (4-15): ")
        #~ if not self.address:
            #~ continue
        self.cmd.append(self.address)
        
        self.byte1 = 3
        #~ input("1st Value 1-9: ")
        #~ if not self.byte1:
            #~ continue
        self.cmd.append(self.byte1)
        
        self.byte2 = 3
        #~ input("2nd Value 1-9: ")
        #~ if not self.byte2:
            #~ continue
        self.cmd.append(self.byte2)
        
        self.bus.write_byte(self.address, self.byte1)
        #~ self.writeNumber(self.address, self.cmd)
        print "RPI: Hi Arduino, I sent you ", self.cmd
        # sleep one second
        time.sleep(1)
    
        #self.number = self.readNumber(self.address, 13 ,3)
        #self.number = self.bus.read_i2c_block_data(4,4)[:6]
        #print "Arduino: Hey RPI, I received a digit ", self.number
        self.x2= self.bus.read_byte(self.address)
        self.x3= self.bus.read_byte(self.address)
        print "recived : ", self.x2, self.x3
        #~ self.x1= self.bus.read_i2c_block_data(self.address,1)[:1]
        #~ self.bus.read_byte(self.address)[:6]
        #~ x2= self.bus.read_byte(self.address)
        #~ x3= self.bus.read_byte(self.address)
        #~ x4= self.bus.read_byte(self.address)
        #~ x5= self.bus.read_byte(self.address)
        #~ x6= self.bus.read_byte(self.address)
        
        #~ print "recived : ", self.x1
  
  #~ def get_addresses(self):
    #~ for strip in xrange(self.max_strips):
      #~ for sensor in xrange(self.max_sensors):
        #~ # Calculate the address
        #~ address = (strip << 4) + 2 * sensor
  
  
if __name__ == '__main__':
  rospy.init_node('read_Motornode')
  interface = I2CInterface()
  interface.execute()
