"""Game.py"""
import re
import os


class Game(object):
    """Game class"""

    def __init__(self):
        self.players = ['', '', 'friendship']
        self.vocabulary = ['X', 'O']
        self.drow = True
        self.field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = False
        self.step_counter = 0

    def print_field(self):
        """print current field"""
        if not self.drow:
            return
        try:
            os.system('clear')
        except Exception:
            os.system('cls')
        print ('|'.join(self.field[0]))
        print ('_____')
        print ('|'.join(self.field[1]))
        print ('_____')
        print ('|'.join(self.field[2]))

    def validate(self, incoming_data):
        """validate incoming data"""
        try:
            incoming_data[0] = int(incoming_data[0])
            incoming_data[1] = int(incoming_data[1])
            if len(incoming_data) != 2:
                return False
            if incoming_data[0] > 2 or incoming_data[0] < 0:
                return False
            if incoming_data[1] > 2 or incoming_data[1] < 0:
                return False
            return True
        except Exception:
            return False

    def read(self, data=None):
        """read step"""
        if data is not None:
            return re.split(r'\s+', data)
        data = input()
        return re.split(r'\s+', data)

    def put(self, step):
        """put current step"""
        if not self.validate(step):
            print ("Invalid cell")
            return False
        if self.field[step[0]][step[1]] != " ":
            print ("Cell is full")
            return False
        current_char = self.vocabulary[int(self.current_player)]
        self.field[step[0]][step[1]] = current_char
        self.current_player = not self.current_player
        return True

    def check_field(self):
        """Check current field"""
        if self.field[0][0] == self.field[1][1] == self.field[2][2]:
            if self.field[1][1] != " ":
                return self.vocabulary.index(self.field[1][1])
        if self.field[0][2] == self.field[1][1] == self.field[2][0]:
            if self.field[1][1] != " ":
                return self.vocabulary.index(self.field[1][1])

        for column in range(0, 3):
            if len(set([line[column] for line in self.field])) == 1:
                if self.field[0][column] != " ":
                    return self.vocabulary.index(self.field[0][column])

        field_status = False
        for line in self.field:
            if len(set(line)) == 1 and line[0] != " ":
                return self.vocabulary.index(line[0])
            for item in line:
                if item == " ":
                    field_status = True
            if field_status:
                break
        if not field_status:
            return 2

    def start(self):
        """Start game"""
        self.field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.current_player = False
        self.step_counter = 0
        print ('Players: \n1st player: ')
        self.players[0] = input()
        print ('2nd player: ')
        self.players[1] = input()

        while True:
            self.print_field()
            if self.step_counter > 4:
                winner = self.check_field()
                if winner is not None:
                    print ('Winner is ' + self.players[winner])
                    return
            if self.drow:
                print (self.players[int(self.current_player)] + ':')
            if not self.put(self.read()):
                self.drow = False
            else:
                self.drow = True
                self.step_counter += 1
