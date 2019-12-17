from avlnode import AVLNode


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = AVLNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if not cur_node.left_child:
                cur_node.left_child = AVLNode(value)
                cur_node.left_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.left_child)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if not cur_node.right_child:
                cur_node.right_child = AVLNode(value)
                cur_node.right_child.parent = cur_node  # set parent
                self._inspect_insertion(cur_node.right_child)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node:
            self._print_tree(cur_node.left_child)
            print('%s, h=%d' % (str(cur_node.value), cur_node.height))
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root:
            return self._height(self.root, 0)

        return 0

    def _height(self, cur_node, cur_height):
        if not cur_node:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root:
            return self._find(value, self.root)
        return None

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child:
            return self._find(value, cur_node.right_child)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):
        if not node or not self.find(node.value):
            print("Node to be deleted not found in the tree!")
            return None

        def min_value_node(n):
            current = n
            while current.left_child:
                current = current.left_child
            return current

        def num_children(n):
            num_children = 0
            if n.left_child:
                num_children += 1
            if n.right_child:
                num_children += 1
            return num_children
        node_parent = node.parent

        node_children = num_children(node)

        # break operation into different cases based on the
        # structure of the tree & node to be deleted

        # CASE 1 (node has no children)
        if not node_children:

            if node_parent:
                # remove reference to the node from the parent
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:

            # get the single child node
            if node.left_child:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent:
                # replace the node to be deleted with its child
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            # correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:

            # get the inorder successor of the deleted node
            successor = min_value_node(node.right_child)

            # copy the inorder successor's value to the node formerly
            # holding the value we wished to delete
            node.value = successor.value

            # delete the inorder successor now that it's value was
            # copied into the other node
            self.delete_node(successor)

            # exit function so we don't call the _inspect_deletion twice
            return

        if node_parent:
            # fix the height of the parent of current node
            node_parent.height = 1 + \
                max(self.get_height(node_parent.left_child),
                    self.get_height(node_parent.right_child))

            # begin to traverse back up the tree checking if there are
            # any sections which now invalidate the AVL balance rules
            self._inspect_deletion(node_parent)

    def search(self, value):
        if self.root:
            return self._search(value, self.root)
        return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child:
            return self._search(value, cur_node.right_child)
        return False

    # Functions added for AVL...

    def _inspect_insertion(self, cur_node, path=[]):
        if not cur_node.parent:
            return
        path = [cur_node]+path

        left_height = self.get_height(cur_node.parent.left_child)
        right_height = self.get_height(cur_node.parent.right_child)

        if abs(left_height-right_height) > 1:
            path = [cur_node.parent]+path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_height = 1+cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self._inspect_insertion(cur_node.parent, path)

    def _inspect_deletion(self, cur_node):
        if not cur_node:
            return

        left_height = self.get_height(cur_node.left_child)
        right_height = self.get_height(cur_node.right_child)

        if abs(left_height-right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)

    def _rebalance_node(self, z, y, x):
        if y == z.left_child and x == y.left_child:
            self._right_rotate(z)
        elif y == z.left_child and x == y.right_child:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right_child and x == y.right_child:
            self._left_rotate(z)
        elif y == z.right_child and x == y.left_child:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception(
                '_rebalance_node: z,y,x node configuration not recognized!')

    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left_child
        t3 = y.right_child
        y.right_child = z
        z.parent = y
        z.left_child = t3
        if t3:
            t3.parent = z
        y.parent = sub_root
        if not y.parent:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.get_height(z.left_child),
                            self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                            self.get_height(y.right_child))

    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right_child
        t2 = y.left_child
        y.left_child = z
        z.parent = y
        z.right_child = t2
        if t2:
            t2.parent = z
        y.parent = sub_root
        if not y.parent:
            self.root = y
        else:
            if y.parent.left_child == z:
                y.parent.left_child = y
            else:
                y.parent.right_child = y
        z.height = 1 + max(self.get_height(z.left_child),
                            self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child),
                            self.get_height(y.right_child))

    def get_height(self, cur_node):
        if not cur_node:
            return 0
        return cur_node.height

    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left_child)
        right = self.get_height(cur_node.right_child)
        return cur_node.left_child if left >= right else cur_node.right_child
