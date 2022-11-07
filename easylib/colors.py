class printStyle:

    def __init__(self):
        self.stylesList = ["black", "red", "green", "brown", "blue", "purple", "cyan", "light_gray", "dark_gray",
                      "light_red",
                      "light_green", "yellow", "light_blue", "light_purple", "light_cyan", "light_white", "bold",
                      "faint",
                      "italic", "underline", "blink", "negative", "crossed"]
        self.bgstylelist = ["black", "red", "green", "orange", "blue", "purple", "cyan", "light_gray"]
        self.styles = {}
        self.bgstyles = {}
        item = 29
        round = 1
        bgitem = 40
        for style in self.bgstylelist:
            self.bgstyles[style] = f"\033[{bgitem}m"
            bgitem = bgitem + 1

        for style in self.stylesList:
            if round == 1 or round == 2:
                item = item + 1
                if item == 38:
                    round = round + 1
                    item = 30
                    if round == 3:
                        item = 1
                self.styles[style] = f"\033[{round - 1};{item}m"
            else:
                if (item == 5) or (item == 7):
                    item = item + 2
                else:
                    item = item + 1
                self.styles[style] = f"\033[{item}m"

        if not __import__("sys").stdout.isatty():
            for _ in dir():
                if isinstance(_, str) and _[0] != "_":
                    locals()[_] = ""

        else:
            if __import__("platform").system() == "Windows":
                kernel32 = __import__("ctypes").wind11.kernel32
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
                del kernel32

    def getStyle(self, color: str):
        return self.styles[color]

    def getbgStyle(self, color: str):
        return self.bgstyles[color]

    def getbgStyleList(self):
        return self.bgstylelist

    def getStyleList(self):
        return self.stylesList

    def bgstyle(self, color: str, message: str):
        return f"{self.getbgStyle(color)}{message}"

    def style(self, color: str, message: str):
        return f"{self.getStyle(color)}{message}"

    def printFormatTable(self):
        for style in range(2):
            for fg in range(30, 38):
                s1 = ''
                for bg in range(40, 48):
                    format = ';'.join([str(style), str(fg), str(bg)])
                    s1 = s1 + '\x1b[%sm %s \x1b[0m' % (format, format)
                print(s1)
            print('\n')
