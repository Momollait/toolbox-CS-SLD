import customtkinter as ctk
import subprocess
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog, messagebox, simpledialog
import tkinter as tk

def install_dependencies():
    packages = ["customtkinter", "python-nmap", "paramiko", "reportlab"]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x300")
app.title("Cyber Toolbox")

def launch_script(script_path, args=[]):
    try:
        proc = subprocess.Popen([sys.executable, script_path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if proc.returncode != 0:
            messagebox.showerror("Error", f"Error executing {script_path}:\n{stderr.decode()}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to start the script: {str(e)}")

def run_network_scan():
    
    launch_script("scannmap.py")

def start_brute_force():

    launch_script("bruteforcessh.py")

def check_password_strength():
    
    launch_script("check_password.py")

def generate_pdf_report():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
    if not filename:
        return
    
    c = canvas.Canvas(filename, pagesize=letter)
    c.setTitle("Cyber Toolbox Report")
    
    files = ["scannmap_results.txt", "bruteforcessh_results.txt", "check_password_results.txt"]
    y_position = 750
    c.setFont("Helvetica", 12)
    for file in files:
        try:
            with open(file, "r") as f:
                c.drawString(72, y_position, f"Results from {file}:")
                y_position -= 20
                for line in f:
                    c.drawString(72, y_position, line.strip())
                    y_position -= 14
                    if y_position < 72:
                        c.showPage()
                        y_position = 750
        except FileNotFoundError:
            c.drawString(72, y_position, f"File {file} not found, skipping...")
            y_position -= 20
    c.save()
    messagebox.showinfo("PDF Generated", "PDF report has been generated.")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

button_scan = ctk.CTkButton(master=frame, text="Run Network Scan", command=run_network_scan)
button_scan.pack(pady=10)

button_bruteforce = ctk.CTkButton(master=frame, text="Start Brute Force", command=start_brute_force)
button_bruteforce.pack(pady=10)

button_check_password = ctk.CTkButton(master=frame, text="Check Password Strength", command=check_password_strength)
button_check_password.pack(pady=10)

button_pdf = ctk.CTkButton(master=frame, text="Generate PDF Report", command=generate_pdf_report)
button_pdf.pack(pady=10)

if __name__ == "__main__":
    install_dependencies()
    app.mainloop()
