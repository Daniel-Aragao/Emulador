# CPU
MAIOR_INTEIRO = 4294967296
MAIOR_REGISTRADOR = ord('D')
MENOR_REGISTRADOR = ord('A')

# MEMORIA
CODIGO_SIZE = 4
MEMORIA_TAMANHO_MINIMO = 32
MEMORIA_TAMANHO_MAXIMO = 32 * (2**30)
MEMORIA_TAMANHO = MEMORIA_TAMANHO_MINIMO


def memoria_particao_codigo():
    return MEMORIA_TAMANHO / 2


def memoria_particao_dados():
    return MEMORIA_TAMANHO / 2


# BARRAMENTO
CLOCK_MINIMO = 100
CLOCK_MAXIMO = 1000000000
TAMANHO_MINIMO_LARGURA_BARRAMENTO = 8
TAMANHO_MAXIMO_LARGURA_BARRAMENTO = 128

CLOCK = CLOCK_MINIMO
LARGURA_BARRAMENTO = 8
LARGURA_DE_BANDA = CLOCK * LARGURA_BARRAMENTO