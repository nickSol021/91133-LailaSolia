import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from mercadinho import Produto, Mercadinho

class App:
    def __init__(self, root):
        self.mercado = Mercadinho()

        root.title("Mercadinho - CRUD")
        root.geometry("600x400")

        tk.Label(root, text="ID").grid(row=0, column=0)
        tk.Label(root, text="Nome").grid(row=0, column=1)
        tk.Label(root, text="Preço").grid(row=0, column=2)
        tk.Label(root, text="Qtd").grid(row=0, column=3)

        self.id_entry = tk.Entry(root, width=5)
        self.nome_entry = tk.Entry(root, width=15)
        self.preco_entry = tk.Entry(root, width=7)
        self.qtd_entry = tk.Entry(root, width=5)

        self.id_entry.grid(row=1, column=0)
        self.nome_entry.grid(row=1, column=1)
        self.preco_entry.grid(row=1, column=2)
        self.qtd_entry.grid(row=1, column=3)

        
        tk.Button(root, text="Adicionar", command=self.adicionar).grid(row=1, column=4)
        tk.Button(root, text="Editar", command=self.editar).grid(row=1, column=5)
        tk.Button(root, text="Remover", command=self.remover).grid(row=1, column=6)

     
        self.tree = ttk.Treeview(root, columns=("ID", "Nome", "Preço", "Qtd"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preço", text="Preço (R$)")
        self.tree.heading("Qtd", text="Quantidade")
        self.tree.grid(row=2, column=0, columnspan=7, padx=10, pady=10, sticky="nsew")

        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def atualizar_tabela(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for p in self.mercado.listar_produtos():
            self.tree.insert("", "end", values=(p.id, p.nome, f"{p.preco:.2f}", p.quantidade))

    def adicionar(self):
        try:
            id = int(self.id_entry.get())
            nome = self.nome_entry.get()
            preco = float(self.preco_entry.get())
            qtd = int(self.qtd_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")
            return

        produto = Produto(id, nome, preco, qtd)
        if not self.mercado.adicionar_produto(produto):
            messagebox.showwarning("Aviso", "ID já existente!")
        else:
            self.atualizar_tabela()

    def remover(self):
        try:
            id = simpledialog.askinteger("Remover Produto", "Digite o ID do produto que deseja remover:")
            if id is None:
                return

            if self.mercado.remover_produto(id):
                messagebox.showinfo("Sucesso", "Produto removido com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Produto não encontrado.")

            self.atualizar_tabela()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

    def editar(self):
      
        item = self.tree.selection()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um produto para editar.")
            return

        valores = self.tree.item(item)["values"]
        id = valores[0]

        novo_nome = simpledialog.askstring("Editar", "Novo nome:", initialvalue=valores[1])
        novo_preco = simpledialog.askfloat("Editar", "Novo preço:", initialvalue=float(valores[2]))
        nova_qtd = simpledialog.askinteger("Editar", "Nova quantidade:", initialvalue=valores[3])

        self.mercado.atualizar_produto(id, {
            "nome": novo_nome,
            "preco": novo_preco,
            "quantidade": nova_qtd
        })
        self.atualizar_tabela()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
