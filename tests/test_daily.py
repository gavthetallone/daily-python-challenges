from programs.monday import alphasort
from programs.tuesday import fibonacci

def test_alphasort():
    assert alphasort("hello world and practice makes perfect and hello world again") == "\n: again and hello makes perfect practice world "

def test_fibonacci():
    assert fibonacci(5) == "\n\tf(n) = 5\n"
    assert fibonacci(1) == "\n\tf(n) = 1\n" 