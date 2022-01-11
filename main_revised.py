from pyblinkpico import *;
import time

m= display
N= 8

def get_character_matrix(char):
        
    dict = {'A' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0]], 
        'B' : [[0,1,1,1,1,1,0,0],[0,1,1,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,1,1,1,1,1,0,0],[0,1,1,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
        'C' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
        'D' : [[0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,0,0]], 
        'E' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
        'F' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0]],
        'G' : [[0,0,1,1,1,1,1,0],[0,1,1,0,0,0,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,1,0,0,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]],
        'H' : [[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0]],
        'I' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
        'J' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,1,1,0],[0,0,0,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,0,0]],
        'K' : [[0,1,1,0,0,0,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,1,1,0,0],[0,1,1,1,1,0,0,0],[0,1,1,1,0,0,0,0],[0,1,1,1,1,0,0,0],[0,1,1,0,1,1,0,0],[0,1,1,0,0,1,1,0]],
        'L' : [[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0]],
        'M' :[[1,1,0,0,0,0,1,1],[1,1,1,0,0,1,1,1],[1,1,1,1,1,1,1,1],[1,1,0,1,1,0,1,1],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1],[1,1,0,0,0,0,1,1]],
        'N' :[[1,1,1,0,0,0,1,1],[1,1,1,0,0,0,1,1],[1,1,1,1,0,0,1,1],[1,1,0,1,0,0,1,1],[1,1,0,0,1,0,1,1],[1,1,0,0,1,1,1,1],[1,1,0,0,0,1,1,1],[1,1,0,0,0,1,1,1]],
        'O' : [[0,0,1,1,1,1,0,0],[0,1,1,1,1,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,1,1,1,1,0,0]],
        'P' : [[0,1,1,1,1,1,0,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,0,0,1,1,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0]],
        'Q' : [[0,0,1,1,0,0,0,0],[0,1,1,1,1,0,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,1,0,0],[1,0,0,0,0,1,1,0],[0,1,1,1,1,1,1,0],[0,0,1,1,0,0,0,1]],
        'R' : [[0,1,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,1,1,1,1,0,0],[0,1,0,1,0,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,1,0]],
        'S' : [[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,1,1],[1,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0],[0,0,0,0,0,0,1,1],[1,1,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
        'T' : [[0,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
        'U' : [[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
        'V' : [[0,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,1],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
        'W' : [[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,0,0,1,1,0,0,1],[1,1,1,1,1,1,1,1]],
        'X' : [[1,0,0,0,0,0,0,1],[1,1,0,0,0,0,1,1],[0,1,1,0,0,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,1,1,0,0,1,1,0],[1,1,0,0,0,0,1,1],[1,0,0,0,0,0,0,1]],
        'Y' : [[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,1,1,0,0,1,1,0],[0,0,1,1,1,1,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]],
        'Z' : [[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]],
        'a' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,1,0]],
        'b' : [[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        'c' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,1,0],[0,0,0,1,1,1,0,0]],
        'd' : [[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0]],
        'e' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0],[0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,1,1,1,0]],
        'f' : [[0,0,0,1,1,1,1,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0]],
        'g' : [[0,0,0,1,1,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
        'h' : [[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0]],
        'i' : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
        'j' : [[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]],
        'k' : [[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,1,0,0,0,0],[0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0],[0,1,0,0,1,0,0,0]],
        'l' : [[0,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0]],
        'm' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0],[0,0,1,0,1,0,1,0]],
        'n' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0]],
        'o' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        'p' :[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0],[0,0,1,0,0,0,1,0],[0,0,1,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,1,0,0,0,0,0]],
        'q' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,1,0,1,0],[0,0,0,0,1,1,0,0],[0,0,0,0,1,0,0,0]],
        'r' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0]],
        's' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        't' : [[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,1,1,0]],
        'u' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,0,1,1,0]],
        'v' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,1,0],[0,1,0,0,0,0,1,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,0,0,0]],
        'w' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,0,1,1,1,1,1,0]],
        'x' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,0,0,1,0,0],[0,0,1,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,0]],
        'y' : [[0,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,0,0,1,0,0,0],[0,0,1,1,1,0,0,0]],
        'z' : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,1,1,1,1,0]],
        '0' : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,1,1,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]],
         0  : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,1,1,0],[0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,0],[0,1,0,1,1,0,1,0],[0,1,1,1,0,0,1,0],[0,1,1,0,0,0,1,0],[0,0,1,1,1,1,0,0]], 
        '1' : [[0,0,0,0,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,1,1,1,1,1,0]],
        1   : [[0,0,0,0,1,0,0,0],[0,0,0,1,1,0,0,0],[0,0,1,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0],[0,1,1,1,1,1,1,0]],
        '2' : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0]], 
        2   : [[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,1,1,1,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,1,1,1,1,0]],
        '3' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0]],
        3   : [[0,0,0,0,0,0,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,0,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        '4' : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0]],
        4   : [[0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,0],[0,0,1,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,1,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0]],
        '5' : [[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
        5   : [[0,0,1,1,1,1,1,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,1,0],[0,1,1,1,1,1,0,0]],
        '6' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        6   : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,1,1,1,1,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        '7' :[[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0]],
        7   :[[0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,0],[0,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,0],[0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0]],
        '8' : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        8   : [[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,1,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        '9' : [[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        9   : [[0,0,0,1,1,0,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,1,0,0,1,0,0],[0,0,0,1,1,1,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,0]],
        ' '   : [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    }
    return dict[char]



def show_character (letter):
        char_matrix = get_character_matrix(letter)
        for i in range(0,8):
            for j in range(0,8):
                m[i, j] = char_matrix[i][j]
    
def show_withoff(char, off):
        char_matrix = get_character_matrix(char)
        if (off>=0):
            sc = off
            ran = 8- off
            for i in range(0,8):
                for j in range(0,ran):
                        m[i,j] = char_matrix[i][j+sc]
        else:
            sc = -off 
            ran = 8+ off
            sc = [0,1,2,3,4,5,6,7,8,9]
            for i in range(0,8):
                x = 0
                for j in range(ran,8):
                    m[i,j] = char_matrix[i][sc[x]]
                    x =x+1
                    
            
    
def clear():
    for i in range(0,8):
            for j in range(0, 8):
                m[i,j] = 0


def character_scroll(char_str):
    a = [None] * len(char_str)
    until = (len(char_str) -1)
    #show_withoff(char_str[0], 0)
    for i in range(until):
    
        for  j in range(1,9):
            
            time.sleep(0.1)
            show_withoff(char_str[i],j)
            show_withoff(char_str[i+1], -j)
            
    for i in range(0,8):
        show_withoff(char_str[until],i)
        time.sleep(0.1)
    
    
    
    
display.fill(0);
display.auto_show(True)

show_character(1)
a = 'hello world '
character_scroll (a)
