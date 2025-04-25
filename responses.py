from openai import OpenAI
###############################
##################################3
##############################
######ANKWFDNOSIEGAHIOEGOAIHOAHIOSGOJIOPSHISRHIPHIS
API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_response(user_input):
    
    if user_input == "start":
        prompt = "Come up with a brief, two-sentence scenario to for a group of fantasy roleplay party members involving them confronting a troll. "
    else:
        prompt = "You are a troll who speaks in very easy terms, along with grunts, gargles and roars. A brave adventurer says the following: " + user_input
    response = client.responses.create(
        model="gpt-4.1",
        input=prompt
    )
    return response.output_text
