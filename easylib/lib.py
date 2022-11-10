import builtins
import datetime
import matplotlib

def split(word: str = None):
    """
    `split` takes a string and returns a list of characters

    :param word: str = None
    :type word: str
    :return: A list of characters
    """
    return [char for char in word]


# dict class


def timestamp_print(*args, sep: str = None, end: str = None, file=None, flush: bool = False, time_format: str = "%Y-%m-%d %H:%M:%S"):
    """
    `timestamp_print` is a function that prints a timestamp and then prints whatever you want to print

    :param sep: The separator between the arguments
    :type sep: str
    :param end: string appended after the last value, default a newline
    :type end: str
    :param file: The file argument is an object with a write(string) method
    :param flush: If True, the stream is forcibly flushed. This is useful when the stream is buffered, defaults to False
    :type flush: bool (optional)
    :param time_format: This is the format of the timestamp, defaults to %Y-%m-%d %H:%M:%S
    :type time_format: str (optional)
    """
    print()
    print_statement = ""
    timeprint = datetime.datetime.now().strftime(time_format)
    for i in args:
        print_statement = f"{print_statement}{i}"
    builtins.print(f"{timeprint}: {print_statement}", sep=sep, end=end, file=file, flush=flush)



