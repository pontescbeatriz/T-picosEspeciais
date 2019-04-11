qpizza =  int ( input ( " Total de pizzas pedidas: " ))
ppizza =  float ( input ( " Valor da Pizza pedida: R $ " ))
valor = qpizza * ppizza
imposto = valor - valor * 0,8
total = valor + imposto
print ( " O valor total das pizzas são de: R $ % .2f "  % (total))
