# ASSESSMENT 3.4
# BINARY TREE - BASTATAS
# Name: Ian Alhjo R. Bastatas

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree():
    """Create a binary tree using the letters in BASTATAS."""
    root = Node("B")

    root.left = Node("A")
    root.right = Node("S")

    root.left.left = Node("T")
    root.left.right = Node("A")

    root.right.left = Node("T")
    root.right.right = Node("A")

    root.left.left.left = Node("S")

    return root


def bfs(root):
    """Breadth-First Search: visit nodes level by level."""
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


def dfs_preorder(root):
    """Depth-First Search (preorder): root, left, right."""
    if root is None:
        return

    print(root.data, end=" ")
    dfs_preorder(root.left)
    dfs_preorder(root.right)


def main():
    root = create_tree()

    print("BINARY TREE - BASTATAS")
    print("----------------------")

    print("BFS Traversal: ", end="")
    bfs(root)

    print("\nDFS Traversal (Preorder): ", end="")
    dfs_preorder(root)

    print("\nProgram completed!")


if __name__ == "__main__":
    main()
