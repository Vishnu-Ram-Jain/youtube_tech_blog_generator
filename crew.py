from crewai import Crew, Process

from agents import research_agent, blog_writer
from tasks import research_task, blog_writing_task

from tools.youtube_search import YouTubeSearcher
from tools.transcript import TranscriptLoader


def run(topic: str, channel: str):

    # ----------------------------------------
    # Step 1 : Search Video
    # ----------------------------------------

    youtube = YouTubeSearcher()

    video = youtube.search_video(
        topic=topic,
        channel_handle=channel
    )

    if video is None:
        raise Exception(
            f"No video found for topic '{topic}' in channel '{channel}'."
        )

    print("\nVideo Found\n")
    print(video)

    # ----------------------------------------
    # Step 2 : Download Transcript
    # ----------------------------------------

    loader = TranscriptLoader()

    transcript = loader.get_transcript(video.video_id)

    print(f"\nTranscript Length : {len(transcript.text)} characters")
    print(f"Transcript Chunks : {len(transcript.chunks)}")

    # ----------------------------------------
    # Step 3 : Build Crew
    # ----------------------------------------

    crew = Crew(

        agents=[
            research_agent,
            blog_writer
        ],

        tasks=[
            research_task,
            blog_writing_task
        ],

        process=Process.sequential,

        verbose=True,

        memory=False,

        cache=False
    )

    # ----------------------------------------
    # Step 4 : Execute Crew
    # ----------------------------------------

    result = crew.kickoff(

        inputs={

            "topic": topic,

            "channel": channel,

            "video_title": video.title,

            "video_url": video.url,

            "video_description": video.description,

            "transcript": transcript.text

        }

    )

    print("\n\n========== FINAL OUTPUT ==========\n")

    print(result)

    return result