"""
Created on 2021/04/25
@author: cyr
@site: https://github.com/Doriskirsy
@description: define class of result interface
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class marvel_result(QMainWindow):

    def __init__(self):     # initialize
        super(marvel_result, self).__init__()
        import params
        import util
        util.cal_MBTI()     # 计算测试出的MBTI人格类型结果
        params.person = params.MBTI2person[params.MBTI]     # 该类型对应的漫威人物
        # params.url = "https://psychology.wikia.org/wiki/" + params.MBTI
        params.url = "https://www.16personalities.com/" + params.MBTI.lower() + "-personality"      # 相关网站url
        self.setupUi(self)

    def setupUi(self, MainWindow):
        import params

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2319, 1491)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 展示对应的漫威人物图片
        self.personpic = QtWidgets.QLabel(self.centralwidget)
        self.personpic.setGeometry(QtCore.QRect(770, 180, 771, 701))
        self.personpic.setText("")
        self.personpic.setPixmap(QtGui.QPixmap(params.Root + "/pics_rc/result/" + params.person2pic[params.person] + ".jpg"))
        self.personpic.setScaledContents(True)  # 自适应QLabel大小
        self.personpic.setObjectName("personpic")

        self.formLayout = QtWidgets.QFormLayout(self.personpic)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # 用户可选择重新进行测试
        self.restartButton = QtWidgets.QPushButton(self.centralwidget)
        self.restartButton.setGeometry(QtCore.QRect(1060, 1290, 181, 71))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.restartButton.setFont(font)
        self.restartButton.setObjectName("restartButton")
        self.restartButton.clicked.connect(MainWindow.close)        # 关闭当前页面
        self.restartButton.clicked.connect(self.restart)        # 触发重测机制

        self.foreword = QtWidgets.QLabel(self.centralwidget)
        self.foreword.setGeometry(QtCore.QRect(500, 80, 361, 61))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.foreword.setFont(font)
        self.foreword.setObjectName("foreword")

        # 对应的漫威人物名字
        self.personname = QtWidgets.QLabel(self.centralwidget)
        self.personname.setGeometry(QtCore.QRect(1020, 910, 261, 91))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.personname.setFont(font)
        self.personname.setObjectName("personname")

        # MBTI类型
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(1060, 1000, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.description.setFont(font)
        self.description.setObjectName("description")

        # 相关信息的url
        self.url = QtWidgets.QLabel(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(770, 1070, 811, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.url.setFont(font)
        self.url.setObjectName("description")
        self.url.setText('<a href={}>点击查看更多信息</a>'.format(params.url))
        self.url.setOpenExternalLinks(True)     # 设置超链接
        self.url.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)      # 双击可选中文本

        # 一个随便的label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(770, 1140, 771, 51))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2319, 45))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        import params
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MBTI小测试"))
        self.restartButton.setText(_translate("MainWindow", "再来一次"))
        self.foreword.setText(_translate("MainWindow", "和你最像的漫威人物是："))
        self.personname.setText(_translate("MainWindow", params.person))
        self.description.setText(_translate("MainWindow", params.MBTI + "人格"))
        self.label.setText(_translate("MainWindow", "感谢使用"))

    # 重新进行测试
    def restart(self, w):
        # 相关参数初始化，并跳转至封面
        import params
        import copy
        params.Round_now = 0
        params.Scores = copy.deepcopy(params.Scores_0)
        params.MBTI = ''
        params.person = ''
        from marvel_cover import marvel_cover
        self.w = marvel_cover()
        self.w.show()
