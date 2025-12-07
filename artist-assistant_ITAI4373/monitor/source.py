import random
import datetime

SAMPLE_POSTS = [
    ("Instagram", "Looking for an artist to draw my dog!", "creativehunter"),
    ("TikTok", "Anyone doing portrait commissions?", "artlover92"),
    ("Instagram", "I love abstract art—recommend artists?", "designseeker"),
    ("TikTok", "Need a surreal painting for my apartment.", "visualvibes"),
    ("Instagram", "Thinking about hiring someone for digital art.", "aestheticqueen"),
    ("TikTok", "Any artists available for album cover art?", "colorjunkie"),
]

def get_new_post():
    platform, text, username = random.choice(SAMPLE_POSTS)

    return {
        "platform": platform,
        "text": text,
        "username": username,
        "timestamp": datetime.datetime.utcnow().isoformat()
    }
