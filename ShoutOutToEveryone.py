import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
l = ["Rahul", "Nisahant", "Harry"]
text = "Shout out to"
for name in l:
    s = text+name
    speaker.Speak(s)
