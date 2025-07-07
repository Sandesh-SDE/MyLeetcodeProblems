class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the 4-level BST
def build_tree():
    # root = TreeNode(2)
    # root.right = TreeNode(3)
    # root.right.right = TreeNode(4)
    # root.right.right.right = TreeNode(5)
    # root.right.right.right.right = TreeNode(6)
    
    

    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)
    
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    return root


def minimum_depth(root):

    queue = [root]
    depth = 1
    
    while queue:

        for _ in range(len(queue)):
            current_node = queue.pop(0)

            # minimum depth
            if current_node.left is None and current_node.right is None:
                print(depth)
                return depth

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)


        depth += 1

def maximum_depth(root):

    queue = [root]
    depth = 0
    
    while queue:

        for _ in range(len(queue)):
            current_node = queue.pop(0)

            if current_node.left:
                queue.append(current_node.left)

            if current_node.right:
                queue.append(current_node.right)

        depth += 1
    return depth

def minimum_depth1(root):

    queue = [(root, 1)]
    # result = []
    
    while len(queue) > 0:
        print()
        current_node, depth = queue.pop(0)
        print(current_node.val,"d", depth)
        # result.append(current_node.val)

        if current_node.left is None and current_node.right is None:
            print("min depth",depth)

        if current_node.left:
            queue.append((current_node.left, depth + 1))

        if current_node.right:
            queue.append((current_node.right, depth + 1))



        

    # print(result)


root = build_tree()
minimum_depth(root)
# print(maximum_depth(root))