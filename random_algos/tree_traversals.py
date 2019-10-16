# traverse trees

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_dfs(root):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node_val = stack.pop()
        print(node_val.val)

        if node_val.right:
            stack.append(node_val.right)
        if node_val.left:
            stack.append(node_val.left)

def postorder_dfs(root):
    if root.left:
        postorder_dfs(root.left)
    if root.right:
        postorder_dfs(root.right)
    print(root.val)


def bfs(root):
    queue = []
    queue.append(root)

    while len(queue) > 0:
        node_val = queue.pop(0)
        print(node_val.val)

        if node_val.left:
            queue.append(node_val.left)
        if node_val.right:
            queue.append(node_val.right)

t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.left.left = TreeNode(4)

t1.right = TreeNode(3)
t1.right.left = TreeNode(5)
t1.right.right = TreeNode(6)
t1.right.left.left = TreeNode(7)

#     1
#    / \
#   2   3
#  /   / \
# 4   5   6
#    /
#   7


preorder_dfs(t1)
print('_____')
bfs(t1)
print('_____')
postorder_dfs(t1)
