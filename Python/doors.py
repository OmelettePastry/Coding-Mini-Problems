# 100 Doors Problem

def main():

    doors = []
    
    for a in range(100):
        doors.append(0)
    
    # Outpuit door status
    print(*doors, sep = " ")
    
    for b in range(100):
        index = b
        while (index < 100):
            doors[index] = doors[index] ^ 1
            index = index + (b + 1)
    
    # Output door status
    print(*doors, sep = " ")
    
    # Output doors that are opened
    for c in range(100):
        if (doors[c] == 1):
            print(str(c+1), end = " ")
    
main()       
    