import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")  # 'light' (default), 'dark'
ctk.set_default_color_theme("blue")  # 'blue' (default), 'green', 'dark-blue'

def verify_password():
    password = password_entry.get()
    if len(password) == 0:
        messagebox.showerror("Erreur", "Veuillez entrer un mot de passe.")
        return "Error: No password entered."

    score = 0
    messages = []
    if len(password) < 8:
        messagebox.showwarning("Faible", "Votre mot de passe est trop court. Il doit contenir au moins 8 caractères.")
        messages.append("Votre mot de passe est trop court. Il doit contenir au moins 8 caractères.")
    else:
        score += 1
        if any(char.isdigit() for char in password):
            score += 1
        if any(char.isupper() for char in password):
            score += 1
        if any(char.islower() for char in password):
            score += 1
        if any(not char.isalnum() for char in password):
            score += 1
        
        if score < 3:
            messagebox.showwarning("Moyen", "Votre mot de passe est moyen. Essayez d'utiliser des chiffres, des lettres majuscules, et des caractères spéciaux.")
            messages.append("Votre mot de passe est moyen. Essayez d'utiliser des chiffres, des lettres majuscules, et des caractères spéciaux.")
        elif score < 5:
            messagebox.showinfo("Bon", "Votre mot de passe est bon, mais peut être amélioré.")
            messages.append("Votre mot de passe est bon, mais peut être amélioré.")
        else:
            messagebox.showinfo("Excellent", "Votre mot de passe est excellent.")
            messages.append("Votre mot de passe est excellent.")

    result = f"Score: {score}, " + ". ".join(messages)
    return result

app = ctk.CTk()
app.title("Vérificateur de mot de passe")

label = ctk.CTkLabel(app, text="Entrez votre mot de passe:", font=("Arial", 12))
label.pack(pady=20)

password_entry = ctk.CTkEntry(app, width=300, font=("Arial", 12), show="*")
password_entry.pack(pady=10)

verify_button = ctk.CTkButton(app, text="Vérifier", command=lambda: print(verify_password()))  # Utiliser print ici pour démontrer
verify_button.pack(pady=20)

app.mainloop()
