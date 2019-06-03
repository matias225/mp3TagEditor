# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/mainWindows.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777115))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPrev = QtWidgets.QPushButton(self.centralwidget)
        self.btnPrev.setGeometry(QtCore.QRect(76, 30, 61, 41))
        self.btnPrev.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/iconos/images/media-skip-forward-rtl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPrev.setIcon(icon)
        self.btnPrev.setIconSize(QtCore.QSize(32, 32))
        self.btnPrev.setObjectName("btnPrev")
        self.btnPlay = QtWidgets.QPushButton(self.centralwidget)
        self.btnPlay.setGeometry(QtCore.QRect(130, 30, 51, 41))
        self.btnPlay.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/iconos/images/media-playback-start.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPlay.setIcon(icon1)
        self.btnPlay.setIconSize(QtCore.QSize(32, 32))
        self.btnPlay.setObjectName("btnPlay")
        self.btnNext = QtWidgets.QPushButton(self.centralwidget)
        self.btnNext.setGeometry(QtCore.QRect(280, 30, 51, 41))
        self.btnNext.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/iconos/images/media-skip-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnNext.setIcon(icon2)
        self.btnNext.setIconSize(QtCore.QSize(32, 32))
        self.btnNext.setObjectName("btnNext")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(180, 30, 51, 41))
        self.btnPause.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/iconos/images/media-playback-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon3)
        self.btnPause.setIconSize(QtCore.QSize(32, 32))
        self.btnPause.setObjectName("btnPause")
        self.btnRandom = QtWidgets.QPushButton(self.centralwidget)
        self.btnRandom.setGeometry(QtCore.QRect(350, 30, 61, 41))
        self.btnRandom.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/iconos/images/media-playlist-shuffle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRandom.setIcon(icon4)
        self.btnRandom.setIconSize(QtCore.QSize(32, 32))
        self.btnRandom.setObjectName("btnRandom")
        self.lcdCurrentTime = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdCurrentTime.setGeometry(QtCore.QRect(30, 80, 64, 23))
        self.lcdCurrentTime.setObjectName("lcdCurrentTime")
        self.lcdDuration = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdDuration.setGeometry(QtCore.QRect(370, 80, 64, 23))
        self.lcdDuration.setObjectName("lcdDuration")
        self.progressTimeBar = QtWidgets.QSlider(self.centralwidget)
        self.progressTimeBar.setGeometry(QtCore.QRect(110, 80, 241, 20))
        self.progressTimeBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressTimeBar.setObjectName("progressTimeBar")
        self.btnVolume = QtWidgets.QPushButton(self.centralwidget)
        self.btnVolume.setGeometry(QtCore.QRect(510, 40, 51, 41))
        self.btnVolume.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/iconos/images/audio-volume-medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVolume.setIcon(icon5)
        self.btnVolume.setIconSize(QtCore.QSize(32, 32))
        self.btnVolume.setObjectName("btnVolume")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(500, 180, 281, 381))
        self.tableView.setObjectName("tableView")
        self.lblListTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblListTitle.setGeometry(QtCore.QRect(500, 150, 131, 17))
        self.lblListTitle.setObjectName("lblListTitle")
        self.imgCover = QtWidgets.QLabel(self.centralwidget)
        self.imgCover.setGeometry(QtCore.QRect(20, 180, 141, 141))
        self.imgCover.setText("")
        self.imgCover.setPixmap(QtGui.QPixmap(":/iconos/images/default_cover.png"))
        self.imgCover.setScaledContents(True)
        self.imgCover.setObjectName("imgCover")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(200, 200, 271, 21))
        self.titleEdit.setObjectName("titleEdit")
        self.artistEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.artistEdit.setGeometry(QtCore.QRect(200, 250, 271, 21))
        self.artistEdit.setObjectName("artistEdit")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(200, 180, 54, 17))
        self.lblTitle.setObjectName("lblTitle")
        self.lblArtist = QtWidgets.QLabel(self.centralwidget)
        self.lblArtist.setGeometry(QtCore.QRect(200, 230, 54, 17))
        self.lblArtist.setObjectName("lblArtist")
        self.lblYear = QtWidgets.QLabel(self.centralwidget)
        self.lblYear.setGeometry(QtCore.QRect(210, 330, 54, 17))
        self.lblYear.setObjectName("lblYear")
        self.yearEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yearEdit.setGeometry(QtCore.QRect(200, 350, 71, 21))
        self.yearEdit.setObjectName("yearEdit")
        self.lblAlbum = QtWidgets.QLabel(self.centralwidget)
        self.lblAlbum.setGeometry(QtCore.QRect(200, 280, 54, 17))
        self.lblAlbum.setObjectName("lblAlbum")
        self.albumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.albumEdit.setGeometry(QtCore.QRect(200, 300, 271, 21))
        self.albumEdit.setObjectName("albumEdit")
        self.lblComposer = QtWidgets.QLabel(self.centralwidget)
        self.lblComposer.setGeometry(QtCore.QRect(200, 430, 71, 17))
        self.lblComposer.setObjectName("lblComposer")
        self.lblGenre = QtWidgets.QLabel(self.centralwidget)
        self.lblGenre.setGeometry(QtCore.QRect(200, 380, 54, 17))
        self.lblGenre.setObjectName("lblGenre")
        self.lblComment = QtWidgets.QLabel(self.centralwidget)
        self.lblComment.setGeometry(QtCore.QRect(200, 480, 71, 17))
        self.lblComment.setObjectName("lblComment")
        self.genreEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.genreEdit.setGeometry(QtCore.QRect(200, 400, 271, 21))
        self.genreEdit.setObjectName("genreEdit")
        self.composerEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.composerEdit.setGeometry(QtCore.QRect(200, 450, 271, 21))
        self.composerEdit.setObjectName("composerEdit")
        self.btnEdit = QtWidgets.QPushButton(self.centralwidget)
        self.btnEdit.setGeometry(QtCore.QRect(50, 430, 87, 29))
        self.btnEdit.setObjectName("btnEdit")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(50, 480, 87, 29))
        self.btnSave.setObjectName("btnSave")
        self.commentEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.commentEdit.setGeometry(QtCore.QRect(200, 500, 271, 41))
        self.commentEdit.setObjectName("commentEdit")
        self.trackEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.trackEdit.setGeometry(QtCore.QRect(310, 350, 101, 21))
        self.trackEdit.setObjectName("trackEdit")
        self.lblTrack = QtWidgets.QLabel(self.centralwidget)
        self.lblTrack.setGeometry(QtCore.QRect(310, 330, 101, 17))
        self.lblTrack.setObjectName("lblTrack")
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setGeometry(QtCore.QRect(230, 30, 51, 41))
        self.btnStop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/iconos/images/media-playback-stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon6)
        self.btnStop.setIconSize(QtCore.QSize(32, 32))
        self.btnStop.setObjectName("btnStop")
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setGeometry(QtCore.QRect(580, 50, 160, 17))
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.btnPrev.raise_()
        self.btnPlay.raise_()
        self.btnNext.raise_()
        self.btnPause.raise_()
        self.btnRandom.raise_()
        self.lcdCurrentTime.raise_()
        self.lcdDuration.raise_()
        self.progressTimeBar.raise_()
        self.btnVolume.raise_()
        self.tableView.raise_()
        self.imgCover.raise_()
        self.titleEdit.raise_()
        self.artistEdit.raise_()
        self.lblTitle.raise_()
        self.lblArtist.raise_()
        self.lblYear.raise_()
        self.yearEdit.raise_()
        self.lblAlbum.raise_()
        self.albumEdit.raise_()
        self.lblComposer.raise_()
        self.lblGenre.raise_()
        self.lblComment.raise_()
        self.genreEdit.raise_()
        self.composerEdit.raise_()
        self.lblListTitle.raise_()
        self.btnEdit.raise_()
        self.btnSave.raise_()
        self.commentEdit.raise_()
        self.trackEdit.raise_()
        self.lblTrack.raise_()
        self.btnStop.raise_()
        self.volumeSlider.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuSalir = QtWidgets.QMenu(self.menubar)
        self.menuSalir.setObjectName("menuSalir")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnAddListMenu = QtWidgets.QAction(MainWindow)
        self.btnAddListMenu.setObjectName("btnAddListMenu")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionPlay = QtWidgets.QAction(MainWindow)
        self.actionPlay.setObjectName("actionPlay")
        self.btnAddFolderListMenu = QtWidgets.QAction(MainWindow)
        self.btnAddFolderListMenu.setObjectName("btnAddFolderListMenu")
        self.menuArchivo.addAction(self.btnAddListMenu)
        self.menuArchivo.addAction(self.btnAddFolderListMenu)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuSalir.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblListTitle.setText(_translate("MainWindow", "Lista de Reproduccion"))
        self.lblTitle.setText(_translate("MainWindow", "Título"))
        self.lblArtist.setText(_translate("MainWindow", "Artista"))
        self.lblYear.setText(_translate("MainWindow", "Año"))
        self.lblAlbum.setText(_translate("MainWindow", "Album"))
        self.lblComposer.setText(_translate("MainWindow", "Compositor"))
        self.lblGenre.setText(_translate("MainWindow", "Género"))
        self.lblComment.setText(_translate("MainWindow", "Comentario"))
        self.btnEdit.setText(_translate("MainWindow", "PushButton"))
        self.btnSave.setText(_translate("MainWindow", "PushButton"))
        self.lblTrack.setText(_translate("MainWindow", "Número de pista"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuSalir.setTitle(_translate("MainWindow", "About"))
        self.btnAddListMenu.setText(_translate("MainWindow", "Agregar a la lista"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionPlay.setText(_translate("MainWindow", "Play"))
        self.btnAddFolderListMenu.setText(_translate("MainWindow", "Agregar carpeta"))


from . import images_rc
