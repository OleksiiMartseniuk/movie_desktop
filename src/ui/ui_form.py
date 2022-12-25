from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
        QGridLayout,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QPushButton,
        QRadioButton,
        QScrollArea,
        QSizePolicy,
        QSpacerItem,
        QStackedWidget,
        QVBoxLayout,
        QWidget
)
from src.config.settings import ICON_DIR


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(802, 600)
        Form.setStyleSheet(u"QWidget {\n"
        "	background-color:rgb(13, 23, 31);\n"
        "	border: none;\n"
        "}\n"
        "QPushButton#button_user {\n"
        "	border: none;\n"
        "	color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton#button_user:hover {\n"
        "	color: rgb(45, 202, 235);\n"
        "}\n"
        "QPushButton#button_user:pressed {\n"
        "	color: rgb(85, 0, 255);\n"
        "}\n"
        "")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_menu = QWidget(Form)
        self.widget_menu.setObjectName(u"widget_menu")
        self.widget_menu.setStyleSheet(u"QWidget {\n"
        "	background-color: rgb(20, 28, 37);\n"
        "}\n"
        "QPushButton {\n"
        "	border: none;\n"
        "	color: rgb(255, 255, 255);\n"
        "}\n"
        "QPushButton:hover {\n"
        "	color: rgb(45, 202, 235);\n"
        "	border-left: 2px solid rgb(45, 202, 235);\n"
        "}\n"
        "QPushButton:pressed {\n"
        "	color: rgb(85, 0, 255);\n"
        "}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_menu)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(40, 0, 40, 0)
        self.logo = QLabel(self.widget_menu)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(100, 100))
        logo = QPixmap(ICON_DIR.joinpath('movie_logo.png'))
        self.logo.setPixmap(logo)

        self.verticalLayout_4.addWidget(self.logo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.button_populat = QPushButton(self.widget_menu)
        self.button_populat.setObjectName(u"button_populat")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.button_populat.setFont(font)

        self.verticalLayout_4.addWidget(self.button_populat)

        self.button_top_rated = QPushButton(self.widget_menu)
        self.button_top_rated.setObjectName(u"button_top_rated")
        self.button_top_rated.setFont(font)

        self.verticalLayout_4.addWidget(self.button_top_rated)

        self.button_tremding = QPushButton(self.widget_menu)
        self.button_tremding.setObjectName(u"button_tremding")
        self.button_tremding.setFont(font)

        self.verticalLayout_4.addWidget(self.button_tremding)

        self.button_person = QPushButton(self.widget_menu)
        self.button_person.setObjectName(u"button_person")
        self.button_person.setFont(font)

        self.verticalLayout_4.addWidget(self.button_person)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.widget_menu, 0, 0, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 30, 50, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEdit_searh = QLineEdit(Form)
        self.lineEdit_searh.setObjectName(u"lineEdit_searh")

        self.horizontalLayout.addWidget(self.lineEdit_searh)

        self.button_user = QPushButton(Form)
        self.button_user.setObjectName(u"button_user")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.button_user.setFont(font1)

        self.horizontalLayout.addWidget(self.button_user)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(600, 300))
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setMidLineWidth(1)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"QWidget {\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(45, 202, 235);\n"
"}\n"
"QPushButton:pressed {\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	background-color: rgb(85, 0, 255);\n"
"	color: rgb(239, 239, 239);\n"
"}\n"
"QRadioButton::indicator\n"
"{\n"
"    image: none;\n"
"}\n"
"QRadioButton:unchecked {\n"
"	background-color:rgb(13, 23, 31);\n"
"	border: 1px solid #4a4a4a;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.page_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.radioButton = QRadioButton(self.page_1)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet(u"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.page_1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet(u"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;")

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 598, 489))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_card = QVBoxLayout()
        self.verticalLayout_card.setObjectName(u"verticalLayout_card")
        self.cart_image = QLabel(self.scrollAreaWidgetContents)
        self.cart_image.setObjectName(u"cart_image")
        self.cart_image.setMinimumSize(QSize(150, 225))
        self.cart_image.setMaximumSize(QSize(150, 225))
        self.cart_image.setStyleSheet(u"border-radius: 15px;\n"
"")

        self.verticalLayout_card.addWidget(self.cart_image)

        self.cart_title = QPushButton(self.scrollAreaWidgetContents)
        self.cart_title.setObjectName(u"cart_title")
        self.cart_title.setMaximumSize(QSize(150, 16777215))
        self.cart_title.setFont(font1)

        self.verticalLayout_card.addWidget(self.cart_title)

        self.cart_date = QLabel(self.scrollAreaWidgetContents)
        self.cart_date.setObjectName(u"cart_date")
        self.cart_date.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.cart_date.setFont(font2)
        self.cart_date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_card.addWidget(self.cart_date)


        self.gridLayout_2.addLayout(self.verticalLayout_card, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_1)
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.profile.setStyleSheet(u"QWidget {\n"
"	color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}\n"
"QLineEdit {\n"
"	border-bottom: 2px solid rgb(239, 239, 239);\n"
"	color: rgb(239, 239, 239);\n"
"	padding-bottom: 7px;\n"
"}\n"
"QLabel {\n"
"	color: rgb(85, 0, 255);\n"
"}\n"
"QPushButton {\n"
"	background-color: rgb(17, 57, 149);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(85, 0, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.profile)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.profile)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(350, 16777215))
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setItalic(False)
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.profile)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(350, 16777215))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        self.label.setFont(font4)
        self.label.setWordWrap(False)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit_username = QLineEdit(self.profile)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMaximumSize(QSize(350, 16777215))
        font5 = QFont()
        font5.setPointSize(12)
        self.lineEdit_username.setFont(font5)
        self.lineEdit_username.setMaxLength(20)

        self.verticalLayout.addWidget(self.lineEdit_username)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.label_3 = QLabel(self.profile)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(350, 16777215))
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_password = QLineEdit(self.profile)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setMaximumSize(QSize(350, 16777215))
        self.lineEdit_password.setFont(font5)
        self.lineEdit_password.setMaxLength(20)

        self.verticalLayout.addWidget(self.lineEdit_password)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.label_4 = QLabel(self.profile)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(350, 16777215))
        self.label_4.setFont(font4)

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_confirm_password = QLineEdit(self.profile)
        self.lineEdit_confirm_password.setObjectName(u"lineEdit_confirm_password")
        self.lineEdit_confirm_password.setMaximumSize(QSize(350, 16777215))
        self.lineEdit_confirm_password.setFont(font5)
        self.lineEdit_confirm_password.setMaxLength(20)

        self.verticalLayout.addWidget(self.lineEdit_confirm_password)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.error_1 = QScrollArea(self.profile)
        self.error_1.setObjectName(u"error_1")
        self.error_1.setMinimumSize(QSize(0, 90))
        self.error_1.setMaximumSize(QSize(350, 16777215))
        self.error_1.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.error_1.setStyleSheet(u"")
        self.error_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 350, 90))
        self.scrollAreaWidgetContents_3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.error_1.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.error_1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.pushButton_save = QPushButton(self.profile)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(350, 40))
        self.pushButton_save.setMaximumSize(QSize(350, 16777215))
        self.pushButton_save.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_save)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.profile)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.logo.setText(QCoreApplication.translate("Form", u"Icon", None))
        self.button_populat.setText(QCoreApplication.translate("Form", u"Popular", None))
        self.button_top_rated.setText(QCoreApplication.translate("Form", u"Top Rated", None))
        self.button_tremding.setText(QCoreApplication.translate("Form", u"Trending", None))
        self.button_person.setText(QCoreApplication.translate("Form", u"Person", None))
        self.button_user.setText(QCoreApplication.translate("Form", u"UserName", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Movie", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"TV", None))
        self.cart_image.setText(QCoreApplication.translate("Form", u"imaga", None))
        self.cart_title.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.cart_date.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Profile", None))
        self.label.setText(QCoreApplication.translate("Form", u"User Name", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"New passwod", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Confirm password", None))
        self.pushButton_save.setText(QCoreApplication.translate("Form", u"SAVE", None))
    # retranslateUi

