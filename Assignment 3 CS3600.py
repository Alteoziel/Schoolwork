#BOUNDING BUFFER PROBLEM
import threading
import time
import random

buffer = [] #Start with an empty buffer
buffer_size = 5 #buffer size of 5

lock = threading.Lock()

empty_slots = threading.Semaphore(buffer_size)
full_slots = threading.Semaphore(0)

def producer(producer_id):
    item_id = 0
    while True:
        item = f"P{producer_id}-item{item_id}"
        item_id += 1 #create a set of items

        empty_slots.acquire()

        with lock:
            buffer.append(item) #and add the items to the buffer
            print(f"[PRODUCER {producer_id}] produced {item} | buffer={buffer}")

        full_slots.release()

        time.sleep(random.uniform(0.1, 0.5)) #make sure that it doesn’t grab an item at the same time as the consumer

def consumer(consumer_id):
    while True:
        full_slots.acquire() #find all slots that have an item

        with lock:
            item = buffer.pop(0) #remove that item
            print(f"[CONSUMER {consumer_id}] consumed {item} | buffer={buffer}")

        empty_slots.release()

        time.sleep(random.uniform(0.2, 0.7)) #make sure it doesn’t grab at the same time as the producer

if __name__ == "__main__":
    producers = [threading.Thread(target=producer, args=(i,), daemon=True)
                 for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i,), daemon=True)
                 for i in range(2)]

    for t in producers + consumers:
        t.start()

    time.sleep(5)







#DINING PHILOSOPHER PROBLEM
