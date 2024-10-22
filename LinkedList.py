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
            
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
       nt while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    

    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                break
            count += 1
            itr = itr.next
                
    
    
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
