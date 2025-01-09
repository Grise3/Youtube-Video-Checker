import requests
import re
import json
import os

def check_youtube_video(youtube_channel_url):
    try:
        response = requests.get(youtube_channel_url)
        response.raise_for_status()
        html_content = response.text

        video_ids = re.findall(r'watch\?v=([a-zA-Z0-9_-]+)', html_content)

        if video_ids:
            latest_video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            return latest_video_url
        else:
            return None
    except Exception as e:
        print(f"Error retrieving page: {str(e)}")
        return None

def load_youtuber(json_file, channel_url):
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            return data.get(channel_url, '')
    return ''

def save_youtuber(json_file, channel_url, video_url):
    data = {}
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
    data[channel_url] = video_url
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=2)

def main(channel_url, json_file='youtubers.json'):
    last_video_url = load_youtuber(json_file, channel_url)
    latest_video_url = check_youtube_video(channel_url)

    if latest_video_url:
        if latest_video_url != last_video_url:
            save_youtuber(json_file, channel_url, latest_video_url)
            result = {
                'channel_url': channel_url,
                'new_video': True,
                'precedent_video_url': last_video_url,
                'video_url': latest_video_url,
                'message': "New video found",
                'code': "200"
            }
        else:
            result = {
                'channel_url': channel_url,
                'new_video': False,
                'precedent_video_url': last_video_url,
                'message': "No new video",
                'code': "200"
            }
    else:
        result = {
            'channel_url': channel_url,
            'new_video': False,
            'message': "No video link found or error occurred",
            'code': "404"
        }

    return json.dumps(result, indent=2)

