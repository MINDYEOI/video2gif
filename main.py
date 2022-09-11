from moviepy.editor import VideoFileClip
import argparse


def parse_args(argv):
    parser = argparse.ArgumentParser(description="..")

    parser.add_argument(
        "--input", "-i",
        type=str,
        help="Enter the input video source's route.")

    args = parser.parse_args(argv)
    return args


def main(argv):

    args = parse_args(argv)
    inputName = args.input
    outputName = inputName - '.mp4' + '.gif'
    videoClip = VideoFileClip(inputName)
    videoClip.write_gif(outputName)
