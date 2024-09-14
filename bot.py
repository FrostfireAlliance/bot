import telebot
from telebot import types

bot_token = "7353529474:AAFmg1yT58lpRXDyoral79r-jyhL_Rcfc3Q"
group_id = "-1002433866648"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(content_types=['new_chat_members'])
def greet_new_members(message):
    for new_member in message.new_chat_members:
        name = new_member.first_name
        profile_link = f"<a href='tg://user?id={new_member.id}'>{name}</a>"
        welcome_text = (
            f"ㅤ<b>{profile_link}, добро пожаловать в</b>\n"
            f"ㅤ<code>❄️Frostfire Alliance❄️</code>\n\n"
            f"<b>Сделай приписку в нике</b> <code>🧊[FA] ник❄️</code>"
        )
        keyboard = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("Правила", url="frostfirealliance.great-site.net")
        keyboard.add(button)
        bot.send_message(message.chat.id, welcome_text, parse_mode="HTML", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == "правила")
def send_rules(message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    profile_link = f"<a href='tg://user?id={user_id}'>{name}</a>"
    rules_text = (
        f"{profile_link}, <b>правила:</b>\n"
    )
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Тык", url="frostfirealliance.great-site.net")
    keyboard.add(button)
    
    bot.send_message(message.chat.id, rules_text, parse_mode="HTML", reply_markup=keyboard)

if __name__ == '__main__':
    bot.polling(none_stop=True)