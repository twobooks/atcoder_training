from collections import deque,Counter

SA = deque(list(input()))
SB = deque(list(input()))
SC = deque(list(input()))

turn = "a"
while len(SA)>=0 or len(SB)>=0 or len(SC)>=0:
    if turn == "a":
        if len(SA) == 0:
            print("A")
            exit()
        else:
            turn = SA.popleft()
    elif turn == "b":
        if len(SB) == 0:
            print("B")
            exit()
        else:
            turn = SB.popleft()
    else:
        if len(SC) == 0:
            print("C")
            exit()
        else:
            turn = SC.popleft()
