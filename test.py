#1 add memory
#2 cheat from the memory
#3 let someone else cheat off of you

memory = [0] *101
def fib(n):
    if memory[n] != 0:
        return memory[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        a = fib(n-1)+fib(n-2)
        memory[n] = a
        return a

#for i in range(1,101):
fib(101)

