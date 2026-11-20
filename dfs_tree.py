
# ASSESSMENT 3.6
# DFS METHODS IN TREE
# Name: IAN

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree using IAN
def create_tree():
    root = Node("I")

    root.left = Node("A")
    root.right = Node("N")

    return root


# PREORDER: Root - Left - Right
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# INORDER: Left - Root - Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# POSTORDER: Left - Right - Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# MAIN PROGRAM
def main():
    root = create_tree()

    print("ASSESSMENT 3.6")
    print("DFS METHODS IN TREE")
    print("NAME: IAN")
    print("---------------------------")

    print("Preorder: ", end="")
    preorder(root)

    print("\nInorder: ", end="")
    inorder(root)

    print("\nPostorder: ", end="")
    postorder(root)

    print("\nProgram Completed!")


if __name__ == "__main__":
    main()

# ASSESSMENT 3.6
# DFS METHODS IN TREE
# Name: IAN

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree using IAN
def create_tree():
    root = Node("I")

    root.left = Node("A")
    root.right = Node("N")

    return root


# PREORDER: Root - Left - Right
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# INORDER: Left - Root - Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# POSTORDER: Left - Right - Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# MAIN PROGRAM
def main():
    root = create_tree()

    print("ASSESSMENT 3.6")
    print("DFS METHODS IN TREE")
    print("NAME: IAN")
    print("---------------------------")

    print("Preorder: ", end="")
    preorder(root)

    print("\nInorder: ", end="")
    inorder(root)

    print("\nPostorder: ", end="")
    postorder(root)

    print("\nProgram Completed!")


if __name__ == "__main__":
    main()
