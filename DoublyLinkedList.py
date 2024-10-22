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
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
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
                itr.next = Node(data,itr,itr.next)
                break
            count += 1
            itr = itr.next

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,data):
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    

    def get_len(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def print(self):
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)

if __name__ == "__main__":
    d_linked_lst = DoublyLinkedList()
    d_linked_lst.insert_at_begining(5)
    d_linked_lst.insert_values([14,15,16])
    d_linked_lst.insert_at_end(34)
    d_linked_lst.remove_at(2)
    d_linked_lst.insert_at(3,"Hollow")
    d_linked_lst.insert_after_value("Hollow","Bleach")
    d_linked_lst.remove_by_value("Hollow")
    d_linked_lst.print()
    print(d_linked_lst.get_len())
    