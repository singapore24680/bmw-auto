#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2024 Kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/AutoAnimeBot/blob/main/LICENSE > .

# if you are using this following code then don't forgot to give proper
# credit to t.me/kAiF_00z (github.com/kaif-00z)

class Var:
    # Telegram Credentials
    API_ID = 23576751
    API_HASH = "5224da0df5c60ec53de09ce79b9aa2c3"
    BOT_TOKEN = "7073096374:AAExF6bh0C9Polj2mQpz7ZqDXlUodeWG_EE"

    # Database Credentials
    REDIS_URI = "redis-13370.c91.us-east-1-3.ec2.cloud.redislabs.com:13370"
    REDIS_PASS = "pw4XVhnBk3msDmA59Ofy3858DWMB8Uhf"

    # Channels Ids
    BACKUP_CHANNEL = -1002062401412
    MAIN_CHANNEL = -1002003808456
    LOG_CHANNEL = -1002080108180
    CLOUD_CHANNEL = -1002130039069
    FORCESUB_CHANNEL = 0  # Set to 0 if not used
    OWNER = 6642501643

# Example of accessing the variables
print(Var.BOT_TOKEN)
print(Var.MAIN_CHANNEL)


    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://telegra.ph/file/9d2bae33cabd7c8d5580e.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    CRF = config("CRF", default="27")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=False, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
    FORCESUB_CHANNEL_LINK = config("FORCESUB_CHANNEL_LINK", default="", cast=str)
