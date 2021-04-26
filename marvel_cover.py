"""
Created on 2021/04/25
@author: cyr
@site: https://github.com/Doriskirsy
@description: define class of cover interface
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class marvel_cover(QMainWindow):

    def __init__(self):     # initialize
        super(marvel_cover, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        import params

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2319, 1491)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 开始按钮一
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(820, 1120, 241, 91))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(MainWindow.close)   # 关闭当前窗口
        self.pushButton.clicked.connect(self.skip)      # 触发跳转机制

        # 开始按钮二
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1240, 1120, 281, 91))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(MainWindow.close)  # 关闭当前窗口
        self.pushButton_2.clicked.connect(self.skip)  # 触发跳转机制

        # 封面图片
        self.cover_pic = QtWidgets.QLabel(self.centralwidget)
        self.cover_pic.setGeometry(QtCore.QRect(590, 200, 1161, 691))
        self.cover_pic.setText("")
        self.cover_pic.setPixmap(QtGui.QPixmap(params.Root + "/pics_rc/cover/marvel_cover.jpg"))
        self.cover_pic.setScaledContents(True)    # 自适应QLabel大小
        self.cover_pic.setObjectName("cover_pic")

        # 测试提示
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(660, 1300, 1031, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.notice.setFont(font)
        self.notice.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.notice.setLineWidth(5)
        self.notice.setMidLineWidth(2)
        self.notice.setObjectName("notice")

        # MBTI测试标题
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(870, 100, 621, 81))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")

        # 引导语
        self.instruction = QtWidgets.QLabel(self.centralwidget)
        self.instruction.setGeometry(QtCore.QRect(800, 970, 751, 91))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(14)
        self.instruction.setFont(font)
        self.instruction.setObjectName("instruction")

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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MBTI小测试"))
        self.pushButton.setText(_translate("MainWindow", "I\'m ready"))
        self.pushButton_2.setText(_translate("MainWindow", "我准备好了"))
        self.notice.setText(_translate("MainWindow", "测试须知：本测试结果仅作参考，如果测得准请赏作者一朵小红花"))
        self.title.setText(_translate("MainWindow", "性格测试——漫威篇"))
        self.instruction.setText(_translate("MainWindow", "来看一下你与哪个漫威人物最相似↓"))

    # 跳转至测试界面
    def skip(self, w):
        import params
        params.Round_now += 1
        if params.Round_now in params.Rounds_pic:       # 判断第一题是否是图片题
            from marvel_test_ import marvel_test_
            self.w = marvel_test_()     # 实例化marvel_test_.py中的marvel_test_类
            self.w.show()       # 显示窗口
        elif params.Round_now in params.Rounds_video:       # 判断第一题是否是视频题
            from marvel_test import marvel_test
            self.w = marvel_test()
            self.w.show()
