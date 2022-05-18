import logging

from qgis.PyQt.QtWidgets import QDialog, QProgressBar, QGridLayout, QLabel, QGroupBox
from qgis.gui import (
    QgsMapLayerComboBox,
    QgsSpinBox,
    QgsDoubleSpinBox,
    QgsCollapsibleGroupBox,
)
from qgis.core import QgsFieldProxyModel, QgsMapLayerProxyModel

from ..definitions.gui import Panels
from ..qgis_plugin_tools.tools.i18n import tr
from ..qgis_plugin_tools.tools.resources import plugin_name
from ..qgis_plugin_tools.tools.exceptions import QgsPluginException
from .base_panel import BasePanel


LOGGER = logging.getLogger(plugin_name())


class HazardRiskIndexPanel(BasePanel):
    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.panel = Panels.HazardRiskIndex

    def setup_panel(self) -> None:

        self.dlg.hri_map_layer_cmb_bx_boundaries: QgsMapLayerComboBox
        self.dlg.hri_map_layer_cmb_bx_schools: QgsMapLayerComboBox
        self.dlg.hri_progress_bar: QProgressBar
        self.dlg.hri_risk_layer_gridlayout: QGridLayout
        self.dlg.groupbox_rasters: QgsCollapsibleGroupBox
        # self.dlg.groupbox_risk_layers: QGroupBox
        # self.dlg.groupbox_risk_layers.addLayout(self.dlg.hri_risk_layer_gridlayout)
        # self.dlg.hri_progress_bar.setMinimum(0)
        self.dlg.hri_progress_bar.setValue(0)
        self.dlg.hri_map_layer_cmb_bx_boundaries.setFilters(
            QgsMapLayerProxyModel.PolygonLayer
        )
        self.dlg.hri_map_layer_cmb_bx_schools.setFilters(
            QgsMapLayerProxyModel.PointLayer
        )
        self.dlg.hri_spn_bx_number_of_hazards: QgsSpinBox
        self.dlg.hri_spn_bx_number_of_hazards.setClearValue(1)
        self.dlg.hri_spn_bx_number_of_hazards.clear()
        self.dlg.hri_spn_bx_number_of_hazards.setMinimum(1)
        self.dlg.hri_spn_bx_number_of_hazards.setMaximum(6)

        self.dlg.hri_spn_bx_number_of_hazards.valueChanged.connect(
            self.__set_hri_risk_layer_grid
        )

        self.dlg.hri_map_layer_cmb_bx_boundaries.setShowCrs(True)
        self.dlg.hri_map_layer_cmb_bx_schools.setShowCrs(True)
        # self.hri_btn_run
        self.dlg.hri_btn_close.clicked.connect(self.__close_dialog)

    def __set_hri_risk_layer_grid(self, nr_of_risks):

        print(nr_of_risks)
        self.__clear_gridlayout(self.dlg.hri_risk_layer_gridlayout)

        for i in range(1, nr_of_risks):
            self.dlg.hri_risk_layer_gridlayout.addWidget(
                QLabel("Layer {}".format(i + 1), self.dlg), i, 0
            )
            self.dlg.hri_risk_layer_gridlayout.addWidget(
                QgsMapLayerComboBox(),
                i,
                1,
            )
            """self.dlg.hri_risk_layer_gridlayout.addWidget(
                self.dlg.hri_widget_list[i], i, 1
            )"""
            self.dlg.hri_risk_layer_gridlayout.addWidget(QgsDoubleSpinBox(), i, 2)

            self.dlg.hri_risk_layer_gridlayout.setRowMinimumHeight(i, 20)

    def __clear_gridlayout(self, layout):
        # does not work
        # while layout.count() > 0:
        #    layout.itemAt(0).setParent(None)

        """for i in range(layout.rowCount()):
        for j in range(layout.columnCount()):
            layout.removeWidget(layout.itemAt(i, j))
        for i in range(layout.rowCount() * layout.columnCount()):
            layout.removeWidget(parent, layout.itemAt(i))"""

    def __close_dialog(self):
        self.dlg.hide()
