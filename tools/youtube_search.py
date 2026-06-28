from googleapiclient.discovery import build
from models.video import VideoMetadata
from config import settings

class YouTubeSearcher:

    def __init__(self):

        self.youtube = build(
            "youtube",
            "v3",
            developerKey=settings.YOUTUBE_API_KEY
        )

    def get_channel_id(self, handle: str):

        request = self.youtube.search().list(

            q=handle,

            part="snippet",

            type="channel",

            maxResults=1

        )

        response = request.execute()

        items = response.get("items", [])

        if not items:
            raise Exception("Channel not found")

        return items[0]["snippet"]["channelId"]
    
    def search_video(self, topic, channel_handle):

        channel_id = self.get_channel_id(channel_handle)

        request = self.youtube.search().list(

            part="snippet",

            channelId=channel_id,

            q=topic,

            type="video",

            maxResults=1,

            order="relevance"

        )

        response = request.execute()

        items = response.get("items", [])

        if not items:
            return None

        item = items[0]


        return VideoMetadata(
            
            video_id=item["id"]["videoId"],

            title=item["snippet"]["title"],

            description=item["snippet"]["description"],

            published_at=item["snippet"]["publishedAt"],

            channel_title=item["snippet"]["channelTitle"],

            channel_id=channel_id,

            url=f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        )