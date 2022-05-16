import logging

from qgis.PyQt.QtWidgets import QDialog, QProgressBar, QGridLayout, QLabel
from qgis.gui import QgsMapLayerComboBox, QgsSpinBox
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

        # self.hri_btn_run
        self.dlg.hri_map_layer_cmb_bx_boundaries: QgsMapLayerComboBox
        self.dlg.hri_map_layer_cmb_bx_schools: QgsMapLayerComboBox
        self.dlg.hri_progress_bar: QProgressBar
        self.dlg.hri_risk_layer_gridlayout: QGridLayout

        # self.dlg.hri_risk_layer_gridlayout.setRowCount(1)
        # self.dlg.hri_risk_layer_gridlayout.setColumnCount(3)

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

        self.dlg.hri_spn_bx_number_of_hazards.valueChanged.connect(
            self.__set_hri_risk_layer_grid
        )
        """
        self.hri_chck_bx_use_selected_boundary
      
        self.dlg.hri_chck_bx_use_selected_schools
        self.hri_risk_layer_gridlayout"""
        self.dlg.hri_map_layer_cmb_bx_boundaries.setShowCrs(True)
        self.dlg.hri_map_layer_cmb_bx_schools.setShowCrs(True)

        self.dlg.hri_btn_close.clicked.connect(self.__close_dialog)

    # self.hri_map_layer_cmb_bx_boundaries.ma

    def __set_hri_risk_layer_grid(self, nr_of_risks):

        print(nr_of_risks)

        """self.stored_queries: List[StoredQuery] = self.sq_factory.list_queries()  # type: ignore # noqa E501
        self.tbl_wdgt_stored_queries.setRowCount(len(self.stored_queries))
        self.tbl_wdgt_stored_queries.setColumnCount(3)"""

        for i in range(nr_of_risks):
            self.dlg.hri_risk_layer_gridlayout.addWidget(
                QLabel("Layer {}".format(i + 1), self.dlg), i, 0
            )
            self.dlg.hri_risk_layer_gridlayout.addWidget(
                QgsMapLayerComboBox(),
                i,
                1,
            )
            """self.dlg.hri_risk_layer_gridlayout.addWidget(
                QLabel("Layer {}".format(i + 1), self.dlg), i, 1
            )"""
            self.dlg.hri_risk_layer_gridlayout.addWidget(
                QLabel("Layer1", self.dlg), i, 2
            )
            # pass
            """self.tbl_wdgt_stored_queries.setItem(i, 0, QTableWidgetItem(sq.title))
            abstract_item = QTableWidgetItem(sq.abstract)
            abstract_item.setToolTip(sq.abstract)
            self.tbl_wdgt_stored_queries.setItem(i, 1, abstract_item)
            id_item = QTableWidgetItem(sq.id)
            id_item.setToolTip(sq.id)
            self.tbl_wdgt_stored_queries.setItem(i, 2, id_item)"""

        print("risks have changed")

    def __close_dialog(self):
        self.dlg.hide()
