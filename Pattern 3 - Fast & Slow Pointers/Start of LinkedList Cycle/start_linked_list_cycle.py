class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


def find_cycle_start(head):
  s, f, = head, head
  while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
          length = get_cycle_length(f)
          f = move_fast_pointer(length, head)
          return find_start_node(head, f)


def get_cycle_length(p):
    pointer, counter = p, 0
    while True:
        pointer = pointer.next
        counter += 1
        if pointer == p:
            break

    return counter


def move_fast_pointer(length, head):
    p = head
    while length > 0:
        p = p.next
        length -= 1
    
    return p


def find_start_node(s, f):
    while s != f:
        s = s.next
        f = f.next
    
    return f


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()