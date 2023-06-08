from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ElementTree

from PatternMatch import PatternMatch


def match_to_hml(matcher: PatternMatch, code: str, pattern: str) -> ElementTree:
    template = load_template()
    code_div = template.find(".//*[@id='code']")

    matches = {}
    patterns = {}
    for pattern_node, code_node in matcher.matches:
        if not hasattr(code_node, "lineno"):
            continue
        if not hasattr(code_node, "col_offset") or not hasattr(code_node, "end_col_offset"):
            continue

        # Add red to line
        if code_node.lineno - 1 not in matches:
            matches[code_node.lineno - 1] = (code_node.col_offset, code_node.end_col_offset)
        else:
            start, end = matches[code_node.lineno - 1]
            if code_node.col_offset < start:
                start = code_node.col_offset
            if code_node.end_col_offset > start:
                end = code_node.end_col_offset
            matches[code_node.lineno - 1] = (start, end)

        # Add pattern line
        if code_node.lineno - 1 not in patterns:
            patterns[code_node.lineno - 1] = pattern_node

    code_line = code.splitlines(False)
    for i, line in enumerate(code_line):
        pre = ET.SubElement(code_div, "pre")

        if i in matches:
            start, end = matches[i]
            pre.text = line[:start]
            b = ET.SubElement(pre, "b")
            b.text = line[start:end + 1]
            b.tail = line[end + 1:]
        else:
            pre.text = line

        #if i in lines:
        #    skip = ET.SubElement(pre, "b")
        #    skip.text = "\u21b2"

    pattern_line = pattern.splitlines(False)
    pattern_div = template.find(".//*[@id='pattern']")
    for i, _ in enumerate(code_line):
        pre = ET.SubElement(pattern_div, "pre")

        text = ""
        if i in matcher.pattern_match:
            line = matcher.pattern_match[i].lineno
            txt = pattern_line[line-1]
            text += txt
        else:
            text += '\t'

        if i+1 in matcher.line_skip_matches:
            text += "{"

        if i+1 in matcher.line_skip_matches.values():
            text += "}"

        pre.text = text

    return template


def __str_to_pre(string):
    pre = ET.Element("pre")
    pre.text = string
    return pre


def load_template() -> ElementTree:
    template = ET.parse("visualizer/template.html")
    return template
