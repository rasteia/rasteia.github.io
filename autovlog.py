# autoblog.py

from moviepy.editor import *
import os
import re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def generate_video(background_image, tts_mp3, output_video, text_content):
    # Load the background image and the TTS MP3 file
    image_clip = ImageClip(background_image)
    audio_clip = AudioFileClip(tts_mp3)

    # Set the duration of the image clip to match the duration of the audio clip
    image_clip = image_clip.set_duration(audio_clip.duration)

    # Create a TextClip with your desired text content, font, size, and color
    text_clip = TextClip(text_content, fontsize=50, color='white', font='Arial-Bold')
    text_clip = text_clip.set_position('center').set_duration(audio_clip.duration)

    # Overlay the text on the background image
    final_clip = CompositeVideoClip([image_clip, text_clip])

    # Set the audio of the final clip to the TTS MP3 file
    final_clip = final_clip.set_audio(audio_clip)

    # Write the final video to a file
    final_clip.write_videofile(output_video, fps=24, codec='libx264')


def process_blog_posts(posts_dir, audio_dir, default_youtube_link, background_image):
    for file in os.listdir(posts_dir):
        if file.endswith(".md"):
            file_path = os.path.join(posts_dir, file)

            with open(file_path, 'r', encoding='utf-8') as post_file:
                content = post_file.read()

            # Check if the post contains the default YouTube link
            if default_youtube_link in content:
                # Extract date and title from the filename
                date, title = os.path.splitext(file)[0].split('-', 1)

                # Create the path to the TTS MP3 file
                tts_mp3 = os.path.join(audio_dir, f'{date}-{title}.mp3')

                # Check if the TTS MP3 file exists
                if os.path.isfile(tts_mp3):
                    # Generate the video using the generate_video function
                    output_video = f'output_videos/{date}-{title}.mp4'
                    generate_video(background_image, tts_mp3, output_video, title.replace('-', ' '))
                    print(f"Video generated: {output_video}")


if __name__ == "__main__":
    posts_dir = '_posts'
    audio_dir = 'assets/audio'
    default_youtube_link = 'https://www.youtube.com/watch?v=ZXJXK8diCPU'  # Replace with your default YouTube link
    background_image = 'background.jpg'  # Replace with the path to your background image

    # Create a directory for output videos if it doesn't exist
    if not os.path.exists('output_videos'):
        os.makedirs('output_videos')

    process_blog_posts(posts_dir, audio_dir, default_youtube_link, background_image)
