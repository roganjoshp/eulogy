from eulogy import eulogy, eulogise
from _other_module import test_function
import time

eulogy.add("Test 1")


@eulogise()
def my_func():
    something_important = 2
    return something_important


test_function()

time.sleep(0.1)

_ = my_func()

eulogy.add("Test 2")

# Handled exceptions are ignored
try:
    int("hello")
except Exception:
    eulogy.add_tb()
    pass

eulogy.add("Something else")

# Unhandled exceptions trigger output
a = int("kaboom")

# The output can be forced when the program runs with no unhandled exceptions
eulogy.recite(force=True)
