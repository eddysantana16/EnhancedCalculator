import pytest
from app.observer import Subject, Observer

def test_subject_attach_notify_detach():
    class TestObserver(Observer):
        def __init__(self):
            self.messages = []

        def update(self, message):
            self.messages.append(message)

    subject = Subject()
    observer1 = TestObserver()
    observer2 = TestObserver()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Hello")
    assert observer1.messages == ["Hello"]
    assert observer2.messages == ["Hello"]

    subject.detach(observer1)
    subject.notify("World")
    assert observer1.messages == ["Hello"]
    assert observer2.messages == ["Hello", "World"]
