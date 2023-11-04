# audio_processing/audio_processing.py
import os
from pydub import AudioSegment
from audio_processing.sibilance_removal import remove_sibilance
from audio_processing.plosive_removal import remove_plosive

def process_audio(audio_file, remove_sibilance_flag, remove_plosive_flag):
    audio = AudioSegment.from_file(audio_file)

    if remove_sibilance_flag:
        audio = remove_sibilance(audio_file)

    if remove_plosive_flag:
        audio = remove_plosive(audio_file)

    return audio
