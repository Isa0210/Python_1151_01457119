import tkinter as tk
from tkinter import messagebox


class TemperatureConverterApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("溫度轉換器")
        self.root.geometry("360x240")
        self.root.resizable(False, False)

        # 轉換模式："c2f" 代表攝氏 -> 華氏，"f2c" 代表華氏 -> 攝氏
        self.mode_var = tk.StringVar(value="c2f")
        self.result_var = tk.StringVar(value="轉換結果：")

        self._build_ui()

    def _build_ui(self) -> None:
        pad_x = 16

        # 輸入提示與輸入框
        lbl_prompt = tk.Label(self.root, text="請輸入溫度：", font=("Microsoft JhengHei", 11))
        lbl_prompt.pack(anchor="w", padx=pad_x, pady=(14, 4))

        self.entry_temp = tk.Entry(self.root, font=("Microsoft JhengHei", 11))
        self.entry_temp.pack(fill="x", padx=pad_x, pady=(0, 10))
        self.entry_temp.focus()

        # 支援按 Enter 直接執行轉換
        self.entry_temp.bind("<Return>", lambda _event: self.convert_temperature())

        # 轉換方向單選鈕
        rb_c2f = tk.Radiobutton(
            self.root,
            text="攝氏 → 華氏",
            variable=self.mode_var,
            value="c2f",
            font=("Microsoft JhengHei", 10),
        )
        rb_c2f.pack(anchor="w", padx=pad_x)

        rb_f2c = tk.Radiobutton(
            self.root,
            text="華氏 → 攝氏",
            variable=self.mode_var,
            value="f2c",
            font=("Microsoft JhengHei", 10),
        )
        rb_f2c.pack(anchor="w", padx=pad_x, pady=(0, 10))

        # 操作按鈕區（轉換 / 清除）
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=pad_x, pady=(2, 12))

        btn_convert = tk.Button(
            btn_frame,
            text="轉換",
            font=("Microsoft JhengHei", 10),
            width=12,
            command=self.convert_temperature,
        )
        btn_convert.pack(side="left", expand=True, padx=(0, 6))

        btn_clear = tk.Button(
            btn_frame,
            text="清除",
            font=("Microsoft JhengHei", 10),
            width=12,
            command=self.clear_all,
        )
        btn_clear.pack(side="left", expand=True, padx=(6, 0))

        # 結果顯示標籤
        lbl_result = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Microsoft JhengHei", 11),
            anchor="w",
        )
        lbl_result.pack(fill="x", padx=pad_x)

    def convert_temperature(self) -> None:
        raw_text = self.entry_temp.get().strip()
        if not raw_text:
            messagebox.showerror("輸入錯誤", "請先輸入數值溫度！")
            return

        try:
            temp = float(raw_text)
        except ValueError:
            messagebox.showerror("輸入錯誤", "請輸入有效的數字（例如：30 或 -5.5）！")
            return

        mode = self.mode_var.get()
        if mode == "c2f":
            converted = temp * 9 / 5 + 32
            self.result_var.set(f"轉換結果：{converted:.2f} °F")
        else:
            converted = (temp - 32) * 5 / 9
            self.result_var.set(f"轉換結果：{converted:.2f} °C")

    def clear_all(self) -> None:
        self.entry_temp.delete(0, tk.END)
        self.result_var.set("轉換結果：")
        self.entry_temp.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()