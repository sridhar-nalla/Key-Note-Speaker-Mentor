# notebooks/kaggle_starter.py
# A simple script you can run inside a Kaggle Notebook cell to test create_ppt
import sys, os
print("Hello from kaggle_starter.py")
 

from agents.presentation_agent import PresentationAgent
pa = PresentationAgent()
pa.create_from_prompt('How to evaluate ML models', out_path='/kaggle/working/demo_output.pptx')
print('Saved to /kaggle/working/demo_output.pptx')

 
