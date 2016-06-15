def dadosDoAluno():
    arquivo = open("alunos.txt","r") 
    aluno = arquivo.readlines() 
    arquivo.close()
    numeroCpf = str(input(":...:: DIGITE O CPF DO ALUNO ::...:"))
    while(numeroCpf == ""):
        numeroCpf = input(":...:: DIGITE O CPF DO ALUNO ::...:")
    achou = False
    for i in range(2,len(aluno),11):
        if(aluno[i] == numeroCpf+"\n"): 
            print("")
            print("")
            print("\n:...:: NOME DO ALUNO ::...: \n"+aluno[i-2]) 
            print("\n:...:: IDADE DO ALUNO ::...: \n"+aluno[i-1])
            print("\n:...:: CPF DO ALUNO ::...: \n"+aluno[i])
            print("\n:...:: O ALUNO É PORTADOR DE ALGUMA DEFICIÊNCIA? ::...: \n"+aluno[i+1])
            print("\n:...:: ETINIA DO ALUNO ::...: \n"+aluno[i+2])
            print("\n:...:: TIPO DE ESCOLA DO ALUNO ::...: \n"+aluno[i+3])
            print("\n:...:: FILIAÇÃO - PAI ::...: \n"+aluno[i+4])
            print("\n:...:: FILIAÇÃO - MÃE ::...: \n"+aluno[i+5])
            print("\n:...:: CIDADE ::...: \n"+aluno[i+6])
            print("\n:...:: ESTADO ::...: \n"+aluno[i+7])
            print("\n:...:: E-MAIL ::...: \n"+aluno[i+8])
            print("")
            print("")
            achou = True
            break
    if(achou == False):
        print("")
        print("")
        print(":...:: CPF INEXISTENTE ::...: ")
        print("")
        print("")

def exibeMenu():
    print ("======================================================================")
    print ("==========/------------------------------------------------\==========")
    print ("=========/              1 = CADASTRAR NOVO ALUNO.           \=========")
    print ("========|               2 = DADOS DO ALUNO.                  |========")
    print ("========\               3 = FECHAR O PROGRMA.                /========")
    print ("=========\--------------------------------------------------/=========")
    print ("======================================================================")
    opcaomenu = int(input(":...:::::::::::::::::::: O QUE DESEJA FAZER? ::::::::::::::::::::...: "))
    return opcaomenu

def cadastro():
    print("")
    print("")
    nome = input(":...:: NOME DO ALUNO ::...: ")          
    idade = input(":...:: IDADE DO ALUNO ::...: ")                
    cpf = input(":...:: CPF DO ALUNO ::...: ")
    deficiencia = input(":...:: O ALUNO É PORTADOR DE NECESSIDADES ESPECIAIS? ::...: ")
    cor = input("...:: QUAL O TIPO DE ETINIA DO ALUNO? ::...: ")
    escola = input(":...:: O ALUNO É DE ESCOLA PÚBLICA OU PARTICULAR? ::...: ")
    pai = input(":...:: FILIAÇÃO - PAI ::...: ")
    mae = input(":...:: FILIAÇÃO - MÃE ::...: ")
    cidade = input(":...:: CIDADE ::...: ")
    estado = input(":...:: ESTADO ::...: ")
    email = input(":...:: E-MAIL ::...: ")
    arquivo = open("alunos.txt","a")
    arquivo.writelines([nome+"\n",idade+"\n",cpf+"\n", deficiencia+"\n", cor+"\n", escola+"\n", pai+"\n", mae+"\n", cidade+"\n", estado+"\n", email+"\n"])
    arquivo.close()
    print ("")
    print (":...:: MUITO OBRIGADO, O ALUNO JÁ ESTA CADASTRADO ::...:")
    print ("")
    

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
        opcaomenu = exibeMenu()
        if (opcaomenu == 1):
            cadastro()    
        elif(opcaomenu == 2):
            dadosDoAluno() 

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


            
