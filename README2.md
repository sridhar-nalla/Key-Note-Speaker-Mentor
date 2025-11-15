## Overview

This project contains a modular multi-agent system to:

. generate PowerPoint presentations from prompts

. edit existing PPTX files and add speaker notes

. evaluate spoken practice sessions (ASR + scoring)

. generate a narrated avatar video (open-source pipeline skeleton)

The code is written for portability on Kaggle: pure Python, Hugging Face models, and local libraries. Replace HF checkpoints with available Kaggle-friendly model files if needed.


### Folder structure

ai-presentation-assistant/
├─ README.md
├─ requirements.txt
├─ agents.py                # Main agent router
├─ tools/
│  ├─ __init__.py
│  ├─ pptx_helper.py        # create/edit PPTX
│  ├─ slides_templates.py   # slide templates and helpers
│  └─ audio_analysis.py     # ASR + scoring utilities
├─ agents/
│  ├─ presentation_agent.py
│  ├─ editor_agent.py
│  ├─ audio_agent.py
│  └─ video_agent.py
├─ notebooks/
│  └─ kaggle_starter.py     # notebook-friendly runner
└─ assets/
   └─ sample_template.pptx


### requirements.txt 
python-pptx==0.6.21
pillow
torch
transformers
accelerate
librosa
soundfile
gradio
moviepy
whisper @ git+https://github.com/openai/whisper.git
ffmpeg-python
numpy
scikit-learn

Note: On Kaggle you may need to adjust package versions and install system packages like ffmpeg.


# AI Presentation Assistant (Kaggle Capstone)

Run the `notebooks/kaggle_starter.py` to try example flows. The project demonstrates PPT generation, ASR-based feedback, and a skeleton for avatar-based narrated video.

See docs in the canvas for how to adapt to Kaggle restrictions.