class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list (if head == NONE LL is empty)
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_head(self, value):
        # create new node with value
        new_node = Node(value)
        # Update pointer of new Node -> head
        new_node.set_next(self.head)

        if self.head is None:  # Insert into empty list
            # Mark new Node as "head" and "tail"
            self.head = new_node
            self.tail = new_node
        else:  # insert in new list with 1+ Nodes
            # Mark new Node as "head"
            self.head = new_node

    def add_to_tail(self, value):
        # Create new Node with Value
        new_node = Node(value)
        if self.tail is None:  # is LL is empty
            # Mark new node as head and tail
            self.head = new_node
            self.tail = new_node
        # insert in new list with 1+
        else:  # If is not empty
            self.tail.set_next(new_node)  # Update next pointer of old tail
            self.tail = new_node

    def remove_from_tail(self):
        if self.head == None:  # remove from empty LL
            return
        if self.head == self.tail:  # remove from LL with 1 elements
            self.head = None
            self.tail = None

        curr_node = self.head
        while curr_node is not None:
            if curr_node.next_node is self.tail:  # triggers if is the node before the last
                curr_node.next_node = None
                return
            curr_node = curr_node.next_node  # move to the next node

    def remove_from_head(self):
        if self.head == None:  # remove from empty LL
            return
        if self.head == self.tail:  # remove from LL with 1 elements
            self.head = None
            self.tail = None
        self.head = self.head.next_node  # set the head as the current head's next

    def insert_at(self, value, position):
        pass

    def contains(self, value):
        cur_node = self.head
        while(cur_node is not None):
            if cur_node.value is value:
                return True
            cur_node = cur_node.get_next()
        return False
    def print_list(self):
        curr_node = self.head
        arr = []
        while curr_node is not None:
            arr.append(curr_node.value)
            curr_node = curr_node.next_node
        print(arr)

linked_list = LinkedList()
linked_list.add_to_head(2)
linked_list.add_to_tail(44)
linked_list.print_list()