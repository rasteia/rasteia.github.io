---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-New
  post image generation..mp3\" type=\"audio/mpeg\">\n              Your browser does
  not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: https://oaidalleapiprodscus.blob.core.windows.net/private/org-a2QK0JEElw5EOqS0Fwy4qUQ2/user-eQXzSJqpkRtH1ZMyafYzf4Cc/img-2cuyCbJJM3sJ5cqVyvhz5uxD.png?st=2023-04-02T01%3A26%3A54Z&se=2023-04-02T03%3A26%3A54Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-01T19%3A35%3A21Z&ske=2023-04-02T19%3A35%3A21Z&sks=b&skv=2021-08-06&sig=cCLnuvgClECOsGfomUNM11BQEIwU9MVnI8uim6GRUW0%3D
layout: post
tags:
- categories
- AI
- tutorial
- template
title: New Post Image Generation.
---

\# Python create newimage.py based on gennewimageallposts.py --all # We are building the functionality for streamlining new https://aitech.tips blog posts. # I am streamlining the jekyll blogpost creation process to take a markdown file from # the web via a browser exension into a published blog post with auto generated tts # via google api in tty.py and then update the post with an image that is auto # generated from dall-e api. # In the repository https://github.com/rasteia/rasteia.github.io you will notice newpost.py, gennewimageallposts.py, and tts,py # I have more updates to the process to see the streamlined process fully working. # newposts.py works, it monitory for new posts and then processes them and creates the tts with tts.py # tts.py works, it creates the tts for the post and updates the post with the tts. But I do need to add the fenced code block removal. # newpost.py is almost finished, we just need to add the image generation and update the post with the new image. # gennewimageallposts.py works, it generates a new image for all the posts in the \_posts directory. # It also updates the posts with the new image. But image generation is not called from newpost.py yet. # So Mainly right now we need to create a newimage.py based on gennewimageallposts.py --all # because now that I updated all my old posts I don't need to update all anymore only new posts. # So istead of all posts updated, only generate a new image for any new posts then update the post with the new image. # I am not sure I will need the loop to continually check for posts in new image.py # because I think I can just have newpost.py # We can call newimage.py to update any new post with a defauly image to a new image. # newimage.py will be called from newpost.py or manually in command prompt # The prompt for the api will be the post filename without the .md extension. ###### # Also possible bugs to avoid and pre-emptivelyy fix: # The new image.py is not generating the new image for the new post. # The new image.py has problems when it is called from newpost.py # The new image.py is updating old posts with the new image instead of the new post. # The new image.py is not updating the new post with the new image.

1 / 1

Here's a new version of the `gennewimageallposts.py` file tailored to generate a new image only for the new post. I've named it `newimage.py`.

```
pythonCopy codeimport os
import subprocess
import re
import sys

from pathlib import Path

POSTS_DIRECTORY = "_posts"
DEFAULT_IMAGE = "default-image.jpg"


def update_post_image(filename, new_image_url):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()

    for index, line in enumerate(content):
        if line.startswith("image:"):
            content[index] = f"image: {new_image_url}\n"
            break

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(content)


def generate_new_image(prompt):
    # Replace this with your Dall-E API code to generate a new image using the prompt
    # For now, we're just returning the default image.
    return DEFAULT_IMAGE


def main():
    if len(sys.argv) < 2:
        print("Usage: python newimage.py <post_filename>")
        sys.exit(1)

    post_filename = sys.argv[1]
    post_file_path = os.path.join(POSTS_DIRECTORY, post_filename)

    if not os.path.isfile(post_file_path):
        print(f"Post file not found: {post_file_path}")
        sys.exit(1)

    prompt = Path(post_filename).stem
    new_image_url = generate_new_image(prompt)

    update_post_image(post_file_path, new_image_url)
    print(f"Updated {post_file_path} with new image: {new_image_url}")


if __name__ == "__main__":
    main()


```

To use this script, call it from `newpost.py` or manually in the command prompt providing the new post filename as an argument.

In `newpost.py`, you can add the following code to call the `newimage.py` script after generating the TTS:

```
pythonCopy codeimport subprocess

# ... other code ...

def process_new_post(post_filename):
    # ... other processing code ...
    
    # Call the newimage.py script to update the post with a new image
    subprocess.run(["python", "newimage.py", post_filename])

# ... other code ...

```

This should resolve your primary concerns. Make sure to replace the `generate_new_image` function in `newimage.py` with the actual Dall-E API code.

Regarding the potential bugs mentioned, the provided code should avoid those issues. It doesn't loop through all posts, and it only updates the specified post with the new image.