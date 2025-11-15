# Key-Note-Speaker-Mentor
An agentic system to prepare content for key note speaker, helps with rehearsals and shares feedback on improvements

### Problem Statement (PPT + avatar + audio scoring)
Often, corporate people struggle with content creation and presenting it to bigger group leads to missing main points, deviating from the topic. This agentic system, creates, guides on the key notes, reviews the recorded content and shares the feedback on further improving the speech. 

### Why agents? -- Why are agents the right solution to this problem
The solution acts as an assistant who processes user prompt to generate key notes by either considering user prompt to generate a presentation (ppt) or upload an existing presentation to generate the Key Notes. 
The solution requires multiple agents, i.e. assistant agent to process user inputs (prompts), 2nd agent to process the uploaded presentation, 3rd agent is to create the Key Notes. Advanced solution, will have two more agents I.e. 4th agent to process the recorded presentation for critic/share improvements. 5th agent, will be able to generate a video with an Avatar presenting the Key Notes with appropriate  visuals.

### What you created -- What's the overall architecture? 
Steps # Generate a PowerPoint (PPTX) from a prompt, Edit an existing PPT, Practice Mode – User speaks, agent listens, Video Generation with Avatar
In this architecture, assistant will generate Key Notes based on user prompt by creating a presentation (ppt) or process an existing presentation if it was uploaded or made available in a location using the agent/tools.
Once the presentation is made available, then Key Notes are generated as Foot notes for each slide so that speaker can rehearsal it.
Audio feedback agent, will process the user uploaded rehearsal content and shares it feedback for further improvements/to make it outstanding.
Advanced level agent will be able to create video with an avatar presenting it. 

 PresentationAgent
     ├── PPT Creator Tool (python-pptx)
     ├── PPT Editor Tool (python-pptx)
     ├── Speaker Notes Generator Tool
     ├── Avatar Video Generator Agent
     ├── Audio Feedback Agent
           ├── ASR Tool (Whisper)
           ├── Speech Analysis Tool
           ├── Scoring Tool

### Demo -- Show your solution 
YouTube link # https://studio.youtube.com/playlist/PLa4uJnqmRsmoobk_SMCkbZ4ZrIpdvE655/videos

### The Build -- How you created it, what tools or technologies you used.
Generate a PowerPoint (PPTX) from a prompt, using HuggingFace/gemini models, Python, Audio libraries

📌 1. PPT Creation Agent
Tools:
To create slides & speaker notes, the tool used is “python-pptx”, 
to add images “pillow + python-pptx”
Generate content “Gemini”

Design Plan
	1.	User gives a prompt:
			“Create a PPT on Quantum Computing for Beginners (10 slides)”
	2.	Model converts prompt → outline
	3.	Outline → slide generator
	4.	For each slide:
		•	Title
		•	Bullet points
		•	Images (optional)
		•	Speaker notes
	5.	Export as output.pptx
📌 2. Existing PPT Editor Agent
Tools:
To add/improve speaker notes/slides, the tool used is “python-pptx”, 
to add images “pillow + python-pptx”
Generate content “Gemini”

📌 3. Audio Practice + Feedback Agent

Pipeline # 
User Audio —> ASR —> Text —> Speech Analyser —> Scoring —> Feedback

Tools#
Speech-to-text => Whisper-large-v3 (HF)
Filter word detection => Regex + LLM
Pace analysis => words/min
Confidence analysis => prosody (energy, pitch) using librosa
Alignment with slides => Compare speech summary vs slide content
Final scoring => LLM

Outputs
Score (0 - 100)
Detailed recommendations 
Slide-by-slide alignment evaluation
Example improved script

📌 4. AI Avatar Video Generation Agent

Generate avatar face —> Stable Diffusion
Generate lip-synched video —> Wav2Lip
Generate narration —> TTS (Bark, Meta TTS)

Steps:
1. Generate narration audio from speaker notes using TTS
2. Generate avatar face image from prompt
3. Use Wav2Lip to sync audio —> avatar animation
4. Convert PPT slides into frames
5. Stitch avatar + slides into final video

Tools:
Moviepy
Wav2Lip
HF TTS models
Stable Diffusion (for avatar)


Your agent system could be structured like this:

📘 MainAgent
    |-- "create_ppt" → call PresentationAgent
    |-- "edit_ppt" → call EditorAgent
    |-- "practice_speech" → call AudioEvaluationAgent
    |-- "create_video" → call AvatarVideoAgent

This matches the design strengths Kaggle judges will look for:
✔ modular
✔ tool-oriented
✔ chain-of-thought (internally)
✔ reproducible

### If I had more time, this is what I'd do
Audio feedback agent, will process the user uploaded rehearsal content and shares it feedback for further improvements/to make it outstanding.
Advanced level agent will be able to create video with an avatar presenting it. 






——————————————
🏗️ Implementation Roadmap (Recommended Order)
