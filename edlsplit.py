#!/usr/bin/env python3

import argparse
import subprocess

import os


def edlsplit(edlfile, videofile):
    # input: edlfile from mplayer, videofile to chop
    # output: videofile/videofile_N.mp4

    outdir = os.path.splitext(os.path.basename(videofile))[0]
    os.mkdir(outdir)

    with open(edlfile) as f:
        edltext = f.read()

    for i, line in enumerate(edltext.split("\n")):
        # skip empty lines
        if line == "":
            continue

        # http://www.mplayerhq.hu/DOCS/HTML/en/edl.html
        # [begin second] [end second] [action]
        chunks = line.strip().split()
        start = chunks[0]
        end = chunks[1]
        output = f"{outdir}/{outdir}_{i+1}.mp4"

        # avoid reencoding video with -vcodec copy and -acodec copy
        subprocess.run([
            "ffmpeg", "-i", videofile, "-ss", start, "-to", end,
            "-vcodec", "copy", "-acodec", "copy", output,
        ])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "edlfile",
        help="EDL file (edit decision list). You should generate this with mplayer -edlout <EDLFILE> <VIDEOFILE>",
    )
    parser.add_argument("videofile", help="Video file to split")
    args = parser.parse_args()

    edlsplit(args.edlfile, args.videofile)


if __name__ == "__main__":
    main()
