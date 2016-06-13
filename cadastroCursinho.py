def dadosDoAluno(numeroCpf):
    
    for i in range(len(alunos)):
        
        if(alunos[i][2] == numeroCpf):            
            return(alunos[i])
    else:
        
        return False

alunos = []


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
print ("==========/------------------------------------------------\==========")
print ("=========/              1 = CADASTRAR NOVO ALUNO.           \=========")
print ("========|               2 = DADOS DO ALUNO.                  |========")
print ("========\               3 = FECHAR O PROGRMA.                /========")
print ("=========\--------------------------------------------------/=========")
print ("======================================================================")
print ("==========/------------------------------------------------\==========")
print ("=========/         EDUCAÇÃO NÃO TRANSFORMA O MUNDO.         \=========")
print ("========|          EDUCAÇÃO MUDA AS PESSOAS.                 |========")
print ("========|          PESSOAS TRANSFORMAM O MUNDO.              |========")
print ("========|                                                    |========")
print ("========\                                     (PAULO FREIRE) /========")
print ("=========\--------------------------------------------------/=========")
print ("======================================================================")
print ("======================================================================")
print ("======================================================================")
print ("")
print ("")
print ("")

continuar = "sim"

while(continuar=="sim"):
        opcaomenu = int(input(":...:::::::::::::::::::: O QUE DESEJA FAZER? ::::::::::::::::::::...: "))


        if (opcaomenu == 1):

                print("")
                print("")
                nome = str(input(":...:: NOME DO ALUNO ::...: "))                
                idade = input(":...:: IDADE DO ALUNO ::...: ")                
                cpf = str(input(":...:: CPF DO ALUNO ::...: "))
                deficiencia = str.lower(input(":...:: O ALUNO É PORTADOR DE NECESSIDADES ESPECIAIS? ::...: "))
                cor = str(input("...:: QUAL O TIPO DE ETINIA DO ALUNO? ::...: "))
                escola = str(input(":...:: O ALUNO É DE ESCOLA PÚBLICA OU PARTICULAR? ::...: "))
                pai = str(input(":...:: FILIAÇÃO - PAI ::...: "))
                mae = str(input(":...:: FILIAÇÃO - MÃE ::...: "))
                cidade = str(input(":...:: CIDADE ::...: "))
                estado = str(input(":...:: ESTADO ::...: "))
                email = str(input(":...:: E-MAIL ::...: "))
                alunos.append([nome,idade,cpf, deficiencia, cor, escola, pai, mae, cidade, estado, email])
                print ("")
                print (":...:: MUITO OBRIGADO, O ALUNO JÁ ESTA CADASTRADO ::...:")
                print ("")
        elif(opcaomenu == 2):

            
            localizar = str(input(":...:: DIGITE O CPF DO ALUNO ::...:"))
                       
            while(localizar == ""):
                localizar = input(":...:: DIGITE O CPF DO ALUNO ::...:")

            
            aluno = dadosDoAluno(localizar)

            
            if(aluno != False):
                
                print("")
                print("")
                print("\n:...:: NOME DO ALUNO ::...: \n"+aluno[0])
                print("\n:...:: IDADE DO ALUNO ::...: \n"+aluno[1])
                print("\n:...:: CPF DO ALUNO ::...: \n"+aluno[2])
                print("\n:...:: O ALUNO É PORTADOR DE ALGUMA DEFICIÊNCIA? ::...: \n"+aluno[3])
                print("\n:...:: ETINIA DO ALUNO ::...: \n"+aluno[4])
                print("\n:...:: TIPO DE ESCOLA DO ALUNO ::...: \n"+aluno[5])
                print("\n:...:: FILIAÇÃO - PAI ::...: \n"+aluno[6])
                print("\n:...:: FILIAÇÃO - MÃE ::...: \n"+aluno[7])
                print("\n:...:: CIDADE ::...: \n"+aluno[8])
                print("\n:...:: ESTADO ::...: \n"+aluno[9])
                print("\n:...:: E-MAIL ::...: \n"+aluno[10])
                print("")
                print("")

            
            else:
                print("")
                print("")
                print(":...:: CPF INEXISTENTE ::...: ")
                print("")
                print("")

        elif(opcaomenu == 3):
            continuar = "nao"
            print("")
            print("")
            print (":...:: OBRIGADO, ATÉ A PRÓXIMA ::...:")
            print("")
            print("")
            
        else:
            print("")
            print("")
            print(":...:: OPÇÃO INVALIDA ::...:")
            print("")
            print("")


            
