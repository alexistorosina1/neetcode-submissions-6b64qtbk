class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # [1, 2, +] -> [3]
        #[3, 3, *] -> [9]
        #[9, 4, -] -> [5]
        # adding to the stack and when we see an operator we pop both elements and compute

        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))
        return stack[0]
