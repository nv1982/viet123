import tkinter as tk
from tkinter import Menu, messagebox
import subprocess
import os
import sys
from find_form import EmployeeSearchForm  # Nhập lớp EmployeeSearchForm
from employee_add import EmployeeAddForm  # Nhập lớp EmployeeAddForm
from employee_management import EmployeeManagementForm  # Nhập lớp EmployeeManagementForm
from form_csdl import FormCSLD  # Nhập lớp FormCSLD

if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# Đường dẫn đến các file bổ sung
form_csdl_path = os.path.join(application_path, 'form_csdl.py')
from_delete_update_path = os.path.join(application_path, 'from_delete_update.py')
new_form_path = os.path.join(application_path, 'new_form.py')
db_connection_path = os.path.join(application_path, 'db_connection.py')
find_form_path = os.path.join(application_path, 'find_form.py')

# Hàm mở form tìm kiếm
def find_file():
    new_window = tk.Toplevel(root)  # Tạo cửa sổ mới
    app = EmployeeSearchForm(new_window)  # Khởi tạo form tìm kiếm với cửa sổ mới

# Hàm mở form quản lý nhân viên
def csdl_delete_update():
    new_window = tk.Toplevel(root)  # Tạo cửa sổ mới
    app = EmployeeManagementForm(new_window)  # Khởi tạo form quản lý nhân viên với cửa sổ mới

# Hàm mở form thêm nhân viên
def csdl_add_employee():
    new_window = tk.Toplevel(root)  # Tạo cửa sổ mới
    app = EmployeeAddForm(new_window)  # Khởi tạo form thêm nhân viên với cửa sổ mới

# Hàm mở form csdl
def csdl_file():
    new_window = tk.Toplevel(root)  # Tạo cửa sổ mới
    app = FormCSLD(new_window)  # Khởi tạo form_csdl với cửa sổ mới

def exit_app():
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("CHƯƠNG TRÌNH QUẢN LÝ NHÂN VIÊN")

# Đặt kích thước cửa sổ 600x800
root.geometry("1400x900")
root.configure(bg='lightblue') 
# Đặt icon cho form
root.iconbitmap(r"F:\PYTHON-APP\PYTHON-GUI\FORM1\app_icon.ico")  # Đường dẫn tới file icon (.ico)

# Tạo menu
menu_bar = Menu(root)
custom_font = ("Arial", 13)

# Tạo menu File
file_menu = Menu(menu_bar, tearoff=0, font=custom_font)
file_menu.add_command(label="Add New Data", command=csdl_add_employee)  # Liên kết với hàm thêm nhân viên
file_menu.add_command(label="View Data", command=csdl_file)  # Liên kết với hàm xem dữ liệu
file_menu.add_command(label="Delete_Update Data", command=csdl_delete_update)  # Liên kết với hàm quản lý nhân viên
file_menu.add_command(label="Find Data", command=find_file)  # Liên kết với hàm tìm kiếm
file_menu.add_separator()  # Dòng phân cách
file_menu.add_command(label="Exit", command=exit_app)  # Liên kết với hàm thoát
menu_bar.add_cascade(label="File-Database", menu=file_menu, font=custom_font)

# Gán menu cho cửa sổ chính
root.config(menu=menu_bar)

# Chạy vòng lặp giao diện
root.mainloop()
