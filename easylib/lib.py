import builtins
import datetime
import matplotlib

def split(word: str = None):
    """Splits a word into a list for each character"""
    return [char for char in word]


# dict class


def timestamp_print(*args, sep: str = None, end: str = None, file=None, flush: bool = False,
                    time_format: str = "%Y-%m-%d %H:%M:%S"):
    """Makes all print statements print with the time in front of them"""
    print()
    print_statement = ""
    timeprint = datetime.datetime.now().strftime(time_format)
    for i in args:
        print_statement = f"{print_statement}{i}"
    builtins.print(f"{timeprint}: {print_statement}", sep=sep, end=end, file=file, flush=flush)



