# You are given an integer N. Print a staircase consisting of N steps using the symbol "#" and spaces.
# For each step, the spaces should be printed first followed by the symbol "#".
# The last line should consist of N symbols "#".

# For example, for N = 6, the staircase should look like this:
#
#      #
#     ##
#    ###
#   ####
#  #####
# ######
# Note: The rightmost "#" should not contain any leading spaces.

n = int(input())
for i in range(1, n + 1):
    print(f'{"#" * i:>{n}}')
