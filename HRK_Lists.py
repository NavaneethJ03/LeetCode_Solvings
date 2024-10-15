if __name__ == '__main__':
    # Initialize an empty list
    lst = []
    
    # Read the number of commands
    N = int(input())
    
    # Iterate through the commands
    for _ in range(N):
        # Read each command
        command = input().split()
        
        # Parse the command and perform the corresponding list operation
        if command[0] == 'insert':
            lst.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(lst)
        elif command[0] == 'remove':
            lst.remove(int(command[1]))
        elif command[0] == 'append':
            lst.append(int(command[1]))
        elif command[0] == 'sort':
            lst.sort()
        elif command[0] == 'pop':
            lst.pop()
        elif command[0] == 'reverse':
            lst.reverse()