'''
Palindrome Linked List
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise. 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head:ListNode) -> bool:
        headlist = []        
        current = head
        while current: #ja que ListNode,next por default é None, e None é falsy para o py:
            headlist.append(current.val)
            current = current.next
        if len(headlist)%2 == 0:
            #lidando com uma lista de nodes de quantidade par(mais "fácil")
            limit = int(len(headlist)/2)
            for index in range(limit):
                    if headlist[index] == headlist[-(index + 1)]:
                        pass
                    else:
                        return False
        else:
            #Aqui cairão os casos de quantidade ímpar ímpares
            limit = int((len(headlist)-1)/2)
            for index in range(limit):
                    if headlist[index] == headlist[-(index + 1)]:
                        pass
                    else:
                        return False
        return True
        