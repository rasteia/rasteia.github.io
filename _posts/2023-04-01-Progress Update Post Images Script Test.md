---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Progress
  Update Post Images Script Test.mp3\" type=\"audio/mpeg\">\n              Your browser
  does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-progress-update-post-images-script-test.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Progress Update Post Images Script Test
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

Replace the placeholders with your actual `newpage.py` code, and make sure to call `run_tts()` and `run_newimage()` at the appropriate place in your script (e.g., in your main function or at the end of your script). This will ensure that `newimage.py` is executed after `tts.py`.Ok we have feedback and progress. it updates the posts that have the default image. But it only works when I run newimage.py directly. I want newpage.py to run it after the tts.py

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

Replace the placeholders with your actual `newpage.py` code, and make sure to call `run_tts()` and `run_newimage()` at the appropriate place in your script (e.g., in your main function or at the end of your script). This will ensure that `newimage.py` is executed after `tts.py`.Ok we have feedback and progress. it updates the posts that have the default image. But it only works when I run newimage.py directly. I want newpage.py to run it after the tts.py

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

Replace the placeholders with your actual `newpage.py` code, and make sure to call `run_tts()` and `run_newimage()` at the appropriate place in your script (e.g., in your main function or at the end of your script). This will ensure that `newimage.py` is executed after `tts.py`.Ok we have feedback and progress. it updates the posts that have the default image. But it only works when I run newimage.py directly. I want newpage.py to run it after the tts.py

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