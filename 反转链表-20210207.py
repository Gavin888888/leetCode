# class Node(object):
#     def __init__(self, elem, next_=None):
#         self.elem = elem
#         self.next = next_
#
#
# def reverseList(head):
#     if head == None or head.next == None:  # 若链表为空或者仅一个数就直接返回
#         return head
#     pre,next = None , None
#     while (head != None):
#         next = head.next  # 1
#         head.next = pre  # 2
#         pre = head  # 3
#         head = next  # 4
#     return pre
#
#
# if __name__ == '__main__':
#     l1 = Node(1)  # 建立链表3->2->1->9->None
#     l1.next = Node(2)
#     l1.next.next = Node(3)
#     l1.next.next.next = Node(4)
#     l1.next.next.next.next = Node(5)
#     print(l1)
#     l = reverseList(l1)
#     print(l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem, l.next.next.next.next.elem)


#自己写一遍 2021.2.7 刻意练习

#定义一个节点
class Node(object):
    def __init__(self,content,next_ = None):
        self.content = content
        self.next = next_
#反转链表
def reveseList(head):
    #先判断链表 是否有 并且 元素大于2
    if head == None or head.next == None:
        return head

    pre , next = None , None
    while head != None:
        next = head.next;
        head.next = pre
        pre = head
        head = next;
    return pre



if __name__ == '__main__':
    l = Node(1)
    l.next = Node(2)
    l.next.next = Node(3)
    l.next.next.next = Node(4)
    l.next.next.next.next = Node(5)
    l1 = reveseList(l)

