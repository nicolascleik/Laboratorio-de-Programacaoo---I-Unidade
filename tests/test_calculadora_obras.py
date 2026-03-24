import pytest
from app.calculadora_obras import calcular_area_em_m2
from app.calculadora_obras import calcular_tijolos_por_parede

# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; SEU_NOME
# ==========================================

def test_calcular_area_em_m2_valores_esperados():
    altura_do_objeto = 10
    comprimento_do_objeto = 30

    resultado = calcular_area_em_m2(altura=altura_do_objeto, comprimento=comprimento_do_objeto)

    assert resultado == 300

def test_calcular_area_em_m2_valores_negativos_igual_a_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_area_em_m2(0, -20)

    assert "Os valores de ALTURA e COMPRIMENTO devem ser maiores que zero" in str(info_erro.value)

def test_calcular_area_em_m2_erro_de_digitacao():
    with pytest.raises(TypeError):
        calcular_area_em_m2("cem", 10)

# ------------------------------------------

def test_calcular_tijolos_por_parede_valores_esperados():
    area_do_tijolo = calcular_area_em_m2(altura=0.20, comprimento=0.30)
    area_da_parede = calcular_area_em_m2(altura=5, comprimento=10)

    resultado = calcular_tijolos_por_parede(area_parede_m2 = area_da_parede, area_tijolo_m2 = area_do_tijolo)

    assert resultado == 833.33

def test_calcular_tijolos_por_parede_valores_negativos_igual_a_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_tijolos_por_parede(0, -20)

    assert "Os valores de AREA_PAREDE e AREA_TIJO devem ser maiores que zero! A função 'calcular_area_em_m2(altura, comprimento)' vai te ajudar entregando o resultado final em m2" in str(info_erro.value)

def test_calcular_tijolos_por_parede_erro_de_digitacao():
    with pytest.raises(TypeError):
        calcular_tijolos_por_parede("cem", 10)

# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: SEU_NOME
# ==========================================,

# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: SEU_NOME
# ==========================================