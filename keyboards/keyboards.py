from aiogram import types
from lexicon.lexicon import LEXICON_RU

yes_key = types.KeyboardButton(LEXICON_RU["yes"])
no_key = types.KeyboardButton(LEXICON_RU["no"])

yes_no_kb = types.ReplyKeyboardMarkup(keyboard=[[yes_key, no_key]])