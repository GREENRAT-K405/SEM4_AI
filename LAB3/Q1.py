import random
#i will use this to create dirt randomly

def rules(room, status):
    if (status == "dirty"):
        return 'suck'
    if room == 'A':
        return 'right'
    if room == 'B':
        return random.choice(['left', 'right'])
    if room == 'C':
        return 'left'
    
def solution():
    s1 = random.choice(['dirty', 'clean'])
    s2 = random.choice(['dirty', 'clean'])
    s3 = random.choice(['dirty', 'clean'])
    print("Room A status: ", s1)
    print("Room B status: ", s2)
    print("Room C status: ",s3)
    
    # store in list
    rooms = [s1, s2, s3]
    
    location = ['A', 'B', 'C']
    print("Start loc (0 for A, 1 for B, 2 for C): ")
    idx = int(input())
    
    score = 0
    print("Step | Percept | Action | Score")
    
    for step in range(1, 11):
        curr_room = location[idx]
        curr_status = rooms[idx]
        
        act = rules(curr_room, curr_status)
        
        if act == 'suck':
            rooms[idx] = 'clean'
            score = score + 10
        elif act == 'right':
            score = score - 1
            if idx < 2: idx = idx + 1
        elif act == 'left':
            score = score - 1
            if idx > 0: idx = idx - 1
            
        print(step, " | ", curr_room, curr_status, " | ", act, " | ", score)
            
        # check if all clean
        if rooms[0] == 'clean' and rooms[1] == 'clean' and rooms[2] == 'clean':
            print("all cleaned")
            break
    print("Final Score: ", score)
    
if __name__ == "__main__":
    solution()