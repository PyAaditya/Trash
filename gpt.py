
from pyrogram import Client, filters
from pyrogram.types import Message
from chatgpt import GPT2

# Initialize the GPT-2 model
gpt = GPT2()

#Fill this 
API_ID = 
API_HASH = ""
BOT_TOKEN = ""

app = Client("chatGPT_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private)
async def chatGPT_bot(client, message: Message):
    if message.text:
        response = gpt.generate_response(message.text)
        await message.reply_text(response)

app.run()
