import customtkinter as ctk
import subprocess
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from tkinter import filedialog, messagebox
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

    # Create a PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add a title
    title = Paragraph("Cyber Toolbox Report", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Files to read data from
    files = ["scannmap_results.txt", "bruteforcessh_results.txt", "check_password_results.txt"]

    for file in files:
        try:
            with open(file, "r") as f:
                content = f.read()
                # Add a header for each section
                header = Paragraph(f"Results from {file}:", styles['Heading2'])
                elements.append(header)
                elements.append(Spacer(1, 12))

                # Split the content into lines
                lines = content.splitlines()

                # Create a table with the results
                table_data = [[line] for line in lines]
                table = Table(table_data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)
                elements.append(Spacer(1, 24))
        except FileNotFoundError:
            error_message = Paragraph(f"File {file} not found, skipping...", styles['Normal'])
            elements.append(error_message)
            elements.append(Spacer(1, 12))

    doc.build(elements)
    messagebox.showinfo("PDF Generated", "PDF report has been generated.")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

button_scan = ctk.CTkButton(master=frame, text="Run Network Scan", command=lambda: launch_script("scannmap.py"))
button_scan.pack(pady=10)

button_bruteforce = ctk.CTkButton(master=frame, text="Start Brute Force", command=lambda: launch_script("bruteforcessh.py"))
button_bruteforce.pack(pady=10)

button_check_password = ctk.CTkButton(master=frame, text="Check Password Strength", command=lambda: launch_script("check_password.py"))
button_check_password.pack(pady=10)

button_pdf = ctk.CTkButton(master=frame, text="Generate PDF Report", command=generate_pdf_report)
button_pdf.pack(pady=10)

if __name__ == "__main__":
    install_dependencies()
    app.mainloop()
