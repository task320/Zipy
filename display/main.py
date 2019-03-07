import tkinter as tk
import tkinter.filedialog as filedialog
import actor.zipper as zipper
import traceback
from errorclass.zipyerror import ZipyError


class MainDisplay():
    def __init__(self):
        root = tk.Tk()
        root.geometry('420x240')
        self.dir_path = ""
        self.master = root
        self.create_widgets()
    
    def run(self):
        self.master.mainloop()

    def create_widgets(self):
        btn_select_dir = tk.Button(text="フォルダ選択", command=self.select_dir)
        btn_select_dir.pack(side="top", pady=10)

        lbl_disp1 = tk.Label(text="■フォルダパス:")
        lbl_disp1.pack(side="top")

        lbl_path = tk.Label(text="")
        lbl_path.pack(side="top")
        self.lbl_path = lbl_path

        lbl_disp2 = tk.Label(text="■パスワード:")
        lbl_disp2.pack(side="top")

        entry_pwd = tk.Entry(width=30)
        entry_pwd.pack(side="top")
        self.entry_pwd = entry_pwd

        btn_select_dir = tk.Button(text="圧縮", command=self.compress)
        btn_select_dir.pack(side="top", pady=10)

    def select_dir(self):
        dir_path = filedialog.askdirectory()
        self.lbl_path["text"] = dir_path
        self.dir_path = dir_path

    def compress(self):
        try:
            zipper.create_zip_file(self.dir_path, self.entry_pwd.get(), 1)
        except ZipyError:
            traceback.print_exc()


