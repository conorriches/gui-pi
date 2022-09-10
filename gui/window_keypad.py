import time
from guizero import Window, Text, PushButton, Waffle, Box

class window_keypad():

  def __init__(self, app):
    global window, error_list, callback, details_window, details_date_txt, details_text_txt

    window = Window(app, title="", bg="white")
    window.text_size = 20
    window.hide()
    window.set_full_screen()
    menu_box = Box(window, align="top")
    close_button = PushButton(menu_box, text="Close", align="left", command=self.close_window)
    close_button.bg = "honeydew"
  
    waffle_box = Box(window, align="bottom", height="fill", width="fill")
    help_text = Text(waffle_box, text="The waffle below indicates current key pressed", align="top")
    waffle = Waffle(waffle_box, height=4, width=3, color="gray", dim=40)

    # Current key being pressed
    current_key_box = Box(window, width="fill")
    current_key_box.bg = "cyan"
    Text(current_key_box, text="Current key:", align="left")
    current_key_text = Text(current_key_box, text="1", size = 80)

    # Sequence of keys
    sequence_key_box = Box(window, width="fill")
    Text(sequence_key_box, text="Sequenced key:", align="left")
    sequence_key_box.bg = "yellow"
    key_text = Text(sequence_key_box, text="1234567890", size = 40)


  def close_window(self):
    window.hide()

  def show_window(self):
    window.show()


