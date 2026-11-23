import sys
from dataclasses import dataclass
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QLabel,
    QMessageBox,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)


@dataclass(frozen=True)
class Question:
    prompt: str
    options: dict[str, str]  # {"A": "...", "B": "...", "C": "...", "D": "..."}
    answer: str


QUIZ_QUESTIONS: list[Question] = [
    Question(
        prompt="在 Python 中，下列哪一個關鍵字用於定義函式？",
        options={
            "A": "function",
            "B": "def",
            "C": "func",
            "D": "define",
        },
        answer="B",
    ),
    Question(
        prompt="下列哪一種資料型態在 Python 中是不可變（Immutable）的？",
        options={
            "A": "list",
            "B": "dict",
            "C": "set",
            "D": "tuple",
        },
        answer="D",
    ),
    Question(
        prompt="Python 串列（List）的第一個元素索引是多少？",
        options={
            "A": "1",
            "B": "0",
            "C": "2",
            "D": "-1",
        },
        answer="B",
    ),
    Question(
        prompt="在 Python 中，`2 ** 3` 的運算結果為何？",
        options={
            "A": "6",
            "B": "8",
            "C": "9",
            "D": "5",
        },
        answer="B",
    ),
    Question(
        prompt="下列哪一個方法可用來在 Python 串列尾端新增元素？",
        options={
            "A": "append()",
            "B": "push()",
            "C": "insert_end()",
            "D": "add()",
        },
        answer="A",
    ),
]


class MultipleChoiceQuizApp(QWidget):
    POINTS_PER_QUESTION = 20

    def __init__(self, questions: list[Question]) -> None:
        super().__init__()
        self.questions = questions
        self.current_index = 0
        self.correct_count = 0
        self.wrong_count = 0

        self.setWindowTitle("Python 選擇題測驗")
        self.setMinimumWidth(460)
        self._build_ui()
        self._load_question()

    def _build_ui(self) -> None:
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(12)

        # 題號進度標籤
        self.lbl_progress = QLabel()
        self.main_layout.addWidget(self.lbl_progress)

        # 題目內容標籤
        self.lbl_question = QLabel()
        self.lbl_question.setWordWrap(True)
        self.main_layout.addWidget(self.lbl_question)

        # 選項容器（A、B、C、D 單選鈕）
        self.options_container = QWidget()
        self.options_layout = QVBoxLayout()
        self.options_layout.setContentsMargins(4, 4, 4, 8)
        self.options_layout.setSpacing(8)
        self.options_container.setLayout(self.options_layout)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)
        self.radio_buttons: dict[str, QRadioButton] = {}

        for key in ("A", "B", "C", "D"):
            rb = QRadioButton()
            self.radio_buttons[key] = rb
            self.button_group.addButton(rb)
            self.options_layout.addWidget(rb)

        self.main_layout.addWidget(self.options_container)

        # 成績結算標籤（完成所有題目後顯示）
        self.lbl_summary = QLabel()
        self.lbl_summary.hide()
        self.main_layout.addWidget(self.lbl_summary)

        # 下一題按鈕
        self.btn_next = QPushButton("下一題")
        self.btn_next.setMinimumHeight(36)
        self.btn_next.clicked.connect(self.handle_next)
        self.main_layout.addWidget(self.btn_next)

        # 重新開始按鈕
        self.btn_restart = QPushButton("重新開始")
        self.btn_restart.setMinimumHeight(36)
        self.btn_restart.clicked.connect(self.restart_quiz)
        self.main_layout.addWidget(self.btn_restart)

        self.setLayout(self.main_layout)

    def _get_selected_option(self) -> str | None:
        for key, rb in self.radio_buttons.items():
            if rb.isChecked():
                return key
        return None

    def _clear_selection(self) -> None:
        self.button_group.setExclusive(False)
        for rb in self.radio_buttons.values():
            rb.setChecked(False)
        self.button_group.setExclusive(True)

    def _load_question(self) -> None:
        total = len(self.questions)
        q = self.questions[self.current_index]

        self.lbl_progress.show()
        self.lbl_question.show()
        self.options_container.show()
        self.btn_next.show()
        self.lbl_summary.hide()

        self.lbl_progress.setText(f"第 {self.current_index + 1} 題 / 共 {total} 題")
        self.lbl_question.setText(q.prompt)

        for key in ("A", "B", "C", "D"):
            self.radio_buttons[key].setText(f"{key}. {q.options[key]}")

        self._clear_selection()

    def handle_next(self) -> None:
        selected = self._get_selected_option()
        if selected is None:
            QMessageBox.warning(self, "尚未作答", "請先選擇一個答案（A、B、C 或 D）再進入下一題！")
            return

        current_q = self.questions[self.current_index]
        if selected == current_q.answer:
            self.correct_count += 1
        else:
            self.wrong_count += 1

        self.current_index += 1
        if self.current_index < len(self.questions):
            self._load_question()
        else:
            self._show_result()

    def _show_result(self) -> None:
        total_questions = len(self.questions)
        max_score = total_questions * self.POINTS_PER_QUESTION
        score = self.correct_count * self.POINTS_PER_QUESTION

        self.lbl_progress.hide()
        self.lbl_question.hide()
        self.options_container.hide()
        self.btn_next.hide()

        self.lbl_summary.setText(
            "測驗完成！\n\n"
            f"總分：{score} / {max_score}\n"
            f"答對題數：{self.correct_count}\n"
            f"答錯題數：{self.wrong_count}"
        )
        self.lbl_summary.show()

    def restart_quiz(self) -> None:
        self.current_index = 0
        self.correct_count = 0
        self.wrong_count = 0
        self._load_question()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MultipleChoiceQuizApp(QUIZ_QUESTIONS)
    window.show()
    sys.exit(app.exec())