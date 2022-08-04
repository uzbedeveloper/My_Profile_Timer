#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [DATE_TIME Telegram userbot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_teletips.quotes_teletips import *
from lists_teletips.emojis_teletips import *
from PIL import Image, ImageDraw, ImageFont
import datetime
import pytz
import asyncio
import random
import os

Date_Time_Userbot_teletips=Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)

Time_Zone = os.environ["TIME_ZONE"]

async def main_teletips():
    try:
        while True:
            if Date_Time_Userbot_teletips.is_connected: 
                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_teletips = TimeZone_teletips.strftime("   %I:%M")
                Date_teletips = TimeZone_teletips.strftime("%d.%m.%Y") 
              
                today = datetime.datetime.now()
                print(today)
                bday = datetime.datetime(2022,8,29,0,0)
                print(bday)
                time_diff = bday - today
                print(f"Your birthday is in {time_diff}")
                tdays = time_diff.days
                print(f"Your birthday is in {tdays} days. abs={abs(int(tdays))}")
                tsecs = time_diff.total_seconds()
                print(f"Your birthday is {tsecs} seconds away. and {int(tsecs)} seconds away. abs={abs(int(tsecs))}")
                tmins = tsecs/60
                print(f"Your birthday is {tmins} minutes away. and {int(tmins)} minutes away. abs={abs(int(tmins))}")
                thrs = tsecs/(60*60)
                print(f"Your birthday is {thrs} hours away. and {int(thrs)} hours away. abs={abs(int(thrs))}")
             
                await Date_Time_Userbot_teletips.update_profile(bio = f"Tug'ulgan kunimga: {abs(int(tdays))}-kun, {abs(int(thrs))}-soat, {abs(int(tmins))}-daqiqa qoldi" , last_name = f"{Time_teletips}")
                       
                print("Profile Updated! ")
                
            await asyncio.sleep(60)     
    except FloodWait as e:
        await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_teletips())
Date_Time_Userbot_teletips.run()
