# agents/audio_agent.py
import whisper
from tools.audio_analysis import compute_wpm, filler_word_score

class AudioAgent:
    def __init__(self, model_name='small'):
        # load whisper model (may need GPU on Kaggle)
        self.model = whisper.load_model(model_name)

    def transcribe(self, audio_path: str):
        res = self.model.transcribe(audio_path)
        return res['text'], res

    def evaluate(self, audio_path: str, reference_ppt: str = None):
        transcript, full = self.transcribe(audio_path)
        wpm, duration = compute_wpm(audio_path, transcript)
        filler = filler_word_score(transcript)
        # simple scoring heuristics
        score = max(0, 100 - filler*5 - abs(wpm-130)*0.2)
        return {
            'transcript': transcript,
            'wpm': wpm,
            'duration': duration,
            'filler_count': filler,
            'score': round(score,1)
        }