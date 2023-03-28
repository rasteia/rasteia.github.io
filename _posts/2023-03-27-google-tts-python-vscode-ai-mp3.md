---
layout: post
title: "Text to Speech with Google TTS and Visual Studio Code AI Tutorial"
date: 2023-03-27
categories: tutorial
---

## Best way to generate text to mp3 audio for free

There are several free text-to-speech (TTS) tools available online that can help you convert text to mp3 audio. Here are some popular ones:

## Google Text-to-Speech:
Google's TTS engine is one of the best free options available. You can use the "gTTS" (Google Text-to-Speech) Python library to convert text to mp3. This requires basic knowledge of Python programming. Here's a simple example to get you started:

## My Friendly AI copiliot, write a jekyll blog post in markdown for any readers following along with me.

Sure! Here's the content as a Jekyll post in Markdown format. Save this as a new file with a ".md" extension in the "_posts" folder of your Jekyll site, and name it using the format "YYYY-MM-DD-title.md" (e.g., "2023-03-28-text-to-speech-with-google-tts-and-vs-code.md"):

In this tutorial, we will create a simple Python script using Visual Studio Code (VS Code) to convert text to mp3 using Google Text-to-Speech (gTTS).

## Prerequisites

1. Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Install [Python](https://www.python.org/downloads/)

## Steps

### Step 1: Configure Python in VS Code

Open VS Code, and install the Python extension from the Visual Studio Code Marketplace. Search for "Python" and click "Install" for the one published by Microsoft.

### Step 2: Create a new Python file

In VS Code, click "File" > "New File" and save it with a ".py" extension, like "text_to_speech.py".

### Step 3: Install gTTS

Open the integrated terminal in VS Code by clicking "Terminal" > "New Terminal". Then, type the following command to install the gTTS library:

```bash
pip install gtts
```
### Step 4: Write the script
In the "text_to_speech.py" file, copy and paste the following code:

```python
from gtts import gTTS
import os

text = "Your text goes here"
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")
os.system("start output.mp3")
```
Replace "Your text goes here" with the text you want to convert to speech. You can also change the language by modifying the 'language' variable.

### Step 5: Run the script
Save the file by clicking "File" > "Save" or pressing Ctrl+S. In the terminal, navigate to the folder containing your "text_to_speech.py" file using the cd command, e.g., cd Desktop. Then, run the script with the following command:

```python
python text_to_speech.py
```

This will generate an "output.mp3" file in the same folder as your script and start playing the audio.

That's it! You've successfully created a Python script in Visual Studio Code to convert text to mp3 using Google Text-to-Speech. You can modify the script to read text from a file or user input, depending on your needs.

```vbnet
This Markdown-formatted Jekyll post can be added to your Jekyll blog. Once you have added it to the "_posts" folder, build and serve your site with `jekyll serve`, and you should see the new post on your blog.
```