from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToeApp(App):
    def build(self):
        self.title = 'Tic-Tac-Toe'
        self.grid = GridLayout(cols=3, rows=3)
        self.board = [' ' for _ in range(9)]
        self.buttons = []

        for i in range(9):
            button = Button(text='', font_size=32)
            button.bind(on_press=self.on_button_press)
            self.grid.add_widget(button)
            self.buttons.append(button)

        return self.grid

    
        
    def on_button_press(self, instance):
        index = self.buttons.index(instance)
        if self.board[index] == ' ':
            self.board[index] = 'X'
            instance.text = 'X'
            print(f'Button {index} clicked, board state: {self.board}')
        
            
    

if __name__ == '__main__':
    TicTacToeApp().run()
