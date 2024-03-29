import logging

from qgis.PyQt.QtWidgets import QDesktopWidget, QDialog, QRadioButton, QWidget

from ..definitions.gui import Panels
from ..qgis_plugin_tools.tools.resources import load_ui, plugin_name
from .about_panel import AboutPanel
from .economic_panel import EconomicSuitabilityPanel
from .environmental_panel import EnvironmentalSuitabilityPanel
from .hazard_panel import HazardRiskIndexPanel
from .help_panel import HelpPanel
from .infrastructure_panel import InfrastructurePanel
from .multicriteria_panel import MultiCriteriaSuitabilityPanel

# from ..qgis_plugin_tools.tools.settings import get_setting, set_setting


FORM_CLASS = load_ui("main_dialog.ui")
LOGGER = logging.getLogger(plugin_name())


class MainDialog(QDialog, FORM_CLASS):  # type: ignore
    """
    The structure and idea of the UI is adapted from https://github.com/3liz/QuickOSM
    licenced under GPL version 2
    """

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self._set_window_location()
        self.panels = {
            Panels.HazardRiskIndex: HazardRiskIndexPanel(self),
            Panels.Infrastructure: InfrastructurePanel(self),
            Panels.EconomicSuitability: EconomicSuitabilityPanel(self),
            Panels.EnvironmentalSuitability: EnvironmentalSuitabilityPanel(self),
            Panels.MultiCriteriaSuitability: MultiCriteriaSuitabilityPanel(self),
            Panels.Help: HelpPanel(self),
            Panels.About: AboutPanel(self),
        }
        for i, panel_enum in enumerate(self.panels):
            item = self.menu_widget.item(i)
            item.setIcon(panel_enum.icon)
            self.panels[panel_enum].panel = panel_enum
        # Change panel as menu item is changed
        self.menu_widget.currentRowChanged["int"].connect(
            self.stacked_widget.setCurrentIndex
        )
        # Set up all the panels
        for panel in self.panels.values():
            panel.setup_panel()
        # The first panel is shown initially
        self.menu_widget.setCurrentRow(0)

    def _set_window_location(self) -> None:
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = int((ag.width() - widget.width()) / 1.5)
        y = int(2 * ag.height() - sg.height() - 1.2 * widget.height())
        self.move(x, y)

    @staticmethod
    def __get_radiobtn_name(parent: QWidget) -> str:
        for radio_button in parent.findChildren(QRadioButton):
            if radio_button.isChecked():
                return radio_button.objectName()
        raise Exception("No checked radio buttons found")  # TODO: exception
