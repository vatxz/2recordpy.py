import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import os

FOLDER_NAME = "vasp_ab"


def create_folder():
  if not os.path.isdir("FOLDER_NAME"):
     os.mkdir("FOLDER_NAME")

class Rec:
    def __init__(self):
      create_folder()
      self.count = 0

    def photo(self):
        x, y = pg.position()
        photo = pg.screenshot(region=(x - 3, y, - 3, 6, 6))
        photo.save(f"{FOLDER_NAME}/flag_(self.count).png")
        self.count = self.count + 1
  
    def key_code(self, key):
        if key == keyboard.key.esc:
            return False
       if key == keyboard.key.insert:
           self.photo()

    def start(self):
        with Listener(on_press=self.key_code) as listener:
             listener.join()

record = Rec()
record.start()
