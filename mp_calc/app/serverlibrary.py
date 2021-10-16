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
  valid_char = '0123456789+-*/() '
  operators = '*/-+()'
  operand = '0123456789'
  def __init__(self, string=""):
    self.expression = string

  @property
  def expression(self):
    return self._expression

  @expression.setter
  def expression(self, new_expr):
    for val in new_expr:
      if val not in self.valid_char:
        self._expression = ''
        return
    else:
      self._expression = new_expr

  def insert_space(self):
    temp = ''
    for i, val in enumerate(self._expression):
      if val in self.operators:
        temp = temp + ' ' + val + ' '
      else:
        temp += val
    return temp

  def applyop(self, opr, val1, val2):
    val1 = float(val1)
    val2 = float(val2)
    if opr == '+':
      return val1 + val2
    if opr == '-':
      return val1 - val2
    if opr == '*':
      return val1 * val2
    if opr == '/':
      return val1 / val2

  def process_operator(self, operand_stack, operator_stack):
    right = operand_stack.pop()
    left = operand_stack.pop()
    opr = operator_stack.pop()
    result = self.applyop(opr, left, right)
    operand_stack.push(result)
    
  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    n = len(self.expression)
    i = 0
    while i < n:
      val = self.expression[i]
      if val in self.operand:
        number = ''
        j = i
        while j < n and '0' <= self.expression[j] <= '9':
          number += self.expression[j]
          j += 1
        i = j-1
        operand_stack.push(number)
      elif val in '+-':
        while not operator_stack.is_empty and \
          operator_stack._Stack__items[-1] not in '()':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(val)
      elif val in '*/':
        while not operator_stack.is_empty and \
          operator_stack._Stack__items[-1] in '*/':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(val)
      elif val == '(':
        operator_stack.push('(')
      elif val == ')':
        while operator_stack._Stack__items[-1] != '(':
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()
      i += 1
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return round(operand_stack.pop(), 2)

def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





