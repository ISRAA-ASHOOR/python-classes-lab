class Game() :

    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    
    def play_game(self):
    
        while not self.winner and not self.tie:
            self.render()  
            move = self.get_move()  
            self.board[move] = self.turn  
            self.check_for_winner()  
            self.check_for_tie() 
            
            if not self.tie: 
                self.switch_turn()  
        
        self.render() 

    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)
    
    def print_message(self):
        if ( self.tie == True ):
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input(f"Enter a valid move (example: a1): ").lower()
            if move in self.board and self.board[move] is None:
                return move 
            else:
                print("Invalid move. Please enter a valid key.")

    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.board['a1'] 
        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = self.board['a2']
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = self.board['a3']
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = self.board['a1']
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = self.board['b1']
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.board['c1']
        elif self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']):
            self.winner = self.board['a1']
        elif self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']):
            self.winner = self.board['a3']

    def check_for_tie(self):
        # the all() is from python doc ( https://docs.python.org/3/library/functions.html ) , I had to make some research to done this game 
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True

    def switch_turn(self):
        turns = {'X': 'O', 'O': 'X'}
        self.turn = turns[self.turn]  


game_instance = Game()
game_instance.play_game()      