import time

from servo import Servo

s12 = Servo(pin_id = 2)
s11 = Servo(pin_id = 26)
s21 = Servo(pin_id = 0)
s22 = Servo(pin_id = 1)
s22 = Servo(pin_id = 1)

r11 = Servo(pin_id = 22)
r12 = Servo(pin_id = 27) 
r21 = Servo(pin_id = 28) 
r22 = Servo(pin_id = 3) 



while True:
   s12.write(90)
   s11.write(90)
   s21.write(90)
   s22.write(90)
   r11.write(90)
   r12.write(90)
   r21.write(90)
   r22.write(90)
   time.sleep(2)
   
   #pie
   s12.write(90)
   s11.write(90)
   s21.write(90)
   s22.write(90)
   r11.write(160)
   r12.write(20)
   r21.write(160)
   r22.write(20)
   time.sleep(0.25)
   
   #1
   s12.write(90)
   s11.write(90)
   s21.write(90)
   s22.write(90)
   r11.write(160)
   r12.write(20)
   r21.write(120)
   r22.write(20)
   time.sleep(0.25)
   
   s12.write(160)
   s11.write(90)
   s21.write(70)
   s22.write(90)
   r11.write(160)
   r12.write(40)
   r21.write(140)
   r22.write(20)
   time.sleep(1)
   
   s12.write(160)
   s11.write(90)
   s21.write(70)
   s22.write(90)
   r11.write(160)
   r12.write(20)
   r21.write(160)
   r22.write(20)
   time.sleep(1)
   
   
   
   """
   s12.write(160)
   s11.write(70)
   s21.write(145)
   s22.write(40)
   r11.write(160)
   r12.write(20)
   r21.write(160)
   r22.write(20)
   time.sleep(1)
   
   s12.write(160)
   s11.write(70)
   s21.write(145)
   s22.write(40)
   r11.write(160)
   r12.write(40)
   r21.write(160)
   r22.write(20)
   time.sleep(1)
   """
   
