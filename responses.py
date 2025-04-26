from openai import OpenAI
from message_history import MessageHistory
from random import choice

API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_response(user_input, messageHistory: MessageHistory):
    
    if user_input == "start" and messageHistory.prompt is None:
        villains = [
            "necromancer",
            "troll",
            "cyclops",
            "vampire",
            "werewolf",
            "riddle sphinx",
            "scarecrow"
        ]
        villain = choice(villains)
        prompt = "Come up with a brief, two-sentence scenario to for a group of fantasy roleplay party members involving them confronting a " + villain + ". Be creative."
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        messageHistory.add_prompt(response.output_text)
        return "***Your scenario is the following:*** \n \n" + response.output_text
    
    elif user_input == "start" and messageHistory is not None: 
        return "Another scenario is already in action, please finish the current one."
    
    elif user_input == "prompt":
        return messageHistory.prompt
    
    if user_input.startswith("response"):
        return messageHistory.return_message_history()
    
    elif user_input == "end" and messageHistory.prompt != None:
        if len(messageHistory.message_history) == 0:
            return "No players have made an action yet!"
        prompt = "You are in the following scenario: " + messageHistory.prompt + "\nCreate an end of game outcome within 1000 characters if the players take the following actions, scoring each player's actions individually: " + messageHistory.return_message_history()
        messageHistory.clear_history()
        response = client.responses.create(
            model="gpt-4.1",
            input=prompt
        )
        return response.output_text
    

    return response.output_text
