from chatbotsclient.chatbot import Chatbot
from chatbotsclient.message import Message
from typing import List
from chatbot import get_response
from chatbot import get_greeting
from chatbot import get_farewell
from colorama import Fore, Style

def compute(input: str, conversation: List[Message]):
    return get_response(input)
    
def respond(message: Message, conversation: List[Message]):
    answer = compute(message.message, conversation)
    return answer

# MAIN METHOD
if __name__ == '__main__':
    print(Fore.RED + "Do you want to establish a connection to other chatbots?" + Style.RESET_ALL + " Answer with 'yes' for yes and 'no' for no...")
    user_input = input(">>> ").strip()
        
    
    if(user_input == "yes"):
        chatbot = Chatbot(respond, "SnapeBot")

    else:
        print(Fore.GREEN + get_greeting() + Style.RESET_ALL)
        user_input = input(">>> ").strip()
        while "exit" not in user_input.lower():
            
            answer = get_response(user_input)       

            print(answer + Style.RESET_ALL)
            print("________________________________________________")
            user_input = input(">>> ").strip()

        print(get_farewell())