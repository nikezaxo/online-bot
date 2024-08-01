from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import requests
from io import BytesIO

# Your bot's API token
API_TOKEN = '7364696581:AAHk1qcga2LUeVBh8wZ58v84JL0q9j9po4A'

# Direct URL of the GIF image
GIF_URL = 'https://raw.githubusercontent.com/nikezaxo/my-telegram-bot-with-best-best-command-and-picture-/main/giphy.gif'

# Web app URL for the game
GAME_URL = 'https://nikezaxo.github.io/Run-3/'

async def start(update: Update, context: CallbackContext) -> None:
    # Full story text
    story = (
        "Welcome to the Dino Game Adventure!\n\n"
        "In a distant land, where the prehistoric meets the pixelated, a brave little dinosaur roams the vast landscapes of an endless desert. "
        "This dino has a simple yet exciting mission: to navigate through the ever-changing terrain, dodge obstacles, and collect points to become the greatest dino champion of all time.\n\n"
        "As the dino traverses the desert, it encounters various challenges – from jumping over cacti to avoiding treacherous pits. The further it goes, the higher the score! "
        "The game is simple but addictive, promising endless fun and a chance to prove your skills.\n\n"
        "Join the adventure and test your reflexes in this thrilling game where the only limit is your score. Are you ready to dive into the action?\n\n"
    )

    # Download the GIF
    response = requests.get(GIF_URL)
    gif_file = BytesIO(response.content)

    # Create buttons
    keyboard = [
        [InlineKeyboardButton("Play", web_app={"url": GAME_URL})],
        [InlineKeyboardButton("Help", url='https://t.me/LEDO_55')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the GIF, story, and buttons
    await update.message.reply_photo(
        photo=gif_file,
        caption=story,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    help_message = "Need help? Visit our support page: [t.me/LEDO_55](https://t.me/LEDO_55)"
    await update.message.reply_text(help_message, parse_mode='Markdown')

def main() -> None:
    application = Application.builder().token(API_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()

if __name__ == '__main__':
    main()
