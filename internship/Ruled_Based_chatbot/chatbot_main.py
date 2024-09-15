def add():
    a=input(str("Enter first number:"))
    b=input(str("Enter second number:"))
    c=a+b
    return c

def chat_response(userInput):
    if userInput=='what is your name' or userInput=='who are you':
        return("I am a Ruled based chatbot \n I can answer some preseted questions only. ")
    elif userInput=='can you sum two numbers':
        print("Yes, I can .\n Do you want sum two digits? (write Yes/No)\n")
        option=input(str("... "))
        if option=='yes':
           print(add())


def main():
    print("welcome to reuled based chat bot. \n Hello sir . how can i help you \n write exit to stop ")

    
    while True:
        promt=input(str("you: "))
        userInput=promt.lower()

        if userInput=='exit':
            print("Have a great day! bye")
            break
        else:
            response=chat_response(userInput)
            print(response)

if __name__ == "__main__":
    main()
