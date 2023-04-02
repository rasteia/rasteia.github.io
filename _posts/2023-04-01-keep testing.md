---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-keep
  testing.mp3\" type=\"audio/mpeg\">\n              Your browser does not support
  the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: https://oaidalleapiprodscus.blob.core.windows.net/private/org-a2QK0JEElw5EOqS0Fwy4qUQ2/user-eQXzSJqpkRtH1ZMyafYzf4Cc/img-q5cTdofINddsp3eQ6BFEAG6h.png?st=2023-04-02T01%3A54%3A05Z&se=2023-04-02T03%3A54%3A05Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-01T18%3A40%3A34Z&ske=2023-04-02T18%3A40%3A34Z&sks=b&skv=2021-08-06&sig=3eP2SGzcMRiAWioSkV7wvzgv0wDerZFyzPlWEEDQbdA%3D
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Keep Testing
---

Ok we have feedback and progress. it updates the posts that have the default image. But it only works when I run newimage.py directly. I want newpage.py to run it after the tts.py

2 / 2

To run `newimage.py` from within `newpage.py` after `tts.py` is executed, you can use the `subprocess` module to run the script as a separate process. Here's an example of how you can modify `newpage.py` to run `tts.py` and then `newimage.py`:

```
pythonCopy codeimport subprocess

# Your newpage.py code here

def run_tts():
    try:
        subprocess.check_call(["python", "tts.py"])
        print("Finished running tts.py")
    except subprocess.CalledProcessError as e:
        print(f"Error running tts.py: {e}")

def run_newimage():
    try:
        subprocess.check_call(["python", "newimage.py"])
        print("Finished running newimage.py")
    except subprocess.CalledProcessError as e:
        print(f"Error running newimage.py: {e}")

# In your main function or at the end of your script
run_tts()
run_newimage()

```

Replace the placeholders with your actual `newpage.py` code, and make sure to call `run_tts()` and `run_newimage()` at the appropriate place in your script (e.g., in your main function or at the end of your script). This will ensure that `newimage.py` is executed after `tts.py`.