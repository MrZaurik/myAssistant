import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = {"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"}

audio_file = open("Grabación.m4a", "rb")

transcription = openai.Audio.transcribe("whisper-1", audio_file)

print('The Result is: ', transcription)