from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTabWidget,
    QVBoxLayout,
    QWidget
)
from settings import ICON_DIR


class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(400, 650)
        Auth.setStyleSheet(u"QWidget {\n"
                           "	background-color: rgb(26, 22, 31);\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab { \n"
                           "	border: none;\n"
                           "	width: 140px;\n"
                           "	height: 40px;\n"
                           "}\n"
                           "\n"
                           "QTabBar::tab:selected{\n"
                           "	border-bottom: 2px solid rgb(17, 57, 149);\n"
                           "}\n"
                           "\n"
                           "QPushButton {\n"
                           "	background-color: rgb(17, 57, 149);\n"
                           "	color: rgb(255, 255, 255);\n"
                           "	border-radius: 15px;\n"
                           "}\n"
                           "QPushButton:hover {\n"
                           "	font: bold;\n"
                           "	background-color: rgb(102, 128, 192);\n"
                           "	color: black;\n"
                           "}\n"
                           "QPushButton:pressed {\n"
                           "	background-color: rgb(85, 85, 0);\n"
                           "	color: rgb(255, 255, 255);\n"
                           " 	background-color: rgb(102, 128, 192);\n"
                           "}\n"
                           "QScrollArea {\n"
                           "	border: none;\n"
                           "}\n"
                           "\n"
                           "QScrollBar::handle:vertical{\n"
                           "	background-color: rgb(26, 22, 31);\n"
                           "	border-right: 2px solid  rgb(17, 57, 149);\n"
                           "}\n"
                           "\n"
                           "QScrollBar::add-line:vertical{\n"
                           "	background-color: rgb(26, 22, 31);\n"
                           "}\n"
                           "QScrollBar::sub-line:vertical{\n"
                           "	background-color: rgb(26, 22, 31);\n"
                           "}\n"
                           "QLabel#exit{\n"
                           "	color: rgb(255, 255, 255);\n"
                           "}\n"
                           "QLabel#exit"
                           ":hover{\n"
                           "	color: rgb(17, 57, 149);\n"
                           "}")
        self.tabWidget = QTabWidget(Auth)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(60, 150, 280, 440))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
                                     "	border: none;\n"
                                     "}\n"
                                     "QLineEdit {\n"
                                     "	border: none;\n"
                                     "	border-bottom: 2px solid rgb(239, 239, 239);\n"
                                     "	color: rgb(239, 239, 239);\n"
                                     "	padding-bottom: 7px;\n"
                                     "}\n"
                                     "")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(0, 0))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_sing_in = QWidget()
        self.tab_sing_in.setObjectName(u"tab_sing_in")
        self.username_1 = QLineEdit(self.tab_sing_in)
        self.username_1.setObjectName(u"username_1")
        self.username_1.setGeometry(QRect(0, 60, 280, 30))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.username_1.setFont(font1)
        self.username_1.setStyleSheet(u"")
        self.username_1.setMaxLength(20)
        self.password_1 = QLineEdit(self.tab_sing_in)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setGeometry(QRect(0, 130, 280, 30))
        self.password_1.setFont(font1)
        self.password_1.setStyleSheet(u"")
        self.password_1.setMaxLength(20)
        self.password_1.setEchoMode(QLineEdit.Password)
        self.password_1.setDragEnabled(False)
        self.password_1.setReadOnly(False)
        self.sing_in = QPushButton(self.tab_sing_in)
        self.sing_in.setObjectName(u"sing_in")
        self.sing_in.setGeometry(QRect(0, 350, 280, 40))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        self.sing_in.setFont(font2)
        self.sing_in.setStyleSheet(u"")
        self.error_1 = QScrollArea(self.tab_sing_in)
        self.error_1.setObjectName(u"error_1")
        self.error_1.setGeometry(QRect(0, 180, 280, 90))
        self.error_1.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.error_1.setStyleSheet(u"")
        self.error_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 280, 90))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.error_1.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_sing_in, "")
        self.tab_sing_up = QWidget()
        self.tab_sing_up.setObjectName(u"tab_sing_up")
        self.password_2 = QLineEdit(self.tab_sing_up)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(0, 130, 280, 30))
        self.password_2.setFont(font1)
        self.password_2.setStyleSheet(u"")
        self.password_2.setMaxLength(20)
        self.password_2.setEchoMode(QLineEdit.Password)
        self.username_2 = QLineEdit(self.tab_sing_up)
        self.username_2.setObjectName(u"username_2")
        self.username_2.setGeometry(QRect(0, 60, 280, 30))
        self.username_2.setFont(font1)
        self.username_2.setStyleSheet(u"")
        self.username_2.setMaxLength(20)
        self.sing_up = QPushButton(self.tab_sing_up)
        self.sing_up.setObjectName(u"sing_up")
        self.sing_up.setGeometry(QRect(0, 350, 280, 40))
        self.sing_up.setFont(font2)
        self.sing_up.setStyleSheet(u"")
        self.confirm_password = QLineEdit(self.tab_sing_up)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setGeometry(QRect(0, 200, 280, 30))
        self.confirm_password.setFont(font1)
        self.confirm_password.setStyleSheet(u"")
        self.confirm_password.setMaxLength(20)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.error_2 = QScrollArea(self.tab_sing_up)
        self.error_2.setObjectName(u"error_2")
        self.error_2.setGeometry(QRect(0, 250, 281, 90))
        self.error_2.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.error_2.setStyleSheet(u"")
        self.error_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 281, 90))
        self.scrollAreaWidgetContents.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.error_2.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_sing_up, "")
        self.logo = QLabel(Auth)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(150, 30, 100, 100))
        logo = QPixmap(ICON_DIR.joinpath('movie_logo.png'))
        self.logo.setPixmap(logo)
        self.exit = QLabel(Auth)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(60, 600, 171, 20))
        font3 = QFont()
        font3.setFamilies([u"Archivo Medium"])
        font3.setPointSize(10)
        self.exit.setFont(font3)

        self.retranslateUi(Auth)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"Auth", None))
        self.username_1.setPlaceholderText(QCoreApplication.translate("Auth", u" User Name", None))
        self.password_1.setPlaceholderText(QCoreApplication.translate("Auth", u" Password", None))
        self.sing_in.setText(QCoreApplication.translate("Auth", u"SING IN", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sing_in), QCoreApplication.translate("Auth", u"Sing in", None))
        self.password_2.setPlaceholderText(QCoreApplication.translate("Auth", u" Password", None))
        self.username_2.setPlaceholderText(QCoreApplication.translate("Auth", u" User Name", None))
        self.sing_up.setText(QCoreApplication.translate("Auth", u"SING UP", None))
        self.confirm_password.setText("")
        self.confirm_password.setPlaceholderText(QCoreApplication.translate("Auth", u" Confirm Password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sing_up), QCoreApplication.translate("Auth", u"Sing up", None))
        self.logo.setText("")
        self.exit.setText(QCoreApplication.translate("Auth", u"Click here to sign out", None))
    # retranslateUi
