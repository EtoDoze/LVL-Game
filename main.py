import json
import functions
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

# Carregar os dados do arquivo JSON
with open("banco.json") as banco:
    dados = json.load(banco)

level = dados["levelj"]
exp = dados["expj"]
ranking = dados["rankingj"]

# Função que será chamada quando o estado das checkboxes mudar
def atualizar_exp():
    global level, exp, ranking
    
    # Verifica se alguma checkbox foi marcada
    if var1.get() or var2.get() or var3.get() or var4.get():
        exp += 10

    # Verifica se XP chegou a 100
    if exp >= 100:
        exp = 0
        level += 1
        ranking = functions.rank(level)
        messagebox.showinfo("Parabéns!", f"Você subiu para o nível {level}!")  # Mensagem de nível

    # Atualiza os dados no dicionário
    dados["levelj"] = level
    dados["expj"] = exp
    dados["rankingj"] = ranking

    # Atualiza a barra de progresso e os rótulos
    barra_progresso["value"] = exp
    label2.config(text=f"Level: {level}       XP: {exp}       Ranking: {ranking}")

    # Salva os dados no arquivo JSON
    try:
        with open("banco.json", 'w') as bancoW:
            json.dump(dados, bancoW, indent=4)
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")


# Criar a janela principal
janela = tk.Tk()
janela.title("LVL Game")
janela.geometry("400x600")
janela.config(bg="darkgray")

# Criar um rótulo (label)
label = tk.Label(janela, text="STATUS")
label.pack(pady=10)
label.config(font=("Helvetica", 16, "bold"))

label2 = tk.Label(janela, text=f"Level: {level}       XP: {exp}       Ranking: {ranking}")
label2.config(font=("Arial", 14))
label2.pack(pady=20)

# Criar a barra de progresso
barra_progresso = ttk.Progressbar(janela, orient="horizontal", length=200, mode="determinate")
barra_progresso.pack(pady=10)
barra_progresso["maximum"] = 100
barra_progresso["value"] = exp  # Inicializa a barra com o valor da XP

# Variáveis associadas a cada checkbox
var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()

# Criar checkboxes
checkbox1 = tk.Checkbutton(janela, text="5 questões de matemática", variable=var1, command=atualizar_exp)
checkbox1.pack(pady=10)
checkbox1.config(bg="darkgray", fg="black", font=("Arial", 10, 'bold'))  # Muda a cor do fundo, texto e a fonte do label

checkbox2 = tk.Checkbutton(janela, text="Estudar inglês (30 min)", variable=var2, command=atualizar_exp)
checkbox2.pack(pady=10)
checkbox2.config(bg="darkgray", fg="black", font=("Arial", 10, 'bold'))  # Muda a cor do fundo, texto e a fonte do label

checkbox3 = tk.Checkbutton(janela, text="Soltar o Jabuti", variable=var3, command=atualizar_exp)
checkbox3.pack(pady=10)
checkbox3.config(bg="darkgray", fg="black", font=("Arial", 10, 'bold'))  # Muda a cor do fundo, texto e a fonte do label

checkbox4 = tk.Checkbutton(janela, text="Criar o site do vídeo", variable=var4, command=atualizar_exp)
checkbox4.pack(pady=10)
checkbox4.config(bg="darkgray", fg="black", font=("Arial", 10, 'bold'))  # Muda a cor do fundo, texto e a fonte do label

imagem = tk.PhotoImage(file="sonic 360.gif")
label_imagem = tk.Label(janela, image=imagem)
label_imagem.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.resizable(True, True)  # Permite redimensionar livremente
janela.mainloop()
