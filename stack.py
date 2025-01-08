from collections import deque

stack = deque()

inp = 'we will conquer covid-19'
for char in inp:
    stack.append(char)
st = stack.reverse()
print(st)
print('-------------------------------------------')
rev_string = ''
while stack:
    rev_string += stack.pop()
print(rev_string)


    
    