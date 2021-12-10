"""
Ethan Gonzalez
Daniel Gonzalez
Hugo Dorta
Connect 4
December 13, 2021
"""
p1Play = ""
p2Play = ""
row1 = []
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []
#variables to be put in a list


#imports numbrt python package, renamed np

def move():
  A1 = "A1"
  B1 = "B1"
  C1 = "C1"
  D1 = "D1"
  E1 = "E1"
  F1 = "F1"
  A2 = "A2"
  B2 = "B2"
  C2 = "C2"
  D2 = "D2"
  E2 = "E2"
  F2 = "F2"
  A3 = "A3"
  B3 = "B3"
  C3 = "C3"
  D3 = "D3"
  E3 = "E3"
  F3 = "F3"
  A4 = "A4"
  B4 = "B4"
  C4 = "C4"
  D4 = "D4"
  E4 = "E4"
  F4 = "F4"
  A5 = "A5"
  B5 = "B5"
  C5 = "C5"
  D5 = "D5"
  E5 = "E5"
  F5 = "F5"
  A6 = "A6"
  B6 = "B6"
  C6 = "C6"
  D6 = "D6"
  E6 = "E6"
  F6 = "F6"
  A7 = "A7"
  B7 = "B7"
  C7 = "C7"
  D7 = "D7"
  E7 = "E7"
  F7 = "F7"

  while True:
    row1 = [A1, A2, A3, A4, A5, A6, A7]
    row2 = [B1, B2, B3, B4, B5, B6, B7]
    row3 = [C1, C2, C3, C4, C5, C6, C7]
    row4 = [D1, D2, D3, D4, D5, D6, D7]
    row5 = [E1, E2, E3, E4, E5, E6, E7]
    row6 = [F1, F2, F3, F4, F5, F6, F7]

    print("Row A: " + str(row1))
    print("Row B: " + str(row2))
    print("Row C: " + str(row3))
    print("Row D: " + str(row4))
    print("Row E: " + str(row5))
    print("Row F: " + str(row6))

    p1Play = input("Where would you like to put your X, P1: ")
    while p1Play not in row1 and p1Play not in row2 and p1Play not in row3 and p1Play not in row4 and p1Play not in row5 and p1Play not in row6:
      p1Play = input("Where would you like to put your X, P1: ")
    
    p2Play = input("Where would you like to put your 0, P2: ")
    while p2Play not in row1 and p2Play not in row2 and p2Play not in row3 and p2Play not in row4 and p2Play not in row5 and p2Play not in row6:
      p2Play = input("Where would you like to put your 0, P2: ")
    
  #all options will be X for player 1
    if p1Play == "A1":
      A1 = "X"
    elif p1Play == "A2":
      A2 = "X"
    elif p1Play == "A3":
      A3 = "X"
    elif p1Play == "A4":
      A4 = "X"
    elif p1Play == "A5":
      A5 = "X"
    elif p1Play == "A6":
      A6 = "X"
    elif p1Play == "A7":
      A7 = "X"
    elif p1Play == "B1":
      B1 = "X"
    elif p1Play == "B2":
      B2 = "X"
    elif p1Play == "B3":
      B3 = "X"
    elif p1Play == "B4":
      B4 = "X"
    elif p1Play == "B5":
      B5 = "X"
    elif p1Play == "B6":
      B6 = "X"
    elif p1Play == "B7":
      B7 = "X"
    elif p1Play == "C1":
      C1 = "X"
    elif p1Play == "C2":
      C2 = "X"
    elif p1Play == "C3":
      C3 = "X"
    elif p1Play == "C4":
      C4 = "X"
    elif p1Play == "C5":
      C5 = "X"
    elif p1Play == "C6":
      C6 = "X"
    elif p1Play == "C7":
      C7 = "X"
    elif p1Play == "D1":
      D1 = "X"
    elif p1Play == "D2":
      D2 = "X"
    elif p1Play == "D3":
      D3 = "X"
    elif p1Play == "D4":
      D4 = "X"
    elif p1Play == "D5":
      D5 = "X"
    elif p1Play == "D6":
      D6 = "X"
    elif p1Play == "D7":
      D7 = "X"
    elif p1Play == "E1":
      E1 = "X"
    elif p1Play == "E2":
      E2 = "X"
    elif p1Play == "E3":
      E3 = "X"
    elif p1Play == "E4":
      E4 = "X"
    elif p1Play == "E5":
      E5 = "X"
    elif p1Play == "E6":
      E6 = "X"
    elif p1Play == "E7":
      E7 = "X"
    elif p1Play == "F1":
      F1 = "X"
    elif p1Play == "F2":
      F2 = "X"
    elif p1Play == "F3":
      F3 = "X"
    elif p1Play == "F4":
      F4 = "X"
    elif p1Play == "F5":
      F5 = "X"
    elif p1Play == "F6":
      F6 = "X"
    elif p1Play == "F7":
      F7 = "X"
    


  # all options will be 0 for player 2  
    if p2Play == "A1":
      A1 = "0"
    elif p2Play == "A2":
      A2 = "0"
    elif p2Play == "A3":
      A3 = "0"
    elif p2Play == "A4":
      A4 = "0"
    elif p2Play == "A5":
      A5 = "0"
    elif p2Play == "A6":
      A6 = "0"
    elif p2Play == "A7":
      A7 = "0"
    elif p2Play == "B1":
      B1 = "0"
    elif p2Play == "B2":
      B2 = "0"
    elif p2Play == "B3":
      B3 = "0"
    elif p2Play == "B4":
      B4 = "0"
    elif p2Play == "B5":
      B5 = "0"
    elif p2Play == "B6":
      B6 = "0"
    elif p2Play == "B7":
      B7 = "0"
    elif p2Play == "C1":
      C1 = "0"
    elif p2Play == "C2":
      C2 = "0"
    elif p2Play == "C3":
      C3 = "0"
    elif p2Play == "C4":
      C4 = "0"
    elif p2Play == "C5":
      C5 = "0"
    elif p2Play == "C6":
      C6 = "0"
    elif p2Play == "C7":
      C7 = "0"
    elif p2Play == "D1":
      D1 = "0"
    elif p2Play == "D2":
      D2 = "0"
    elif p2Play == "D3":
      D3 = "0"
    elif p2Play == "D4":
      D4 = "0"
    elif p2Play == "D5":
      D5 = "0"
    elif p2Play == "D6":
      D6 = "0"
    elif p2Play == "D7":
      D7 = "0"
    elif p2Play == "E1":
      E1 = "0"
    elif p2Play == "E2":
      E2 = "0"
    elif p2Play == "E3":
      E3 = "0"
    elif p2Play == "E4":
      E4 = "0"
    elif p2Play == "E5":
      E5 = "0"
    elif p2Play == "E6":
      E6 = "0"
    elif p2Play == "E7":
      E7 = "0"
    elif p2Play == "F1":
      F1 = "0"
    elif p2Play == "F2":
      F2 = "0"
    elif p2Play == "F3":
      F3 = "0"
    elif p2Play == "F4":
      F4 = "0"
    elif p2Play == "F5":
      F5 = "0"
    elif p2Play == "F6":
      F6 = "0"
    elif p2Play == "F7":
      F7 = "0"


    if p1Play in row1 or p1Play in row2 or p1Play in row3 or p1Play in row4 or p1Play in row5:
      if p1Play == A1 or p1Play == B1 or p1Play == C1 or p1Play == D1 or p1Play == E1:
        p1Play == F1
  
while True:
  move()