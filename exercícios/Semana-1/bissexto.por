programa {
  funcao inicio() {
    inteiro ano
    logico divisivelPorQuatro, divisivelPorCem, divisivelPorQuatrocentos, bissexto

    escreva("Digite seu ano: ")
    leia(ano)

    divisivelPorQuatro = ano % 4 == 0
    divisivelPorCem = ano % 100 == 0
    divisivelPorQuatrocentos = ano % 400 == 0
    bissexto = divisivelPorQuatro && (!divisivelPorCem || divisivelPorQuatrocentos)

    se(bissexto == falso){
      escreva("Não é bissexto")
    } senao{
      escreva("É bissexto")
    }
  }
}
