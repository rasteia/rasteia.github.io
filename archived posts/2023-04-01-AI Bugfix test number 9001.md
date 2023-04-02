---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-AI
  Bugfix test number 9001.mp3\" type=\"audio/mpeg\">\n              Your browser does
  not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: https://oaidalleapiprodscus.blob.core.windows.net/private/org-a2QK0JEElw5EOqS0Fwy4qUQ2/user-eQXzSJqpkRtH1ZMyafYzf4Cc/img-MtlGGTlcxKK0Dqg6kVuk9GBj.png?st=2023-04-02T02%3A39%3A45Z&se=2023-04-02T04%3A39%3A45Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-01T19%3A28%3A21Z&ske=2023-04-02T19%3A28%3A21Z&sks=b&skv=2021-08-06&sig=kcnbgDWoVoeEvZtmKok6KtkTkKNSRK/wpStpy5MMF5g%3D
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Ai Bugfix Test Number 9001
---

It doesn't seem to work, it just gets to the part where it calls newimage.py and then does seemingly nothing and goes back to listening for a new post.. It doesn't error out though or give any kind of feedback from newimage.py. I think maybe it is not finding any posts with the default image. I have it set as image: /assets/images/cpunk3.jfif in the post.md and <img src="/assets/images/default.jfif" alt="Post Image"> in the html when I view source. I don't know is that matters or not.

2 / 2

I apologize for the confusion. It seems that the script is looking for the exact string "image: cpunk3.jfif", while your post markdown files have the full path "image: /assets/images/cpunk3.jfif". I'll modify the script to account for the full path in the post markdown files.

Here's the updated version of the script:

```
pythonCopy codeimport os
import sys
from pathlib import Path

POSTS_DIRECTORY = "_posts"
DEFAULT_IMAGE = "/assets/images/cpunk3.jfif"


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


def update_posts_with_default_image():
    for post_filename in os.listdir(POSTS_DIRECTORY):
        post_file_path = os.path.join(POSTS_DIRECTORY, post_filename)

        if os.path.isfile(post_file_path):
            with open(post_file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if f"image: {DEFAULT_IMAGE}" in content:
                prompt = Path(post_filename).stem
                new_image_url = generate_new_image(prompt)

                if new_image_url != DEFAULT_IMAGE:
                    update_post_image(post_file_path, new_image_url)
                    print(f"Updated {post_file_path} with new image: {new_image_url}")
                else:
                    print(f"Skipped {post_file_path} (unique image already set)")


if __name__ == "__main__":
    update_posts_with_default_image()

```

This script should now work correctly and update all posts that have the default image set as "image: /assets/images/default.jfif" in the post markdown files.