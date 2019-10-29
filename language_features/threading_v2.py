import ctypes
import queue
import random
import signal
import threading
import time


class InterruptThreadException(Exception):
    pass


class InterruptableThread(threading.Thread):

    def _get_thread_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id

        for thread_id, thread_object, in threading._active.items():
            if thread_object is self:
                self._thread_id = thread_id
                return thread_id

    def terminate(self):
        thread_id = ctypes.c_long(self._get_thread_id())
        exception = ctypes.py_object(InterruptThreadException)

        if ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, exception) > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, None)


class ThreadingPlayground:
    def __init__(self):
        self._queue = queue.Queue(maxsize=100)
        self._counter_lock = threading.Lock()  # Mutex protecting the "counter" variable
        self._counter = 0
        self._threads = []

    def _producer(self):
        try:

            while True:
                val = random.randint(1, 101)
                self._queue.put(val)
                time.sleep(1)

        except InterruptThreadException:
            print('[Interrupt received]')

        finally:
            print('[Cleaning up and exiting]')

    def _consumer(self):
        try:

            while True:
                val = self._queue.get()
                with self._counter_lock:
                    self._counter += val
                time.sleep(1)

        except InterruptThreadException:
            print('[Interrupt received]')

        finally:
            print('[Cleaning up and exiting]')

    def _logger(self):
        try:
            while True:

                with self._counter_lock:
                    print('Current counter value:', self._counter)

                # self._counter_lock.acquire()
                # print('Current counter value:', self._counter)
                # self._counter_lock.release()

                time.sleep(1)

        except InterruptThreadException:
            print('[Interrupt received]')

        finally:
            print('[Cleaning up and exiting]')

    def spawn_threads(self):
        threads_to_start = [
            (self._producer, []),
            (self._producer, []),
            (self._consumer, []),
            (self._consumer, []),
            (self._logger, []),
        ]

        for thread_to_start in threads_to_start:
            new_thread = InterruptableThread(target=thread_to_start[0], args=tuple(thread_to_start[1]))
            new_thread.start()
            self._threads.append(new_thread)

    def terminate_threads(self):
        for thread in self._threads:
            thread.terminate()

    def join_threads(self):
        for thread in self._threads:
            thread.join()


if __name__ == '__main__':
    tp = ThreadingPlayground()

    # Handle SIGINT (Ctrl+C) gracefully and stop all the threads
    def signal_handler(signal_received, frame):
        if signal_received == signal.SIGINT:
            tp.terminate_threads()

    signal.signal(signal.SIGINT, signal_handler)

    tp.spawn_threads()
    tp.join_threads()
