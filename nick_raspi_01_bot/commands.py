from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from .util.allower import allowed_only


@allowed_only
def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Welcome home, {update.effective_user.first_name}",
    )


@allowed_only
def get_ip(update: Update, context: CallbackContext):
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("1.1.1.1", 80))
        ip_a = s.getsockname()[0]
    except Exception:
        ip_a = "127.0.0.1"
    finally:
        s.close()

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"*IP:* `{ip_a}`",
        parse_mode=ParseMode.MARKDOWN_V2,
        disable_web_page_preview=True,
    )
