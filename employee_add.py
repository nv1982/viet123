import tkinter as tk
from tkinter import messagebox
from db_connection import connect_db
import mysql.connector  # Đảm bảo đã import mysql.connector

class EmployeeAddForm:
    def __init__(self, master):
        self.master = master
        self.master.title("THÊM NHÂN VIÊN")
        self.master.geometry("400x300")
        self.master.iconbitmap(r"F:\PYTHON-APP\PYTHON-GUI\FORM1\app_icon.ico")

        # Label và Entry cho ID
        tk.Label(self.master, text="ID").grid(row=0, column=0, padx=10, pady=5)
        self.entry_id = tk.Entry(self.master)
        self.entry_id.grid(row=0, column=1, padx=10, pady=5)

        # Label và Entry cho Lastname
        tk.Label(self.master, text="Lastname").grid(row=1, column=0, padx=10, pady=5)
        self.entry_lastname = tk.Entry(self.master)
        self.entry_lastname.grid(row=1, column=1, padx=10, pady=5)

        # Label và Entry cho Firstname
        tk.Label(self.master, text="Firstname").grid(row=2, column=0, padx=10, pady=5)
        self.entry_firstname = tk.Entry(self.master)
        self.entry_firstname.grid(row=2, column=1, padx=10, pady=5)

        # Label và Entry cho DOB
        tk.Label(self.master, text="DOB (YYYY-MM-DD)").grid(row=3, column=0, padx=10, pady=5)
        self.entry_dob = tk.Entry(self.master)
        self.entry_dob.grid(row=3, column=1, padx=10, pady=5)

        # Label và Entry cho Gender
        tk.Label(self.master, text="Gender").grid(row=4, column=0, padx=10, pady=5)
        self.entry_gender = tk.Entry(self.master)
        self.entry_gender.grid(row=4, column=1, padx=10, pady=5)

        # Label và Entry cho HireDate
        tk.Label(self.master, text="Hire Date (YYYY-MM-DD)").grid(row=5, column=0, padx=10, pady=5)
        self.entry_hiredate = tk.Entry(self.master)
        self.entry_hiredate.grid(row=5, column=1, padx=10, pady=5)

        # Tạo một frame để chứa các nút trên cùng một hàng
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)

        # Nút thêm nhân viên
        tk.Button(button_frame, text="Thêm nhân viên", command=self.add_employee).pack(side=tk.LEFT, padx=5)

        # Nút làm sạch các ô nhập
        tk.Button(button_frame, text="Xóa", command=self.clear_entries).pack(side=tk.LEFT, padx=5)

    # Hàm thêm dữ liệu vào bảng employee
    def add_employee(self):
        conn = connect_db()  # Ensure to call the connect_db function
        cursor = conn.cursor(dictionary=True)

        employee_id = self.entry_id.get()
        lastname = self.entry_lastname.get()
        firstname = self.entry_firstname.get()
        dob = self.entry_dob.get()
        gender = self.entry_gender.get()
        hiredate = self.entry_hiredate.get()

        if employee_id and lastname and firstname and dob and gender and hiredate:
            try:
                cursor.execute(f"""
                    INSERT INTO employee (employee_id, lastname, firstname, DOB, gender, hireDate) 
                    VALUES (%s, %s, %s, %s, %s, %s)""", 
                    (employee_id, lastname, firstname, dob, gender, hiredate))
                conn.commit()
                messagebox.showinfo("Success", "Employee added successfully!")
                self.clear_entries()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
        else:
            messagebox.showerror("Error", "All fields must be filled!")

        cursor.close()
        conn.close()

    # Hàm xóa dữ liệu sau khi thêm, xóa, hoặc sửa
    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_lastname.delete(0, tk.END)
        self.entry_firstname.delete(0, tk.END)
        self.entry_dob.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)
        self.entry_hiredate.delete(0, tk.END)

# Chạy giao diện
if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeAddForm(root)
    root.mainloop()