programa {
  funcao inicio() {
    inteiro numero, fatorial = 1
    
    escreva("Digite seu número: ")
    leia(numero)

    escreva("Fatorial de: ", numero,"! = ")

    para(inteiro i = numero; i >= 1; i--){
      fatorial *= i
      se(i > 1){
        escreva(i, " x ")
      }senao{
        escreva(i, " = ", fatorial)
      }
    }
  }
}
