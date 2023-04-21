import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time(hours):")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(["Miles", "Kilometers"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        # Add Widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        # Get distance and time from the input boxes
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        # Calculate average speed
        speed = distance / time

        # Check what user chose in the combo
        if self.combo.currentText() == 'Kilometers':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.combo.currentText() == 'Miles':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        # Display the result
        self.result_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
speedCalc = SpeedCalculator()
speedCalc.show()
sys.exit(app.exec())
