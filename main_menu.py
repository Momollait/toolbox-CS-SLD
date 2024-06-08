import subprocess
import sys
import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from fpdf import FPDF

# Classe pour créer le PDF
class PDF(FPDF):
    def header(self):
        # Supposons que vous ayez un logo à ajouter
        # self.image('logo.png', 10, 8, 33)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Toolbox Activity Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Chapter {num} : {label}', 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)

def install_dependencies():
    try:
        import pip
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'ensurepip'])
    
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'customtkinter', 'python-nmap', 'paramiko', 'fpdf'])

script_results = []

def launch_script(script_name):
    global script_results
    actions = []
    if script_name == "scannmap":
        import scannmap
        result = scannmap.create_gui()
        actions.append((1, "Network Scanning", result))
    elif script_name == "bruteforcessh":
        import bruteforcessh
        result = bruteforcessh.app.mainloop()
        actions.append((2, "Brute Force SSH/FTP", result))
    elif script_name == "check_password":
        import check_password
        result = check_password.app.mainloop()
        actions.append((3, "Password Strength Check", result))
    print("Launch script:", script_name, actions)  # Debug print
    script_results.extend(actions)  # Store the results in the global variable
    return actions

def save_pdf_report():
    global script_results
    print("Script results:", script_results)  # Debug print
    pdf = PDF()
    pdf.add_page()
    for action, detail in script_results:
        pdf.chapter_title(action[0], action[1])
        pdf.chapter_body(detail)
    
    filepath = filedialog.asksaveasfilename(defaultextension=".pdf",
                                            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if filepath:
        pdf.output(filepath)



def create_menu():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Toolbox Menu")

    btn_scan = ctk.CTkButton(app, text="Run Nmap Scan", command=lambda: launch_script("scannmap"))
    btn_scan.pack(pady=20)

    btn_brute = ctk.CTkButton(app, text="Brute Force SSH/FTP", command=lambda: launch_script("bruteforcessh"))
    btn_brute.pack(pady=20)

    btn_check = ctk.CTkButton(app, text="Check Password Strength", command=lambda: launch_script("check_password"))
    btn_check.pack(pady=20)

    btn_report = ctk.CTkButton(app, text="Generate Report", command=save_pdf_report)
    btn_report.pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    install_dependencies()
    create_menu()
