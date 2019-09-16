class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, curr, key):
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else:
                self._insert(curr.right_child, key)

        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        """left, root, right"""
        self._in_order(self.root)
        print("")

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end=" ")
            self._in_order(curr.right_child)

    # def pre_order(self):
    #     """root, left, right"""
    #     self._pre_order(self.root)
    #     print("")
    #
    # def _pre_order(self, curr):
    #     if curr:
    #         print(curr.data, end=" ")
    #         self.pre_order(curr.left_child)
    #         self._pre_order(curr.right_child)
    #
    #
    # def post_order(self):
    #     '''left, right, root'''
    #     self._post_order(self.root)
    #     print("[value]", [...])
    #
    #
    # def _post_order(self, curr):
    #     if curr:
    #         self.post_order(curr.left_child)
    #         self.post_order(curr.right_child)
    #         print(curr.data)

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        if curr:
            if key == curr.data:
                return 'Value found in tree'
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else:
                return self._find_val(curr.right_child, key)
        return 'Value not found in tree'

    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

        # DELETING WITH 2 CHILDREN:
    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            if key == curr.data:
                if curr.left_child and curr.right_child:
                    print("problem scenario!")
                elif curr.left_child == None and curr.right_child == None:

                    if is_left:
                        prev.left_child = None
                    else:
                        prev.right_child = None
                elif curr.left_child == None:
                    if prev:
                        if is_left:
                            prev.left_child = curr.right_child
                        else:
                            prev.right_child = curr.right_child
                    else:
                        self.root = curr.right_child
                else:
                    if prev:
                        if is_left:
                            prev.left_child = curr.left_child
                        else:
                            prev.right_child = curr.left_child
                    else:
                        self.root = curr.left_child
            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)
        else:
            print(f"{key} was not found in Tree")


        # DELETING NODES WITH ONE CHILD
    # def _delete_val(self, curr, prev, is_left, key):
    #     if curr:
    #         if key == curr.data:
    #             # print(f"Found {key} node to delete")
    #             # self.root = None
    #             if curr.left_child and curr.right_child:
    #                 print("problem scenario")
    #             elif curr.left_child == None and curr.right_child == None:
    #                 if is_left:
    #                     prev.left_child = None
    #                 else:
    #                     prev.right_child = None
    #             elif curr.left_child == None:
    #                 if prev:
    #                     if is_left:
    #                         prev.left_child = curr.right_child
    #                     else:
    #                         prev.right_child = curr.right_child
    #                 else:
    #                     self.root = curr.right_child
    #             else:
    #                 if prev:
    #                     if is_left:
    #                         prev.left_child = curr.left_child
    #                     else:
    #                         prev.right_child = curr.left_child
    #                 else:
    #                     self.root = curr.left_child
    #         elif key < curr.data:
    #             self._delete_val(curr.left_child, curr, True, key)
    #         elif key > curr.data:
    #             self._delete_val( curr.right_child, curr, False, key)
    #     else:
    #         print(f"{key} not found in tree")

    # def _delete_val(self, curr, prev, is_left, key):
    #     pass

tree = BSTDemo()

tree.insert('F')
# tree.insert('C')
tree.insert('G')
tree.in_order()
# tree.delete_val('C')
tree.delete_val('G')
# tree.delete_val('F')
tree.in_order()

# tree.insert("F")
# # print(tree.root.data)
# tree.insert("C")
# # print(tree.root.left_child.data)
# tree.insert("G")
# # print(tree.root.right_child.data)
# tree.insert("A")
# # print(tree.root.left_child.left_child.data)
# tree.insert("B")
# # print(tree.root.left_child.left_child.right_child.data)
# tree.insert("K")
# # print(tree.root.right_child.right_child.data)
# tree.insert("H")
# # print(tree.root.right_child.right_child.left_child.data)
# tree.insert("E")
# tree.insert("D")
# tree.insert("I")
# tree.insert("M")
# tree.insert("J")
# tree.insert("L")
# tree.in_order()
# tree.pre_order()
# tree.posts_order()
# print(tree.in_order())
# print(tree.pre_order())
# print(tree.post_order())
