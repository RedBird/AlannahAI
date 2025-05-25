#This page is for the CLI controller / entry point
# main.py
import sys
sys.path.append("./moviepy")

# Import display banner with ASCII art
from ascii_art import show_banner

# Import prompt logic (auto, manual, GPT)
from prompt_generator import get_prompt

# Import video generation logic (stub/API)
from video_generator import generate_video

# Import YouTube uploader
from youtube_uploader import upload_to_youtube

#__________________________________________
# f(x): main
# Purpose: Entry point for the AlannahAI app.
# Displays banner, lets user choose a prompt mode,
# generates video, and uploads to YouTube.
#____________________________________________
def main():
    # This f(x) shows the ASCII art Sphixes + title banner
    show_banner()

    # Display user menu
    print("\nChoose an option:")
    print("1. Auto-generate prompt (from list)")
    print("2. Enter prompt manually")
    print("3. Use GPT to generate idea")

    # Get user choice
    choice = input("Your choice (1, 2, or 3): ").strip()

    # Get prompt based on selected mode
    prompt = get_prompt(choice)

    # Generate video from the prompt
    video_path = generate_video(prompt)

    # Upload video to YouTube
    upload_to_youtube(video_path, prompt)

# Entry point check
if __name__ == "__main__":
    main()
