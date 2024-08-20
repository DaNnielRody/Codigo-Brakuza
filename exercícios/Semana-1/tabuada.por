programa {
  funcao inicio() {
    inteiro numero, index = 1

    escreva("Digite seu número: ")
    leia(numero)

    escreva("Tabuada de ", numero, "\n")

    para(inteiro i = 1; i<= 10; i++){
      escreva(numero, " x ", i, " = ", (numero * i), "\n")
    }
  }
}
