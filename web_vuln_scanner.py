import os
import sys
import shodan
import subprocess
import customtkinter as ctk
from tkinter import messagebox, filedialog

def install_dependencies():
    packages = ['shodan', 'customtkinter']
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except Exception as e:
            print(f"Failed to install {package}: {str(e)}")
            sys.exit(1)

def run_shodan_scan():
    api_key = 'Xvh6AUTIqBdLOZwBVGbGGLSs2Jfj413B'  # Remplacez par votre clé API Shodan
    target = target_entry.get()
    if not target:
        messagebox.showerror("Input Error", "Please enter a target IP address.")
        return

    api = shodan.Shodan(api_key)

    try:
        # Perform the Shodan search
        result = api.host(target)
        save_results(result)
        display_results(result)
    except shodan.APIError as e:
        messagebox.showerror("Scan Error", str(e))

def save_results(result):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, "shodan_scan_results.txt")
    with open(filename, "w") as file:
        file.write(f"Scan Results for {result['ip_str']}:\n")
        file.write(f"Organization: {result.get('org', 'n/a')}\n")
        file.write(f"Operating System: {result.get('os', 'n/a')}\n")
        for item in result['data']:
            file.write(f"Port: {item['port']}\n")
            file.write(f"Banner: {item['data']}\n")
            if 'vulns' in item:
                file.write("Vulnerabilities:\n")
                for vuln in item['vulns']:
                    file.write(f"- {vuln}\n")
                    if 'cve' in item['vulns'][vuln]:
                        file.write(f"  CVE: {', '.join(item['vulns'][vuln]['cve'])}\n")
            file.write("\n")

def display_results(result):
    result_textbox.delete(1.0, ctk.END)
    result_textbox.insert(ctk.END, f"Scan Results for {result['ip_str']}:\n")
    result_textbox.insert(ctk.END, f"Organization: {result.get('org', 'n/a')}\n")
    result_textbox.insert(ctk.END, f"Operating System: {result.get('os', 'n/a')}\n")
    for item in result['data']:
        result_textbox.insert(ctk.END, f"Port: {item['port']}\n")
        result_textbox.insert(ctk.END, f"Banner: {item['data']}\n")
        if 'vulns' in item:
            result_textbox.insert(ctk.END, "Vulnerabilities:\n")
            for vuln in item['vulns']:
                result_textbox.insert(ctk.END, f"- {vuln}\n")
                if 'cve' in item['vulns'][vuln]:
                    result_textbox.insert(ctk.END, f"  CVE: {', '.join(item['vulns'][vuln]['cve'])}\n")
        result_textbox.insert(ctk.END, "\n")

def create_gui():
    global target_entry, result_textbox

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Shodan IP Scanner")
    root.configure(bg='#333333')

    frame = ctk.CTkFrame(root, corner_radius=10)
    frame.pack(padx=20, pady=20, fill="both", expand=True)

    target_label = ctk.CTkLabel(frame, text="Target IP:")
    target_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    target_entry = ctk.CTkEntry(frame, width=200)
    target_entry.grid(row=0, column=1, padx=10, pady=10)

    scan_button = ctk.CTkButton(frame, text="Scan", command=run_shodan_scan, fg_color="blue", hover_color="blue")
    scan_button.grid(row=0, column=2, padx=10, pady=10)

    result_textbox = ctk.CTkTextbox(frame, width=600, height=400, wrap="none")
    result_textbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    install_dependencies()
    create_gui()
