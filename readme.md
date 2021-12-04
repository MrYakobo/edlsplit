# edlsplit

This is a tool that optimizes the workflow of splitting videos that contain many clips (think: VHS footage) into separate clips. The alternative is to launch a video editor and click around just to extract some clips.

The tool works by parsing an EDL (edit decision list)-file, that is generated from (for example) [mplayer](http://www.mplayerhq.hu/). It then calls `ffmpeg` with arguments that avoids reencoding the video and audio. Sweet.

# Recommended workflow

1. Launch mplayer and pick out your splitpoints by pressing 'i'
    - `mplayer -edlout edlfile.txt myvideo.mp4`

Contents of edlfile.txt should now be something like this:
```
21.600000 34.939999 0
420.100006 457.739990 0
701.760010 802.780029 0
```

2. Run edlsplit with the same file names as above
    - `./edlsplit.py edlfile.txt myvideo.mp4`

When the script is finished, your clips are put in this file structure:

```
myvideo/
├── myvideo_1.mp4
├── myvideo_2.mp4
└── myvideo_3.mp4
```

