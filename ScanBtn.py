import RPi.GPIO as GPIO   
import time   
import os
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)   
#######################################################
#                Set  Input                           #
#-----------------------------------------------------#  
# set up pin 08 as an input for upload(Drive)
GPIO.setup(8, GPIO.IN)
# set up pin 10 as an input for upload(Dropbox)
GPIO.setup(10, GPIO.IN)
# set up pin 12 as an input for upload(Facebook)
GPIO.setup(12, GPIO.IN)
# set up pin 16 as an input for TakeBySelf
GPIO.setup(16, GPIO.IN)
# set up pin 18 as an input for Shutdown
GPIO.setup(18, GPIO.IN) 
# set up pin 22 as an input for ClickBtn
GPIO.setup(22, GPIO.IN)
#-----------------------------------------------------#

#######################################################
#                Set  Out                             #
#-----------------------------------------------------#
# set up pin 7 as an output for LED
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)
#-----------------------------------------------------#
x=0
y=0
z=0
while True:
# set up upload pin to Doogle Drive as GPIO.8
 upDrive = GPIO.input(8)
# set up upload pin to Dropbox as GPIO.10
 upDB = GPIO.input(10)
# set up up load pin to Facebook as GPIO.12
 upFB = GPIO.input(12)
# set up Btn click as GPIO.22
 clickbtn = GPIO.input(22)
# when user press the btn
 if clickbtn == False:
  y+=1
########################################################
#                  LED Shinning                        #
#------------------------------------------------------#
  GPIO.setup(7, GPIO.OUT)
  while x<4:
   GPIO.output(7,True)
   time.sleep(1)
   GPIO.output(7,False)
   time.sleep(1)
   x+=1
#------------------------------------------------------#

########################################################
#                  Take Pictures                       #
#------------------------------------------------------#   
  os.system("raspistill -o /home/pi/Desktop/image"+`y`+".jpg -t 2000")
  x=0
#------------------------------------------------------#

########################################################
#                  Check Button(Drive)                 #
#------------------------------------------------------# 
 if upDrive == False:
  os.system("/home/pi/drive upload -f /home/pi/Desktop/image"+`y`+".jpg -p 0B8Sukf_bQDsYfk0wNm9YYktvN21mc1MtUHdhTDJ1Y0VXUkg4eUFWY3pPLVl4YzVpa2lzQkk")
#------------------------------------------------------#

########################################################
#                  Check Button(Dropbox)               #
#------------------------------------------------------#
 if upDB == False:
  os.system("Dropbox/Dropbox-Uploader/dropbox_uploader.sh upload "+"/home/pi/Desktop/image"+`y`+".jpg /home/pi/Dropbox/image"+`y`+".jpg")
#------------------------------------------------------#

########################################################
#                  Check Button(Facebook)              #
#------------------------------------------------------#
  if upFB == False:
   z=z+4
#------------------------------------------------------#

########################################################
#                  Upload Picture                      #
#------------------------------------------------------#

# Set time interval as 0.05 second delay
 time.sleep(0.05)   
