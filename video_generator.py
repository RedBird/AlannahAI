#This sectionb is what turns your prompt(s) into .mp4 stuff ;3
# video_generator.py

# video_generator.py
# Generates a narrated AI video from a prompt using free tools

import os
import requests
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from pydub import AudioSegment
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from dotenv import load_dotenv

# Load .env for API key
load_dotenv()
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")
HEADERS = {"Authorization": PEXELS_API_KEY} if PEXELS_API_KEY else {}

# Directory setup
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

#----------------------------------------
# f(x): fetch_image
# Purpose: Search Pexels for topic image or use fallback
#----------------------------------------
def fetch_image(query, out_path):
    if not PEXELS_API_KEY:
        print("[⚠] No Pexels API key found. Using fallback image.")
        fallback = Image.new("RGB", (1280, 720), color="black")
        draw = ImageDraw.Draw(fallback)
        draw.text((100, 300), f"{query}", fill="white")
        fallback.save(out_path)
        return out_path

    print(f"[📷] Searching Pexels for '{query}'...")
    try:
        res = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=1",
            headers=HEADERS
        )
        data = res.json()
        url = data['photos'][0]['src']['landscape']
        img_data = requests.get(url).content
        with open(out_path, 'wb') as f:
            f.write(img_data)
        return out_path
    except:
        print("[⚠] Failed to fetch from Pexels. Using blank image.")
        fallback = Image.new("RGB", (1280, 720), color="gray")
        fallback.save(out_path)
        return out_path

#----------------------------------------
# f(x): text_to_speech
# Purpose: Converts scene text to voice using gTTS
#----------------------------------------
def text_to_speech(text, out_path):
    tts = gTTS(text=text)
    tts.save(out_path)
    return out_path

#----------------------------------------
# f(x): generate_scene
# Purpose: Create a video clip with synced audio + image + text
#----------------------------------------
def generate_scene(scene_text, index):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = os.path.join(OUTPUT_DIR, f"scene_{index}_{timestamp}")
    image_path = fetch_image(scene_text.split()[0], base + ".jpg")
    audio_path = text_to_speech(scene_text, base + ".mp3")

    # Load audio duration
    audio = AudioFileClip(audio_path)
    duration = audio.duration

    # Create text overlay image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 600), scene_text, font=font, fill="white")
    img.save(base + "_captioned.jpg")

    # Create clip
    clip = ImageClip(base + "_captioned.jpg").with_duration(duration)
    clip = clip.with_audio(AudioFileClip(audio_path))
    return clip

#----------------------------------------
# f(x): generate_video
# Purpose: Master function to create full video from prompt
#----------------------------------------
def generate_video(prompt):
    print(f"\n[🎬] Generating video for: {prompt}")
    scenes = prompt.strip().split(".")
    scenes = [s.strip() for s in scenes if s.strip()]

    clips = []
    for i, scene in enumerate(scenes):
        print(f"[🧩] Scene {i+1}/{len(scenes)}")
        clips.append(generate_scene(scene, i))

    final = concatenate_videoclips(clips, method="compose")
    out_file = os.path.join(OUTPUT_DIR, "final_video.mp4")
    final.write_videofile(out_file, fps=24)

    print(f"\n[✅] Done! Video saved to: {out_file}")
    return out_file

