import pytest

class StackEE():

    def __init__(self):
        self.stack = list()

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
    
    def is_empty(self) -> bool:
        return True if self.stack else False
    

if __name__ == "__main__":
    stack_obj = StackEE()
    stack_obj.push("1")
    stack_obj.push("2")
    stack_obj.push("3")
    print(stack_obj.is_empty())
    print(stack_obj.size())
    print(stack_obj.pop())
    print(stack_obj.pop())
    print(stack_obj.pop())

@pytest.mark.parametrize("inx, outx", [(1, 1), (2, 2)])
def test_stack(inx, outx):
    stack_obj = StackEE()
    stack_obj.push(inx)
    assert outx == stack_obj.pop()
