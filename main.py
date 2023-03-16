from env import token
import asyncio
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command, Text

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token)
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    btn_1 = InlineKeyboardButton('Готово', callback_data='button1')
    button_1 = InlineKeyboardMarkup().add(btn_1)
    await message.answer("Привет! Я бот для рассылок почты!\n"
                         "Перед началом работы со мной, следует создать пароль для приложения по которому"
                         "будет заходить бот на вашу почту!\n"
                         "1) Для Yahoo https://login.yahoo.com/account/security\n"
                         "2) Для Mail https://help.mail.ru/mail/security/protection/external\n"
                         "Полная документация как выполнить данные операции будет по ссылке:"
                         " https://docs.google.com/document/d/1HVv1lPkywRlX-EmdsjAwDUG7C3aag4TuJpX4Ld53RcU/edit\n"
                         "Если у вас все готово, нажмите на кнопку 'Готово'!"
                         , reply_markup=button_1)

@dp.callback_query_handler(Text("button1"))
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Хорошо, сейчас я вам вышлю файлы, вы их должны заполнить по'
                         ' примеру: https://disc.google.com/')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())