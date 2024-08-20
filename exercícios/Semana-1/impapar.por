programa {
  funcao inicio() {
    // O número não pode ser real, porque tem que evitar número decimal:
    inteiro numero

    escreva("Digite seu número: ")
    leia(numero)

    se(numero % 2 == 0){
      escreva("Par")
    }senao{
      escreva("Ímpar")
    }
  }
}
