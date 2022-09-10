from guizero import Window, Text, PushButton, ListBox, Box
import time
import pigpio
import wiegand

class Doorbot():
  def __init__(self):
    print("doorbot init")
    global pi, w
    pi = pigpio.pi()
    w = wiegand.decoder(pi, 14, 15, self.wiegand_callback)
 
  def __del__(felf):
   w.cancel()
   pi.stop()

  def __read_keypad():
    print("read keypad")

  def __wiegand_callback(bits, code):
    print("bits={} code={}".format(bits, code))

