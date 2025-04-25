from openai import OpenAI
API_KEY = "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"
client = OpenAI(api_key=API_KEY)
def get_response(user_input):
    total_input = "You are a troll who speaks in very easy terms, along with grunts, gargles and roars. A brave adventurer says the following: " + user_input
    response = client.responses.create(
        model="gpt-4.1",
        input=total_input
    )
    return response.output_text


#HELLO HIH IHOW YOU DOING
