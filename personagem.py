import random

class Personagem:
    """Classe base com sistema de esquiva e vida."""
    
    def __init__(self, nome, vida_max, ataque, defesa, agilidade):
        self.nome = nome
        self.vida_max = vida_max
        self.vida_atual = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.agilidade = agilidade  # Porcentagem de chance de esquiva (ex: 10 = 10%)
        self.esta_defendendo = False

    def resetar(self):
        """Restaura o personagem para uma nova batalha."""
        self.vida_atual = self.vida_max
        self.esta_defendendo = False

    def esta_vivo(self):
        return self.vida_atual > 0

    def sofrer_dano(self, dano):
        """Processa o dano recebido, considerando esquiva e defesa."""
        # 1. Tentativa de Esquiva
        if random.randint(1, 100) <= self.agilidade:
            return 0, f"💨 {self.nome} foi mais rápido e ESQUIVOU do ataque!"

        # 2. Cálculo com Defesa
        if self.esta_defendendo:
            dano_real = max(1, dano - (self.defesa * 2)) # Defesa bloqueia muito dano
            self.esta_defendendo = False
            msg_defesa = f"🛡️ {self.nome} bloqueou parte do golpe!"
        else:
            dano_real = max(1, dano - (self.defesa * 0.5)) # Dano base com leve redução da armadura
            msg_defesa = ""

        self.vida_atual = max(0, self.vida_atual - dano_real)
        return int(dano_real), msg_defesa

    def defender(self):
        self.esta_defendendo = True
        return f"🛡️ {self.nome} levantou a guarda e se preparou para o impacto!"