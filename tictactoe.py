from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        
        # Initialize game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # Set up the window
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 350)
        
        # Create main vertical layout
        self.main_layout = QVBoxLayout()
        
        # Player turn label centered in a horizontal layout
        self.turn_label = QLabel(f"Player {self.current_player}'s Turn", self)
        self.turn_label.setAlignment(Qt.AlignCenter)
        self.turn_label.setStyleSheet("font-size: 18px; color: #306998;")  # Blue text color
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(self.turn_label)
        label_layout.addStretch()
        
        self.main_layout.addLayout(label_layout)
        
        # Grid layout for Tic-Tac-Toe buttons
        self.grid_layout = QGridLayout()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Create 3x3 grid of buttons
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda _, r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col] = button
                self.grid_layout.addWidget(button, row, col)
        
        self.main_layout.addLayout(self.grid_layout)
        
        # Reset button with color
        self.reset_button = QPushButton("Reset Game")
        self.reset_button.setStyleSheet("font-size: 16px; background-color: #ffd43b; color: black;")
        self.reset_button.clicked.connect(self.reset_game)
        self.main_layout.addWidget(self.reset_button)
        
        # Set the main layout
        self.setLayout(self.main_layout)
    
    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.buttons[row][col].setStyleSheet("color: #306998; font-size: 24px;")  # Blue for X
                self.buttons[row][col].setText("X")
            else:
                self.buttons[row][col].setStyleSheet("color: #ffd43b; font-size: 24px;")  # Yellow for O
                self.buttons[row][col].setText("O")
            winner = self.check_winner()
            if winner:
                self.turn_label.setText(f"Player {winner} wins!")
                self.turn_label.setStyleSheet("font-size: 18px; color: green;")  # Green for win message
                self.disable_buttons()
            elif all(self.board[r][c] != "" for r in range(3) for c in range(3)):
                self.turn_label.setText("It's a draw!")
                self.turn_label.setStyleSheet("font-size: 18px; color: orange;")  # Orange for draw message
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.setText(f"Player {self.current_player}'s Turn")
                self.turn_label.setStyleSheet(f"font-size: 18px; color: {'#306998' if self.current_player == 'X' else '#ffd43b'};")
    
    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None
    
    def disable_buttons(self):
        # Disable all buttons after a win or draw
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)
    
    def reset_game(self):
        # Reset the game board and UI elements
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.turn_label.setText(f"Player {self.current_player}'s Turn")
        self.turn_label.setStyleSheet("font-size: 18px; color: #306998;")  # Reset to blue
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
                self.buttons[row][col].setEnabled(True)
                self.buttons[row][col].setStyleSheet("font-size: 24px;")

# Run the application
app = QApplication(sys.argv)
window = TicTacToe()
window.show()
sys.exit(app.exec_())