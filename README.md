# youtube-audio-downloader

## credit

Based on [Stokry](https://github.com/stokry)'s tutorial on [how to download a YouTube video to mp3 with Python](https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p).

## requirements

- [youtube-dl](https://github.com/ytdl-org/youtube-dl) git-version (release 2021.12.17 on pypi has a feature breaking bug)

## usage

```bash
usage: main.py [-h] [--safe] [--debug] video_url

Simple YouTube video to mp3 downloader.

positional arguments:
  video_url   URL to YouTube Video (ex: https://www.youtube.com/watch?v=dQw4w9WgXcQ)

options:
  -h, --help  show this help message and exit
  --safe      sanitize the video title for a safe filename
  --debug     increase verbosity with debug messages
```
