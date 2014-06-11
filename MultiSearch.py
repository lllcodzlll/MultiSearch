from ciscoconfparse import CiscoConfParse
import os, sys
os.system('cls')
print "h ou help para ajuda"
print "------------------------------------------------------------------"
Direc_Pa = "Confi/"
if os.path.isdir(Direc_Pa):
        os.chdir(Direc_Pa)
def Procurar_CCP():
        print "------------------------------------------------------------------"
        print "1 - Pesquisa somente por Linha"
        print "2 - Pesquisa somente por Pai e Filho"
        print "3 - Pesquisa somente por Filhos de um mesmo Pai"
        print "------------------------------------------------------------------"
        op1_pes = str(raw_input("Qual Metodo de pesquisa deseja: "))
        print "------------------------------------------------------------------"
        if op1_pes == "1":
                for arq in os.listdir('.'):
                        print arq
                print "------------------------------------------------------------------"
                op1_pes = str(raw_input("Qual arquivo de pesquisa>> "))
                try:
                        op1_pes = "./" + op1_pes
                        pes = CiscoConfParse(op1_pes)
                        print "------------------------------------------------------------------"
                        print "int = interface"
                        print "por obj = colocar o nome do objecto"
                        print "ip = para ip"
                        print "Ou qualquer outra linha de comando"
                        print "------------------------------------------------------------------"
                        op2_pes = str(raw_input("Voce quer procurar por ?\n"))
                        pes1 = pes.find_objects(op2_pes)
                        print "------------------------------------------------------------------"
                        print op1_pes.split("/")[len(op1_pes.split("/"))-1] + ":"
                        print "------------------------------------------------------------------"
                        for resul in pes1:
                                print resul.text
                except:
                        print "Falha na abertura do arquivo favor verificar."
                print "------------------------------------------------------------------"
                main()  
        elif op1_pes == "2":
                for arq in os.listdir('.'):
                        print arq
                print "------------------------------------------------------------------"
                op1_pes = str(raw_input("Qual arquivo de pesquisa>> "))
                print "------------------------------------------------------------------"
                try:
                        op1_pes = "./" + op1_pes
                        pes = CiscoConfParse(op1_pes)
                        print "------------------------------------------------------------------"
                        print "1 - interface"
                        print "2 - object-group"
                        #print "99 - Avancado"
                        print "------------------------------------------------------------------"
                        op2_pes = str(raw_input("Qual Pai voce quer procurar ?\n"))
                        if op2_pes == "int" or op2_pes == "interface" or op2_pes == "inter" or op2_pes == "1":
                                op3_pes = str(raw_input("Qual filho voce quer procurar ?\n"))
                                pes1 = pes.find_parents_w_child("^inter", op3_pes)
                                print "------------------------------------------------------------------"
                                print op1_pes.split("/")[len(op1_pes.split("/"))-1] + ":"
                                print "------------------------------------------------------------------"
                                for resul in pes1:
                                        print resul
                                print "------------------------------------------------------------------"

                        elif op2_pes == "obj" or op2_pes == "object" or op2_pes == "group" or op2_pes == "2":
                                op3_pes = str(raw_input("Qual filho voce quer procurar ?\n"))
                                pes1 = pes.find_parents_w_child("^object-group", op3_pes)
                                print "------------------------------------------------------------------"
                                print op1_pes.split("/")[len(op1_pes.split("/"))-1] + ":"
                                print "------------------------------------------------------------------"
                                for resul in pes1:
                                        print resul
                                print "------------------------------------------------------------------"
                        else:
                                main()
                except:
                        pass
        elif op1_pes == "3":
                for arq in os.listdir('.'):
                        print arq
                print "------------------------------------------------------------------"
                op1_pes = str(raw_input("Qual arquivo de pesquisa>> "))
                print "------------------------------------------------------------------"
                try:
                        op1_pes = "./" + op1_pes
                        pes = CiscoConfParse(op1_pes)
                        print "------------------------------------------------------------------"
                        #print "1 - interface"
                        print "1 - object-group"
                        #print "99 - Avancado"
                        print "------------------------------------------------------------------"
                        op2_pes = str(raw_input("Qual Pai voce quer procurar ?\n"))
                        if op2_pes == "obj" or op2_pes == "object" or op2_pes == "group" or op2_pes == "1":
                                op3_pes = str(raw_input("Qual o nome do grupo que voce quer ver as configuracoes ?\n"))
                                pes1 = pes.find_children_w_parents("^object-group\snetwork\s"+op3_pes+"$", "net")
                                print "------------------------------------------------------------------"
                                print op1_pes.split("/")[len(op1_pes.split("/"))-1] + ":"
                                print "object-group network " + op3_pes
                                print "------------------------------------------------------------------"
                                for resul in pes1:
                                        print resul
                                print "------------------------------------------------------------------"
                except:
                        pass
        else:
                main()
        main()
def main():
        try:
                str1=os.getcwd()
                str2=str1.split('\\')
                n=len(str2)
                str1=str2[n-1]
                str2 = "MultiSearch[",str1,"]>>"
                prompt = "".join(str2)
                op1_global = str(raw_input(prompt))
                #op1_global = str(raw_input("MultiSearch[Global]>>"))
                if op1_global == "h" or op1_global == "help":
                        print "------------------------------------------------------------------"
                        print "Escolha algum das seguintes opcoes."
                        print "------------------------------------------------------------------"
                        print "ls - para ver quais as configuracoes existe nesse diretorio."
                        #print "pwd - para verificar qual diretorio esta.                         "
                        print "cd - para mudar de diretorio."
                        #print "pesquisa - para iniciar uma pesquisa."
                        print "exit - para sair."
                        print "easter - Tem Certeza!?"
                        print "------------------------------------------------------------------"
                        main()
                elif op1_global == "clear" or op1_global == "cl" or op1_global == "cls":
                        os.system('cls')
                        main()
                elif op1_global == "ls" or op1_global == "l" or op1_global == "dir":
                        print "------------------------------------------------------------------"
                        for arq in os.listdir('.'):
                                if os.path.isdir(arq):
                                        print 'dir - ', arq
                                else:
                                        print 'arq - ', arq
                        print "------------------------------------------------------------------"
                        main()
                #elif op1_global == "ls -l" or op1_global == "l -l":
                #        os.system('ls -l')
                #        main()
                #elif op1_global == "pwd" or op1_global == "pw" or op1_global == "p":
                #        os.system('pwd')
                #        main()
                elif op1_global == "exit" or op1_global == "q" or op1_global == "ex" or op1_global == "e":
                        sys.exit("Saindo.....")
                elif op1_global == "cd" or op1_global == "c":
                        print "------------------------------------------------------------------"
                        for arq in os.listdir('.'):
                                if os.path.isdir(arq):
                                        print 'dir - ', arq
                        print "------------------------------------------------------------------"
                        print "Use .. para voltar para a pasta anterior"
                        op2_global = str(raw_input("Para qual pasta acima voce quer ir ? >> "))
                        if os.path.isdir(op2_global):
                                os.chdir(op2_global)
                                main()
                        else:
                                if op2_global == "":
                                        print "------------------------------------------------------------------"
                                        main()
                                else:
                                        print "------------------------------------------------------------------"
                                        print "Erro ao mudar de pasta, favor verificar."
                                        main()
                #elif op1_global == "pesquisa" or op1_global == "pes" or op1_global == "p":
                #        print "Entrou no Mode de Pesquisa"
                #        os.system('pause 1')
                #        pesquisa()
                elif op1_global == "easter":
                        print"         (__)"
                        print"         (oo)"
                        print"   /-----(__)"
                        print"  / | ||"
                        print" * /\---/\""
                        print"    ~~ ~~"
                        print"....Have you mooed today?..."
                        print "------------------------------------------------------------------"
                        main()
                elif op1_global == "abir" or op1_global == "ab":
                        Procurar_CCP()
                #elif op1_global == os.path.isfile                             
                else:
                        main()
        except:
                sys.exit("Saindo....")
main()
