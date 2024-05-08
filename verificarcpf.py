import random
#cpf = input("Digite o CPF para verificação.")
novo_cpf_final = ''
gerador_confirmado = True
gerar_cpf = []
while gerador_confirmado:
    gerar_cpf = []
    qtd_cpf = 0
    for i in range(11):
        gerar_cpf.append(str(random.randrange(0,9)))
        i += 1

    cpf_final = ''.join(gerar_cpf)
    nove_digito = cpf_final[:9]
    dez_digito = cpf_final[:10]
    verificacao = cpf_final[9:]

    contador_1 = 10
    contador_2 = 11
    resultado_primeiro_digito = 0
    resultado_segundo_digito = 0
    for digito in nove_digito:
        resultado_primeiro_digito += int(digito) * contador_1
        contador_1 -= 1
    for digito in dez_digito:
        resultado_segundo_digito += int(digito) * contador_2
        contador_2 -= 1

    primeiro_digito = (resultado_primeiro_digito * 10) % 11
    segundo_digito = (resultado_segundo_digito * 10) % 11


    if primeiro_digito > 9:
        primeiro_digito = 0
    if  segundo_digito > 9 :
        segundo_digito = 0



    if primeiro_digito == int(verificacao[0]) and segundo_digito == int(verificacao[1]):
        print('CPF válido.')
        gerador_confirmado = False
    
 


for index in range(len(str(cpf_final))):
    if not cpf_final[index] in '0123456789':continue 
    if index in [2,5]: novo_cpf_final += cpf_final[index] + "."
    elif index == 8 : novo_cpf_final += cpf_final[index] + "-"
    else: novo_cpf_final += cpf_final[index]


print(novo_cpf_final)