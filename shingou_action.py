from enum import Enum
import sys
class Shingou(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3

def act_shingou(color):
    if color == 1:
        print("とまれ")
    elif color == 2:
        print("すすめ")
    elif color == 3:
        print("ちゅうい") 
    else:
        raise Exception("信号機の色に対応していません")
    return Shingou(color)
args = sys.argv
act_shingou(int(args[1]))