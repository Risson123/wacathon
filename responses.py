from openai import OpenAI
from message_history import MessageHistory

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_response(user_input, messageHistory: MessageHistory):
    
    if user_input == "start":
        prompt = "Come up with a brief, two-sentence scenario to for a group of fantasy roleplay party members involving them confronting a troll. "
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        messageHistory.add_prompt(response.output_text)
        return response.output_text
    elif user_input.startswith("response"):
        return messageHistory.return_message_history()
    elif user_input == "end":
        prompt = "You are in the following scenario: " + messageHistory.prompt + "\nCreate an outcome within 1000 characters if the players take the following actions: " + messageHistory.return_message_history()
        messageHistory.clear_history()
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        return response.output_text
    

    raise ValueError
