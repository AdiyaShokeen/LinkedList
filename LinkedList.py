class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)   

    def insert_values(self,data_list):
        self.data_list = data_list
        if self.head is None:
            for i in self.data_list[::-1]:
                self.insert_at_begining(i)
            return

        for i in self.data_list:
            self.insert_at_end(i)

    def remove_at(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1
       
    
    def print(self):
        if self.head is None:
            print("Linked List is empty.")
            return

        itr = self.head
        while itr:
            print(str(itr.data))
            itr = itr.next

    def get_len(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter

if __name__ == "__main__":
    link_lst = LinkedList()
