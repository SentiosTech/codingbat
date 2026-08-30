"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""


# normal
def make_tags(tag, word):
    wrap_word = "<" + tag + ">" + word + "</" + tag + ">"
    return wrap_word


# optimal
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}>"


# test
if __name__ == "__main__":
    make_tags("i", "Yay") == "<i>Yay</i>"
    make_tags("i", "Hello") == "<i>Hello</i>"
    make_tags("cite", "Yay") == "<cite>Yay</cite>"
    make_tags("address", "here") == "<address>here</address>"
    make_tags("body", "Heart") == "<body>Heart</body>"
    make_tags("i", "i") == "<i>i</i>"
    make_tags("i", "") == "<i></i>"
