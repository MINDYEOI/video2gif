from moviepy.editor import VideoFileClip
import argparse
import sys


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Let's make GIF!")

    parser.add_argument(
        "--input",
        help="Enter the input video source's route.",
        required=True)

    args = parser.parse_args(argv)
    return args


def main(argv):

    args = parse_args(argv)
    inputName = args.input
    outputName = inputName[:-4] + '.gif'
    print(inputName)
    print(outputName)
    videoClip = VideoFileClip(inputName)
    videoClip.write_gif(outputName)


if __name__ == "__main__":
    main(sys.argv[1:])
