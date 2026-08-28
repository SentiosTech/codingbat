"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""


# normal
def hello_name(name):
    return "Hello" + name + "!"


# optimal
def hello_name(name):
    return f"Hello {name}!"


# test
if __name__ == "__main__":
    hello_name("Bob") == "Hello Bob!"
    hello_name("Alice") == "Hello Alice!"
    hello_name("X") == "Hello X!"
    hello_name("Dolly") == "Hello Dolly!"
    hello_name("Alpha") == "Hello Alpha!"
    hello_name("Omega") == "Hello Omega!"
    hello_name("Goodbye") == "Hello Goodbye!"
    hello_name("ho ho ho") == "Hello ho ho ho!"
    hello_name("xyz!") == "Hello xyz!!"
    hello_name("Hello") == "Hello Hello!"
