import telebot
from pytube import YouTube

# Initialize the Telegram bot
bot = telebot.TeleBot('6641754002:AAFfrhSlA9hdpdA6canVczQjEw-5llClbKc')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the YouTube downloader bot! Send a YouTube video URL to get started. \n Feel Free To Contact Admin @MR_S74RK \n Created By Stark🛸✅")
@bot.message_handler(commands=['support','admin'])
def send_suppprt(message):
	bot.reply_to(message, "ADMIN : STARK🛸✅ \n TG : @MR_S74RK \n Instagram : la1uuuuu \n Github : github.com/STARK-404\n Buy Me  a coffee☕ :-  USDT(polygon) 0xc3d35d064154ca94c212f636730e133f66624126 ")

@bot.message_handler(func=lambda message: True)
def process_message(message):
    try:
        # Extract the YouTube URL from the message
        url = message.text
        
        # Download the video
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(filename=yt.title)
        
        # Send the downloaded video to the user
        bot.send_video(message.chat.id, open(yt.title + ".mp4", 'rb'))
    except Exception as e:
        bot.reply_to(message, "An error occurred while processing your request.")
        print(str(e))

# Start listening for incoming messages
bot.polling()
