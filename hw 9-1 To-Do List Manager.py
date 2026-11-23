import tkinter as tk
from tkinter import messagebox


class TodoListManagerApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("待辦事項管理")
        self.root.geometry("420x440")
        self.root.minsize(360, 380)

        self.total_var = tk.StringVar(value="事項總數：0")
        self._build_ui()

    def _build_ui(self) -> None:
        pad_x = 16

        # 輸入提示與輸入框
        lbl_prompt = tk.Label(self.root, text="請輸入待辦事項：", font=("Microsoft JhengHei", 11))
        lbl_prompt.pack(anchor="w", padx=pad_x, pady=(14, 4))

        self.entry_todo = tk.Entry(self.root, font=("Microsoft JhengHei", 11))
        self.entry_todo.pack(fill="x", padx=pad_x, pady=(0, 10))
        self.entry_todo.focus()
        self.entry_todo.bind("<Return>", lambda _event: self.add_todo())

        # 待辦事項清單區（含垂直與水平捲軸）
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=pad_x)

        v_scroll = tk.Scrollbar(list_frame, orient="vertical")
        h_scroll = tk.Scrollbar(list_frame, orient="horizontal")

        self.listbox_todo = tk.Listbox(
            list_frame,
            font=("Microsoft JhengHei", 10),
            selectmode=tk.SINGLE,
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set,
            activestyle="none",
        )
        v_scroll.config(command=self.listbox_todo.yview)
        h_scroll.config(command=self.listbox_todo.xview)

        v_scroll.pack(side="right", fill="y")
        h_scroll.pack(side="bottom", fill="x")
        self.listbox_todo.pack(side="left", fill="both", expand=True)

        # 操作按鈕列（新增 / 刪除選取 / 全部清除）
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=pad_x, pady=(12, 8))

        btn_add = tk.Button(
            btn_frame,
            text="新增",
            font=("Microsoft JhengHei", 10),
            width=10,
            command=self.add_todo,
        )
        btn_add.pack(side="left", expand=True, padx=(0, 6))

        btn_delete = tk.Button(
            btn_frame,
            text="刪除選取",
            font=("Microsoft JhengHei", 10),
            width=10,
            command=self.delete_selected,
        )
        btn_delete.pack(side="left", expand=True, padx=6)

        btn_clear_all = tk.Button(
            btn_frame,
            text="全部清除",
            font=("Microsoft JhengHei", 10),
            width=10,
            command=self.clear_all,
        )
        btn_clear_all.pack(side="left", expand=True, padx=(6, 0))

        # 目前事項總數顯示
        lbl_total = tk.Label(
            self.root,
            textvariable=self.total_var,
            font=("Microsoft JhengHei", 10),
            anchor="w",
        )
        lbl_total.pack(fill="x", padx=pad_x, pady=(0, 14))

    def _update_total(self) -> None:
        count = self.listbox_todo.size()
        self.total_var.set(f"事項總數：{count}")

    def add_todo(self) -> None:
        item = self.entry_todo.get().strip()
        if not item:
            messagebox.showwarning("提示", "不得新增空白待辦事項！")
            self.entry_todo.focus()
            return

        self.listbox_todo.insert(tk.END, item)
        self.entry_todo.delete(0, tk.END)
        self.entry_todo.focus()
        self._update_total()

    def delete_selected(self) -> None:
        selected_indices = self.listbox_todo.curselection()
        if not selected_indices:
            messagebox.showwarning("提示", "請先選取要刪除的待辦事項！")
            return

        # 依索引由大到小刪除，避免索引位移
        for idx in reversed(selected_indices):
            self.listbox_todo.delete(idx)

        self._update_total()

    def clear_all(self) -> None:
        if self.listbox_todo.size() == 0:
            messagebox.showinfo("提示", "目前沒有待辦事項可清除。")
            return

        confirmed = messagebox.askyesno("確認清除", "確定要清空所有待辦事項嗎？")
        if confirmed:
            self.listbox_todo.delete(0, tk.END)
            self._update_total()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListManagerApp(root)
    root.mainloop()