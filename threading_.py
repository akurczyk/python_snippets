import queue
import random
import signal
import sys
import threading
import time


class ThreadingPlayground:
    def __init__(self):
        self._queue = queue.Queue(maxsize=100)
        self._counter_lock = threading.Lock()  # Mutex protecting the "counter" variable
        self._counter = 0
        self._threads = []

    def _producer(self):
        global stop_threads

        while True:
            if stop_threads:
                break

            val = random.randint(1, 101)
            self._queue.put(val)
            time.sleep(1)

    def _consumer(self):
        global stop_threads

        while True:
            if stop_threads:
                break

            val = self._queue.get()
            with self._counter_lock:
                self._counter += val
            time.sleep(1)

    def _logger(self):
        global stop_threads

        while True:
            if stop_threads:
                break

            with self._counter_lock:
                print('Current counter value:', self._counter)

            # self._counter_lock.acquire()
            # print('Current counter value:', self._counter)
            # self._counter_lock.release()

            time.sleep(1)

    def spawn_threads(self):
        threads_to_start = [
            (self._producer, []),
            (self._producer, []),
            (self._consumer, []),
            (self._consumer, []),
            (self._logger, []),
        ]

        for thread_to_start in threads_to_start:
            new_thread = threading.Thread(target=thread_to_start[0], args=tuple(thread_to_start[1]))
            new_thread.start()
            self._threads.append(new_thread)

    def wait_for_threads_to_finish(self):
        for thread in self._threads:
            thread.join()


stop_threads = False


def signal_handler(signal_received, frame):
    global stop_threads

    if signal_received == signal.SIGINT:
        stop_threads = True
        sys.exit()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  # Handle SIGINT (Ctrl+C) gracefully and stop all the threads

    tp = ThreadingPlayground()
    tp.spawn_threads()
    tp.wait_for_threads_to_finish()
