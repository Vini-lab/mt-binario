import tkinter as tk
from turingMachine import TuringMachine

class TmInterfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing - Verificación de Cadena")
        self.root.geometry("450x350")
        self.root.configure(bg="#f5f5f5")

        self.title_label = tk.Label(
            root, text="Máquina de Turing", font=("Arial", 24, "bold"), bg="#f5f5f5", fg="#34495e"
        )
        self.title_label.pack(pady=20)

        self.label = tk.Label(
            root, text="Escribe la cadena que se analizará:",
            font=("Arial", 12), bg="#f5f5f5", fg="#34495e"
        )
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12), bg="#ecf0f1", fg="#34495e", bd=2, relief="groove")
        self.entry.pack(pady=10, ipadx=5, ipady=5)

        self.verify_button = tk.Button(
            root, text="Verificar", font=("Arial", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, borderwidth=1, command=self.verify_string
        )
        self.verify_button.pack(pady=20)


        self.result_label = tk.Label(
            root, text="", font=("Arial", 12), bg="#f5f5f5", fg="#34495e"
        )
        self.result_label.pack(pady=10)

    def verify_string(self):
        input_string = self.entry.get().strip()

        if not input_string.isdigit() or any(c not in '01' for c in input_string):
            self.show_popup("Error: La cadena debe contener solo caracteres binarios (0 y 1)", "Error", "#e74c3c")
            return

        try:
            tm = TuringMachine(list(input_string))
            result, total_sum = tm.run()
            
            if result:
                binary_result = bin(total_sum)[2:]
                self.show_popup(f"Suma: {total_sum} - Binario: {binary_result}", "Resultado", "#2ecc71")
            else:
                self.show_popup("¡Cadena inválida!", "Resultado", "#e74c3c")
        
        except Exception as e:
            self.show_popup(f"Error: {str(e)}", "Error", "#e74c3c")

    def show_popup(self, message, title, color):
        popup = tk.Toplevel(self.root)
        popup.title(title)
        popup.geometry("350x200")
        popup.configure(bg="#f7f9f9")

        label = tk.Label(
            popup, text=message, font=("Arial", 12, "bold"), bg="#f7f9f9", fg=color, wraplength=300
        )
        label.pack(pady=20)

        close_button = tk.Button(
            popup, text="Cerrar", font=("Arial", 12, "bold"), bg="#3498db", fg="white",
            relief="flat", padx=10, pady=5, borderwidth=1, command=popup.destroy
        )
        close_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = TmInterfaz(root)
    root.mainloop()
