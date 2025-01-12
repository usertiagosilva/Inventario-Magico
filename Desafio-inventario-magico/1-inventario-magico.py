import sys
sys.stdout.reconfigure(encoding='utf-8')
import tkinter as tk
from PIL import Image, ImageTk, ImageEnhance


class InventarioMagicoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("INVENTÁRIO MÁGICO")

        # Dimensões da janela
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        # Configurar tamanho da janela para ocupar a tela inteira
        self.root.geometry(f"{self.width}x{self.height}")

        # Carregar e redimensionar o background
        self.background_image = Image.open("bg.jfif")
        self.background_image = self.background_image.resize((self.width, self.height), Image.LANCZOS)

        # Aplicar opacidade ao background
        enhancer = ImageEnhance.Brightness(self.background_image)
        self.background_image = enhancer.enhance(0.7)  # Para 70% de opacidade
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Adicionar o background à janela
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Configurar inventário
        self.inventario = []

        # Criar categorias e itens
        categorias = {
            "Itens Mágicos de Combate": [
                "📜 Pergaminho de Gelo", "🗡️ Adaga Envenenada", "🛡️ Escudo de Dragão",
                "🔥 Anel de Fogo", "❄️ Cetro de Gelo", "⚡ Bastão do Trovão",
                "💎 Amuleto da Proteção", "🌪️ Capa do Vento", "🖤 Elmo das Sombras", "🌟 Espada das Estrelas"
            ],
            "Poções e Consumíveis": [
                "🧪 Poção de Cura", "💧 Poção de Energia", "🍃 Poção da Invisibilidade",
                "🦋 Elixir da Vida Eterna"
            ],
        }

        # Botões dinâmicos para cada item em categorias
        y_position = 50
        for categoria, itens in categorias.items():
            tk.Label(
                self.root, text=categoria, font=("Arial", 11, "bold"), 
                bg="#333333", fg="white", relief="raised", bd=2, padx=5, pady=5
            ).place(x=50, y=y_position)
            y_position += 40
            for item in itens:
                button = tk.Button(
                    self.root, text=item, font=("Arial", 10), bg="#333333", fg="white", 
                    activebackground="#555555", activeforeground="white", bd=2, relief="raised",
                    command=lambda i=item: self.adicionar_item(i)
                )
                button.place(x=50, y=y_position, width=250, height=30)

                # Efeito hover aos botões
                button.bind("<Enter>", lambda e, btn=button: btn.config(bg="#555555"))
                button.bind("<Leave>", lambda e, btn=button: btn.config(bg="#333333"))

                y_position += 40
            y_position += 20

        # Botões de ação
        self.button_remove = tk.Button(
            self.root, text="Remover Último Item", command=self.remover_item, font=("Arial", 12),
            bg="#333333", fg="white", activebackground="#555555", activeforeground="white", bd=2, relief="raised"
        )
        self.button_remove.place(x=350, y=250, width=150, height=40)

        self.button_list = tk.Button(
            self.root, text="Listar Itens", command=self.listar_itens, font=("Arial", 12),
            bg="#333333", fg="white", activebackground="#555555", activeforeground="white", bd=2, relief="raised"
        )
        self.button_list.place(x=520, y=250, width=150, height=40)

        # Campo de saída estilizado
        self.output_label = tk.Label(
            self.root, text="", font=("Arial", 14), bg="#333333", fg="white", bd=2, relief="sunken", wraplength=600
        )
        self.output_label.place(x=350, y=300, width=600, height=300)

    def adicionar_item(self, item):
        self.inventario.append(item)
        self.output_label.config(text=f"'{item}' adicionado com sucesso!")

    def remover_item(self):
        if not self.inventario:
            self.output_label.config(text="O inventário está vazio.")
            return

        item_removido = self.inventario.pop()  # Remove o último item adicionado
        self.output_label.config(text=f"'{item_removido}' removido com sucesso!")

    def listar_itens(self):
        if self.inventario:
            itens = "\n".join(self.inventario)
            self.output_label.config(text=f"Itens no inventário:\n{itens}")
        else:
            self.output_label.config(text="O inventário está vazio.")


# Inicializar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioMagicoGUI(root)
    root.mainloop()



