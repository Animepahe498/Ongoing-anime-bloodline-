#    This file is part of the AutoAnime distribution.
#    Copyright (c) 2023 Kaif_00z
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

from decouple import config


class Var:
    # Telegram Credentials

    API_ID = config("API_ID", default=23902408, cast=int)
    API_HASH = config("API_HASH", default="6a36a4ef2f07d63aeba7b53b99c64d73")
    BOT_TOKEN = config("BOT_TOKEN", default="6784687538:AAHSHUFb-YIWpeQ52Y5A_ogRSHMbe-uJUas")

    # Database Credentials

    REDIS_URI = config("REDIS_URI", default="redis-11976.c74.us-east-1-4.ec2.cloud.redislabs.com:11976")
    REDIS_PASS = config("REDIS_PASSWORD", default="HDWNzDMfwtnXM6Kq63UIgAquSH4fj5mw")

    # Channels Ids

    BACKUP_CHANNEL = config("BACKUP_CHANNEL", default=0, cast=int)
    MAIN_CHANNEL = config("MAIN_CHANNEL", default="-1002100360610", cast=int)
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1002096389479", cast=int)
    CLOUD_CHANNEL = config("CLOUD_CHANNEL", default="-1002096389479", cast=int)
    OWNER = config("OWNER", default="5086525318", cast=int)

    # Other Configs

    THUMB = config(
        "THUMBNAIL", default="https://graph.org/file/37d9d0657d51e01a71f26.jpg"
    )
    FFMPEG = config("FFMPEG", default="ffmpeg")
    SEND_SCHEDULE = config("SEND_SCHEDULE", default=True, cast=bool)
    RESTART_EVERDAY = config("RESTART_EVERDAY", default=True, cast=bool)
