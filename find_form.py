import tkinter as tk
from tkinter import messagebox
from tkinter import font
from db_connection import connect_db

class EmployeeSearchForm:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.iconbitmap(r"F:\PYTHON-APP\PYTHON-GUI\FORM1\app_icon.ico")
        self.master.title("Tìm nhân viên theo họ và tên:")

        # Tạo font với kích thước 13
        self.custom_font = font.Font(size=13)

        # Tạo Label và Entry cho tìm kiếm
        label = tk.Label(self.master, text="Nhập tên để tìm:", font=self.custom_font)
        label.pack(pady=5)

        self.entry = tk.Entry(self.master, font=self.custom_font)
        self.entry.pack(pady=5)

        # Tạo Button tìm kiếm
        button = tk.Button(self.master, text="Tìm", command=self.search_employee, font=self.custom_font)
        button.pack(pady=5)

        # Tạo Listbox để hiển thị kết quả
        self.listbox = tk.Listbox(self.master, width=100, font=self.custom_font)
        self.listbox.pack(pady=5)

    def search_employee(self):
        search_term = self.entry.get()
        if not search_term:
            messagebox.showerror("Error", "Please enter a search term")
            return
        
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM employee WHERE firstname LIKE %s OR lastname LIKE %s"
        cursor.execute(query, ('%' + search_term + '%', '%' + search_term + '%'))
        
        results = cursor.fetchall()
        
        # Xóa nội dung của listbox trước khi thêm kết quả mới
        self.listbox.delete(0, tk.END)
        
        if results:
            for employee in results:
                firstname = employee.get('firstname', 'N/A')
                lastname = employee.get('lastname', 'N/A')
                
                dob_date = employee.get('DOB', None)
                dob_date = dob_date.strftime("%Y-%m-%d") if dob_date else 'N/A'
                
                gender = employee.get('gender', 'N/A')
                
                hire_date_str = employee.get('hireDate', None)
                hire_date_str = hire_date_str.strftime("%Y-%m-%d") if hire_date_str else 'N/A'
                
                # Chèn dữ liệu vào listbox
                self.listbox.insert(tk.END, f"{lastname} {firstname} {dob_date} {gender} {hire_date_str}")
        else:
            self.listbox.insert(tk.END, "No results found")
        
        cursor.close()
        conn.close()

# Chạy giao diện
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeSearchForm(root)
    root.mainloop()
