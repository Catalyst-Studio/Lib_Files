from xml.dom.minidom import parseString as string_to_dom
import pathlib


def Attributes(args: dict):
    if args is not None:
        arg_list = []
        for x in args:
            arg_list.append(f' {x.lower()}="{args[x]}"')
        attributes = ""
        for i in arg_list:
            attributes = attributes + i
        return attributes
    else:
        return ""


def Internals(args: tuple):
    internals = ""
    if args is not None:
        for x in args:
            internals = internals + x
    return internals


def Customtag(tag: str, *args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<{tag}{attributes}>{internals}</{tag}>"


def HTMLStarter(**attributes):
    attributes = Attributes(attributes)
    return f"<!DOCTYPE html{attributes}>"


def HTML(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<html{attributes}>{internals}</html>"


def Head(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<head{attributes}>{internals}</head>"


def Comment(content: str):
    return f"<!--{content}-->"


def P(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<p{attributes}>{internals}</p>"


def Body(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<body{attributes}>{internals}</body>"


class Generate:

    def __init__(self, *args):
        """the arguments for the html generator"""
        html = ""
        for x in args:
            html = html + x
        self.html = html

    def prettify(self, html: bool = True):
        """will give back the properly indented and multiline version of the html"""
        dom = string_to_dom(string=str(self.mini()))
        ugly = dom.toprettyxml(indent="  ")
        split = list(filter(lambda x: len(x.strip()), ugly.split('\n')))
        if html:
            split = split[1:]
        pretty = '\n'.join(split)
        return pretty

    def pretty_print(self):
        """Will print the prettified version of the html"""
        print(self.prettify())

    def mini(self):
        """Will give back the minified version of the html"""
        return self.html

    def write(self, filename: pathlib.Path, mini: bool = True):
        """Used to write the html that is generated to a file. If the file path does not exist it will be created"""
        with filename.open("w") as f:
            f.write(self.mini() if mini is True else self.prettify())


def Title(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<title{attributes}>{internals}</title>"


def A(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<a{attributes}>{internals}</a>"


def Abbr(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<abbr{attributes}>{internals}</abbr>"


def Address(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<address{attributes}>{internals}</address>"


def Area(**attributes):
    attributes = Attributes(attributes)
    return f"<area{attributes}>"


def Article(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<article{attributes}>{internals}</article>"


def Aside(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<aside{attributes}>{internals}</aside>"


def Audio(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<audio{attributes}>{internals}</audio>"


def B(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<b{attributes}>{internals}</b>"


def Base(**attributes):
    attributes = Attributes(attributes)
    return f"<base{attributes}>"


def Bdo(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<bdo{attributes}>{internals}</bdo>"


def Blockquote(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<blockquote{attributes}>{internals}</blockquote>"


def Br(**attributes):
    attributes = Attributes(attributes)
    return f"<br{attributes}/>"


def Button(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<button{attributes}>{internals}</button>"


def Canvas(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<canvas{attributes}>{internals}</canvas>"


def Caption(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<caption{attributes}>{internals}</caption>"


def Cite(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<cite{attributes}>{internals}</cite>"


def Code(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<code{attributes}>{internals}</code>"


def Col(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<col{attributes}>{internals}</col>"


def Colgroup(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<colgroup{attributes}>{internals}</colgroup>"


def Command(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<command{attributes}>{internals}</command>"


def Datagrid(*args, **attributes):
    attributes = Attributes(attributes)
    internals = Internals(args)
    return f"<datagrid{attributes}>{internals}</datagrid>"
