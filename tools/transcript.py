from youtube_transcript_api import YouTubeTranscriptApi
from models.transcript import Transcript
from utils.chunker import TranscriptChunker

class TranscriptLoader:

    def __init__(self):

        self.api = YouTubeTranscriptApi()

        self.chunker = TranscriptChunker()

    def get_transcript(self, video_id: str) -> Transcript:

        transcript = self.api.fetch(video_id)

        text = " ".join(

            snippet.text

            for snippet in transcript

        )

        chunks = self.chunker.split(text)

        return Transcript(

            video_id=video_id,

            language="en",

            text=text,

            chunks=chunks

        )












# from dataclasses import dataclass
# from youtube_transcript_api import YouTubeTranscriptApi



# @dataclass
# class Transcript:
#     video_id: str
#     language: str
#     text: str
#     segments: list


# class TranscriptLoader:
#     """
#     Downloads the transcript of a YouTube video.
#     """

#     def get_transcript(self, video_id: str) -> Transcript:
#         """
#         Fetch transcript for a YouTube video.

#         Args:
#             video_id: YouTube video ID

#         Returns:
#             Transcript object
#         """
        
#         self.ytt_api = YouTubeTranscriptApi()
#         try:
#             transcript = self.ytt_api.fetch(video_id,languages=["en"])
#             print(type(transcript))
#             print(type(transcript[0]))
#             print(transcript[0])

#             text = " ".join(snippet.text for snippet in transcript)    

#             return Transcript(
#             video_id=video_id,
#             language="en",
#             text=text,
#             segments=transcript
#         )

#         except Exception as e:
#             raise Exception(
#                 f"Failed to fetch transcript for video '{video_id}'.\n{e}"
#             )