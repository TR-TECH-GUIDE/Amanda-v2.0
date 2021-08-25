# Made By @TharukRenuja On Telegram & Github Id TR-TECH-GUIDE
import random

from telegram import Update
from telegram.ext import CallbackContext, run_async

import Amanda.modules.animequotesstring as animequotesstring
from Amanda import dispatcher
from Amanda.modules.disable import DisableAbleCommandHandler


@run_async
def animequotes(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(animequotesstring.ANIMEQUOTES))


ANIMEQUOTES_HANDLER = DisableAbleCommandHandler("animequotes", animequotes)

dispatcher.add_handler(ANIMEQUOTES_HANDLER)
