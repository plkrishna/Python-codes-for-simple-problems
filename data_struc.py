class stack:
   
    """this class allows to create a stack
       with default size 50.It allows for custom specification of size.
       s=stack() stack size 50
       s1=stack(10) stack size 10"""
     
    def __init__(self,size=50):
        self.ds=[]
        self.size=size
        print("stack with size %d created"%self.size)
    def push(self,ele):
        if len(self.ds)==self.size:
            print("stack has overflown")
            return
        else:
            self.ds.append(ele)
    def pop(self):
        if len(self.ds)==0:
            #print("stack has underflown")
            return None
        else:
            x=self.ds[len(self.ds)-1]
            del self.ds[len(self.ds)-1]
            return x
    def top(self):
        x=self.pop()
        self.push(x)
        return x
    def show(self):
        print("stack from top to bottom")
        k=""
        for i in range(len(self.ds)-1,-1,-1):
            k+=self.ds[i]
        print(k)
    def __str__(self):
        return "stack with the size {}".format(self.size)


class node:
    '''This class allows us to create a linked list
    of arbitrary size. It returns the first node in the list'''
    def __init__(self,value=None):
        self.value=value
        self.next=None
    @classmethod
    def createList(self,li):
        '''Creates a linked list with the given '''
        k=node()
        for i in li:
            k.append(i)
        return k
    @classmethod
    def concat(self,l1,l2):
        '''Concatenates the two lists and returns the result'''
        temp=l1
        while temp.next!=None:
            temp=temp.next
        temp.next=l2
        return l1
    @classmethod
    def reverse(self,li):
        '''This method reverses the given linked list
        and returns it'''
        prev=None
        current=li
        while current!=None:
            k=current.next
            current.next=prev
            prev=current
            current=k
        return prev
    def isempty(self):
        '''Checks whether the list is empty or not
        Returns True if list is empty
        else returns False'''
        return (self.value==None)
    def append(self,v):
        '''Appends the element at the end of the list.'''
        if self.isempty():
            self.value=v
        elif self.next==None:
            s=node(v)
            self.next=s
        else:
            self.next.append(v)
    def insert_beg(self,v):
        '''Inserts the specified element at the beginning of the list.'''
        if self.isempty():
            self.value=v
        else:
            nn=node()
            nn.next=self.next
            self.next=nn
            nn.value=self.value
            self.value=v
    def pop(self):
        '''Deletes the last element in the list'''
        k=self
        if self.isempty():
            print('Empty')
        elif self.next==None:
            self.value=None
        else:            
            while (k.next).next!=None:
                k=k.next
            k.next=None
    def delete_beg(self):
        if self.isempty():
            print('Empty')
        elif self.next==None:
            self.value=None
        else:
            self.value,(self.next).value=self.next.value,self.value
            self.next=self.next.next
    def delete_val(self,v):
        '''Deletes the specified value in the list.'''
        if self.isempty():
            print('Empty')
        if self.value==v:
            self.delete_beg()
        else:
            temp=self
            while temp.next!=None:
                if temp.next.value==v:
                    temp.next=temp.next.next
                    return
                else:
                    temp=temp.next
            else:
                print('Element not found')
    def countNodes(self):
        '''Counts the number of nodes in the list and returns the count.'''
        cnt=0
        temp=self
        while temp!=None:
            cnt+=1
            temp=temp.next
        if self.value==None:
            return 0
        else:
            return cnt
    def rec_count(self):
        if self.value==None:
            return 0
        elif self.next==None:
            return 1
        else:
            return 1+self.next.rec_count()
            
    def show(self):
        '''Prints all the elements in the list'''
        k=self
        if self.isempty():
            print('List is empty')
        else:
            while k.next!=None:
                print(k.value,'->',end='',sep='')
                k=k.next
            print(k.value)
    def rotate(self):
        '''Performs single left rotation on the linked list
        Example:(1->2->3)=>(2->1->3)'''
        if self.next==None:
            return
        else:
            self.value,self.next.value=self.next.value,self.value
            self.next.swap()
    def rotateLeft(self,n=1):
        '''Performs left rotation by n times
        if no parameter is specified, it performs a single left rotation
        Example:(1->2->3->4) on rotating 2 times becomes (3->4->1->2)'''
        for i in range(n):
            self.rotate()
    def rotateRight(self):
        '''Performs single right rotation on list
        Example:(1->2->3)=>(3->1->2)'''
        k=self
        prev=None
        while k.next!=None:
            prev=k
            k=k.next
        prev.next=None
        self.insert_beg(k.value)
    def sort(self):
        '''Performs bubble sort on the linked list in place.
        Sorting is done on the basis of values in the nodes.'''
        count=self.countNodes()
        temp=self
        for i in range(count-1):
            for j in range(count-i-1):
                if temp.value>temp.next.value:
                    temp.value,temp.next.value=temp.next.value,temp.value
                temp=temp.next
            temp=self
            
    
    @classmethod
    def sum_lists(self,l1,l2):
        '''This method adds the elements of the two lists and returns the 
        result in the form of a list which has the length of the longest 
        list of the two
        Example:(1->2->3)+(10+11+12+13)=(11->13->15->16)'''
        len1=l1.countNodes()
        len2=l2.countNodes()
        l3=node()
        if len1>len2:
            temp1=l1
            temp2=l2
            while temp2!=None:
                l3.append(temp1.value+temp2.value)
                temp1=temp1.next
                temp2=temp2.next
            while temp1!=None:
                l3.append(temp1.value)
                temp1=temp1.next
            return l3
        else:
            temp1=l1
            temp2=l2
            while temp1!=None:
                l3.append(temp1.value+temp2.value)
                temp1=temp1.next
                temp2=temp2.next
            while temp2!=None:
                l3.append(temp2.value)
                temp2=temp2.next
            return l3
    @classmethod
    def arithmeticadd(self,l1,l2):
        '''This method performs arithmetic addition on two lists
        and returns the result in the form of list which contains 
        only single digit elements.Ex:1->2->3,9->7,etc
        Example:(1->2->3)+(3->4->5)=(4->6->8)
        (3->4->5)+(8->7->8)=(1->2->2->3)'''
        l3=node.sum_lists(l1,l2)
        l3=node.reverse(l3)
        temp=l3
        #cnt=l3.countNodes()
        carry=0
        while temp!=None:
            temp.value=temp.value+carry
            if temp.value>9:
                rem=temp.value%10
                q=int(str(temp.value)[0])
                carry=q
                temp.value=rem
            else:
                carry=0
            if carry>0 and temp.next==None:
                l3.append(carry)
                break
            temp=temp.next
        return node.reverse(l3)
        
if __name__=='__main__':
    ne1=node.createList([3,4,5])
    ne2=node.createList([8,7,8])
    ne3=node.arithmeticadd(ne1,ne2)
    ne3.show()
    #print(c)