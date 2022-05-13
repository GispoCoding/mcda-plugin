"""Panel core base class."""
from typing import Dict, Optional

from qgis.PyQt.QtWidgets import QDialog

from ..definitions.gui import Panels
from ..qgis_plugin_tools.tools.exceptions import QgsPluginNotImplementedException


class BasePanel:
    """
    Base panel for dialog. Adapted from https://github.com/3liz/QuickOSM
    licenced under GPL version 2
    """

    def __init__(self, dialog: QDialog) -> None:
        self._panel: Optional[Panels] = None
        self._dialog = dialog
        self.elem_map: Dict[int, bool] = {}

    @property
    def panel(self) -> Panels:
        if self._panel:
            return self._panel
        else:
            raise NotImplementedError

    @panel.setter
    def panel(self, panel: Panels) -> None:
        self._panel = panel

    @property
    def dlg(self) -> QDialog:
        """Return the dialog."""
        return self._dialog

    def setup_panel(self) -> None:
        """Setup the UI for the panel."""
        raise QgsPluginNotImplementedException()

    def teardown_panel(self) -> None:
        """Teardown for the panels"""

    def on_update_map_layers(self) -> None:
        """Occurs when map layers are updated"""

    def is_active(self) -> bool:
        """Is the panel currently active (selected)"""
        curr_panel = list(self.dlg.panels.keys())[self.dlg.menu_widget.currentRow()]
        return curr_panel == self.panel
