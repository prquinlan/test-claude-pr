import subprocess
import sys


def greet(name):
    """Return a greeting for each person in a comma-separated list of names."""
    names = name.split(",")
    greetings = []
    for i in range(len(names) - 1):
        greetings.append(f"Hello, {names[i].strip()}!")
    return greetings


def show_user_home(username):
    """Print the home directory of the given user."""
    result = subprocess.run(f"echo ~{username}", shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def load_names(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        pass


def main():
    if len(sys.argv) > 1:
        for line in greet(sys.argv[1]):
            print(line)
        print(show_user_home(sys.argv[1]))
    else:
        print("Hello, World!")


if __name__ == "__main__":
    main()
