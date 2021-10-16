def merge(array, p, q, r, byfunc):
    # print('merging')
    nleft = q - p + 1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[(q+1):r+1]
    left = 0
    right = 0
    dest = p
    while left < nleft and right < nright:
        if byfunc(left_array[left]) <= byfunc(right_array[right]):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1
    # print('stop merging')

def mergesort_recursive(array, p, r,byfunc):
    q = (r+p)//2
    if r-p <= 1:
        # print('r', r)
        # print('p', p)
        merge(array, p, q, r, byfunc)
        # print('done')
        return
    else:
        
        mergesort_recursive(array, p, q, byfunc)
        # print('p', p)
        # print('q', q+1)
        # print('r', r)
        mergesort_recursive(array, q+1, r, byfunc)
        # print('doing')
        merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
  if len(array) == 1:
    return
  mergesort_recursive(array, 0, len(array)-1, byfunc)

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty:
            return None
        else:
            item = self.__items[-1]
            del self.__items[-1]
            return item

    def peek(self):
        if self.is_empty:
            return None
        else:
            return self.__items[-1]

    @property
    def is_empty(self):
        if self.__items == []:
            return True
        else:
            return False

    @property
    def size(self):
        return len(self.__items)

class Queue:
    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()
    
    @property
    def is_empty(self):
        return self.right_stack.is_empty
        
    @property
    def size(self):
        return self.right_stack.size
        
    def enqueue(self, item, side):
        if side == 'left':
          self.left_stack.push(item)
        else:
          self.right_stack.push(item)
        
    def dequeue(self, side):
        if side == 'left':
          item = self.left_stack.pop()
        else:
          item = self.right_stack.pop()
        return item
                
    def peek(self):
        return self.right_stack.peek()

class EvaluateExpression:
    operators = "+-*/"
    check_operators = '+-*/('

    def __init__(self, data):
        self.expression = data
        self.queue = Queue()

    def applyop(self, opr, val1, val2):
        val1 = int(val1)
        val2 = int(val2)
        if opr == '+':
          return val1 + val2
        if opr == '-':
          return val1 - val2
        if opr == '*':
          return val1 * val2
        if opr == '/':
          return val1 / val2
    
    def check_precedence(self, op1, op2):
      if op2 == '(':
          return False
      if (op1 == '*' or op1 == '/') and (op2 == '-' or op2 == '+'):
          return False
      else:
          return True

    def evaluate(self):
      left_stack = Stack()
      right_stack = Stack()
      n = len(self.expression)
      i = 0
      while i < n:
          val = self.expression[i]
          if val.isdigit():
              if i < n-1:
                  while self.expression[i+1] not in '+-*/()':
                      val += self.expression[i+1]
                      i += 1
              left_stack.push(val)
          elif val == '(':
              right_stack.push('(')
          elif val in '+-/*':
              if not right_stack.is_empty and self.check_precedence(val, right_stack._Stack__items[-1]):
                  right = int(left_stack.pop())
                  left = int(left_stack.pop())
                  result = self.applyop(val, left, right)
              right_stack.push(val)
          elif val == ')':
              while right_stack._Stack__items[-1] != '(':
                  right = int(left_stack.pop())
                  left = int(left_stack.pop())
                  result = self.applyop(right_stack.pop(), left, right)
                  left_stack.push(result)
              right_stack.pop()
          i += 1
      while right_stack._Stack__items != []:
          right = left_stack.pop()
          left = left_stack.pop()
          opr = right_stack.pop()
          result = self.applyop(opr, left, right)
          left_stack.push(result)
      return round(left_stack.pop(), 2)

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





