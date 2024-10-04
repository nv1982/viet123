import tkinter as tk
from tkinter import ttk
from db_connection import connect_db
from datetime import datetime

class FormCSLD:
    def __init__(self, master):
        self.master = master
        self.master.title("Xem nhân viên")
        self.master.geometry("800x300")
        self.master.iconbitmap(r"F:\PYTHON-APP\PYTHON-GUI\FORM1\app_icon.ico")  # Tạo icon cho chương trình

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Arial", 13))
        self.style.configure("Treeview", font=("Arial", 13))

        self.table = ttk.Treeview(self.master, columns=(1, 2, 3, 4, 5, 6), show="headings", height="10")
        self.table.pack(side="top", fill="x")

        self.table.heading(1, text="Số tt")
        self.table.heading(2, text="Họ")
        self.table.heading(3, text="Tên")
        self.table.heading(4, text="Ngày sinh")
        self.table.heading(5, text="Giới tính")
        self.table.heading(6, text="Ngày đi làm")

        self.table.column(1, width=100)
        self.table.column(2, width=200)
        self.table.column(3, width=150)
        self.table.column(4, width=100)
        self.table.column(5, width=100)
        self.table.column(6, width=100)

        load_button = tk.Button(self.master, text="Tải cơ sở dữ liệu", command=self.get_employee_data)
        load_button.pack(pady=20)

    def get_employee_data(self):
        conn = connect_db()
        if conn is None:
            messagebox.showerror("Lỗi kết nối", "Không thể kết nối đến cơ sở dữ liệu.")
            return

        cursor = conn.cursor(dictionary=True)
        try:
            for item in self.table.get_children():
                self.table.delete(item)

            cursor.execute("SELECT * FROM employee")
            rows = cursor.fetchall()

            for row in rows:
                dob = row['DOB'].strftime('%Y-%m-%d') if isinstance(row['DOB'], datetime) else row['DOB']
                hire_date = row['hireDate'].strftime('%Y-%m-%d') if isinstance(row['hireDate'], datetime) else row['hireDate']
                self.table.insert("", tk.END, values=(row['employee_id'], row['lastname'], row['firstname'], dob, row['gender'], hire_date))

        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra khi lấy dữ liệu: {str(e)}")
        finally:
            cursor.close()
            conn.close()

# Tạo cửa sổ chính
if __name__ == "__main__":
    root = tk.Tk()
    app = FormCSLD(root)
    root.mainloop()
