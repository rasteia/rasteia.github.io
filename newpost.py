import os
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

def move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path):
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

            # Run photo.py
            print(f"Running photo.py for {file}...")
            os.system(f"python {photo_script_path}")

def main():
    src_dir = 'C:/Users/darde/Downloads/jekyllposts'
    dest_dir = './_posts'
    template_path = './templatehead.txt'
    tts_script_path = './tts.py'
    photo_script_path = './image.py'

    move_and_process_posts(src_dir, dest_dir, template_path, tts_script_path, photo_script_path)

if __name__ == "__main__":
    main()
