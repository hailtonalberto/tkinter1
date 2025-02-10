import tkinter as tk
from tkinter import ttk
#criar uma janela
janela =tk.Tk()
#criar o tema da janela
janela.title("cotação de moedas")

janela.rowconfigure(0,weight=1)
janela.columnconfigure([0,1],weight=1)

#bg tela de fundo e fg letras
mensagem = tk.Label(text='SISTEMA DE COTAÇÕES DE MOEDAS',fg="white",bg="black",width=35,height=5)
mensagem.grid(row=0,column=0,columnspan=2,sticky="NSEW")

mensagem2 =tk.Label(text="selecione a moeda desejada")
mensagem2.grid(row=1,column=0)

#moeda = tk.Entry()
#moeda.grid(row=2,column=2)



dicionario_cotacoes = {
    "dolar": 5.47,
    "euro": 6.64,
    "bitcoin": 20000,
}
moedas = list(dicionario_cotacoes.keys())

moeda = ttk.Combobox(janela,values=moedas)
moeda.grid(row=2,column=2)
def buscar_cotação():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="")
    mensagem_cotacao.grid(row=3,column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f"cotacao do {moeda_preenchida} é de {cotacao_moeda} reais"



botao = tk.Button(text="buscar cotação",command=buscar_cotação)
botao.grid(row=2,column=1)

mensagem3 = tk.Label(text="caso queira pegar mais de 1 cotacao ao mesmo tempo,digite uma moeda em cada linha")
mensagem3.grid(row=4,column=0,columnspan=2)

caixa_texto = tk.Text(width=10,height=5)
caixa_texto.grid(row=5,column=0,sticky="nswe")

def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)
    lista_moedas = texto.split('\n')
    mensagem_cotacao = []
    for item in lista_moedas:
        cotacao = dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacao.append(f"{item}: {cotacao}")
    mensagem4 = tk.Label(text="\n".join(mensagem_cotacao))
    mensagem4.grid(row=6,column=1)


botao_multiplascotacoes = tk.Button(text="buscar cotacoes",command=buscar_cotacoes)
botao_multiplascotacoes.grid(row=5,column=1)

janela.mainloop()


