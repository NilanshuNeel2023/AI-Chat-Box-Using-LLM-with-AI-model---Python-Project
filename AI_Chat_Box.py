import dotenv
import os
from openai import OpenAI   
dotenv.load_dotenv()

client = OpenAI(api_key = os.getenv("GROQ_API_KEY"),
                base_url = "https://api.groq.com/openai/v1")

message = [{"role": "system", "content" : """
            You are a helpful assistance,
            your name is NeoBot,
            Give me short and consie answer.
            Introduce your in first person. 
""" }]

def bot():
    response = client.chat.completions.create(model= "openai/gpt-oss-120b",
                                        messages=message,
                                        temperature= 0.7,
                                        max_tokens= 280)
    reponse_content = response.choices[0].message.content
    message.append({"role": "assistant", "content": reponse_content})
    print("AI: ", response.choices[0].message.content)

def chat():
    while True:
        user_input = input("Your Question :")
        message.append({"role":"user",
                        "content": user_input})
        if user_input.strip().lower() == "q":
            break
        bot_response = bot()
        print(bot_response)


def main():
    chat()
    
if __name__ == '__main__':
    main()    