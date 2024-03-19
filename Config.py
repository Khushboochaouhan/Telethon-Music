import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6879179186:AAGGN_c-7wA6brXZv9SQ2K_jPsNeTipjJRk)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOJIBu4j7D_XNM80Gnr2OJp9dairLJNm4KhzrCkn9CzfJlzfxoP3ghWS8V7_Gbkb4v8XPpGOe-r76C65i2G2csyEiNHauTwX3POx4CLTY5gTmx1bzB0MHaP3K01Qz5auiEtkfdoJQVdBjc_hzraDFznWa_Qlzi-PQ0rM0_yPsq2Ts9TIPXoHCh_-0J-gli9alkzJiXCHVUQhdZ5IpWOQ7sHeq0C6ZroE-6d2fGAf6ZuXI7zcX6122vNNJQHASsbHWSZvOzNgZBoK7oQGREKdkF2t_XsQsLZASLYcQXLT5pVtZMi5sIKiFzfKnAyG9eBCZ89vlljcrJ3Vy6cOzi7L_nUAARes=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", on)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Soul_X_Music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat" @soul_society_shh) # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6606066603")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', true) # Change it to "True"
