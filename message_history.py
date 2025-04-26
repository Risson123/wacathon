from discord import Message
class MessageHistory:
    def __init__(self):
        self.clear_history()
        self.prompt = ""
        self.message_history: list[Message] = []
    def add_prompt(self, gpt_prompt:str) -> None:
    # SETS THE PROMPT FOR THE CURRENT MESSAGE HISTORY
        self.prompt = gpt_prompt

    def add_response(self, user_response:Message ) -> None:
    # ADDS THE RESPONSE TO SELF.MESSAGE_HISTORY
        self.message_history.append(user_response)

    def return_message_history(self) -> str:
        ret = ""
        for message in self.message_history:
            ret += f"{message.author}'s response was to {message.content.replace("!response", "")} \n"
        return ret
            

    def clear_history(self):
        self.message_history = []
        self.prompt = None