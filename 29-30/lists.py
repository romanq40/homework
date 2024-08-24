
def list(text):
    t = text[0]
    for i in text:
        if len(t) > len(i):
            t = i
    return t
