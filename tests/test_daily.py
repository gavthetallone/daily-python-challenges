from programs.monday import alphasort
from programs.tuesday import fibonacci
from programs.wednesday import evendigits

def test_alphasort():
    assert alphasort("hello world and practice makes perfect and hello world again") == "\n: again and hello makes perfect practice world "

def test_fibonacci():
    assert fibonacci(5) == "\n\tf(n) = 5\n"
    assert fibonacci(1) == "\n\tf(n) = 1\n" 

def test_evendigits():
    assert evendigits("10 30") == "20, 22, 24, 26, 28, "
    assert evendigits("1 100") == "2, 4, 6, 8, 20, 22, 24, 26, 28, 40, 42, 44, 46, 48, 60, 62, 64, 66, 68, 80, 82, 84, 86, 88, "
    assert evendigits("200 400") == "200, 202, 204, 206, 208, 220, 222, 224, 226, 228, 240, 242, 244, 246, 248, 260, 262, 264, 266, 268, 280, 282, 284, 286, 288, 400, "