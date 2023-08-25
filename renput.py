import msvcrt
import sys
import colorama

def input(prompt="", auto_complete=[]):
    sys.stdout.write(prompt)
    sys.stdout.flush()

    input_chars = []
    input_buffer = ""
    matching_words = []

    while True:
        try:
            char = msvcrt.getch().decode("utf-8")
        except UnicodeDecodeError:
            continue

        if char == "\r":
            sys.stdout.write("\n")
            break
        elif char == "\x08":
            if input_chars:
                input_chars.pop()
                input_buffer = input_buffer[:-1]
                sys.stdout.write("\b \b")
        elif char == "\t":
            if matching_words:
                match = matching_words[0]
                input_chars = list(match)
                input_buffer = match
                sys.stdout.write("\r" + prompt + match + " " * (len(input_buffer) - len(match)) + "\r" + prompt + match)
        else:
            input_chars.append(char)
            input_buffer += char
            sys.stdout.write(char)

        if input_buffer:
            matching_words = [word for word in auto_complete if word.startswith(input_buffer)]

        sys.stdout.flush()

    sys.stdout.write("\r" + " " * len(prompt) + "\r")
    return "".join(input_chars)
