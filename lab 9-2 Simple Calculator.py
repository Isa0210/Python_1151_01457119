import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class SimpleCalculator(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("簡易計算機")
        self.setMinimumWidth(380)
        self._build_ui()

    def _build_ui(self) -> None:
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(10)

        # 第一個數字
        row1 = QHBoxLayout()
        lbl_num1 = QLabel("第一個數字：")
        lbl_num1.setFixedWidth(90)
        self.input_num1 = QLineEdit()
        self.input_num1.setPlaceholderText("輸入整數、小數或負數")
        row1.addWidget(lbl_num1)
        row1.addWidget(self.input_num1)
        main_layout.addLayout(row1)

        # 第二個數字
        row2 = QHBoxLayout()
        lbl_num2 = QLabel("第二個數字：")
        lbl_num2.setFixedWidth(90)
        self.input_num2 = QLineEdit()
        self.input_num2.setPlaceholderText("輸入整數、小數或負數")
        row2.addWidget(lbl_num2)
        row2.addWidget(self.input_num2)
        main_layout.addLayout(row2)

        # 四則運算按鈕列（+、-、×、÷）
        op_layout = QHBoxLayout()
        op_layout.setSpacing(8)

        operations = [
            ("+", "+"),
            ("-", "-"),
            ("×", "*"),
            ("÷", "/"),
        ]
        for label_text, op_symbol in operations:
            btn = QPushButton(label_text)
            btn.setMinimumHeight(34)
            btn.clicked.connect(lambda _checked=False, op=op_symbol: self.calculate(op))
            op_layout.addWidget(btn)

        main_layout.addLayout(op_layout)

        # 計算結果顯示
        self.lbl_result = QLabel("計算結果：")
        self.lbl_result.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        main_layout.addWidget(self.lbl_result)

        # 清除按鈕
        self.btn_clear = QPushButton("清除")
        self.btn_clear.setMinimumHeight(34)
        self.btn_clear.clicked.connect(self.clear_all)
        main_layout.addWidget(self.btn_clear)

        self.setLayout(main_layout)

    def _parse_operands(self) -> tuple[float, float] | None:
        s1 = self.input_num1.text().strip()
        s2 = self.input_num2.text().strip()

        if not s1 or not s2:
            QMessageBox.warning(self, "輸入錯誤", "請完整輸入兩個數字！")
            return None

        try:
            n1 = float(s1)
            n2 = float(s2)
            return n1, n2
        except ValueError:
            QMessageBox.warning(self, "輸入錯誤", "請輸入有效的數字（整數、小數或負數）！")
            return None

    @staticmethod
    def _format_number(val: float) -> str:
        # 避免浮點數誤差如 -0.0
        if val == 0:
            val = 0.0
        # 若為整數值則以整數顯示（例如 176.0 -> 176），否則保留適當小數
        if val.is_integer():
            return str(int(val))
        return f"{val:.6g}"

    def calculate(self, op: str) -> None:
        parsed = self._parse_operands()
        if parsed is None:
            return

        n1, n2 = parsed

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            if n2 == 0:
                QMessageBox.critical(self, "運算錯誤", "除數不能為零！")
                return
            result = n1 / n2
        else:
            return

        self.lbl_result.setText(f"計算結果：{self._format_number(result)}")

    def clear_all(self) -> None:
        self.input_num1.clear()
        self.input_num2.clear()
        self.lbl_result.setText("計算結果：")
        self.input_num1.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleCalculator()
    window.show()
    sys.exit(app.exec())