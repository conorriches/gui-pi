import time
from guizero import Window, Text, PushButton, ListBox, Box

class Window_Maintenance():

  def __init__(self, app, cb):
    global window, error_list, callback, details_window, details_date_txt, details_text_txt

    window = Window(app, title="", bg="white")
    window.text_size = 20
    window.hide()
    window.set_full_screen()
    menu_box = Box(window, align="top")
    close_button = PushButton(menu_box, text="Close", align="left", command=self.close_window)
    close_button.bg = "honeydew"
    clear_button = PushButton(menu_box, text="Clear", align="right", command=self.__clear)
    clear_button.bg = "mistyrose"
    error_list = ListBox(window, items=[], width="fill", align="bottom", height="fill", command=self.show_details)
    callback = cb

    details_window = Window(app, bg="black")
    details_window.hide()
    details_window.set_full_screen()
    close_details_button = PushButton(details_window, text="Close", align="top", width="fill", command=self.hide_details)
    close_details_button.bg = "honeydew"
    details_date_txt = Text(details_window, align="top", width="fill")
    details_date_txt.bg = "red"
    details_text_txt = Text(details_window, color="white", width="fill", height="fill")

  def close_window(self):
    window.hide()

  def show_window(self):
    window.show()

  def show_details(self, item):
    global details_text_txt, details_date_txt
    split = item.split(" ", 2)
    date = " ".join(split[:2])
    text = " ".join(split[2:])
    details_date_txt.value = date
    details_text_txt.value = text
    details_window.show()

  def hide_details(self):
    details_window.hide()

  def set_errors(self, errors):
    global error_list
    error_list.clear()
    for val in errors:
      error_list.append(time.strftime("%Y-%m-%d %H:%M:%S", val[0]) + " " + val[1])

  def __clear(self):
    global callback, error_list
    error_list.clear()
    callback()



