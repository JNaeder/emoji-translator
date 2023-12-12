import argparse
import pyperclip


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()

    original_message = args.text.lower()
    output = ""

    for letter in original_message:
        if letter.isalpha():
            output += f":alphabet-white-{letter}:"
        else:
            output += letter
        # new_letter = master_dict.get(letter, letter)

    print("Translation Saved To Clipboard!")
    pyperclip.copy(output)


if __name__ == "__main__":
    main()
