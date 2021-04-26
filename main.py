"""
Created on 2021/04/25
@author: cyr
@site: https://github.com/Doriskirsy
@description: launch a MBTI test GUI
"""

import sys
from marvel_cover import *
from PyQt5.QtWidgets import QApplication


import sys
if __name__ == '__main__':
   app = QApplication(sys.argv)
   ui = marvel_cover()     # 创建PyQt设计的窗体对象
   ui.show()
   sys.exit(app.exec_())      # 程序关闭时退出进程
