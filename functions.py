def rank(level):
    if level is None:  # Valida se level é None
        raise ValueError("O nível não pode ser None")
    
    if level < 10:
        ranking = "Noob"
    elif 10 <= level < 20:  # Melhor uso de operadores de comparação
        ranking = "Estudioso"
    elif 20 <= level < 50:
        ranking = "Habilidoso"
    elif 50 <= level < 100:
        ranking = "Lenda"
    else:  # Se é maior que 100, não precisa de nova verificação
        ranking = "God"
        
    return ranking


def upar(exp, level):
    if exp == 100 or exp > 100:
        try:
            exp = 0
            level += 1  # Incremento simplificado
        except ValueError:  # Este try-except é desnecessário, mas mantive a estrutura
            print("Erro ao upar de nível")
    
    return exp, level  # Certifique-se de retornar exp e level para atualizar o jogo