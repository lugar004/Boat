# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

boat = 0
limit = int(input("Limit:"))
crew = list(map(int,input("Members in group:")[1:-1].strip().split(',')))
crew.sort()
temp = crew.copy()
j = len(crew)-1
l = 0
for i in range(0,len(crew)):
    if len(temp) == 0:
            break
    if (len(crew) == 1):
        if (crew[0] < limit):
            boat += 1
            temp.pop()
            if len(temp) == 0:
                break
        else:
            print("Huge groups are not allowed")
    elif (crew[l] + crew[j] > limit):
        boat += 1 
        j -= 1 # j enters the boat
        l = l # l waits for the next boat
        temp.pop()
        if len(temp) == 0:
            break
    else:
        boat += 1 # l and j gets into the boat
        l += 1
        j -= 1
        temp.pop(0)
        if (len(temp) != 0):
            temp.pop()
        if len(temp) == 0:
            break

print("boat = ",boat)
            
            
            
            
    
