from telegram import Update
from telegram.ext import CallbackContext

from .util.allower import allowed_only


@allowed_only
def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Welcome home, {update.effective_user.first_name}",
    )
