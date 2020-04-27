import datetime as dt

def print_timestamp():
    print("Date now", dt.datetime.now())

def print_fruits(fruits):
    for fruit in fruits:
        print(f"bought {fruit}")

def print_starches(starches):
    for starch in starches:
        print(f"bought {starch}")


def main(args):
    """This function starts processing of new commands."""
    print(f"hello world: {args}")
    print_timestamp()
    print("ran to store")
    print_fruits(("apple", "cherry", "grape"))
    print_starches(("rice", "bread"))
    print("bought sugar")
    print("bought egg")


if __name__ == "__main__":
    """This function starts processing of new commands."""
    main(("--args", "/home/example"))
