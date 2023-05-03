from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ElementTree

from PatternMatch import PatternMatch


def match_to_hml(matcher: PatternMatch, code: str) -> ElementTree:
    html = ET.Element("html", attrib={'lang': 'en'})

    head = ET.SubElement(html, "head")
    title = ET.SubElement(head, "title")
    title.text = "Match"
    style = ET.SubElement(head, "style")
    style.text = "b {color: red;}"

    body = ET.Element("body")
    html.append(body)
    div = ET.Element("div", attrib={'id': 'code'})
    body.append(div)

    matches = {}
    for _, code_node in matcher.matches:
        if not hasattr(code_node, "lineno"):
            continue
        if not hasattr(code_node, "col_offset") or not hasattr(code_node, "end_col_offset"):
            continue

        if code_node.lineno-1 not in matches:
            matches[code_node.lineno-1] = (code_node.col_offset, code_node.end_col_offset)
        else:
            start, end = matches[code_node.lineno-1]
            if code_node.col_offset < start:
                start = code_node.col_offset
            if code_node.end_col_offset > start:
                end = code_node.end_col_offset
            matches[code_node.lineno-1] = (start, end)

    lines = []
    for _, code_node in matcher.line_skip_matches:
        if not hasattr(code_node, "lineno"):
            continue
        if not hasattr(code_node, "col_offset") or not hasattr(code_node, "end_col_offset"):
            continue

        if code_node.lineno-1 not in lines:
            lines.append(code_node.lineno-1)

    code_line = code.splitlines(False)
    for i, line in enumerate(code_line):
        pre = ET.SubElement(div, "pre")

        if i in matches:
            start, end = matches[i]
            pre.text = line[:start]
            b = ET.SubElement(pre, "b")
            b.text = line[start:end+1]
            b.tail = line[end+1:]
        else:
            pre.text = line

        if i in lines:
            skip = ET.SubElement(pre, "b")
            skip.text = "\u21b2"



    return ET.ElementTree(html)


def __str_to_pre(string):
    pre = ET.Element("pre")
    pre.text = string
    return pre
