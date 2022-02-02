from docutils import nodes
import jinja2
from docutils.parsers.rst import Directive
from sphinx.application import Sphinx
from docutils.parsers.rst import roles
from docutils.parsers.rst.states import Inliner
from typing import List, Dict

HELP_TEMPLATE = jinja2.Template("""
    <span class="help-button">؟
        <span class="text">{{ text }}</span>
    </span>
""")


class ButtonNode(nodes.Element):
    ...


class ButtonDirective(Directive):
    def run(self):
        node = ButtonNode()
        node['text'] = ''.join(self.content.data)
        return [node]


def html_visit_button_node(self, node: ButtonNode):
    html = HELP_TEMPLATE.render({k: v for k, v in node.attributes.items()})
    self.body.append(''.join([_.strip() for _ in html.split('\n') if _.strip()]))
    raise nodes.SkipNode


def button_role(role, rawtext, text, line_no, in_liner: Inliner, options: Dict = None, content: List = None):
    node = ButtonNode()
    node['text'] = text.rstrip()
    return [node], []


def setup(app: Sphinx):
    app.add_node(ButtonNode,
                 # ↓ kwargs
                 html=(html_visit_button_node, lambda: None)
                 )
    app.add_directive('button', ButtonDirective)

    """
    :help:`[Help text]`
    """

    roles.register_canonical_role('help', button_role)