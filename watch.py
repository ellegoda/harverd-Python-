import re
import sys


def main():
    print(parse(input("HTML: ")))

def get_sort_url(url):
    video_id = url.split("/")[-1]
    return f"https://youtu.be/{video_id}"

def validate_youtube_url(url):
    youtube_regex = (
        r'(https?://)?(www\.)?''(youtube|youtu|youtube-nocookie)\.(com|be)/''(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
    match = re.match(youtube_regex, url)
    return match is not None

def parse(s):
    if "src" in s:
        for i in s.split('"'):
            if not validate_youtube_url(i):
                continue
            else:
                return get_sort_url(i)
    else:
        return None

if __name__ == "__main__":
    main()
