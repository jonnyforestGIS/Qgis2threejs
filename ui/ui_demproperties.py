# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\minorua\.qgis2\python\developing_plugins\Qgis2threejs\ui\demproperties.ui'
#
# Created: Wed May 27 09:36:22 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DEMPropertiesWidget(object):
    def setupUi(self, DEMPropertiesWidget):
        DEMPropertiesWidget.setObjectName(_fromUtf8("DEMPropertiesWidget"))
        DEMPropertiesWidget.resize(386, 656)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DEMPropertiesWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout_DEMLayer = QtGui.QFormLayout()
        self.formLayout_DEMLayer.setObjectName(_fromUtf8("formLayout_DEMLayer"))
        self.label_DEMLayer = QtGui.QLabel(DEMPropertiesWidget)
        self.label_DEMLayer.setObjectName(_fromUtf8("label_DEMLayer"))
        self.formLayout_DEMLayer.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_DEMLayer)
        self.comboBox_DEMLayer = QtGui.QComboBox(DEMPropertiesWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_DEMLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_DEMLayer.setSizePolicy(sizePolicy)
        self.comboBox_DEMLayer.setMaximumSize(QtCore.QSize(350, 16777215))
        self.comboBox_DEMLayer.setObjectName(_fromUtf8("comboBox_DEMLayer"))
        self.formLayout_DEMLayer.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_DEMLayer)
        self.verticalLayout_2.addLayout(self.formLayout_DEMLayer)
        self.groupBox_Resampling = QtGui.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Resampling.setObjectName(_fromUtf8("groupBox_Resampling"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_Resampling)
        self.verticalLayout_6.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.radioButton_Simple = QtGui.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Simple.setChecked(True)
        self.radioButton_Simple.setObjectName(_fromUtf8("radioButton_Simple"))
        self.verticalLayout_6.addWidget(self.radioButton_Simple)
        self.verticalLayout_Simple = QtGui.QVBoxLayout()
        self.verticalLayout_Simple.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_Simple.setObjectName(_fromUtf8("verticalLayout_Simple"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalSlider_Resolution = QtGui.QSlider(self.groupBox_Resampling)
        self.horizontalSlider_Resolution.setEnabled(True)
        self.horizontalSlider_Resolution.setMinimum(1)
        self.horizontalSlider_Resolution.setMaximum(6)
        self.horizontalSlider_Resolution.setSingleStep(1)
        self.horizontalSlider_Resolution.setPageStep(1)
        self.horizontalSlider_Resolution.setProperty("value", 2)
        self.horizontalSlider_Resolution.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_Resolution.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider_Resolution.setTickInterval(1)
        self.horizontalSlider_Resolution.setObjectName(_fromUtf8("horizontalSlider_Resolution"))
        self.horizontalLayout.addWidget(self.horizontalSlider_Resolution)
        self.label_Resolution = QtGui.QLabel(self.groupBox_Resampling)
        self.label_Resolution.setMinimumSize(QtCore.QSize(80, 0))
        self.label_Resolution.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Resolution.setObjectName(_fromUtf8("label_Resolution"))
        self.horizontalLayout.addWidget(self.label_Resolution)
        self.verticalLayout_Simple.addLayout(self.horizontalLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_8 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_HRes = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_HRes.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_HRes.sizePolicy().hasHeightForWidth())
        self.lineEdit_HRes.setSizePolicy(sizePolicy)
        self.lineEdit_HRes.setReadOnly(True)
        self.lineEdit_HRes.setObjectName(_fromUtf8("lineEdit_HRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_HRes)
        self.label_9 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_VRes = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_VRes.setEnabled(True)
        self.lineEdit_VRes.setReadOnly(True)
        self.lineEdit_VRes.setObjectName(_fromUtf8("lineEdit_VRes"))
        self.horizontalLayout_4.addWidget(self.lineEdit_VRes)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.verticalLayout_Simple.addLayout(self.formLayout_2)
        self.formLayout_Surroundings = QtGui.QFormLayout()
        self.formLayout_Surroundings.setObjectName(_fromUtf8("formLayout_Surroundings"))
        self.checkBox_Surroundings = QtGui.QCheckBox(self.groupBox_Resampling)
        self.checkBox_Surroundings.setObjectName(_fromUtf8("checkBox_Surroundings"))
        self.formLayout_Surroundings.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_Surroundings)
        self.gridLayout_Surroundings = QtGui.QGridLayout()
        self.gridLayout_Surroundings.setObjectName(_fromUtf8("gridLayout_Surroundings"))
        self.label_2 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_2.setEnabled(False)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_Surroundings.addWidget(self.label_2, 0, 0, 1, 1)
        self.spinBox_Size = QtGui.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Size.setEnabled(False)
        self.spinBox_Size.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_Size.setMinimum(3)
        self.spinBox_Size.setMaximum(9)
        self.spinBox_Size.setSingleStep(2)
        self.spinBox_Size.setProperty("value", 5)
        self.spinBox_Size.setObjectName(_fromUtf8("spinBox_Size"))
        self.gridLayout_Surroundings.addWidget(self.spinBox_Size, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_3.setEnabled(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_Surroundings.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinBox_Roughening = QtGui.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Roughening.setEnabled(False)
        self.spinBox_Roughening.setMinimumSize(QtCore.QSize(70, 0))
        self.spinBox_Roughening.setMinimum(2)
        self.spinBox_Roughening.setMaximum(64)
        self.spinBox_Roughening.setSingleStep(4)
        self.spinBox_Roughening.setProperty("value", 4)
        self.spinBox_Roughening.setObjectName(_fromUtf8("spinBox_Roughening"))
        self.gridLayout_Surroundings.addWidget(self.spinBox_Roughening, 0, 3, 1, 1)
        self.formLayout_Surroundings.setLayout(0, QtGui.QFormLayout.FieldRole, self.gridLayout_Surroundings)
        self.verticalLayout_Simple.addLayout(self.formLayout_Surroundings)
        self.verticalLayout_6.addLayout(self.verticalLayout_Simple)
        self.radioButton_Advanced = QtGui.QRadioButton(self.groupBox_Resampling)
        self.radioButton_Advanced.setObjectName(_fromUtf8("radioButton_Advanced"))
        self.verticalLayout_6.addWidget(self.radioButton_Advanced)
        self.verticalLayout_Advanced = QtGui.QVBoxLayout()
        self.verticalLayout_Advanced.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_Advanced.setObjectName(_fromUtf8("verticalLayout_Advanced"))
        self.horizontalLayout_Advanced1 = QtGui.QHBoxLayout()
        self.horizontalLayout_Advanced1.setObjectName(_fromUtf8("horizontalLayout_Advanced1"))
        self.label_11 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_Advanced1.addWidget(self.label_11)
        self.spinBox_Height = QtGui.QSpinBox(self.groupBox_Resampling)
        self.spinBox_Height.setEnabled(True)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(8)
        self.spinBox_Height.setProperty("value", 4)
        self.spinBox_Height.setObjectName(_fromUtf8("spinBox_Height"))
        self.horizontalLayout_Advanced1.addWidget(self.spinBox_Height)
        self.label_10 = QtGui.QLabel(self.groupBox_Resampling)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_Advanced1.addWidget(self.label_10)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_Advanced1.addWidget(self.lineEdit)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced1)
        self.horizontalLayout_Advanced2 = QtGui.QHBoxLayout()
        self.horizontalLayout_Advanced2.setObjectName(_fromUtf8("horizontalLayout_Advanced2"))
        self.label_Focus = QtGui.QLabel(self.groupBox_Resampling)
        self.label_Focus.setObjectName(_fromUtf8("label_Focus"))
        self.horizontalLayout_Advanced2.addWidget(self.label_Focus)
        self.toolButton_PointTool = QtGui.QToolButton(self.groupBox_Resampling)
        self.toolButton_PointTool.setObjectName(_fromUtf8("toolButton_PointTool"))
        self.horizontalLayout_Advanced2.addWidget(self.toolButton_PointTool)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced2)
        self.horizontalLayout_Advanced3 = QtGui.QHBoxLayout()
        self.horizontalLayout_Advanced3.setObjectName(_fromUtf8("horizontalLayout_Advanced3"))
        self.label_centerX = QtGui.QLabel(self.groupBox_Resampling)
        self.label_centerX.setMinimumSize(QtCore.QSize(30, 0))
        self.label_centerX.setObjectName(_fromUtf8("label_centerX"))
        self.horizontalLayout_Advanced3.addWidget(self.label_centerX)
        self.lineEdit_centerX = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_centerX.setEnabled(True)
        self.lineEdit_centerX.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_centerX.setReadOnly(True)
        self.lineEdit_centerX.setObjectName(_fromUtf8("lineEdit_centerX"))
        self.horizontalLayout_Advanced3.addWidget(self.lineEdit_centerX)
        self.label_centerY = QtGui.QLabel(self.groupBox_Resampling)
        self.label_centerY.setMinimumSize(QtCore.QSize(30, 0))
        self.label_centerY.setObjectName(_fromUtf8("label_centerY"))
        self.horizontalLayout_Advanced3.addWidget(self.label_centerY)
        self.lineEdit_centerY = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_centerY.setEnabled(True)
        self.lineEdit_centerY.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_centerY.setReadOnly(True)
        self.lineEdit_centerY.setObjectName(_fromUtf8("lineEdit_centerY"))
        self.horizontalLayout_Advanced3.addWidget(self.lineEdit_centerY)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced3)
        self.horizontalLayout_Advanced4 = QtGui.QHBoxLayout()
        self.horizontalLayout_Advanced4.setObjectName(_fromUtf8("horizontalLayout_Advanced4"))
        self.label_rectWidth = QtGui.QLabel(self.groupBox_Resampling)
        self.label_rectWidth.setEnabled(True)
        self.label_rectWidth.setMinimumSize(QtCore.QSize(30, 0))
        self.label_rectWidth.setObjectName(_fromUtf8("label_rectWidth"))
        self.horizontalLayout_Advanced4.addWidget(self.label_rectWidth)
        self.lineEdit_rectWidth = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_rectWidth.setEnabled(True)
        self.lineEdit_rectWidth.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_rectWidth.setReadOnly(True)
        self.lineEdit_rectWidth.setObjectName(_fromUtf8("lineEdit_rectWidth"))
        self.horizontalLayout_Advanced4.addWidget(self.lineEdit_rectWidth)
        self.label_rectHeight = QtGui.QLabel(self.groupBox_Resampling)
        self.label_rectHeight.setMinimumSize(QtCore.QSize(30, 0))
        self.label_rectHeight.setObjectName(_fromUtf8("label_rectHeight"))
        self.horizontalLayout_Advanced4.addWidget(self.label_rectHeight)
        self.lineEdit_rectHeight = QtGui.QLineEdit(self.groupBox_Resampling)
        self.lineEdit_rectHeight.setEnabled(True)
        self.lineEdit_rectHeight.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_rectHeight.setReadOnly(True)
        self.lineEdit_rectHeight.setObjectName(_fromUtf8("lineEdit_rectHeight"))
        self.horizontalLayout_Advanced4.addWidget(self.lineEdit_rectHeight)
        self.verticalLayout_Advanced.addLayout(self.horizontalLayout_Advanced4)
        self.verticalLayout_6.addLayout(self.verticalLayout_Advanced)
        self.verticalLayout_2.addWidget(self.groupBox_Resampling)
        self.groupBox_DisplayType = QtGui.QGroupBox(DEMPropertiesWidget)
        self.groupBox_DisplayType.setObjectName(_fromUtf8("groupBox_DisplayType"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_DisplayType)
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton_MapCanvas = QtGui.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_MapCanvas.setChecked(True)
        self.radioButton_MapCanvas.setObjectName(_fromUtf8("radioButton_MapCanvas"))
        self.verticalLayout.addWidget(self.radioButton_MapCanvas)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton_LayerImage = QtGui.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_LayerImage.setObjectName(_fromUtf8("radioButton_LayerImage"))
        self.horizontalLayout_5.addWidget(self.radioButton_LayerImage)
        self.label_LayerImage = QtGui.QLabel(self.groupBox_DisplayType)
        self.label_LayerImage.setEnabled(False)
        self.label_LayerImage.setText(_fromUtf8(""))
        self.label_LayerImage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_LayerImage.setObjectName(_fromUtf8("label_LayerImage"))
        self.horizontalLayout_5.addWidget(self.label_LayerImage)
        self.toolButton_SelectLayer = QtGui.QToolButton(self.groupBox_DisplayType)
        self.toolButton_SelectLayer.setEnabled(False)
        self.toolButton_SelectLayer.setObjectName(_fromUtf8("toolButton_SelectLayer"))
        self.horizontalLayout_5.addWidget(self.toolButton_SelectLayer)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_ImageFile = QtGui.QHBoxLayout()
        self.horizontalLayout_ImageFile.setObjectName(_fromUtf8("horizontalLayout_ImageFile"))
        self.radioButton_ImageFile = QtGui.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_ImageFile.setEnabled(True)
        self.radioButton_ImageFile.setObjectName(_fromUtf8("radioButton_ImageFile"))
        self.horizontalLayout_ImageFile.addWidget(self.radioButton_ImageFile)
        self.lineEdit_ImageFile = QtGui.QLineEdit(self.groupBox_DisplayType)
        self.lineEdit_ImageFile.setEnabled(False)
        self.lineEdit_ImageFile.setObjectName(_fromUtf8("lineEdit_ImageFile"))
        self.horizontalLayout_ImageFile.addWidget(self.lineEdit_ImageFile)
        self.toolButton_ImageFile = QtGui.QToolButton(self.groupBox_DisplayType)
        self.toolButton_ImageFile.setEnabled(False)
        self.toolButton_ImageFile.setObjectName(_fromUtf8("toolButton_ImageFile"))
        self.horizontalLayout_ImageFile.addWidget(self.toolButton_ImageFile)
        self.verticalLayout.addLayout(self.horizontalLayout_ImageFile)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.radioButton_SolidColor = QtGui.QRadioButton(self.groupBox_DisplayType)
        self.radioButton_SolidColor.setObjectName(_fromUtf8("radioButton_SolidColor"))
        self.horizontalLayout_7.addWidget(self.radioButton_SolidColor)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label = QtGui.QLabel(self.groupBox_DisplayType)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_7.addWidget(self.label)
        self.lineEdit_Color = QtGui.QLineEdit(self.groupBox_DisplayType)
        self.lineEdit_Color.setEnabled(False)
        self.lineEdit_Color.setObjectName(_fromUtf8("lineEdit_Color"))
        self.horizontalLayout_7.addWidget(self.lineEdit_Color)
        self.toolButton_Color = QtGui.QToolButton(self.groupBox_DisplayType)
        self.toolButton_Color.setEnabled(False)
        self.toolButton_Color.setObjectName(_fromUtf8("toolButton_Color"))
        self.horizontalLayout_7.addWidget(self.toolButton_Color)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_TextureSize = QtGui.QLabel(self.groupBox_DisplayType)
        self.label_TextureSize.setObjectName(_fromUtf8("label_TextureSize"))
        self.gridLayout.addWidget(self.label_TextureSize, 0, 0, 1, 1)
        self.comboBox_TextureSize = QtGui.QComboBox(self.groupBox_DisplayType)
        self.comboBox_TextureSize.setObjectName(_fromUtf8("comboBox_TextureSize"))
        self.gridLayout.addWidget(self.comboBox_TextureSize, 0, 1, 1, 2)
        self.label_17 = QtGui.QLabel(self.groupBox_DisplayType)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)
        self.spinBox_demtransp = QtGui.QSpinBox(self.groupBox_DisplayType)
        self.spinBox_demtransp.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_demtransp.sizePolicy().hasHeightForWidth())
        self.spinBox_demtransp.setSizePolicy(sizePolicy)
        self.spinBox_demtransp.setPrefix(_fromUtf8(""))
        self.spinBox_demtransp.setMinimum(0)
        self.spinBox_demtransp.setMaximum(100)
        self.spinBox_demtransp.setSingleStep(10)
        self.spinBox_demtransp.setProperty("value", 0)
        self.spinBox_demtransp.setObjectName(_fromUtf8("spinBox_demtransp"))
        self.gridLayout.addWidget(self.spinBox_demtransp, 1, 1, 1, 1)
        self.checkBox_TransparentBackground = QtGui.QCheckBox(self.groupBox_DisplayType)
        self.checkBox_TransparentBackground.setObjectName(_fromUtf8("checkBox_TransparentBackground"))
        self.gridLayout.addWidget(self.checkBox_TransparentBackground, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.checkBox_Shading = QtGui.QCheckBox(self.groupBox_DisplayType)
        self.checkBox_Shading.setChecked(False)
        self.checkBox_Shading.setObjectName(_fromUtf8("checkBox_Shading"))
        self.verticalLayout_4.addWidget(self.checkBox_Shading)
        self.verticalLayout_2.addWidget(self.groupBox_DisplayType)
        self.groupBox_Clip = QtGui.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Clip.setObjectName(_fromUtf8("groupBox_Clip"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_Clip)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.checkBox_Clip = QtGui.QCheckBox(self.groupBox_Clip)
        self.checkBox_Clip.setObjectName(_fromUtf8("checkBox_Clip"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.checkBox_Clip)
        self.comboBox_ClipLayer = QtGui.QComboBox(self.groupBox_Clip)
        self.comboBox_ClipLayer.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ClipLayer.sizePolicy().hasHeightForWidth())
        self.comboBox_ClipLayer.setSizePolicy(sizePolicy)
        self.comboBox_ClipLayer.setMaximumSize(QtCore.QSize(220, 16777215))
        self.comboBox_ClipLayer.setObjectName(_fromUtf8("comboBox_ClipLayer"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox_ClipLayer)
        self.verticalLayout_2.addWidget(self.groupBox_Clip)
        self.groupBox_Accessories = QtGui.QGroupBox(DEMPropertiesWidget)
        self.groupBox_Accessories.setObjectName(_fromUtf8("groupBox_Accessories"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_Accessories)
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.checkBox_Sides = QtGui.QCheckBox(self.groupBox_Accessories)
        self.checkBox_Sides.setChecked(True)
        self.checkBox_Sides.setObjectName(_fromUtf8("checkBox_Sides"))
        self.verticalLayout_5.addWidget(self.checkBox_Sides)
        self.checkBox_Frame = QtGui.QCheckBox(self.groupBox_Accessories)
        self.checkBox_Frame.setObjectName(_fromUtf8("checkBox_Frame"))
        self.verticalLayout_5.addWidget(self.checkBox_Frame)
        self.verticalLayout_2.addWidget(self.groupBox_Accessories)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.retranslateUi(DEMPropertiesWidget)
        QtCore.QObject.connect(self.checkBox_Clip, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.comboBox_ClipLayer.setEnabled)
        QtCore.QObject.connect(self.radioButton_LayerImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.label_LayerImage.setEnabled)
        QtCore.QObject.connect(self.radioButton_LayerImage, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toolButton_SelectLayer.setEnabled)
        QtCore.QObject.connect(self.radioButton_ImageFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_ImageFile.setEnabled)
        QtCore.QObject.connect(self.radioButton_ImageFile, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toolButton_ImageFile.setEnabled)
        QtCore.QObject.connect(self.radioButton_SolidColor, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.lineEdit_Color.setEnabled)
        QtCore.QObject.connect(self.radioButton_SolidColor, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toolButton_Color.setEnabled)
        QtCore.QObject.connect(self.checkBox_Clip, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.checkBox_Frame.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(DEMPropertiesWidget)

    def retranslateUi(self, DEMPropertiesWidget):
        DEMPropertiesWidget.setWindowTitle(_translate("DEMPropertiesWidget", "Form", None))
        self.label_DEMLayer.setText(_translate("DEMPropertiesWidget", "DEM Layer", None))
        self.groupBox_Resampling.setTitle(_translate("DEMPropertiesWidget", "&Resampling", None))
        self.radioButton_Simple.setText(_translate("DEMPropertiesWidget", "Simple", None))
        self.label_Resolution.setText(_translate("DEMPropertiesWidget", "about 200 x 200 px", None))
        self.label_8.setText(_translate("DEMPropertiesWidget", "Grid spacing:", None))
        self.label_4.setText(_translate("DEMPropertiesWidget", "X", None))
        self.label_9.setText(_translate("DEMPropertiesWidget", "Y", None))
        self.checkBox_Surroundings.setText(_translate("DEMPropertiesWidget", "Surroundings", None))
        self.label_2.setText(_translate("DEMPropertiesWidget", "Size", None))
        self.label_3.setText(_translate("DEMPropertiesWidget", "Roughening", None))
        self.radioButton_Advanced.setText(_translate("DEMPropertiesWidget", "Advanced (quad tree)", None))
        self.label_11.setText(_translate("DEMPropertiesWidget", "Quad tree height", None))
        self.label_10.setText(_translate("DEMPropertiesWidget", "Quad size", None))
        self.lineEdit.setText(_translate("DEMPropertiesWidget", "64", None))
        self.label_Focus.setText(_translate("DEMPropertiesWidget", "Focus point", None))
        self.toolButton_PointTool.setText(_translate("DEMPropertiesWidget", "Get point from map", None))
        self.label_centerX.setText(_translate("DEMPropertiesWidget", "x", None))
        self.label_centerY.setText(_translate("DEMPropertiesWidget", "y", None))
        self.label_rectWidth.setText(_translate("DEMPropertiesWidget", "Width", None))
        self.label_rectHeight.setText(_translate("DEMPropertiesWidget", "Height", None))
        self.groupBox_DisplayType.setTitle(_translate("DEMPropertiesWidget", "&Display type", None))
        self.radioButton_MapCanvas.setText(_translate("DEMPropertiesWidget", "Map canvas image", None))
        self.radioButton_LayerImage.setText(_translate("DEMPropertiesWidget", "Layer image", None))
        self.toolButton_SelectLayer.setText(_translate("DEMPropertiesWidget", "Select layer(s)...", None))
        self.radioButton_ImageFile.setText(_translate("DEMPropertiesWidget", "Image file", None))
        self.toolButton_ImageFile.setText(_translate("DEMPropertiesWidget", "Browse...", None))
        self.radioButton_SolidColor.setText(_translate("DEMPropertiesWidget", "Solid color", None))
        self.label.setText(_translate("DEMPropertiesWidget", "Color", None))
        self.lineEdit_Color.setPlaceholderText(_translate("DEMPropertiesWidget", "0xrrggbb", None))
        self.toolButton_Color.setText(_translate("DEMPropertiesWidget", "...", None))
        self.label_TextureSize.setText(_translate("DEMPropertiesWidget", "Resolution", None))
        self.label_17.setText(_translate("DEMPropertiesWidget", "Transparency (%)", None))
        self.checkBox_TransparentBackground.setText(_translate("DEMPropertiesWidget", "Transparent background", None))
        self.checkBox_Shading.setText(_translate("DEMPropertiesWidget", "Enable shading", None))
        self.groupBox_Clip.setTitle(_translate("DEMPropertiesWidget", "Clip", None))
        self.checkBox_Clip.setText(_translate("DEMPropertiesWidget", "Clip DEM with polygon layer", None))
        self.groupBox_Accessories.setTitle(_translate("DEMPropertiesWidget", "&Sides and frame", None))
        self.checkBox_Sides.setText(_translate("DEMPropertiesWidget", "Build sides", None))
        self.checkBox_Frame.setText(_translate("DEMPropertiesWidget", "Build frame", None))

