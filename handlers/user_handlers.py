from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram import Router, F
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb
from services.card_deck import Game


router = Router()
game = Game()

# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU['/start'], reply_markup=yes_no_kb)


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])

@router.message(Command(commands=['card']))
async def process_card_command(message: Message):
    urlPhoto, value = await game.getCard()
    await message.answer_photo(photo=urlPhoto)

@router.message(Command(commands=['shuffle']))
async def process_shuffle_command(message: Message):
    await game.shuffle()

@router.message(F.text == LEXICON_RU['yes_button'])
async def shuffle(message: Message):
    await message.answer(LEXICON_RU['start_game'], reply_markup=ReplyKeyboardRemove())

@router.message(F.text == LEXICON_RU['no_button'])
async def send_photo(message: Message):
    await message.answer(LEXICON_RU['user_no'], reply_markup=ReplyKeyboardRemove())