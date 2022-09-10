# MAIN SCRIPT FOR THE PROJECT
# This GUI script imports the business logic keeping things separate

# Python Modules
import time
from guizero import App, Text, PushButton, Box, Window

# Import GUI windows
from gui.window_maintenance import window_maintenance

# Import business logic
#from app import doorbot

# App settings
app_name = "Doorbot"

# System variables
isAdmin = False
maintenance = []
last_updated = "1h ago"
info_flag = 0

def log_maintenance():
  global maintenance
  maintenance.append([time.localtime(), "Pump Failure"])

def clear_maintenance():
  global maintenance
  maintenance = []

def say_hello():
  global isAdmin
  isAdmin = not isAdmin

def status_icons():
  global maintenance, isAdmin, info_flag

  title_box.bg = "yellow2" if len(maintenance) else "green2"

  # Admin
  if(isAdmin):
    admin_txt.show()
    admin_btn.bg = "chartreuse2"
  else:
    admin_txt.hide()
    admin_btn.bg = "white"

  # Play icon (show it's alive)
  if(int(time.time()) % 2 == 0):
    status.value = " "
  else:
    status.value = "➤"

  if(int(time.time()) % 4 == 0):
    info_flag+=1
    if(info_flag == 2):
      info_flag = 0

  # Mainenance
  if(len(maintenance)):
    log_btn.bg = "yellow2"
    time_txt.value = "Maintenance is required"
    time_txt.text_color = "yellow2"
    warn_txt.show()
  else:
    log_btn.bg = "white"
    time_txt.text_color = "green2"
    warn_txt.hide()
    if(info_flag == 0):
      time_txt.value = "Date: " + time.strftime("%A %d %b %H:%M")
    elif(info_flag == 1):
      time_txt.value = "System running normally"
    else:
      time_txt.value = ""

def admin_check():
  global isAdmin

  if(isAdmin):
    log_btn.enable()
    activity_btn.enable()
  else:
    log_btn.disable()
    activity_btn.disable()

app = App(title=app_name, bg="white")
app.set_full_screen()
app.text_size = 26

# Header
title_box = Box(app, width="fill", align="bottom")
title_box.bg = "orange"
title_box.text_size = 40
title = Text(title_box, text= app_name + " ", align="left")
admin_txt = Text(title_box, align="right", visible=False, text="★")
warn_txt = Text(title_box, align="right", visible=False, text="⚠")
status = Text(title_box, text="INIT", align="right")
status.repeat(1000, status_icons)

# Footer
footer_box = Box(app, width="fill", align="bottom")
footer_box.bg = "black"
footer_box.text_size = 24
footer_box.text_color = "green2"
text = Text(footer_box, align="right")
time_txt = Text(footer_box, text="Loading...", align="left", size=28)

# Main
main = Box(app, width="fill", height="fill")
main.repeat(500, admin_check)

left_box = Box(main, width="fill", height="fill", align="left")
right_box = Box(main, width="fill", height="fill", align="right")

keypad_btn = PushButton(left_box, text="Read Keypad", command=say_hello, width="fill")
fob_btn = PushButton(right_box, text="Read Fob", command=say_hello, width="fill")
activity_btn = PushButton(left_box, text="Activity", enabled=False, command=say_hello, width="fill")
log_btn = PushButton(right_box, text="Logs", command=(lambda: show_window("maintenance")), enabled=False, width="fill")
admin_btn = PushButton(left_box, command=say_hello, text="Admin", width="fill")
maint_btn = PushButton(right_box, command=log_maintenance, text="Maintenance")

# Set up windows
maintenance_window = window_maintenance(app, clear_maintenance)

def show_window(key):
  maintenance_window.close_window()

  if(key=="maintenance"):
    maintenance_window.set_errors(maintenance)
    maintenance_window.show_window()

# Run!
app.display()

