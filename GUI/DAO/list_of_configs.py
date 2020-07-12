from PyQt5 import QtCore
import requests as rq
import json


class GetListOfFiles(QtCore.QThread):
    task_done = QtCore.pyqtSignal(object)
    task_done_error = QtCore.pyqtSignal(object)

    def __init__(self, url) -> None:
        super().__init__()
        self.url = url

    def run(self) -> None:
        try:
            session = rq.Session()
            list_of_files = session.get(self.url + '/api/open').text
        except Exception as e:
            self.task_done_error.emit(e)
        else:
            self.task_done.emit(json.loads(list_of_files))
