import logging
import os

from telegram import Update
from telegram.ext import CallbackContext


def allowed_only(cmd):
    allowed_ids = os.getenv("ALLOWED_IDS", "").split(",")
    logger = logging.getLogger("raspibot")

    def inner(update: Update, context: CallbackContext):
        if str(update.effective_user.id) in allowed_ids:
            cmd(update, context)
        else:
            logger.warning(
                f"{update.effective_user.full_name} "
                f"(ID:{update.effective_user.id}) "
                f"tried to execute {cmd.__name__}"
            )
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="You are not allowed to use this command",
            )

    return inner
