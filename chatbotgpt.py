#!/usr/bin/env python
import openai
import readline                                                                                                                                                       

# Set the API key
with open('apikey.txt', 'r') as f:
    api_token = f.read()
openai.api_key = api_token[:-1]
# Use the ChatGPT model to generate text
model_engine = "text-davinci-002"
                                                                                                                                                                       
# Main loop                                                                                                                                                           
def main():                                                                                                                                                           
    readline.parse_and_bind("tab: complete")
    readline.parse_and_bind("set editing-mode vi")
    with open("journal.txt", "a") as f:
        while True:
            try:
                question_Asked = input("User> ").lower()
            except EOFError:
                break
            if question_Asked in ("#quit", "#bye", "#exit"):
                break
            else:
                completion = openai.Completion.create(engine=model_engine, prompt=question_Asked, max_tokens=1024, n=1,stop=None,temperature=0.7)
                msg =completion.choices[0].text
                print("AI> "+msg)
                f.write("User> "+question_Asked+"\n")
                f.write("AI> "+msg+"\n")
    return

if __name__ == '__main__':                                                                                                                                            
    main() 
