# Imports 
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QFileDialog, QSlider, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

# MY App

class AudioApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()

    

    


    # Settings 
    def settings(self):
        self.setWindowTitle("Aud-Just")
        self.setGeometry(800, 500, 600, 300)
        
    
    # Design
    def initUI(self):
        self.title = QLabel("Audio Adjuster")
        self.file_list = QListWidget()
        self.btn_open = QPushButton("Choose a file") 
        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_reset = QPushButton("Reset")

        self.slider = QSlider(Qt.Orientation.Horizontal)
        
        self.slider.setMinimum(50)
        self.slider.setMaximum(150)
        self.slider.setValue(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)

        # Create a Layout
        
        self.master = QVBoxLayout()
        row = QHBoxLayout()
        col1 = QVBoxLayout()
        col2 = QVBoxLayout()

        self.master.addWidget(self.title)
        self.master.addWidget(self.slider)

        col1.addWidget(self.file_list)
        col2.addWidget(self.btn_open)
        col2.addWidget(self.btn_play)
        col2.addWidget(self.btn_pause)
        col2.addWidget(self.btn_reset)

        row.addLayout(col1)
        row.addLayout(col2)

        self.master.addLayout(row)
        self.setLayout(self.master)





    # Event Handler

        


# Boilerplate code

if __name__ == "__main__":
    app = QApplication([])
    main = AudioApp()
    main.show()
    app.exec()
