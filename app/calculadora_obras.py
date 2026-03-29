# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; SEU_NOME
# ==========================================

def calcular_area_em_m2(altura, comprimento):
    """
    Calcula a área total de uma superfície em metros quadrados (m²).

    Parâmetros:
        altura (float): A medida da altura da superfície.
        comprimento (float): A medida do comprimento da superfície.

    Retorno:
        float: O resultado da multiplicação da altura pelo comprimento.
    """

    try:
        altura = float(altura)
        comprimento = float(comprimento)
    except ValueError:
        raise TypeError("O valor informado deve ser um número válido e não uma letra.")

    if altura <= 0 or comprimento <= 0:
        raise ValueError("Os valores de ALTURA e COMPRIMENTO devem ser maiores que zero")

    area_m2 = altura * comprimento

    return area_m2

def calcular_tijolos_por_parede(area_parede_m2, area_tijolo_m2):
    """
    Calcula a quantidade estimada de tijolos necessários para preencher uma parede.

    Parâmetros:
        area_parede_m2 (float): A área total da parede em metros quadrados.
        area_tijolo_m2 (float): A área que um único tijolo ocupa em metros quadrados.

    Retorno:
        float: A quantidade de tijolos (blocos) necessários, arredondada para duas casas decimais.
    """
    
    try:
        area_parede_m2 = float(area_parede_m2)
        area_tijolo_m2 = float(area_tijolo_m2)
    except ValueError:
        raise TypeError("O valor informado deve ser um número válido e não uma letra.")

    if area_parede_m2 <= 0 or area_tijolo_m2 <= 0:
        raise ValueError("Os valores de AREA_PAREDE e AREA_TIJO devem ser maiores que zero! A função 'calcular_area_em_m2(altura, comprimento)' vai te ajudar entregando o resultado final em m2")


    quantidade_de_blocos = round((area_parede_m2 / area_tijolo_m2), 2)

    return quantidade_de_blocos

# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: Pedro Gustavo;
# ==========================================

import math

def calcular_caixas_piso(area_ambiente_m2, rendimento_caixa_m2):
    # Calcula a quantidade de caixas de piso necessárias para um ambiente.
    
    # Parâmetros:
    # area_ambiente_m2: A área do ambiente em metros quadrados.
    # rendimento_caixa_m2: Quantos metros quadrados uma caixa cobre
    if rendimento_caixa_m2 <= 0:
        return "Erro: O rendimento da caixa deve ser maior que zero."
        
    # Divide a área exata pelo rendimento e arredonda para cima
    qtd_caixas = math.ceil(area_ambiente_m2 / rendimento_caixa_m2)
    
    return qtd_caixas

def calcular_rejunte_necessario(area_revestimento_m2, consumo_rejunte_kg_m2, tamanho_pacote_kg=1.0):
    # Calcula a quantidade de rejunte necessária para um ambiente.
    
    # Parâmetros:
    # area_revestimento_m2 : A área total de revestimento em metros quadrados.
    # consumo_rejunte_kg_m2 : Consumo de rejunte em kg por metro quadrado.
    # tamanho_pacote_kg : O peso de cada pacote de rejunte em kg (padrão é 1kg).
    if consumo_rejunte_kg_m2 <= 0:
        return "Erro: O consumo de rejunte deve ser maior que zero."
        
    # Calcula a quantidade total exata em kg (área * consumo)
    total_kg = area_revestimento_m2 * consumo_rejunte_kg_m2
    
    # Calcula quantos pacotes serão necessários // arredodando
    qtd_pacotes = math.ceil(total_kg / tamanho_pacote_kg)
    
    return {
        "total_kg": round(total_kg, 2),
        "quantidade_pacotes": qtd_pacotes
    }

def calcular_litros_tinta(area_pintura_m2, rendimento_lata_m2, quantidade_demaos):
    # Calcula a quantidade de latas/litros de tinta necessárias.
    
    # Parâmetros:
    # area_pintura_m2: A área total a ser pintada em metros quadrados.
    # rendimento_lata_m2: Quantos metros quadrados a embalagem de tinta cobre por demão.
    # quantidade_demaos: Número de demãos (camadas) que serão aplicadas.
    if rendimento_lata_m2 <= 0:
        return "Erro: O rendimento da lata deve ser maior que zero."
        
    # Multiplica a área pelo número de demãos para saber a área total de cobertura exigida
    area_total_cobertura = area_pintura_m2 * quantidade_demaos
    
    # Divide a área total de cobertura pelo rendimento da lata e arredonda para cima
    qtd_latas = math.ceil(area_total_cobertura / rendimento_lata_m2)
    
    return qtd_latas
# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: SEU_NOME
# ==========================================