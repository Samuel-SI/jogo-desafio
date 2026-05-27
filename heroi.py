from personagem import Personagem

class Heroi(Personagem):
    """Herói com sistema de Energia, Habilidades Especiais e Nível."""
    
    def __init__(self, nome, vida_max, ataque, defesa, agilidade, energia_max, inventario_inicial=None):
        super().__init__(nome, vida_max, ataque, defesa, agilidade)
        self.energia_max = energia_max
        self.energia_atual = energia_max
        self.nivel = 1
        self.xp = 0
        self.inventario_inicial = inventario_inicial if inventario_inicial else {"Poção de Cura": 3, "Poção de Mana": 1}
        self.inventario = self.inventario_inicial.copy()

    def resetar(self):
        super().resetar()
        self.energia_atual = self.energia_max
        self.inventario = self.inventario_inicial.copy()

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        if self.xp >= 100:
            self.nivel += 1
            self.xp = 0
            self.vida_max += 20
            self.ataque += 5
            return f"🌟 LEVEL UP! {self.nome} alcançou o nível {self.nivel}!"
        return f"✨ {self.nome} ganhou {quantidade} XP."

    def ataque_carregado(self, alvo):
        custo = 20
        if self.energia_atual >= custo:
            self.energia_atual -= custo
            dano_causado, msg = alvo.sofrer_dano(self.ataque * 2.5)
            return True, f"⚡ GOLPE CRÍTICO! Causou {dano_causado} de dano! {msg}"
        return False, "❌ Sem energia suficiente para o golpe especial!"

    def magia_elemental(self, alvo):
        """Novo ataque que consome mais energia, mas ignora parte da esquiva."""
        custo = 35
        if self.energia_atual >= custo:
            self.energia_atual -= custo
            # Reduzimos a agilidade do alvo temporariamente para a magia
            agilidade_original = alvo.agilidade
            alvo.agilidade = max(0, alvo.agilidade - 15) 
            dano_causado, msg = alvo.sofrer_dano(self.ataque * 1.8)
            alvo.agilidade = agilidade_original # Restaura a agilidade
            return True, f"🔥 MAGIA ELEMENTAL! Uma explosão causou {dano_causado} de dano! {msg}"
        return False, "❌ Sem energia para conjurar magia!"

    def usar_item(self, item):
        if self.inventario.get(item, 0) > 0:
            self.inventario[item] -= 1
            if item == "Poção de Cura":
                cura = self.vida_max * 0.5
                self.vida_atual = min(self.vida_max, self.vida_atual + cura)
                return True, f"❤️ Curou {int(cura)} HP!"
            elif item == "Poção de Mana":
                self.energia_atual = self.energia_max
                return True, "🔵 Energia restaurada ao máximo!"
        return False, f"❌ Você não tem mais {item}!"