import argparse
import pyperclip

symbols = {
    "@": ":alphabet-white-at:",
    "!": ":alphabet-white-exclamation:",
    "#": ":alphabet-white-hash:",
    "?": ":alphabet-white-question:"
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()

    if args.text.endswith(".txt"):
        with open(args.text,  "r") as the_file:
            original_message = the_file.read().lower()
    else:
        original_message = args.text.lower()

    output = ""

    for letter in original_message:
        if letter.isalpha():
            output += f":alphabet-white-{letter}:"
        elif letter.isspace():
            output += " " * 3
        elif letter in symbols:
            output += symbols[letter]
        else:
            output += letter

    pyperclip.copy(output)
    print("Translation Saved To Clipboard!")


if __name__ == "__main__":
    main()
