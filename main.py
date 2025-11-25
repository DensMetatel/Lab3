import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView
from field import FieldMonopoly

class MonopolyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Монополия")
        self.resize(600, 600)

        # Создаём сцену поля из отдельного файла
        self.scene = FieldMonopoly()
        self.view = QGraphicsView(self.scene, self)
        self.setCentralWidget(self.view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonopolyWindow()
    window.show()
    sys.exit(app.exec())
