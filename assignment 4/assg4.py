#Question1
print('Question 1\n')
def towerofhanoi(n, source, destination, aux):
    if n == 0:
        return
    
    towerofhanoi(n-1, source, aux, destination)
    print(f"Move Disk {n} from {source} to {destination}")
    towerofhanoi(n-1, aux, destination, source)

#calling TOH funtion 
towerofhanoi(3, 'A', 'C', 'B')
