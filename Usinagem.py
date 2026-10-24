import math
import questionary

def ler_numero(mensagem):
    while True:
        entrada = input(mensagem).replace(',', '.').strip()
        try:
            return float(entrada)
        except ValueError:
            print("❌ Valor inválido! Por favor, digite um número (ex: 12.5 ou 12,5).")

def dimensõesiniciais():
    print("\n--- Digite as dimensões brutas da peça (mm) ---")
    comprimento = ler_numero("Digite o comprimento inicial da peça (em mm): ")
    largura = ler_numero("Digite a largura inicial da peça (em mm): ")
    altura = ler_numero("Digite a altura inicial da peça (em mm): ")
    return comprimento, largura, altura

def dimensõesfinais():
    print("\n--- Digite as dimensões finais da peça (mm) ---")
    comprimento_final = ler_numero("Digite o comprimento final da peça (em mm): ")
    largura_final = ler_numero("Digite a largura final da peça (em mm): ")
    altura_final = ler_numero("Digite a altura final da peça (em mm): ")
    return comprimento_final, largura_final, altura_final

def material():
    c_inicial, l_inicial, a_inicial = dimensõesiniciais()
    c_final, l_final, a_final = dimensõesfinais()
    
    if c_final > c_inicial or l_final > l_inicial or a_final > a_inicial:
        print("\n⚠️  ATENÇÃO: Pelo menos uma dimensão final é maior que a peça bruta!")
        return

    if c_final == c_inicial and l_final == l_inicial and a_final == a_inicial:
        print("\nAs dimensões finais são iguais às iniciais. Nenhum material será removido.")
        return

    remoção_comprimento = c_inicial - c_final
    remoção_largura = l_inicial - l_final
    remoção_altura = a_inicial - a_final

    print("\n--- Quantidade de material a ser removido ---")
    print(f"Comprimento: {remoção_comprimento:.2f} mm")
    print(f"Largura:     {remoção_largura:.2f} mm")
    print(f"Altura:      {remoção_altura:.2f} mm")

def avm(rpm_predefinido=None):
    print("\n--- Cálculo de Avanço por Minuto (AVM) ---")
    
    if rpm_predefinido is not None:
        rpm = rpm_predefinido
        print(f"Usando o RPM calculado anteriormente: {rpm:.2f}")
    else:
        rpm = ler_numero("Digite o RPM da máquina: ")

    avanço_por_dente = ler_numero("Digite o avanço por dente (mm/dente): ")
    numero_dentes = ler_numero("Digite o número de dentes da ferramenta: ")

    avm_resultado = rpm * avanço_por_dente * numero_dentes
    print(f"\nO Avanço por Minuto (AVM) calculado é: {avm_resultado:.2f} mm/min")

def calculo_rpm():
    print("\n--- Cálculo de RPM ---")
    velocidade_corte = ler_numero("Digite a velocidade de corte (m/min): ")
    diametro_ferramenta = ler_numero("Digite o diâmetro da ferramenta (mm): ")

    rpm = (1000 * velocidade_corte) / (math.pi * diametro_ferramenta)
    print(f"\nO RPM calculated é: {rpm:.2f} rotações por minuto")
    
    # Menu interativo para sim/não
    resposta = questionary.select(
        "Quer saber o Avanço por Minuto (AVM) com base nesse RPM?",
        choices=["Sim", "Não"]
    ).ask()
    
    if resposta == "Sim":
        avm(rpm_predefinido=rpm)
    else:
        print("\nObrigado por usar o programa de usinagem!")

def main():
    while True:
        print("\n=== PROGRAMA DE USINAGEM ===")
        
        # Menu principal interativo
        opcao = questionary.select(
            "O que vamos calcular hoje?",
            choices=[
                "1 - RPM",
                "2 - Material a remover",
                "3 - AVM (Avanço por Minuto)",
                "Sair"
            ]
        ).ask()
        
        if opcao == "1 - RPM":
            calculo_rpm()
            break
        elif opcao == "2 - Material a remover":
            material()
            break
        elif opcao == "3 - AVM (Avanço por Minuto)":
            avm()
            break
        elif opcao == "Sair" or opcao is None:
            print("\nEncerrando o programa. Através do corte, a precisão!")
            break

if __name__ == "__main__":
    main()