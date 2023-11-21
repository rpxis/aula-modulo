from use_cases.buscar_por_cod import buscarPorCodigo
def editarProduto(codigo, nome, categoria, preco):
    produto = buscarPorCodigo(codigo)
    if produto:
        produto['codigo'] = codigo
        produto['nome'] = nome
        produto['categoria'] = categoria
        produto['preco'] = preco
        print('Dados alterado com sucesso!')

    else:
        print('Produto não encontrado!')


