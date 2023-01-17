'''
Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head:ListNode) -> ListNode:
        
        headlist = []        
        current = head
        while current: #ja que ListNode,next por default é None, e None é falsy para o py:
            headlist.append(current.val)
            current = current.next
        #Aqui vamos saber se é par ou impar a sequência de nodes, logo se teremos 1 ou 2 termos no meio
        lenh = len(headlist)

        newhead = [] # <-- aqui vamos armazenar somentes os nodes do meio para adiante, porém serão armazenados como simples Ints.

        #como indices começam no 0 em pi, se eu fizer len/2 vou obeter justamente o índice do segundo termo do meio nas situações de len par.
        if lenh%2 == 0:
            limit = lenh/2            
            for index,node in enumerate(headlist):
                if index >= limit:
                    newhead.append(node)
        else:
            limit = (lenh-1)/2 #remove um termo e torna para, para tirar a dif de index que o py usa a partir do 0
            for index,node in enumerate(headlist):
                if index >= limit:
                    newhead.append(node)
        
#Nest ultimo Loop vamos transformar os numeros dos nodes em nodes propriamente
        for index,node in enumerate(newhead):
            if index == 0:
                newhead[index] = ListNode(node) #Aqui geramos o node n(1)
            else:
                newhead[index] = ListNode(node) #Depois germaos o node n+1 e o conectamos com n(ou seja, o termo anterior)
                newhead[index - 1].next = newhead[index]

#Retornamos o primeiro node, que por sua vez tera todos outros linkados dentro de si, por se tratar de uma LinkedNodeList
        return newhead[0] 
