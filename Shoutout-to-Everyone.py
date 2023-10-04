# Write a program to pronounce list of names using win32 API.

import win32com.client as win

speaker = win.Dispatch("SAPI.SpVoice")

list = ["Sandeep Verma", "Manish Puri Goswami", "Vandana Pandey", "Gautam Negi", "Kavya Verma", "Naveen Sajwan", "Vikas Yadav", "Molester Mehra"]

for name in list:
    print(f"Shoutout to {name}")
    speaker.speak(f"Shoutout to {name}")
