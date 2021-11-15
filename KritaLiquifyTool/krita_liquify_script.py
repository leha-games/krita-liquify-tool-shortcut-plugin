from krita import *
from PyQt5.QtWidgets import QWidget, QSpinBox, QToolButton

def find_transform_tool_options_widget():
    qwindow = Krita.instance().activeWindow().qwindow()    
    for c in qwindow.findChildren(QWidget):
        if c.metaObject().className() == "KisToolTransformConfigWidget":
            return c

class LiquifyTool(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def switch_liquify_tool(self):
        Krita.instance().action("KisToolTransform").trigger()
        # Krita.instance().action("reselect").trigger()
        transform_widget = find_transform_tool_options_widget()
        liquifyButton = transform_widget.findChild(QToolButton, "liquifyButton")
        liquifyButton.click()

    def createActions(self, window):
        action = window.createAction("switch_liquify", "Liquify Tool", "tools/scripts")
        action.triggered.connect(self.switch_liquify_tool)

Krita.instance().addExtension(LiquifyTool(Krita.instance()))