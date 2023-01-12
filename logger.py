from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

def logger(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('logger.csv', 'a')
    file.write(f'{update.effective_user.first_name}\n')
    file.close()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
