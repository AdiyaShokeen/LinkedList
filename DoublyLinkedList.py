class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,None,self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,itr.next,None)

    def insert_values(self,data_list):
        for i in data_list:
            self.insert_at_end(i)

    def remove_at(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                break
            count += 1
            itr = itr.next

    def insert_at(self,index,data):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data,itr,itr.next)
                itr.next.prev = new_node
                itr.next = new_node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert,itr,itr.next)
                if itr.next is not None:
                    itr.next.prev = new_node
                itr.next = new_node
                break
            itr = itr.next

    def remove_by_value(self,data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                if itr.next is not None:
                    itr.next.prev = itr
                break
            itr = itr.next

    def print_forward(self):
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)

    def print_backward(self):
        llstr = ""
        itr = self.get_last_node()
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.prev
        print(llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
        

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def print(self):
        self.print_forward()

if __name__ == "__main__":
    d_linked_lst = DoublyLinkedList()
    