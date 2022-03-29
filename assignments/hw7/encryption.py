def encode():
    message = open("friend_message", "r")
    key =
    code = ""
    for ch in message:
        unicode = ord(ch) + key
        new_message = chr(unicode)
        code = code + new_message
    print(code)
encode()