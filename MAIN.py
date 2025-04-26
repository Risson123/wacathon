from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from message_history import MessageHistory

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

mess_hist = MessageHistory()

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message was empty because intents were not enabled properly")
        return
    if is_private:=user_message[0] == "?":
        user_message = user_message[1:]
    try:
        response: str = get_response(user_message, mess_hist)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready()-> None:
    print(f"{client.user} is running")

@client.event
async def on_message(message: Message) -> None:
    commands = ["start", "end", "response", "help"]
    # Prevents the bot triggering itself
    if message.author == client.user: 
        return None
    user_message = message.content
    if user_message[0] == "!" and user_message[1:] in commands:
        await send_message(message, user_message[1:])
    elif user_message[0] == "!" and mess_hist.prompt != None:
        mess_hist.add_response(user_message[1:])
        await message.channel.send(f"{message.author}'s fate is being decided . . .")

def main():
    client.run(token=TOKEN)
if __name__ == "__main__":
    main()