opcao = 0
alunos = []

while (opcao <= 2):
        

    print ("======================================================================")
    print ("======================================================================")
    print ("======================================================================")
    print ("==========/------------------------------------------------\==========")
    print ("=========/              OLÁ, SEJAM BEM VINDOS!              \=========")
    print ("========|          UNIVERSIDADE FEDERAL DA PARAIBA           |========")
    print ("========|      CENTRO DE CIÊNCIAS APLICADAS E EDUCAÇÃO       |========")
    print ("========|                                                    |========")
    print ("========|            CURSINHO PRÉ VESTIBULAR 2016            |========")
    print ("========|                                                    |========")
    print ("========|         CAMPUS IV - RIO TINTO E MAMANGUAPE         |========")
    print ("========\        OBRIGADO POR ACREDITAR NESSE PROJETO        /========")
    print ("=========\--------------------------------------------------/=========")
    print ("======================================================================")
    print ("======================================================================")
    print ("======================================================================")

    opcaomenu = int(input("DIGITE [1] PARA CADASTRAR NOVO ALUNO, DIGITE [2] PARA VER SITUAÇÃO DO ALUNO :"))

    if (opcaomenu == 1):
        
        print ("========|     MATRICULAR ALUNO     |========")
        continuar = "sim"
        
        while continuar == "sim" or continuar == "SIM":
            
            nome = str(input("Por favor, digite o nome do aluno: "))
            idade = int(input("Agora digite a idade do aluno: "))
            cpf = int(input("digite seu cpf:"))
            deficiencia = str(input("O aluno possui alguma deficiência? "))
            cor = str(input("Qual etinia o aluno se declara? "))
            escola = str(input("O aluno é de escola pública ou particular? "))
            pai = str(input("Filiação - PAI: "))
            mae = str(input("Filiação - MÃE: "))
            cidade = str(input("Cidade: "))
            estado = str(input("Estado: "))
            email = str(input("E-mail: "))
            alunos.append([nome,idade,cpf, deficiencia, cor, escola, pai, mae, cidade, estado, email])
            print ("Múito obrigado, o aluno já está cadastrado")
            continuar = str(input("VOCÊ DESEJA CONTINUAR? [SIM / NÃO]?:" ))
    elif (opcaomenu == 2):
        print ("========|     ALUNOS MATRICULADOS     |========")
        for i in range(len(alunos)):
        
            print(i+1,":",alunos[i])



    else :
        print ("Opção invalida!")
    
    
    


