from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def add():
    a = input("Enter first number:")
    b = input("Enter second number:")
    c = a + b
    return c

def sub():
    a= input("Enter first number:")
    b=input("Enter second number:")
    return a-b

def chat_response(userInput):
    if userInput == 'what is your name' or userInput == 'who are you':
        return "I am a rule-based chatbot. I can answer some preset questions only."
    elif userInput == 'what can you do':
        return "I can sum two numbers, subtract two numbers, and perform some minor operations."
    elif userInput == 'can you sum two numbers':
        return "Yes, I can. Do you want to sum two digits? (write Yes/No)"
    elif userInput == 'subtract two numbers':
        return sub()
    else:
        return "I am not sure how to answer that."

class ChatBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatBotUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.label = Label(text="Welcome to the rule-based chatbot! How can I help you?\nWrite 'exit' to stop.")
        self.add_widget(self.label)
        
        self.chat_input = TextInput(size_hint_y=None, height=40)
        self.add_widget(self.chat_input)
        
        self.send_button = Button(text="Send", size_hint_y=None, height=40)
        self.send_button.bind(on_press=self.send_message)
        self.add_widget(self.send_button)
        
        self.output_label = Label(text="")
        self.add_widget(self.output_label)
    
    def send_message(self, instance):
        userInput = self.chat_input.text
        userInput = userInput.lower()
        # chat_response(userInput)
        
        if userInput == 'exit':
            self.output_label.text = "Have a great day! Bye"
        else:
            response = chat_response(userInput)
            self.output_label.text = response

class ChatBotApp(App):
    def build(self):
        return ChatBotUI()

if __name__ == '__main__':
    ChatBotApp().run()
