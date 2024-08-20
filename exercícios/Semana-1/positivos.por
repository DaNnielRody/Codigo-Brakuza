programa {
  funcao inicio() {
    inteiro numero, contador = 0

    para(inteiro i = contador; i < 5; i++){
      escreva("Digite seu número: \n")
      leia(numero)
      
      se(numero > 0){
        contador+=1
      }
    }
    escreva("Você teve ", contador, " números positivos")
  }
}
