---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-02-ChatGPT
  Python GUI Setup.mp3\" type=\"audio/mpeg\">\n              Your browser does not
  support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-02'
image: /assets/images/2023-04-02-ChatGPT Python GUI Setup.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Chatgpt Python Gui Setup
---

Setup ChatGPT local Python GUI (TKINTER) Windows 64bit https://platform.openai.com/docs/api-reference/chat/create

2 / 2

To set up a local Python GUI using Tkinter for the ChatGPT API on a Windows 64-bit system, follow the steps below:

1.  Install Python and required packages

-   If you haven't installed Python yet, download the latest Python version for Windows 64-bit from [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and install it.
-   Open a command prompt or terminal, and install the required packages:

```
shCopy codepip install openai requests

```

2.  Obtain your API key

-   Visit [https://platform.openai.com/signup](https://platform.openai.com/signup) and sign up for an account.
-   Once logged in, navigate to the API Keys section to get your API key: [https://platform.openai.com/dashboard/api-keys](https://platform.openai.com/dashboard/api-keys)

3.  Create the Python script for the Tkinter GUI

-   Open your favorite text editor or IDE and create a new Python file (e.g., chatgpt\_tkinter.py).
-   Paste the following code into the file:

```
pythonCopy codeimport openai
import requests
import tkinter as tk
from tkinter import scrolledtext

openai.api_key = "your-api-key"  # Replace with your actual API key

def send_message(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def on_send_click():
    user_message = user_input.get()
    chat_history.insert(tk.END, f"User: {user_message}\n")
    user_input.delete(0, tk.END)
    chat_history.yview(tk.END)

    chat_history.insert(tk.END, f"AI: Thinking...\n")
    chat_history.yview(tk.END)
    root.update()

    ai_response = send_message(user_message)
    chat_history.insert(tk.END, f"AI: {ai_response}\n")
    chat_history.yview(tk.END)

root = tk.Tk()
root.title("ChatGPT Tkinter GUI")

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, padx=5, pady=5)
chat_history.grid(row=0, column=0, columnspan=2)

user_input = tk.Entry(root, width=50)
user_input.grid(row=1, column=0)

send_button = tk.Button(root, text="Send", command=on_send_click)
send_button.grid(row=1, column=1)

root.mainloop()

```

Make sure to replace `your-api-key` with your actual API key obtained from OpenAI.

4.  Run the script

-   Save the file and close the text editor or IDE.
-   Open a command prompt or terminal, navigate to the directory where you saved the Python file, and run the script:

```
shCopy codepython chatgpt_tkinter.py

```

This will launch the Tkinter GUI for the ChatGPT API. You can now interact with the ChatGPT model by entering text in the input field and clicking the "Send" button.

Please note that the code above uses the "text-davinci-002" engine, which may not be available for free users. Replace it with "text-davinci-001" or other available engines as per your subscription.

1 / 1

can you add a button to save the chat or clear it

1 / 1

Certainly! I'll add two buttons to the Tkinter GUI: one for saving the chat to a text file and another one to clear the chat history. Update your script with the following changes:

1.  Add two new functions for saving and clearing the chat:

```
pythonCopy codedef save_chat_history():
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write(chat_history.get(1.0, tk.END))
    chat_history.insert(tk.END, "Chat history saved to 'chat_history.txt'.\n")
    chat_history.yview(tk.END)

def clear_chat_history():
    chat_history.delete(1.0, tk.END)

```

2.  Add two new buttons for saving and clearing the chat:

```
pythonCopy code# Replace these lines
send_button = tk.Button(root, text="Send", command=on_send_click)
send_button.grid(row=1, column=1)

# With these lines
save_button = tk.Button(root, text="Save Chat", command=save_chat_history)
save_button.grid(row=1, column=1)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat_history)
clear_button.grid(row=1, column=2)

send_button = tk.Button(root, text="Send", command=on_send_click)
send_button.grid(row=1, column=3)

```

The updated script should look like this:

```
pythonCopy codeimport openai
import requests
import tkinter as tk
from tkinter import scrolledtext

openai.api_key = "your-api-key"  # Replace with your actual API key

def send_message(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

def on_send_click():
    user_message = user_input.get()
    chat_history.insert(tk.END, f"User: {user_message}\n")
    user_input.delete(0, tk.END)
    chat_history.yview(tk.END)

    chat_history.insert(tk.END, f"AI: Thinking...\n")
    chat_history.yview(tk.END)
    root.update()

    ai_response = send_message(user_message)
    chat_history.insert(tk.END, f"AI: {ai_response}\n")
    chat_history.yview(tk.END)

def save_chat_history():
    with open("chat_history.txt", "w", encoding="utf-8") as file:
        file.write(chat_history.get(1.0, tk.END))
    chat_history.insert(tk.END, "Chat history saved to 'chat_history.txt'.\n")
    chat_history.yview(tk.END)

def clear_chat_history():
    chat_history.delete(1.0, tk.END)

root = tk.Tk()
root.title("ChatGPT Tkinter GUI")

chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, padx=5, pady=5)
chat_history.grid(row=0, column=0, columnspan=4)

user_input = tk.Entry(root, width=50)
user_input.grid(row=1, column=0)

save_button = tk.Button(root, text="Save Chat", command=save_chat_history)
save_button.grid(row=1, column=1)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat_history)
clear_button.grid(row=1, column=2)

send_button = tk.Button(root, text="Send", command=on_send_click)
send_button.grid(row=1, column=3)

root.mainloop()

```

Now you should see two new buttons in the GUI: "

1 / 1