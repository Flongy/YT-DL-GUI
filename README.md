# Downloader GUI

## Description
Simple GUI client for [youtube-dl](https://github.com/ytdl-org/youtube-dl) tool built with 
[tkinter](https://docs.python.org/library/tkinter.html) lib provided by Python's standard library.

This tool can be used to download media (video, audio) from vast list of sources: 
[yt-dl supported sites](https://github.com/ytdl-org/youtube-dl/blob/master/docs/supportedsites.md).

## Requirements
- [httpx](https://github.com/encode/httpx) - http client;
- [Pillow](https://github.com/python-pillow/Pillow) - image processing library;
- [youtube-dl](https://github.com/ytdl-org/youtube-dl) - video downloading tool;
- [_Optional_] [ffmpeg](https://www.ffmpeg.org/) - media processing library (primarily for combining video and audio).

## Usage
If all dependencies are installed (`pip install -r requirements.txt`) you can run the `start` script 
(or better just execute the `main.py` script in a Python interpreter).  

You'll see the main screen of the program composed of:
- Textbox for entering the link to the media you want to download;
- `Check` button to retrieve the preview, title and duration of that media file;
- Preview image;
- Title and duration labels;
- Quality combobox with options: 
  - bestvideo+bestaudio: for example, youtube usually stores video and audio of best quality separately so this option 
  will download both and combine into a single file afterwards, if `ffmpeg` or `avconv` were installed on the system,
  - best: best quality combined file,
  - bestvideo: best quality video without audio,
  - bestaudio: best quality audio without video,
  - worst: worst quality combined file;
- `Download` button to start the download.

If the link is incorrect, clicking the buttons will show a messagebox telling you about failure of processing that link.

The progress is (for now) shown in the console. 
When the download is complete, the desirable media can be found in the `./media/` folder.

https://user-images.githubusercontent.com/22942979/130280569-453664f2-4ec6-44d0-beee-f0af7bdc7981.mov

## Features
- [x] Simple GUI with textbox for the link to the media
- [x] Thumbnail and title preview to confirm the resource you about to download
- [x] Simple quality picker
- [ ] Probably, should start the download in a separate thread/process so that UI won't freeze 
- [ ] Force redownload checkbox
- [ ] Download status
- [ ] A way to stop downloading the file
- [ ] Queue multiple downloads
- [ ] Choose the path to save the file to
- [ ] Better (or, i guess, correct) error handling and demonstration to the user
- [ ] A more clear preview for playlists
- [ ] Show the list of available formats and let user pick
- [ ] Improve upon the GUI

First version was made in, like, four hours or something. So, yes, it's laking a ton of features. 
But i'll try to improve it in the future. 

## Disclaimer
Before downloading copyrighted content you probably should ask the right owner for permission. 
I, the author of this program, am **not** responsible for any trouble you (user) get into by using the program.
