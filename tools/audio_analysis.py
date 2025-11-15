# tools/audio_analysis.py
import librosa
import numpy as np


def compute_wpm(audio_path, transcript_text):
    # simple words per minute estimate
    y, sr = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=y, sr=sr)
    words = len(transcript_text.split())
    wpm = words / (duration/60.0)
    return wpm, duration


def filler_word_score(transcript, filler_words=None):
    if filler_words is None:
        filler_words = ['um','uh','you know','like','so']
    t = transcript.lower()
    count = sum(t.count(w) for w in filler_words)
    return count