from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
import os


class MyBrowser(QMainWindow):
    def __init__(self):
        super(MyBrowser,self).__init__()
        self.Browser = QWebEngineView()
        self.Browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.Browser)
        self.showMaximized()

# navigation
        nav = QToolBar()
        nav.setIconSize(QSize(30,30))
        self.addToolBar(nav)

        # backbutton
        back_btn = QAction(QIcon(os.path.join('icons','back.PNG')),"Back",self)
        back_btn.triggered.connect(self.Browser.back)
        nav.addAction(back_btn)

        # forward button
        fwd_btn = QAction(QIcon(os.path.join('icons','next.PNG')),"Next",self)
        fwd_btn.triggered.connect(self.Browser.forward)
        nav.addAction(fwd_btn)

        # reload button
        reload_btn = QAction(QIcon(os.path.join('icons','refresh.PNG')),"Reload",self)
        reload_btn.triggered.connect(self.Browser.reload)
        nav.addAction(reload_btn)

        #search bar
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.search)
        nav.addWidget(self.search_bar)

        # update url
        self.Browser.urlChanged.connect(self.update_url)

    def  update_url(self,url_update):
        self.search_bar.setText(url_update.toString()) 

    
    def search(self):
        url = self.search_bar.text()
        self.Browser.setUrl(QUrl(url))



exec_browser = QApplication(sys.argv)
QApplication.setApplicationDisplayName('Special Browser') 
main = MyBrowser()
exec_browser.exec()       