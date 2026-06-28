from dataclasses import dataclass


@dataclass
class Transcript:
    """
    Represents the transcript of a YouTube video.
    """
    video_id: str
    language: str
    text: str
    chunks: list[str]