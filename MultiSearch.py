from ciscoconfparse import CiscoConfParse
import os, sys
os.system('cls')
print "h ou help para ajuda"
def Procurar_CCP():
        str1=os.getcwd()
        str2=str1.split('\\')
        n=len(str2)
        str1=str2[n-1]
        str2 = "MSearch@Pes[",str1,"]>>"
        prompt = "".join(str2)
        op1_pes = str(raw_input(prompt))
        if op1_pes == "v" or op1_pes == "voltar":
                main()
        if op1_pes == "exit" or op1_pes == "e":
                sys.exit("Saindo....")
        if op1_pes == "pes":
                for arq in os.listdir('.'):
                        if os.path.isfile(arq):
                                print 'arq - ', arq
                                op2_pes = str(raw_input("Qual Arquivo quer Abrir >>"))
                                if op2_pes == os.path.isfile:
                                        ccp = CiscoConfParse(op2_pes)
                                        print ccp.find_parents_w_child("^interface","no shut")
                                        Procurar_CCP()
                                
        else:
                Procurar_CCP()
def main():
        Direc_Pa = ".\Confs"
        try:
                if os.path.isdir(Direc_Pa):
                        os.chdir(Direc_Pa)
                str1=os.getcwd()
                str2=str1.split('\\')
                n=len(str2)
                str1=str2[n-1]
                str2 = "MSearch[",str1,"]>>"
                prompt = "".join(str2)
                op1_global = str(raw_input(prompt))
                #op1_global = str(raw_input("MultiSearch[Global]>>"))
                if op1_global == "h" or op1_global == "help":
                        print "------------------------------------------------------------------"
                        print "Escolha algum das seguintes opcoes"
                        print "ls - para ver quais as configuracoes existe nesse diretorio"
                        print "pwd - para verificar qual diretorio esta"
                        print "cd - para mudar de diretorio, lembrando que a arvore e' em unix"
                        print "pesquisa - para iniciar uma pesquisa"
                        print "exit - para sair"
                        print "------------------------------------------------------------------"
                        main()
                elif op1_global == "clear" or op1_global == "cl":
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
                elif op1_global == "pwd" or op1_global == "pw" or op1_global == "p":
                        os.system('pwd')
                        main()
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
                elif op1_global == "abir" or op1_global == "ab":
                        Procurar_CCP()
                else:
                        op1_global = os.path.isfile(op1_global)
                        if op1_global:
                                try:
                                        ccp = CiscoConfParse(opt_global.replace('\\','/'))
                                        print ccp.find_parents_w_child("^interface","no shut")
                                        main()
                                except:
                                        print "Erro ao abrir o arquivo"
                                        main()
                                
                        else:
                                main()
        except KeyboardInterrupt:
                print "Saindo"
main()
