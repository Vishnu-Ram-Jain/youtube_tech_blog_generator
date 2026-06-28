from dataclasses import dataclass


@dataclass
class VideoMetadata:
    """
    Stores metadata of the selected YouTube video.
    """

    video_id: str
    title: str
    description: str
    published_at: str
    channel_title: str
    channel_id: str
    url: str