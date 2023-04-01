---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Jekyll\
  \ Workflow File Location.mp3\" type=\"audio/mpeg\">\n              Your browser\
  \ does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/cpunk3.jfif
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Jekyll Post Processing
---
create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.txt (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.

Have it give feedback what it is doing.

I've updated the script to provide feedback. Here's the modified script:

```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
from pathlib import Path

def update_title_and_date(post, file):
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    post.metadata['date'] = current_date
    title = os.path.splitext(file)[0].replace('-', ' ').title()
    post.metadata['title'] = title

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path):
    for file in os.listdir(src_dir):
        if file.endswith('.md'):
            print(f"Processing {file}...")

            src_file_path = os.path.join(src_dir, file)
            with open(src_file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)

            with open(template_path, 'r', encoding='utf-8') as f:
                template_head = f.read()

            # Append template_head to post content
            post.content = template_head + post.content

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

            # Remove the original file from the source directory
            os.remove(src_file_path)
            print(f"Moved {file} to {dest_file_path}")

            # Run tts.py
            print(f"Running tts.py for {file}...")
            os.system(f"python {tts_script_path}")

def main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'

    move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path)

if __name__ == "__main__":
    main()

```

Now the script will print out information about its progress, including the current file it's processing, the destination path of the processed file, and when it's running the `tts.py` script for each file.