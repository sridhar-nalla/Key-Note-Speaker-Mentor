# agents.py
import argparse
from agents.presentation_agent import PresentationAgent
from agents.editor_agent import EditorAgent
from agents.audio_agent import AudioAgent
from agents.video_agent import VideoAgent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', choices=['create_ppt','edit_ppt','practice','create_video'], required=True)
    parser.add_argument('--prompt', type=str, default=None)
    parser.add_argument('--pptx', type=str, default=None)
    parser.add_argument('--audio', type=str, default=None)
    args = parser.parse_args()

    if args.action == 'create_ppt':
        pa = PresentationAgent()
        pa.create_from_prompt(args.prompt or 'A short demo presentation', out_path='output.pptx')

    if args.action == 'edit_ppt':
        ed = EditorAgent()
        ed.add_speaker_notes(args.pptx)

    if args.action == 'practice':
        aa = AudioAgent()
        report = aa.evaluate(args.audio, reference_ppt=args.pptx)
        print(report)

    if args.action == 'create_video':
        vv = VideoAgent()
        vv.create_from_ppt(args.pptx, out_video='output.mp4')


if __name__ == '__main__':
    main()