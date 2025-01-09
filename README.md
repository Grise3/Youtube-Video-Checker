# YouTube Video Checker

## Description

A simple Python script to track and detect new videos on a YouTube channel.

## Features

-  Detection of new videos
-  Video history saving
-  Video link extraction
-  JSON report generation

## Prerequisites

- Libraries:
  - `requests`
  - `json`

## Installation

```bash
git clone https://github.com/Grise3/Youtube-Video-Checker.git
cd youtube-video-tracker
pip install requests
```

## Usage

```python
# Usage example
channel_url = 'https://www.youtube.com/@ChannelName'
result = main(channel_url)
print(result)
```

## Detailed Operation

1. Retrieval of the channel's HTML content
2. Extraction of the latest video ID
3. Comparison with the last known video
4. Update of the JSON file

## Project Structure

```
Youtube-Video-Checker/
│
├── main.py           # Main script
├── youtubers.json    # Save file
└── README.md         # Documentation
```

## Json responses

### No new video
```json
{
  "channel_url": "https://www.youtube.com/@[youtuber]",
  "new_video": false,
  "precedent_video_url": "https://www.youtube.com/watch?v=[ID]",
  "message": "No new video",
  "code": "200"
}

```

### New video

```json
{
  "channel_url": "https://www.youtube.com/@[youtuber]",
  "new_video": true,
  "precedent_video_url": "https://www.youtube.com/watch?v=s",
  "video_url": "https://www.youtube.com/watch?v=[ID]",
  "message": "New video found",
  "code": "200"
}
```

### No video link found or error occurred
```json
{
  "channel_url": "https://www.youtube.com/@[youtuber]",
  "new_video": false,
  "message": "No video link found or error occurred",
  "code": "404"
}
```
