#ALONE CODER
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", "26676259"))
        self.API_HASH = getenv("API_HASH", "a6194f7e8ec4adf87e5a50c7e9335f5c")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "8869365977:AAF7ozd4DB38nu9Y_q_v7FccRoemE8AV0eo")
        self.MONGO_URL = getenv("MONGO_URL", "Apna Mongo Db Dalo")

        self.LOGGER_ID = int(getenv("LOGGER_ID", "-1003864442012"))
        self.OWNER_ID = int(getenv("OWNER_ID", "8619158508"))
        
        self.SESSION1 = getenv("SESSION", "BQGXDCMAHLc2VQJz2mG6vAyTchsTtgeOCe_yWtEBOCl-vombLb57UV0Zcy6COvjywe9awKMKcZ-Miopf-YC0Ofl41YfovztCiPZNWe185szFZV5BghuMzkIb1GzgSu4pCcsRDFQ9EVZ8Ma37y0oIQodghmIZ2ZMP_NGQwoL6CH75swlj1wl8k2kPyMgRVSzoSb9ZQM0NW0LZN4tJEbNjDtVEu5AVW3a6jsutOdI_LcGmLRmJmZdRNJAIm7tB3rYAhqWorE4hg3SajH4Nwh9VrVx1VpGrWFmNCageJpHBCPX08OVVAcs4IcQLtu1anE3aBchxftZdHW9IvOVevCZu6OCglA1DLwAAAAIBvevsAA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PatelGxCheat")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+jY4N29HHCT5kMTE1")

        self.AUTO_END: bool = getenv("AUTO_END", False)
        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", False)
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", True)

        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "50"))
        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", "20"))
        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
