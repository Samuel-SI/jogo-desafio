from personagem import Personagem
import random

class Vilao(Personagem):
    """Chefão com sistema de Inteligência Artificial e Modo Fúria."""
    
    def __init__(self, nome, vida_max, ataque, defesa, agilidade, maldade):
        super().__init__(nome, vida_max, ataque, defesa, agilidade)
        self.maldade = maldade
        self.em_furia = False

    def resetar(self):
        super().resetar()
        self.em_furia = False

    def ativar_furia_se_necessario(self):
        """Passiva: Ativa ao ficar com pouca vida."""
        if not self.em_furia and self.vida_atual < (self.vida_max * 0.3):
            self.em_furia = True
            self.ataque += 15  # Buff permanente
            return f"💢 MODO FÚRIA! Os olhos de {self.nome} brilham em vermelho. Seu ataque aumentou!"
        return ""

    def decisao_ia(self, heroi):
        """Decide o próximo movimento considerando a fúria."""
        msg_furia = self.ativar_furia_se_necessario()
        acoes_log = [msg_furia] if msg_furia else []

        if self.em_furia:
            escolha = random.choices(["atacar", "roubo_vida"], weights=[60, 40])[0]
        else:
            escolha = random.choices(["atacar", "defender"], weights=[70, 30])[0]

        if escolha == "atacar":
            dano, msg_def = heroi.sofrer_dano(self.ataque)
            acoes_log.append(f"👹 {self.nome} atacou! Você sofreu {dano} de dano.")
            if msg_def: acoes_log.append(msg_def)
        elif escolha == "roubo_vida":
            dano, msg_def = heroi.sofrer_dano(self.ataque * 0.8)
            cura = dano * 0.5
            self.vida_atual = min(self.vida_max, self.vida_atual + cura)
            acoes_log.append(f"🦇 DRENAR! {self.nome} causou {dano} de dano e curou {int(cura)} HP.")
            if msg_def: acoes_log.append(msg_def)
        else:
            acoes_log.append(self.defender())

        return "\n> ".join(acoes_log)