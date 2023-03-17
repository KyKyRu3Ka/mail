from env import token
import asyncio
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentTypes, Message
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command, Text

email_accounts_txt = {}
for_email_accounts_txt = {}
text_emails_txt = {}

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token)
# Диспетчер
dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    btn = InlineKeyboardButton('Готово', callback_data='button1')
    button = InlineKeyboardMarkup().add(btn)
    await message.answer(
        "Привет! Я бот для рассылок почты!\n"
        "Перед началом работы со мной, следует создать пароль для приложения по которому"
        "будет заходить бот на вашу почту!\n"
        "1) Для Yahoo https://login.yahoo.com/account/security\n"
        "2) Для Mail https://help.mail.ru/mail/security/protection/external\n"
        "Полная документация будет по ссылке:"
        " https://docs.google.com/document/d/1HVv1lPkywRlX-EmdsjAwDUG7C3aag4TuJpX4Ld53RcU\n"
        "Если у вас все готово, нажмите на кнопку 'Готово'!",
        reply_markup=button
    )


@dp.callback_query_handler(Text("button1"))
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        'Хорошо, сейчас я вам вышлю файлы!\n'
        'Как заполнять файлы указано в документации!'
    )
    with open('for_user_txt/email_accounts'+'.txt', 'r') as file:
        await bot.send_document(
            callback_query.from_user.id,
            document=file
        )
    with open("for_user_txt/for_email_accounts.txt", 'r') as file:
        await bot.send_document(
            callback_query.from_user.id,
            document=file
        )
    with open('for_user_txt/Text_email.txt', 'r') as file:
        await bot.send_document(
            callback_query.from_user.id,
            document=file
        )
    btn = InlineKeyboardButton('Готово', callback_data='button2')
    button = InlineKeyboardMarkup().add(btn)
    await bot.send_message(
        callback_query.from_user.id,
        "Как заполните файлы, скидывайте их мне! А затем нажмите 'Готово'.",
        reply_markup=button
    )


@dp.callback_query_handler(Text("button2"))
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    from_id = f'{callback_query.from_user.id}'
    print(f'{callback_query.from_user.id}')
    if f'{callback_query.from_user.id}' not in email_accounts_txt.keys() and\
            f'{callback_query.from_user.id}' not in for_email_accounts_txt.keys() and\
            f'{callback_query.from_user.id}' not in text_emails_txt.keys():
        await bot.send_message(
            callback_query.from_user.id,
            'У меня нету некоторых файлов!\n'
            'Проверьте, отправили ли вы все 3 файла?'
        )
    else:
        await bot.send_message(
            callback_query.from_user.id,
            'Отлично'
        )


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def doc_handler(message: Message):
    if document := message.document:
        destination_file = "input/" + f'{document.file_name}'
        if f"{message.from_user.id}" not in email_accounts_txt.keys():
            await document.download(destination_file=destination_file)
            await message.answer(
             f'{document.file_name}'+' поймаль'
            )
            email_accounts_txt[f'{message.from_user.id}'] = f'{document.file_name}'
            print(email_accounts_txt.keys())
        elif f"{message.from_user.id}" not in for_email_accounts_txt.keys():
            await document.download(destination_file=destination_file)
            await message.answer(
                f'{document.file_name}' + ' поймаль'
            )
            for_email_accounts_txt[f'{message.from_user.id}'] = f'{document.file_name}'
            print(for_email_accounts_txt.keys())
        elif f"{message.from_user.id}" not in text_emails_txt.keys():
            await document.download(destination_file=destination_file)
            await message.answer(
                f'{document.file_name}' + ' поймаль'
            )
            text_emails_txt[f'{message.from_user.id}'] = f'{document.file_name}'
            print(text_emails_txt.keys())
        else:
            await message.answer(
                f'{document.file_name}' + ' уже есть у меня.'
            )
# Запуск процесса поллинга новых апдейтов


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
