import argparse
import logging
import string
import youtube_dl


logging_level = logging.INFO

def download_mp3_youtube(video_url, safe_filename=False, quiet=True):
    logging.info("Fetching video information.")
    video_info = youtube_dl.YoutubeDL({"quiet": quiet}).extract_info(url=video_url, download=False)

    if safe_filename:
        valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
        video_title_sanitized = "".join(
            c for c in video_info["title"] if c in valid_chars
        )
        filename_stem = video_title_sanitized.replace(" ", "_")  # space causes issues
        logging.debug(f'Sanitized video title for filename:')
        logging.debug(f'{video_info["title"]} -> {filename_stem}')
    else:
        filename_stem = video_info["title"]

    filename = f"{filename_stem}.mp3"
    options = {"format": "bestaudio/best", "keepvideo": False, "outtmpl": filename, "quiet": quiet}

    with youtube_dl.YoutubeDL(options) as ydl:
        logging.info("Downloading video...")
        ydl.download([video_info["webpage_url"]])

    logging.info(f"Download complete, audio saved to: {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple YouTube video to mp3 downloader."
    )
    parser.add_argument(
        "video_url",
        help="URL to YouTube Video (ex: https://www.youtube.com/watch?v=dQw4w9WgXcQ)",
    )
    parser.add_argument(
        "--safe", action="store_true", help="sanitize the video title for a safe filename"
    )
    parser.add_argument(
        "--debug", action="store_true", help="increase verbosity with debug messages"
    )

    args = parser.parse_args()
    
    if args.debug:
        logging_level = logging.DEBUG
        
    logging.basicConfig(
        format="%(asctime)s: %(message)s", level=logging_level, datefmt="%H:%M:%S"
    )
    
    if args.video_url:
        if args.debug:
            quiet = False
        else:
            quiet = True
        
        download_mp3_youtube(args.video_url, args.safe, quiet)
