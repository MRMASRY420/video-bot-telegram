import os
import subprocess
import telebot

TOKEN = os.getenv("7635198963:AAH_HjpfascTAV_E9znav4mdj6-8Myce1is")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def download_video(message):

    m3u8 = message.text
    output = "video.mp4"

    cmd = [
        "ffmpeg",
        "-y",
        "-i", m3u8,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output
    ]

    subprocess.run(cmd)

    with open(output, "rb") as v:
        bot.send_video(message.chat.id, v)

    os.remove(output)

bot.polling()