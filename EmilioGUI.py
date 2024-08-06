import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(image)

def set_background(window, image_path):
    background_image = Image.open(image_path)
    background_photo = ImageTk.PhotoImage(background_image)

    background_label = tk.Label(window, image=background_photo)
    background_label.image = background_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.bind("<Enter>", lambda event: on_enter(event, background_label))
    background_label.bind("<Leave>", lambda event: on_leave(event, background_label))

def make_entry_oval(entry_widget):
    entry_widget.config(relief="flat", bd=1, highlightthickness=0)
    entry_widget.bind("<FocusIn>", lambda event: entry_widget.config(relief="groove", bd=2))
    entry_widget.bind("<FocusOut>", lambda event: entry_widget.config(relief="flat", bd=1))

def make_entry_highlighted(entry_widget):
    entry_widget.config(highlightbackground="black", highlightcolor="black", highlightthickness=1)

def on_enter(event, widget):
    widget.config(cursor="hand2")

def on_leave(event, widget):
    widget.config(cursor="")

def open_second_window():
    second_window = Toplevel(root)
    second_window.title("Ingresar Datos")
    set_background(second_window, "C:/Users/emili/Downloads/s.jpg")  # Ruta de la imagen de fondo

    frame_style = {'bg': 'white', 'bd': 2, 'relief': 'groove'}  # Estilo para los recuadros

    entry_frame = tk.Frame(second_window, bg='white', padx=20, pady=10)
    entry_frame.pack(padx=20, pady=20)

    tk.Label(entry_frame, text="Nombre:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
    name_entry = tk.Entry(entry_frame, font=("Arial", 12))
    name_entry.grid(row=0, column=1, padx=10, pady=5)
    make_entry_oval(name_entry)
    make_entry_highlighted(name_entry)

    tk.Label(entry_frame, text="Edad:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
    age_entry = tk.Entry(entry_frame, font=("Arial", 12))
    age_entry.grid(row=1, column=1, padx=10, pady=5)
    make_entry_oval(age_entry)
    make_entry_highlighted(age_entry)

    tk.Label(entry_frame, text="Peso (kg):", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky='w')
    weight_entry = tk.Entry(entry_frame, font=("Arial", 12))
    weight_entry.grid(row=2, column=1, padx=10, pady=5)
    make_entry_oval(weight_entry)
    make_entry_highlighted(weight_entry)

    tk.Label(entry_frame, text="Altura (m):", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky='w')
    height_entry = tk.Entry(entry_frame, font=("Arial", 12))
    height_entry.grid(row=3, column=1, padx=10, pady=5)
    make_entry_oval(height_entry)
    make_entry_highlighted(height_entry)

    def calculate_bmi():
        try:
            name = name_entry.get()
            age = age_entry.get()
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            bmi = weight / (height ** 2)
            bmi_status = ""

            if bmi < 18.5:
                bmi_status = "Bajo peso"
            elif 18.5 <= bmi < 24.9:
                bmi_status = "Peso normal"
            elif 25 <= bmi < 29.9:
                bmi_status = "Sobrepeso"
            else:
                bmi_status = "Obesidad"

            result_window = Toplevel(root)
            result_window.title("Resultado IMC")
            set_background(result_window, "C:/Users/emili/Downloads/s.jpg")  # Ruta de la imagen de fondo

            result_label = tk.Label(result_window, text=f"Nombre: {name}\nEdad: {age}\nPeso: {weight} kg\nAltura: {height} m\n\nBMI: {bmi:.2f}\nEstado: {bmi_status}",
                                    font=("Arial", 12), bg='white', padx=20, pady=20)
            result_label.pack()

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores válidos para peso y altura.")

    calculate_image = resize_image("C:/Users/emili/Downloads/C.png", 150, 80)
    calculate_hover_image = resize_image("C:/Users/emili/Downloads/Calcular.png", 150, 80)
    calculate_button = tk.Button(second_window, image=calculate_image, command=calculate_bmi, borderwidth=0)
    calculate_button.image = calculate_image
    calculate_button.pack(pady=10)
    calculate_button.bind("<Enter>", lambda event: on_enter(event, calculate_button))
    calculate_button.bind("<Leave>", lambda event: on_leave(event, calculate_button))

    def open_third_window():
        third_window = Toplevel(root)
        third_window.title("Más Información")
        set_background(third_window, "C:/Users/emili/Downloads/s.jpg")  # Ruta de la imagen de fondo

        third_image = resize_image("C:/Users/emili/OneDrive/Imágenes/Capturas de pantalla/TablaImc.png", 400, 400)
        tk.Label(third_window, image=third_image).pack()
        third_window.mainloop()

    info_image = resize_image("C:/Users/emili/Downloads/info.png", 150, 80)
    info_hover_image = resize_image("C:/Users/emili/Downloads/R.png", 150, 80)
    info_button = tk.Button(second_window, image=info_image, command=open_third_window, borderwidth=0)
    info_button.image = info_image
    info_button.pack(pady=10)
    info_button.bind("<Enter>", lambda event: on_enter(event, info_button))
    info_button.bind("<Leave>", lambda event: on_leave(event, info_button))

    second_window.mainloop()

root = tk.Tk()
root.title("Cálculo de BMI")
set_background(root, "C:/Users/emili/Downloads/s.jpg")  # Ruta de la imagen de fondo

button_image = resize_image("C:/Users/emili/Downloads/Imss.png", 250, 250)

image_button = tk.Button(root, image=button_image, command=open_second_window, borderwidth=0)
image_button.pack(pady=20)

root.mainloop()
