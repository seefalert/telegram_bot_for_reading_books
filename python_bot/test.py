from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config_data.config import Config, load_config

config: Config = load_config('.env')

bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

buttons: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)]

kb_builder.row(*buttons)


@dp.message(CommandStart())
async def start_process_command(message: Message):
    await message.answer(text='This',reply_markup=kb_builder.as_markup())


if __name__ == '__main__':
    dp.run_polling(bot)
