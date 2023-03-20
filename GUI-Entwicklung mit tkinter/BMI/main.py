import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100
    bmi = round(weight / (height ** 2), 2)
    result_label.config(text=f"Dein BMI ist: {bmi}")

    if bmi < 18.5:
        classification_label.config(text="Du hast Untergewicht.", fg="#E74C3C")
    elif bmi < 25:
        classification_label.config(text="Du hast Normalgewicht.", fg="#2ECC71")
    elif bmi < 30:
        classification_label.config(text="Du hast Übergewicht.", fg="#F1C40F")
    elif bmi < 35:
        classification_label.config(text="Du hast Adipositas Grad I.", fg="#E67E22")
    elif bmi < 40:
        classification_label.config(text="Du hast Adipositas Grad II.", fg="#E74C3C")
    else:
        classification_label.config(text="Du hast Adipositas Grad III.", fg="#C0392B")

root = tk.Tk()
root.title("BMI Rechner")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#FDFEFE")
root.iconbitmap("GUI-Entwicklung mit tkinter\BMI\icon.ico")

header_label = tk.Label(root, text="BMI Rechner", font=("Arial", 24), bg="#FDFEFE")
header_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#FDFEFE")
input_frame.pack()

weight_label = tk.Label(input_frame, text="Gewicht (in kg):", font=("Arial", 14), bg="#FDFEFE")
weight_label.grid(row=0, column=0, padx=10, pady=10)

weight_entry = tk.Entry(input_frame, font=("Arial", 14))
weight_entry.grid(row=0, column=1, padx=10, pady=10)

height_label = tk.Label(input_frame, text="Größe (in cm):", font=("Arial", 14), bg="#FDFEFE")
height_label.grid(row=1, column=0, padx=10, pady=10)

height_entry = tk.Entry(input_frame, font=("Arial", 14))
height_entry.grid(row=1, column=1, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#FDFEFE")
button_frame.pack()

calculate_button = tk.Button(button_frame, text="BMI berechnen", font=("Arial", 14), command=calculate_bmi)
calculate_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#FDFEFE")
result_label.pack(pady=10)

classification_label = tk.Label(root, text="", font=("Arial", 14), bg="#FDFEFE")
classification_label.pack(pady=10)

root.mainloop()
