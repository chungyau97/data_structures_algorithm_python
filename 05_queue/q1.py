from queue_deque import Queue
import threading
import time

def place_order(queue_order: Queue):
    incoming_orders = ['pizza','samosa','pasta','biryani','burger']

    for order in incoming_orders:
        print('place_order:', order)
        queue_order.enqueue(order)
        time.sleep(0.5)

def serve_order(queue_order: Queue):
    while queue_order.container:
        print('serve_order:', queue_order.dequeue())
        time.sleep(2)

time_start = time.time()

queue_order = Queue()

thread_1 = threading.Thread(target= place_order, args= (queue_order, ))
thread_2 = threading.Thread(target= serve_order, args= (queue_order, ))

thread_1.start()
time.sleep(1)
thread_2.start()

thread_1.join()
thread_2.join()

print('Order complete:', queue_order.is_empty())

time_finish = time.time()
print('Duration:', round(time_finish - time_start, 2))