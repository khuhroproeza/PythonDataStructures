class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linked_list:
    
    def __init__(self):
        self.head = None
        
    def append(self, data):
        now = node(data)
        if self.head==None:
            self.head = now
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = now
    
    def deleteIndex(self, index):
        cur_node = self.head
        i = 0
        if index == 0:
            self.head = cur_node.next
            return
        while cur_node.next!=None:
            
            if index == i+1:
                cur_node.next = cur_node.next.next
                return
            
            print(i)
            cur_node = cur_node.next
            i +=1
            
                
            
        
    
    def display(self):
        new_list = []
        cur_node = self.head
        new_list.append(cur_node.data)
        while cur_node.next!=None:
            
            cur_node = cur_node.next
            new_list.append(cur_node.data)
            
        print(new_list)
