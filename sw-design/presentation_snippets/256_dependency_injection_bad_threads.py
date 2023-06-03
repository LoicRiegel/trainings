# BEFORE
from threading import Thread, Event

class SendThread(Thread):
    def __init__(self, queue: Queue, stop_event: Event):
        pass
    
    def run():
        """Handle messages to send."""

class ReceiveThread(Thread):
    def __init__(self, queue: Queue, stop_event: Event):
        pass
    
    def run():
        """Handle received messages."""


class CommunicationHandler:
    def __init__(self):
        self._send_stop_event: Event()
        self._receive_stop_event: Event()
        self._receive_queue = queue.Queue()
        self._send_queue = queue.Queue()
        self._send_thread = SendThread(self._send_queue, self._send_stop_event)
        self._receive_thread = ReceiveThread(self._receive_queue, self._receive_stop_event)
    
    def start(self):
        self._send_thread.start()
        self._receive_thread.start()
    
    def send(self, msg):
        self._send_queue.put(msg)
