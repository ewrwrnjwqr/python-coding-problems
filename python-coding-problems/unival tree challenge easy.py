#coding problem #8
#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#Given the r to a binary tree, count the number of unival subtrees.
# the given tree looks like..
#         0
#        / \
#       1   0
#          / \
#         1   0
#        / \
#       1   1

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

node_right_left1 = Node(1, Node(1), Node(1))
node_right1 = Node(0, node_right_left1, Node(0))
t = Node(0, Node(1), node_right1)
def in_order(r):
    if r.left:
        in_order(r.left)
    print(str(r.value) + ', ', end='')
    if r.right:
        in_order(r.right)

in_order(t)
print('')

def is_unival(r):
    if r is None:
        return True
    if r.left is not None and r.left.value != r.value:
        return False
    if r.right is not None and r.right.value != r.value:
        return False
    if is_unival(r.left) and is_unival(r.right):
        return True
    return False

def count_univals(r):
    if r is None:
        return 0

    total_count = count_univals(r.left) + count_univals(r.right)
    if is_unival(r):
        total_count += 1
    return total_count

def count_univals2(r):
    total_count, is_unival = helper(r)
    return total_count

def helper(r):
    if r is None:
        return 0, True

    left_count, is_left_unival = helper(r.left)
    right_count, is_right_unival = helper(r.right)

    is_unival = True
    if not is_left_unival or not is_right_unival:
        is_unival = False
    if r.left is not None and r.left.value != r.value:
        is_unival = False
    if r.right is not None and r.right.value != r.value:
        is_unival = False
    if is_unival:
        return left_count + right_count + 1, True
    else:
        return left_count + right_count, False

print(count_univals(t), 'should be 5')



