class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = ListNode()
        cursor = merge
        while list1 and list2:
            if list1.val <= list2.val:
                cursor.next = list1
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next
            cursor=cursor.next
        if list1:
            cursor.next = list1
        else:
            cursor.next = list2
        return merge.next
