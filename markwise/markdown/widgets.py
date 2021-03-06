class Widget:
    pass


class Text(Widget):
    def __init__(self, text: str, bold=False, italic=False, strikeout=False):
        self.text = text
        self.bold = bold
        self.italic = italic
        self.strikeout = strikeout

    def __repr__(self):
        a = (self.italic * 1 + self.bold * 2) * '*'
        b = "~~"
        
        if (self.bold + self.italic + self.strikeout != 0):
            if self.strikeout is None:
                return f"{b}{self.text}{b}"
            else:
                return f"{a}{self.text}{a}"
        else:
            return self.text


class Heading(Widget):
    def __init__(self, level: int, text: Widget):
        self.level = level
        self.text = text

    def __repr__(self):
        return f"{self.level * '#'} {self.text}"


Header = Heading


class Link(Widget):
    def __init__(self, link: str, text: Widget):
        self.link = link
        self.text = text

    def __repr__(self):
        return f"[{self.text}]({self.link})"


class BlockQuote(Widget):
    def __init__(self, text: Widget):
        self.text = text

    def __repr__(self):
        return f"> {self.text}"


class Mark(Widget):
    def __init__(self, child: Widget):
        self.child = child

    def __repr__(self):
        return f"- {self.child}"


class NumberMark(Widget):
    def __init__(self, child: Widget, number: int = 1):
        self.number = number
        self.child = child

    def __repr__(self):
        return f"{self.number}. {self.child}"


class WidgetList(Widget):
    def __init__(self, children):
        self.children = children

    def __repr__(self):
        return "\n".join(str(a) for a in self.children)


class Indent(Widget):
    def __init__(self, child, amount: int = 1):
        self.child = child
        self.amount = amount

    def __repr__(self):
        return f"{' ' * self.amount * 3}{self.child}"


class CodeBlock(Widget):
    def __init__(self, text: Text, lang=None):
        self.highlighters = ["py", "python", "json", "shell", "bash", "js", "html", "css", "asciidoc"]
        self.text = text
        self.lang = lang

        if self.lang not in self.highlighters:
            self.lang = None

    def __repr__(self):
        return f"""```{self.lang if self.lang else ""}\n{self.text}\n```"""


class Line:
    def __init__(self, length: int = 60):
        self.length = length

    def __repr__(self):
        return "-" * self.length


class Image(Widget):
    def __init__(self, url: str, description: str):
        self.url = url
        self.description = description

    def __repr__(self):
        return f"![{self.description}]({self.url})"


class HorizontalRuler(Widget):
    def __repr__(self):
        return "***"
