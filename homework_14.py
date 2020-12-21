#1
class User:
    def __init__(self, name):
        self.name = name
        
    def send_message(self, user, message):
        pass
    
    def post(self, message):
        pass
    
    def info(self):
        return ""
    
    def describe(self):
        print(f"{self.name} {self.info()}")
    

class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.bth_date = birthday
    
    def info(self):
        print(f"Date of birth: {self.bth_date}")
    
    def subscribe(self, user):
        pass
        
        
class Community(User):
<<<<<<< HEAD
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
=======
    def __init__(self, name, discription):
        super().__init__(name)
        self.description = discription
>>>>>>> 80228d4541f0cacf12b391a1c2469bd2d6c28f59
        
    def info(self):
        print(f"Description: {self.description}")

u = User("Hayk")
p = Person(u,"Feb 27")
d = Community(u,"...")
print(u.info())
u.describe()
p.info()
d.info()


#2
import copy
class TicTacToe:
    def __init__(self):
        self.new_game()
        
    def new_game(self):
        print(5*" - ")
        self.board = [["-", "-", "-"] for _ in range(3)]
        self.move = 'X'
        self.winner = None
        self.flag_move = False
        self.flag_winner = False

    def get_field(self):
        print(copy.deepcopy(self.board))

    def check_field(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '-':
                self.winner = self.board[i][0]
                break
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '-':
                self.winner = self.board[0][i]
                break
        if not self.winner and (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                                self.board[0][2] == self.board[1][1] == self.board[2][0]) and \
                                self.board[1][1] != '-':
            self.winner = self.board[1][1]
        if "-" not in "".join(self.board[0]) + "".join(self.board[0]) + "".join(self.board[0]) and not self.winner:
            self.winner = "D"
        if self.winner:
            return self.winner
        else:
            return None

    def make_move(self, row, col):
        if self.board[row - 1][col - 1] != "-":
            print(f"Cell {row}, {col} is already filled")
            self.flag_move = True
        self.board[row - 1][col - 1] = self.move
        if self.move == 'X' and not self.flag_move:
            self.move = 'O'
        else:
            self.move = 'X'
        winner = self.check_field()
        if not self.flag_winner:
            if winner == "X":
                print("X-player won")
                self.flag_winner = True
            elif winner == "O":
                print("O-Player won")
                self.flag_winner = True
            elif winner == "D":
                print("Draw")
                self.flag_winner = True
            else:
                print("Continue playing")
            if self.flag_winner:
                print("Game Over")
        else:
            print("Game Over")
    
t = TicTacToe()
t.make_move(1,1)
t.make_move(3,1)
t.make_move(2,2)
t.make_move(3,3)
t.make_move(3,2)
t.make_move(1,2)
t.make_move(2,3)
t.make_move(2,3)
t.make_move(2,1)
t.make_move(1,3)
t.make_move(1,3)
t.get_field()
t.new_game()
t.make_move(3,2)
t.make_move(2,3)
t.make_move(2,2)
t.make_move(1,1)
print(t.check_field())
t.make_move(1,2)
print(t.check_field())
