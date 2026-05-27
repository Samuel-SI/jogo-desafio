import customtkinter as ctk
from heroi import Heroi
from vilao import Vilao

class JogoRPG(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Defensores de OOP - Edição Épica")
        self.geometry("900x700")
        ctk.set_appearance_mode("dark")
        self.resizable(False, False)

        # 1. Energia Aumentada e Mais Opções de Personagens!
        self.herois_disponiveis = {
            "Guerreiro Link": Heroi("Link", 180, 25, 15, 10, energia_max=120, inventario_inicial={"Poção de Cura": 4, "Poção de Mana": 2}),
            "Maga Zelda": Heroi("Zelda", 110, 45, 5, 20, energia_max=250, inventario_inicial={"Poção de Cura": 3, "Poção de Mana": 5}),
            "Arqueiro Legolas": Heroi("Legolas", 140, 30, 10, 35, energia_max=150, inventario_inicial={"Poção de Cura": 3, "Poção de Mana": 3}),
            "Paladino Arthur": Heroi("Arthur", 220, 20, 25, 5, energia_max=100, inventario_inicial={"Poção de Cura": 5, "Poção de Mana": 1})
        }
        self.viloes_disponiveis = {
            "Lorde Ganon": Vilao("Ganon", 250, 30, 20, 5, "Alta"),
            "Rei Caveira": Vilao("Caveira", 180, 40, 10, 15, "Média"),
            "Dragão Smaug": Vilao("Smaug", 350, 45, 25, 5, "Alta"),
            "Bruxa Morgana": Vilao("Morgana", 160, 55, 5, 25, "Alta")
        }

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)
        self.mostrar_tela_selecao()

    def limpar_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def mostrar_tela_selecao(self):
        self.limpar_container()
        self.turno_bloqueado = False

        ctk.CTkLabel(self.container, text="⚔️ SELEÇÃO DE COMBATENTES ⚔️", font=("Consolas", 32, "bold")).pack(pady=40)

        frame_selecao = ctk.CTkFrame(self.container, fg_color="transparent")
        frame_selecao.pack(pady=20)

        ctk.CTkLabel(frame_selecao, text="Escolha seu Herói:").grid(row=0, column=0, padx=20, pady=10)
        self.combo_heroi = ctk.CTkComboBox(frame_selecao, values=list(self.herois_disponiveis.keys()), width=200)
        self.combo_heroi.grid(row=1, column=0, padx=20)

        ctk.CTkLabel(frame_selecao, text="Escolha o Vilão:").grid(row=0, column=1, padx=20, pady=10)
        self.combo_vilao = ctk.CTkComboBox(frame_selecao, values=list(self.viloes_disponiveis.keys()), width=200)
        self.combo_vilao.grid(row=1, column=1, padx=20)

        ctk.CTkButton(self.container, text="INICIAR BATALHA", height=50, font=("Arial", 16, "bold"), command=self.iniciar_batalha).pack(pady=30)

    def iniciar_batalha(self):
        self.heroi_atual = self.herois_disponiveis[self.combo_heroi.get()]
        self.vilao_atual = self.viloes_disponiveis[self.combo_vilao.get()]
        self.heroi_atual.resetar()
        self.vilao_atual.resetar()
        self.mostrar_tela_batalha()

    def mostrar_tela_batalha(self):
        self.limpar_container()
        self.container.grid_columnconfigure((0, 1), weight=1)

        # --- Frames Visuais ---
        frame_heroi = ctk.CTkFrame(self.container, fg_color="#1a331a")
        frame_heroi.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        ctk.CTkLabel(frame_heroi, text=self.heroi_atual.nome, font=("Consolas", 24, "bold"), text_color="#55ff55").pack(pady=5)
        self.lbl_hp_heroi = ctk.CTkLabel(frame_heroi, text="")
        self.lbl_hp_heroi.pack()
        self.lbl_energia = ctk.CTkLabel(frame_heroi, text="", text_color="#55aaff")
        self.lbl_energia.pack()

        frame_vilao = ctk.CTkFrame(self.container, fg_color="#331a1a")
        frame_vilao.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")
        ctk.CTkLabel(frame_vilao, text=self.vilao_atual.nome, font=("Consolas", 24, "bold"), text_color="#ff5555").pack(pady=5)
        self.lbl_hp_vilao = ctk.CTkLabel(frame_vilao, text="")
        self.lbl_hp_vilao.pack()

        # --- Log ---
        self.log_box = ctk.CTkTextbox(self.container, height=200, font=("Consolas", 14), state="disabled")
        self.log_box.grid(row=1, column=0, columnspan=2, padx=15, pady=10, sticky="nsew")

        # --- Ações (Reorganizadas) ---
        frame_botoes = ctk.CTkFrame(self.container, fg_color="transparent")
        frame_botoes.grid(row=2, column=0, columnspan=2, pady=5)

        # Linha 1 de Botões
        self.btn_atacar = ctk.CTkButton(frame_botoes, text="Atacar 🗡️", command=lambda: self.acao_jogador("atacar"), width=130)
        self.btn_atacar.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_especial = ctk.CTkButton(frame_botoes, text="Especial ⚡", fg_color="#aa5500", command=lambda: self.acao_jogador("especial"), width=130)
        self.btn_especial.grid(row=0, column=1, padx=5, pady=5)

        self.btn_magia = ctk.CTkButton(frame_botoes, text="Magia 🔥", fg_color="#8a1a1a", hover_color="#b30000", command=lambda: self.acao_jogador("magia"), width=130)
        self.btn_magia.grid(row=0, column=2, padx=5, pady=5)

        # Linha 2 de Botões
        self.btn_defender = ctk.CTkButton(frame_botoes, text="Defender 🛡️", command=lambda: self.acao_jogador("defender"), width=130)
        self.btn_defender.grid(row=1, column=0, padx=5, pady=5)

        self.btn_cura = ctk.CTkButton(frame_botoes, text="Cura 💖", fg_color="#2b8a2b", command=lambda: self.acao_jogador("cura"), width=130)
        self.btn_cura.grid(row=1, column=1, padx=5, pady=5)

        self.btn_mana = ctk.CTkButton(frame_botoes, text="Mana 🔵", fg_color="#2b2b8a", command=lambda: self.acao_jogador("mana"), width=130)
        self.btn_mana.grid(row=1, column=2, padx=5, pady=5)

        ctk.CTkButton(self.container, text="Fugir 🏃", fg_color="#555", command=self.mostrar_tela_selecao).grid(row=3, column=0, columnspan=2, pady=10)

        self.atualizar_interface()
        self.adicionar_log(f"Batalha iniciada! O destino de todos está nas mãos de {self.heroi_atual.nome}.")

    def atualizar_interface(self):
        self.lbl_hp_heroi.configure(text=f"HP: {int(self.heroi_atual.vida_atual)} / {self.heroi_atual.vida_max}")
        self.lbl_energia.configure(text=f"Energia: {int(self.heroi_atual.energia_atual)} / {self.heroi_atual.energia_max}")
        self.lbl_hp_vilao.configure(text=f"HP: {int(self.vilao_atual.vida_atual)} / {self.vilao_atual.vida_max}")
        
        c = self.heroi_atual.inventario.get('Poção de Cura', 0)
        m = self.heroi_atual.inventario.get('Poção de Mana', 0)
        self.btn_cura.configure(text=f"Cura ({c}) 💖")
        self.btn_mana.configure(text=f"Mana ({m}) 🔵")

    def adicionar_log(self, mensagem):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"\n> {mensagem}")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")

    def acao_jogador(self, acao):
        if getattr(self, 'turno_bloqueado', False): return
        self.turno_bloqueado = True

        if acao == "atacar":
            dano, msg_def = self.vilao_atual.sofrer_dano(self.heroi_atual.ataque)
            self.adicionar_log(f"Você atacou e causou {dano} de dano!")
            if msg_def: self.adicionar_log(msg_def)
        elif acao == "especial":
            sucesso, msg = self.heroi_atual.ataque_carregado(self.vilao_atual)
            self.adicionar_log(msg)
            if not sucesso:
                self.turno_bloqueado = False
                return
        elif acao == "magia":
            sucesso, msg = self.heroi_atual.magia_elemental(self.vilao_atual)
            self.adicionar_log(msg)
            if not sucesso:
                self.turno_bloqueado = False
                return
        elif acao == "defender":
            self.adicionar_log(self.heroi_atual.defender())
        elif acao == "cura":
            sucesso, msg = self.heroi_atual.usar_item("Poção de Cura")
            self.adicionar_log(msg)
            if not sucesso:
                self.turno_bloqueado = False
                return
        elif acao == "mana":
            sucesso, msg = self.heroi_atual.usar_item("Poção de Mana")
            self.adicionar_log(msg)
            if not sucesso:
                self.turno_bloqueado = False
                return

        self.atualizar_interface()

        if not self.vilao_atual.esta_vivo():
            self.finalizar_jogo(vitoria=True)
            return

        self.after(1200, self.turno_inimigo)

    def turno_inimigo(self):
        msg = self.vilao_atual.decisao_ia(self.heroi_atual)
        self.adicionar_log(msg)
        self.atualizar_interface()

        if not self.heroi_atual.esta_vivo():
            self.finalizar_jogo(vitoria=False)
        else:
            self.adicionar_log("--- Seu Turno ---")
            self.turno_bloqueado = False

    def finalizar_jogo(self, vitoria):
        self.turno_bloqueado = True
        if vitoria:
            self.adicionar_log(f"🏆 {self.vilao_atual.nome} foi destruído!")
            self.adicionar_log(self.heroi_atual.ganhar_xp(120))
        else:
            self.adicionar_log(f"💀 O herói caiu. As trevas venceram.")