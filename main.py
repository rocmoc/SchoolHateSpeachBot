from bot import TelegramBot
from norm import TextNormalizer, WordExtractor, ApplyStemmer
bot = TelegramBot("Salut")
update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            if message:
                chat_id = item["message"]["chat"]["id"]
                bot.chose_reply(message, chat_id)