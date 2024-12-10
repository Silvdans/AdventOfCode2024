import sys
 
D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[int(c) for c in row] for row in L]

COUNT = 0
def check_if_path_can_continue(liste: list, i, j, nb, direction):
    new_coordinates = None
    rows = len(liste)
    cols = len(liste[0])

    if direction == "down" and i + 1 < rows and liste[i + 1][j] == nb + 1:
        new_coordinates = i + 1, j
    if direction == "up" and i - 1 >= 0 and liste[i - 1][j] == nb + 1:
        new_coordinates = i - 1, j
    if direction == "right" and j + 1 < cols and liste[i][j + 1] == nb + 1:
        new_coordinates = i, j + 1
    if direction == "left" and j - 1 >= 0 and liste[i][j - 1] == nb + 1:
        new_coordinates = i, j - 1

    return new_coordinates


def main():
    for i, liste in enumerate(G):
        for j, number in enumerate(liste):
            if number == 0:
                    k = i
                    l = j
                    while True:
                        if not recursive_check(G, k, l, number):
                            break
    print(COUNT)
                            
def recursive_check(G, k, l, number): 
    global COUNT                          
    for direction in ["up", "down", "left", "right"]: 
        if new_coordinates := check_if_path_can_continue(G, k, l, number, direction):
            k = new_coordinates[0]
            l = new_coordinates[1]
            number +=1
            if recursive_check(G, k, l, number):
                return True
        else:
            if number == 9:
                COUNT += 1
                number = 0
    return False

main()    
    
    
