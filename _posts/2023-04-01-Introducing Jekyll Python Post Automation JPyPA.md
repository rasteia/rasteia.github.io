---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Introducing
  Jekyll Python Post Automation JPyPA.mp3\" type=\"audio/mpeg\">\n              Your
  browser does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: https://oaidalleapiprodscus.blob.core.windows.net/private/org-a2QK0JEElw5EOqS0Fwy4qUQ2/user-eQXzSJqpkRtH1ZMyafYzf4Cc/img-GBPvSo8CLn6pQkIuv1KUocnN.png?st=2023-04-02T02%3A39%3A51Z&se=2023-04-02T04%3A39%3A51Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-02T00%3A18%3A02Z&ske=2023-04-03T00%3A18%3A02Z&sks=b&skv=2021-08-06&sig=NWuYhHkTuLy3tBYI70RwaJsPf3xeMgNcOiunZEpr7CY%3D
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Introducing Jekyll Python Post Automation Jpypa
---

# Jekyll Python Post Automation (JPyPA)

Jekyll Python Post Automation (JPyPA) is a set of Python scripts that work together to automate the process of creating new blog posts in Jekyll and pushing them to GitHub Pages. The system automatically processes new Markdown files placed in the `jekyllposts` folder, generating a text-to-speech audio file, updating the post's image, and pushing the changes live to your GitHub Pages site in real-time.

## How it works

JPyPA consists of the following Python scripts:

1.  `newpost.py`: Monitors the `jekyllposts` folder for new Markdown files, processes them, and moves them to the Jekyll `_posts` directory.
2.  `tts.py`: Converts the text content of a post to an audio file using text-to-speech.
3.  `newimage.py`: Updates the post's image based on the post's title and content.

When you save a new Markdown file in the `jekyllposts` folder, `newpost.py` detects the file and processes it in the following sequence:

1.  Copies the metadata from the `templatehead.txt` file to the new post.
2.  Updates the post title and date.
3.  Moves the processed file to the `_posts` directory and removes the original file from `jekyllposts`.
4.  Calls `tts.py` to generate an audio version of the post.
5.  Calls `newimage.py` to update the post's image.
6.  Pushes the changes to your GitHub Pages repository, making the post live.

## Usage

1.  Install the [MarkDownload] Chrome extension to easily save web content as Markdown.
2.  Configure the extension to save downloaded content to the `jekyllposts` folder.
3.  When you find interesting content on the web, use the MarkDownload extension to save it as a Markdown file in the `jekyllposts` folder.
4.  The JPypA system will automatically process the new file and make it live on your GitHub Pages site moments later.

With JPyPA, you can quickly and easily create new blog posts from web content, complete with text-to-speech audio and relevant images, and have them go live on your site in real-time.