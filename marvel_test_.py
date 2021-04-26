"""
Created on 2021/04/25
@author: cyr
@site: https://github.com/Doriskirsy
@description: define class of test interface which contains one picture
"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QMessageBox


class marvel_test_(QMainWindow):

    def __init__(self):     # initialize
        super(marvel_test_, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        import params

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2319, 1491)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 问题的文本
        self.question = QtWidgets.QLabel(self.centralwidget)
        self.question.setGeometry(QtCore.QRect(420, 80, 1511, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(16)
        self.question.setFont(font)
        self.question.setObjectName("question")

        # 进度条，显示当前题号和总题数
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        #self.progressBar.setStyleSheet("QProgressBar::chunk {background-color: #007FFF;}")     # 改变样式
        self.progressBar.setGeometry(QtCore.QRect(990, 1310, 361, 38))
        font = QtGui.QFont()
        font.setFamily("黑体")
        self.progressBar.setFont(font)
        self.progressBar.setMaximum(params.Rounds)            # 进度最大值，即总题数
        self.progressBar.setProperty("value", params.Round_now)      # 进度当前值，即当前题号
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")

        # 利用QLabel显示图片
        self.picarea = QtWidgets.QLabel(self.centralwidget)
        self.picarea.setGeometry(QtCore.QRect(710, 180, 961, 701))
        self.picarea.setText("")
        # self.picarea.setPixmap(QtGui.QPixmap(params.Add_pic[params.Round_now]))       # 显示本地图片
        self.picarea.setScaledContents(True)  # 自适应QLabel大小
        self.picarea.setObjectName("picarea")

        self.formLayout = QtWidgets.QFormLayout(self.picarea)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(580, 980, 1031, 231))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        # 选项A描述
        self.optionA = QtWidgets.QLabel(self.groupBox)
        self.optionA.setGeometry(QtCore.QRect(10, 30, 731, 81))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.optionA.setFont(font)
        self.optionA.setObjectName("optionA")

        # 选项B描述
        self.optionB = QtWidgets.QLabel(self.groupBox)
        self.optionB.setGeometry(QtCore.QRect(10, 120, 731, 81))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.optionB.setFont(font)
        self.optionB.setObjectName("optionB")

        # radio按钮A
        self.radioA = QtWidgets.QRadioButton(self.groupBox)
        self.radioA.setGeometry(QtCore.QRect(970, 50, 31, 34))
        self.radioA.setText("")
        self.radioA.setObjectName("radioA")

        # radio按钮B
        self.radioB = QtWidgets.QRadioButton(self.groupBox)
        self.radioB.setGeometry(QtCore.QRect(970, 140, 31, 41))
        self.radioB.setText("")
        self.radioB.setObjectName("radioB")

        # 将radio按钮A和B组合成单选按钮组
        self.bg = QButtonGroup(self)
        self.bg.addButton(self.radioA, 1)       # 选项A对应索引值1
        self.bg.addButton(self.radioB, 2)       # 选项B对应索引值2
        self.bg.buttonClicked.connect(self.rb_clicked)       # 监听按钮

        # 被选中的radio按钮，没有选中则为0
        self.chosen = 0

        # 当用户确定好选项后，点击确认按钮进入下一题
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(1670, 1060, 141, 71))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(10)
        self.confirmButton.setFont(font)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.skip)       # 触发跳转机制
        # self.confirmButton.clicked.connect(MainWindow.close)

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
        self.question.setText(_translate("MainWindow", params.Questions[params.Round_now - 1]))     # 设置本题题目的文本
        self.progressBar.setFormat(_translate("MainWindow", "%v/%m"))       # %v为当前值，%m为最大值
        self.optionA.setText(_translate("MainWindow", params.OptionAtexts[params.Round_now - 1]))       # 设置选项A的文本描述
        self.optionB.setText(_translate("MainWindow", params.OptionBtexts[params.Round_now - 1]))       # 设置选项B的文本描述
        self.confirmButton.setText(_translate("MainWindow", "确定"))

    # 单选按钮监听
    def rb_clicked(self):
        sender = self.sender()
        if sender == self.bg:       # 判断信号发出者是否为radio按钮组
            if self.bg.checkedId() == 1:
                self.chosen = 'A'
            elif self.bg.checkedId() == 2:
                self.chosen = 'B'

    # 跳转页面
    def skip(self, w):
        if self.chosen == 0:        # 首先判断用户是否选了某一选项
            QMessageBox.information(self, '???', '你还没有选呢')      # 弹出提示框
        elif self.chosen == 'A' or self.chosen == 'B':
            import params
            import util
            util.add_score(self.chosen)     # 累加该题得分
            params.Round_now += 1
            if params.Round_now in params.Rounds_pic:       # 判断下一题是否是图片题
                from marvel_test_ import marvel_test_
                self.w = marvel_test_()     # 实例化marvel_test_.py中的marvel_test_类
                self.w.show()       # 显示窗口
            elif params.Round_now in params.Rounds_video:       # 判断下一题是否是视频题
                from marvel_test import marvel_test
                self.w = marvel_test()
                self.w.show()
            else:       # 所有题做完，转入结果界面
                from marvel_result import marvel_result
                self.w = marvel_result()
                self.w.show()
            self.close()        # 关闭当前界面
