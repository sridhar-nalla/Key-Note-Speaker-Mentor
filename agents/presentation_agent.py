# agents/presentation_agent.py
from tools.pptx_helper import create_basic_presentation

class PresentationAgent:
    def __init__(self, llm=None):
        self.llm = llm

    def prompt_to_outline(self, prompt: str, num_slides: int = 8):
        # placeholder: replace with your LLM call
        # output should be list of slides: [{'title':'...','bullets':[...],'notes':'...'}, ...]
        slides = []
        for i in range(num_slides):
            slides.append({
                'title': f'{prompt} — Slide {i+1}',
                'bullets': [f'Point {i+1}.1','Point {i+1}.2'],
                'notes': f'Speaker notes for slide {i+1}.'
            })
        return slides

    def create_from_prompt(self, prompt: str, out_path='output.pptx'):
        outline = self.prompt_to_outline(prompt)
        return create_basic_presentation(outline, out_path=out_path)