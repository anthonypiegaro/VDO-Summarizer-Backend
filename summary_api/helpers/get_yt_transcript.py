from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(id):

    all_data = YouTubeTranscriptApi.get_transcript(id)

    video_text = ""

    for data in all_data:
        video_text += (" " + data["text"])
    
    return video_text
