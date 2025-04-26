class MessageHistory:
    def __init__(self):
        self.message_history = []
        self.prompt = None
    
    def add_prompt(self, gpt_prompt:str) -> None:
        self.prompt = gpt_prompt

    def add_response(self, user_response:str ) -> None:
        self.message_history.append(user_response)

    def return_message_history(self) -> str:
        return "".join(self.message_history)
