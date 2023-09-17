# # Task
# # You have a non-empty set s, and you have to execute N commands given in N lines.
# #
# # The commands will be pop, remove and discard.
#
# Input Format
#
# The first line contains integer n, the number of elements in the set s.
# The second line contains n space separated elements of set s.
# All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

# Sample Input
#
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5

# Sample Output
#
# 4


_ = input()
my_set = set(map(int, input().split()))
command_list = [input().split() for i in range(int(input()))]

for command in command_list:
    match command[0]:
        case 'pop':
            my_set.pop()
        case 'remove' if int(command[1]) in my_set:
            my_set.remove(int(command[1]))
        case 'discard':
            my_set.discard(int(command[1]))

print(sum(my_set))