import stack_linked_list

class StringChecker:
    def isBalanced(self, str):
        stacky = stack_linked_list.StackLinkedList(len(str))
        for c in str:
            if c == '{' or c == '[' or c == '(':
                stacky.push(c)
            if c == ')' or c == ']' or c == '}':
                if stacky.is_empty() or self.balance(stacky, c):
                    return False
                stacky.pop()
        if stacky.is_empty():
            return True
        else:
            return False
    def balance(self,stacky, c):
        if c == '}' and stacky.head.item == '{':
            return False
        if c == ']' and stacky.head.item == '[':
            return False
        if c == ')' and stacky.head.item == '(':
            return False
        return True





