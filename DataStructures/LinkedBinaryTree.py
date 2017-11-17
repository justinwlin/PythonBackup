import ArrStackQueue

class Empty(Exception):
    pass


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1

    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise Empty("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)
    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root
            yield from self.subtree_inorder(subtree_root.right)

    def __iter__(self):
        for node in self.inorder():
            yield node.data


    def leaves_lst(self):
        #HELPER FUNCTION
        def subtree(self, subtree_root, lst):
            if (subtree_root.left is None and subtree_root.right is None):
                if subtree_root.data != self.root:
                    lst.append(subtree_root.data)
                return lst
            else:
                debug = subtree_root.left
                debug2 = debug.data
                if subtree_root.left is not None:
                    left_sum = subtree(self, subtree_root.left, lst)
                if subtree_root.right is not None:
                    right_sum = subtree(self, subtree_root.right, lst)
                return lst
        if self.is_empty():
            raise Empty
        root = self.root
        lst = []
        return subtree(self, root, lst)

    def breadth_first(self):
        if self.is_empty():
            return
        nodes_q = ArrStackQueue.ArrayQueue()
        nodes_q.enqueue(self.root)
        while nodes_q.is_empty() == False:
            curr_node = nodes_q.dequeue()
            yield curr_node
            if curr_node.left is not None:
                nodes_q.enqueue(curr_node.left)
            if curr_node.right is not None:
                nodes_q.enqueue(curr_node.right)


# l_ch1 = LinkedBinaryTree.Node(1)
# r_ch1 = LinkedBinaryTree.Node(5)
# l_ch2 = LinkedBinaryTree.Node(0, l_ch1, r_ch1)
# l_ch3 = LinkedBinaryTree.Node(8)
# r_ch2 = LinkedBinaryTree.Node(4)
# a = LinkedBinaryTree.Node(2, l_ch2)
# b = LinkedBinaryTree.Node(7,l_ch3,r_ch2)
# root = LinkedBinaryTree.Node(3,a,b)
# tree = LinkedBinaryTree(root)

# l_ch1 = LinkedBinaryTree.Node(5)
# r_ch1 = LinkedBinaryTree.Node(1)
# l_ch2 = LinkedBinaryTree.Node(0, l_ch1, r_ch1)
# l_ch3 = LinkedBinaryTree.Node(8)
# r_ch2 = LinkedBinaryTree.Node(4)
# a = LinkedBinaryTree.Node(2, l_ch2)
# b = LinkedBinaryTree.Node(7,l_ch3,r_ch2)
# root = LinkedBinaryTree.Node(3,a,b)
# tree = LinkedBinaryTree(root)

# for node in tree.breadth_first():
#     print(node.data)
