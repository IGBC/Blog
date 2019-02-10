#!/usr/bin/env python3
from sys import argv

class Move:
    def __init__(self, string):
        self.string = string
        self.opp = string[0]
        if "R" in string:
            self.opp = "R"
            self.val = 0
        elif "=>" in self.string:
            self.opp = "=>"
            args = string.split("=>")
            self.val = args[1]
            self.val2 = args[0]
        elif self.string.isdigit():
            self.val = int(self.string)
            self.opp = "ins"
        elif self.opp == "<":
            self.opp = "<<"
            self.val = 0
        else:
            self.val = int(string[1:])
    
    def do(self, current):
        return int(self.solve(current))
    def solve(self, current):
        if self.opp == "+":
            return current + self.val
        elif self.opp == "-":
            return current - self.val
        elif self.opp == "x":
            return current * self.val
        elif self.opp == "*":
            return current * self.val
        elif self.opp == "/":
            return current / self.val
        elif self.opp == "^":
            return current ** self.val
        elif self.opp == "<<":
            s = current
            frac = current % 10
            current = current - frac
            current = current / 10
            return current
        elif self.opp == "ins":
            if current >= 0:
                return (current * 10**len(self.string)) + self.val
            else:
                return (current * 10**len(self.string)) - self.val
        elif self.opp == "=>":
            return int(str(current).replace(self.val2, self.val))
        elif self.opp == "R":
            if current < 0:
                return int(str(current*-1)[::-1])*-1
            else:    
                return int(str(current)[::-1])    
        else:
            print("unknown command")
            exit()
    
    def __str__(self):
        return self.string
        
def recursive_move(movelist, current, moves_available, moves_remaining, goal):
    for move in moves_available:
        tmpmovelist = movelist.copy()
        tmpmovelist.append(move)
        next = move.do(current)
        #for i in tmpmovelist:
        #    print(str(i), end=" ")
        #print("= " + str(next))
        if next == goal:
            for i in tmpmovelist:
                print(str(i), end=" ")
            print("= " + str(next))
            return 1
        if moves_remaining > 1:
            res = recursive_move(tmpmovelist, next, moves_available, moves_remaining - 1, goal)
            if res == 1:
                return 1
    return 0

initial = int(argv[1])
goal = int(argv[2])
moves = int(argv[3])
available = []
for i in argv[4:]:
    available.append(Move(i))
recursive_move([], initial, available, moves, goal)
