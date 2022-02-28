from graphics import *



def encode_part_2():
    win = GraphWin('Vignere', 700, 500)
    win.setCoords(0, 0, 10, 10)
    message_text = Text(Point(3, 8), 'Message to code')
    message_text.draw(win)
    message_entry = Entry(Point(7, 8), 30)
    message_entry.draw(win)
    key_text = Text(Point(3, 7), 'Enter Keyword')
    key_text.draw(win)
    key_entry = Entry(Point(7, 7), 30)
    key_entry.draw(win)

    click_text = Text(Point(5, 5), "Encode")
    click_text.draw(win)
    click_text_box = Rectangle(Point(4, 4), Point(6, 6))
    click_text_box.draw(win)
    win.getMouse()

    # convert
    message = message_entry.getText()
    key = key_entry.getText()
    new_message = message.upper().replace("", "")
    new_key = key.upper().replace("", "")
    encoded_message = ""

    for i in range(len(new_message)):
        letter_value = ord(new_message[i]) - 65
        shift_amt = ord(key[i % len(new_key)]) - 65
        new_letter = letter_value + shift_amt
        new_letter = new_letter % 26
        new_letter = new_letter + 65
        new_letter = chr(new_letter)
        encoded_message = encoded_message + new_letter

    win.getMouse()
    resulting_message = Text('Resulting Message', Point(5, 3))
    resulting_message.draw(win)
    result_message = Text(encoded_message, Point(5, 2.5))
    result_message.draw(win)
    final_message = Text('Click Anywhere to Close Window', Point(5, 1))
    final_message.draw(win)

    win.getMouse()
    win.close()
