
um = 3 
uc = 3 
rm = 0 
rc = 0 
flag = 0 


def display():
    print(f"Left: {'M ' * um} {'C ' * uc} | Boat: {'M ' * rm} {'C ' * rc} | Right: {'M ' * (3 - rm)} {'C ' * (3 - rc)}")


def is_reached():
    return rm == 3 and rc == 3


def solve():
    global um, uc, rm, rc, flag
    
    while not is_reached():
        if flag == 0:
            if um >= 2: 
                rm += 2
                um -= 2
                print("Moving 2 Missionaries.")
            elif uc >= 2:  
                rc += 2
                uc -= 2
                print("Moving 2 Cannibals.")
            elif um >= 1 and uc >= 1:  
                rm += 1
                uc -= 1
                um -= 1
                print("Moving 1 Missionary and 1 Cannibal.")
            elif um >= 1: 
                rm += 1
                um -= 1
                print("Moving 1 Missionary.")
            elif uc >= 1:  
                rc += 1
                uc -= 1
                print("Moving 1 Cannibal.")
            flag = 1  
        else: 
            if rm >= 2:  
                rm -= 2
                um += 2
                print("Returning with 2 Missionaries.")
            elif rc >= 2:  
                rc -= 2
                uc += 2
                print("Returning with 2 Cannibals.")
            elif rm >= 1 and rc >= 1:  
                rm -= 1
                rc -= 1
                um += 1
                uc += 1
                print("Returning with 1 Missionary and 1 Cannibal.")
            elif rm >= 1: 
                rm -= 1
                um += 1
                print("Returning with 1 Missionary.")
            elif rc >= 1:  
                rc -= 1
                uc += 1
                print("Returning with 1 Cannibal.")
            flag = 0  
        
        display()  

def main():
    print("Missionaries And Cannibals Problem")
    display()
    solve()
    display()  

main()
