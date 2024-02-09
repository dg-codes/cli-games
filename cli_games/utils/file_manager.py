from os import getcwd
from pathlib import Path


def write_words_for_hangman(word_list: list[str], file_path: Path):
    with open(file_path, "w") as file:
        for word in word_list:
            # Write each word followed by a newline character to the file
            file.write(word + "\n")


def load_data(file_path: Path) -> list[str]:
    with open(file_path, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines


def prepare_hangman_file():
    current_directory = Path(getcwd())
    words = set(load_data(current_directory / "data" / "hangman_copy.txt"))
    save_file_path = current_directory / "data" / "hangman.txt"
    write_words_for_hangman(sorted(words), save_file_path)


if __name__ == "__main__":
    prepare_hangman_file()
