---
audio_embed_code: "\n            <audio controls>\n              <source src=\"/assets/audio/2023-04-01-Jekyll
  Workflow Auto Add Post and Process.mp3\" type=\"audio/mpeg\">\n              Your
  browser does not support the audio element.\n            </audio>\n            "
categories:
- AI
- tutorial
date: '2023-04-01'
image: /assets/images/2023-04-01-jekyll-workflow-auto-add-post-and-process.png
layout: post
tags:
- categories
- AI
- tutorial
- template
title: Jekyll Workflow Auto Add Post And Process
---

create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.create a new script to automatically detect new md files in C:\\Users\\darde\\Downloads\\jekyllposts then process it to include append my templatehead.md (contains my audio\_embed\_code, categories, tags, name, image, date, layout, and title to the beginning of the post before moving it to the \_posts directory and running the tts.py. Then at some point in the process update the date with current date, update the title using the filename, ignoring the file extension and replacing hyphens with spaces Capitalize with title format, don't forget to update the filename in \_posts with the date.


Here's a script that does the following:

1.  Detects new markdown files in the specified directory (`C:\Users\darde\Downloads\jekyllposts`).
2.  Appends the content of `templatehead.md` to the beginning of the post.
3.  Updates the date with the current date, and the title based on the filename.
4.  Moves the file to the `_posts` directory with an updated filename.
5.  Runs `tts.py` to generate the audio file.

Please make sure to adjust the paths according to your setup before running the script.


Here's the updated script:


```
pythonCopy codeimport os
import shutil
import datetime
import frontmatter
import yaml
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
                template = frontmatter.load(f)

            # Update the post's front matter with the template's metadata
            for key, value in template.metadata.items():
                post.metadata[key] = value

            # Update title and date
            update_title_and_date(post, file)

            # Move and update post
            current_date = datetime.datetime.now().strftime('%Y-%m-%d')
            new_file = f"{current_date}-{os.path.splitext(file)[0]}.md"
            dest_file_path = os.path.join(dest_dir, new_file)

            with open(dest_file_path, 'w', encoding='utf-8') as f:
                f.write(''.join(['---\n', yaml.safe_dump(post.metadata), '---\n', post.content]))

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

This updated script serializes the front matter as a string using `yaml.safe_dump()` before writing it to the file with `f.write()`. This should resolve any `TypeError` issue.