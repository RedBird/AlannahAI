#So This section is what Handels both auto + maunal prompt logic :3

import random
import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

# Load environment variables (like OPENAI_API_KEY) from .env file
load_dotenv()

# Get the OpenAI key securely from environment
api_key = os.getenv("OPENAI_API_KEY")

# Raise an error if the key isn't found
if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Make sure it's in your .env file.")

# Initialize OpenAI client (using SDK v1.0+)
client = OpenAI(api_key=api_key)

# _____________________________________
# f(x): get_prompt
# Purpose: Handles all prompt input logic
# Accepts: choice (str) — 1 for auto, 2 for manual, 3 for GPT
# Returns: A usable prompt (str)
# ______________________________________

def get_prompt(choice):
    # This is whre you can put all ur cool ideas (used in auto and GPT fallback)
    #anything in "blah, blah" fallowed by a , will be a sigle option
    prompt_bank = [
        "Top 5 free AI tools in 2025",
        "How to automate your content pipeline",
        "What is AlannahAI and how does it work?",
        "Intro to making YouTube videos with Python",
        "Why are Sphixs cats the greatest thing ever",
        "What Magical powers do Bunnys have"
    ]

    # Option 1: Pick a random topic from list in the promps 
    if choice == "1":
        prompt = random.choice(prompt_bank)
        print(f"\n[Auto-Generated Prompt]: {prompt}")
        return prompt

    # Option 2: creates a story: whatever you type will be the dialog for the video
    elif choice == "2":
        prompt = input("\nEnter your video idea: ").strip()
        return prompt

    # Option 3: Use OpenAI GPT to generate it
    elif choice == "3":
        try:
            print("\n[GPT Mode] Generating idea from OpenAI...\n")

            # Structure for chat completion input
            messages: list[ChatCompletionMessageParam] = [
                {"role": "system", "content": "You are a creative YouTube idea generator."},
                {"role": "user", "content": "Give me one YouTube video topic for a tech or AI channel."}
            ]

            # Make the GPT API call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            # Get the text result
            prompt = response.choices[0].message.content.strip()
            print(f"[GPT Prompt]: {prompt}")
            return prompt

        except Exception as e:
            # If GPT fails, fallback to static list
            print(f"[ERROR]: Could not reach GPT API. {e}")
            return random.choice(prompt_bank)

    # Invalid choice fallback
    else:
        print("\nInvalid option. Using default prompt.")
        return "Welcome to AlannahAI"
