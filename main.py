from ast import Delete
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        self = uic.loadUi('interface.ui', self)
        self.show()

        self.setWindowTitle("Secure Text Editor")

        ######### file ######### 
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionExit.triggered.connect(exit)

        ######### edit ######### 
        self.actionUndo.triggered.connect(self.undo_Text)
        self.actionCut.triggered.connect(self.cut_Text)
        self.actionCopy.triggered.connect(self.copy_Text)
        self.actionPase.triggered.connect(self.paste_Text)
        self.actionDelete.triggered.connect(self.delete_Text)

        ######### option ######### 
        self.action8.triggered.connect(lambda: self.change_size(8))
        self.action9.triggered.connect(lambda: self.change_size(9))
        self.action10.triggered.connect(lambda: self.change_size(10))
        self.action11.triggered.connect(lambda: self.change_size(11))
        self.action12.triggered.connect(lambda: self.change_size(12))
        self.action14.triggered.connect(lambda: self.change_size(14))
        self.action16.triggered.connect(lambda: self.change_size(16))
        self.action18.triggered.connect(lambda: self.change_size(18))
        self.action20.triggered.connect(lambda: self.change_size(20))
        self.action22.triggered.connect(lambda: self.change_size(22))
        self.action24.triggered.connect(lambda: self.change_size(24))
        self.action26.triggered.connect(lambda: self.change_size(26))
        self.action28.triggered.connect(lambda: self.change_size(28))
        self.action36.triggered.connect(lambda: self.change_size(36))
        self.action48.triggered.connect(lambda: self.change_size(48))
        self.action72.triggered.connect(lambda: self.change_size(72))
        
#  OPEN WITH AUTO DECRYPTION #
    def open_file(self):
        options =QFileDialog.Options()
        filename, _ =QFileDialog.getOpenFileName(self,"Open File","","Text Files (*.txt);;Python Files (*.py)",options=options )
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

# SAVE WITH AUTO ENCRYPTION #
    def save_file(self):
        options =QFileDialog.Options()
        filename, _ =QFileDialog.getSaveFileName(self,"Save File","","Text Files (*.txt);;ALL Files (*)",options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

# EXIT PROGRAM #
    def closeEvent(self,event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"),QMessageBox.YesRole)
        dialog.addButton(QPushButton("No"),QMessageBox.NoRole)
        dialog.addButton(QPushButton("Cancel"),QMessageBox.RejectRole)
        answer =dialog.exec_()
        if answer ==0:
            self.save_file()
            event.accept
        elif answer==2:
            event.ignore()

# UNDO #
    def undo_Text(self):
        self.plainTextEdit.undo()

# CUT TEXT #
    def cut_Text(self):
        self.plainTextEdit.cut()

# COPY TEXT #
    def copy_Text(self):
        self.plainTextEdit.copy()
        
# PASTE TEXT #
    def paste_Text(self):
        self.plainTextEdit.paste()

# DELETE #
    def delete_Text(self):
        self.plainTextEdit.clear()

#  CHANGE FONT SIZE #
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial",size))

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
