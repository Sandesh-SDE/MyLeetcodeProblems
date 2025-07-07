class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build the 4-level BST
def build_tree():
    root = TreeNode(3)
    
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    return root
    
'''
Note : when we want to traverse bST in level order we need to apply BFS
    
    for other traversal like inorder, preorder, postorder apply DFS

    here is the same code to print items level wise

    step 1 : create queue with list data structure and append root value to queue
    step 2 : while queue - this willl execute till queue does not become empty
    step 3 : use the for loop for len(queue)
    step 4 : pop the queue from 0 index until it becomes empty
    step 5 : get the current node value and print it this is what level wise printing
    step 6 : check if current node has left and right 
    step 7 : if it has then append it to queue accordingly and loops runs so on

'''
def bfs(root):

    if root is None:
        return None
    
    queue = [root]

    avg_output = []

    while queue:
        print()
        # print(len(queue))
        level = len(queue)
        levels = []
        
        l = 0
        count = 0
        for _ in range(level):

            curr = queue.pop(0)
            print(curr.val)
            l += curr.val
            count += 1
            
            levels.append(curr.val)
            

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)

            
        avg = l / count
        print("l value==>",l, count, avg)
        avg_output.append(avg)
        # print(levels)

    print(avg_output)
    return avg_output
            
    

root = build_tree()
# print_tree(root)
bfs(root)
