from ascii_art import show_banner
from prompt_generator import auto_prompt
from video_generator import generate_video
from youtube_uploader import upload_to_youtube

def menu():
    print("\nChoose an option:")
    print("1. Auto-generate prompt")
    print("2. Enter prompt manually")
    choice = input("Your choice (1 or 2): ")

    if choice == "1":
        prompt = auto_prompt()
    else:
        prompt = input("Enter your video prompt: ")

    print(f"\nPrompt: {prompt}")
    video_file = generate_video(prompt)
    upload_to_youtube(video_file, prompt)

if __name__ == "__main__":
    show_banner()
    menu()
