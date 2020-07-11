from PyQt5 import QtWidgets, QtCore
import sys
import subprocess
import form
import os
import platform
from string import Template


class Window(QtWidgets.QMainWindow, form.Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.process = QtCore.QProcess()
		self.log_path = './../log'
		self.main_path = 'Main_excel_parser.py'
		self.command = Template('python3 $main_script --test_mode $mode --config $path_to_config')
		self.pushButton.clicked.connect(lambda:self.on_start(self.main_path, self.config_path, self.mode))
		self.radioButton.toggled.connect(self.check1)
		self.radioButton_2.toggled.connect(self.check2)
		self.comboBox.activated.connect(self.on_combox)
		self.pushButton_2.clicked.connect(self.open_logs)

		for i in os.listdir('../designer/config'):
			self.comboBox.addItem(i)

		self.config_path = self.comboBox.currentText()


	def on_combox(self):
		self.config_path = self.comboBox.currentText()


	def on_start(self, main_path, config_path, mode):
		self.process.execute(self.command.substitute(main_script=self.main_path, mode=self.mode, path_to_config=self.config_path))
		# print(self.command.substitute(main_script=main_path, mode=mode, path_to_config=config_path))

	def check1(self):
		if self.radioButton.isChecked():
			self.mode = 'true'

	def check2(self):
		if self.radioButton_2.isChecked():
			self.mode = 'false'

	def open_logs(self):
		self.open_file(self.log_path)

	def open_file(self, path):
	    if platform.system() == "Windows":
	        os.startfile(path)
	    elif platform.system() == "Darwin":
	        subprocess.Popen(["open", path])
	    else:
	        subprocess.Popen(["xdg-open", path])

	def closeEvent(self, event):
		answer = QtWidgets.QMessageBox.question(self,
				"Question",
				"Exit?",
				QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
				QtWidgets.QMessageBox.No
			)

		if answer == QtWidgets.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = Window()
	w.show()
	sys.exit(app.exec_())
