# unordered_list.py  Class declaration of UnorderedList and methods of it

class Node:
    def __init__(self, value):
        self.next_node = None
        self.value = value

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, node):
        self.next_node = node


class UnorderedList:
    def __init__(self):
        self.head = None
        self.end = None

    def add(self, value):
        temp = Node(value)
        temp.set_next_node(self.head)  # Node that used to be head is now second node
        self.head = temp  # Adds the new node to the head of list
        if temp.get_next_node() == None:  # If added node is last node, Unordered pointer end to this node
            self.end = temp

    def show_end_value(self):  # Prints the value of end node without traversing through list
        if self.end != None:
            end_list_value = self.end.get_value()
            print(f'{end_list_value}')
        else:
            print('List is empty')

    def size(self):
        size = 0
        next_node = self.head
        while next_node != None:
            size += 1
            next_node = next_node.get_next_node()
        return size

    def isEmpty(self):
        return self.head == None

    def search(self, value):
        current_node = self.head
        value_found = False
        while current_node != None and value_found == False:
            if current_node.get_value() == value:
                value_found = True
            current_node = current_node.get_next_node()
        return value_found

    def remove(self, value):
        current_node = self.head
        previous_node = self.head
        value_found = False
        while current_node != None and not value_found:
            if current_node.get_value() == value:
                next_node = current_node.get_next_node()
                previous_node.set_next_node(next_node)
                if next_node == None:  # if the item removed is end of list, set end pointer to the node before
                    self.end = previous_node
                if self.head == current_node:  # if node removed is at head of list, head pointer is set to next node
                    self.head = next_node
                value_found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next_node()

    def insert(self, pos, value):
        if pos > self.size():
            raise Exception('Invalid position')

        if pos == 0:
            self.add(value)

        counter = 0  # Counter is used to track how many nodes have been visited
        previous_node = None
        current_node = self.head
        while counter < pos:  # At the end of this while loop, current node equals to the node right of inserted node
            previous_node = current_node
            current_node = current_node.get_next_node()
            counter += 1
        temp = Node(value)
        temp.set_next_node(current_node)
        if current_node == None:  # Sets end pointer to newly inserted node if its the end
            self.end = temp
        if previous_node != None:  # This line will always execute as long as list is not empty
            previous_node.set_next_node(temp)

    def append(self, value):  # Appends new node to end of list
        temp = Node(value)
        end_node = self.end
        end_node.set_next_node(temp)
        self.end = temp

    def index(self, value):
        vindex = 0  # Keeps track of the index of current_node
        current_node = self.head
        value_found = False
        while current_node != None and value_found == False:  # Stops when value is found or end of list
            if current_node.get_value() == value:
                value_found = True
            else:
                vindex += 1
                current_node = current_node.get_next_node()

        if value_found:
            return vindex
        else:
            return False

    def pop(self, pos):  # Removes the index [pos] from list
        if pos > self.size():
            raise Exception('Cannot pop a position that doesnt exist')

        current_node = self.head
        previous_node = None
        pos_counter = 0
        while pos_counter < pos:  # Traverses through nodes until current_node is equal to pos
            previous_node = current_node
            current_node = current_node.get_next_node()
            pos_counter += 1
        next_node = current_node.get_next_node()

        if next_node == None:  # The node popped was last node in list, set end pointer to previous node
            self.end = previous_node

        if previous_node != None:  # Will always execute if list is not empty
            next_node = current_node.get_next_node()
            previous_node.set_next_node(next_node)

        return current_node.get_value()
