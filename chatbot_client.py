from chatbotsclient.chatbot import Chatbot
from chatbotsclient.message import Message
from typing import List
from chatbot import get_response
from colorama import Fore, Style

def compute(input: str, conversation: List[Message]):
    return get_response(input)
    
def respond(message: Message, conversation: List[Message]):
    answer = compute(message.message, conversation)
    return answer

# MAIN METHOD
if __name__ == '__main__':
    print(Fore.RED + "Do you want to establish a connection to other chatbots?" + Style.RESET_ALL + " Answer with 'yes' for yes and 'no' for no...")
    user_input = input(">>> ").lower().strip()
        
    
    if(user_input == "yes"):
        chatbot = Chatbot(respond, "SnapeBot")

    else:
        print(Fore.GREEN + "Alright. You may speak now!" + Style.RESET_ALL)
        user_input = input(">>> ").lower().strip()
        while "exit" not in user_input.lower():
            
            answer = get_response(user_input)       

            print(Fore.GREEN + answer + Style.RESET_ALL)
            user_input = input(">>> ").lower().strip()