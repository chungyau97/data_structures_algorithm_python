from queue_deque import Queue

def print_binary_number(max: int):
    queue = Queue()
    queue.enqueue('1')

    for index in range(max):
        front = queue.front()
        print('   ', front)

        queue.enqueue(front + '0')
        queue.enqueue(front + '1')

        queue.dequeue()

print_binary_number(10)