import telebot
from discord_webhook import DiscordWebhook
channel_id=*тут id тг канала*
webhook_url="*тут вебхук дискорд*"
bot=telebot.TeleBot("*тут токен бота тг*")
@bot.channel_post_handler(content_types=["photo", "text", "video", "document"])
def text(message):
    if message.chat.id == channel_id:
        if (not message.photo) and (not message.video) and (not message.document):
            DiscordWebhook(url=webhook_url, content=message.text).execute()
        elif (message.photo) and (not message.video) and (not message.document):
            webhook=DiscordWebhook(url=webhook_url, content=message.caption)
            file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            webhook.add_file(downloaded_file, file_info.file_path)
            webhook.execute()
        elif (not message.photo) and (message.video) and (not message.document):
            webhook=DiscordWebhook(url=webhook_url, content=message.caption)
            file_info = bot.get_file(message.video.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            webhook.add_file(downloaded_file, file_info.file_path)
            webhook.execute()
        elif (not message.photo) and (not message.video) and (message.document):
            webhook=DiscordWebhook(url=webhook_url, content=message.caption)
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            webhook.add_file(downloaded_file, file_info.file_path)
            webhook.execute()
bot.infinity_polling()
