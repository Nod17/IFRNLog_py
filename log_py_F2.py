import pandas as pd
import matplotlib.pyplot as plt
import re



def processar(dic):
    log_file_name = "apache_logs.log"
    csv_file_name = "out.csv"
    
    try:
        file = open(log_file_name, 'r')
        with open(csv_file_name, 'w') as out:
            for line in file:
            
        # -------------------- Host - IP -------------------------------------
                
                dic['Host'].append(line.split(' - - ')[0])

        # -------------------- METHOD ----------------------------------------

                dic['Method'].append((line.split('"', 1)[1]).split(' ', 1)[0])
        
        # -------------------- CODE ------------------------------------------

                dic['Code'].append((line.split('" ', 1)[1]).split(' ', 1)[0])

        # -------------------- BYTES -----------------------------------------
        
                b=(((line.split('" ', 1)[-1]).split(' "', 3)[0]).split(' ', 1)[-1])
                if (b == '-'):
                    dic['Byte'].append(0)
                else:
                    dic['Byte'].append(b)
        
        # -------------------- HORARIO ---------------------------------------
        
                h = int(((line.split(':', 1)[1])).split(':', 1)[0])
                if (h >= 6 and h < 12):
                    dic['Access'].append('Manhã')
                elif (h >= 12 and h < 18):
                    dic['Access'].append('Tarde')
                elif (h > 18 or h < 6):
                    dic['Access'].append('Noite')
                else:
                    dic['Access'].append('erro')
        
        # -------------------- SISTEMA OPERACIONAL ---------------------------
                
                if re.search(r'Windows\sNT', line):
                    dic['Os'].append('Windows_NT')
                elif re.findall(r'Linux\s', line):
                    dic['Os'].append('Linux')
                elif re.findall(r'Mac\sOS', line):
                    dic['Os'].append('Mac_OS')
                else:
                    dic['Os'].append('Outro')
            
    except:
        print('ERRO, ARQUIVO LOG NÃO ENCONTRADO')

#-----------------------------------------------------------------------------------


    df = pd.DataFrame(dic)
#-------------------------------------------------------------------------------------
    print(df)

    df.to_csv('out.csv')
    
 #-----------------------------------------------------------------------------------   
    def processar_os():
        
        print('\n\nParticipação dos sistemas operacionais)\n')
        os = df['Os'].value_counts() 
        df_os = pd.DataFrame(os)
        print(df_os)
        df['Os'].value_counts().plot.pie(title = 'Participação dos sistemas operacionais')
    
    def processar_mtd():
        
        print('\n\nQuantidade de solicitações por método de acesso\n')
        mtd = df['Method'].value_counts() 
        df_mtd = pd.DataFrame(mtd)
        print(df_mtd)

        axis = df_mtd.plot.bar(rot=0)
        print(axis)
        plt.show()
    
    def processar_cd():
        
        print('\n\nQuantidade de solicitações com sucesso)\n')

        cd = df['Code'].value_counts() 
        df_cd = pd.DataFrame(cd)
        print(df_cd)

        axis = df_cd.plot.bar(rot=0)
        print(axis)
        plt.show()
    
    def processar_acc():
        print('\n\nHorários com maior número de acesso\n')

        acc = df['Access'].value_counts() 
        df_acc = pd.DataFrame(acc)
        print(df_acc)
        
        plt.plot(df_acc)
        plt.title('Horários com maior número de acesso')
        plt.show()

        
    
    
    def menu2():
    
    
        while True:
            
            print("1 - Participação dos sistemas operacionais")
            print("2 - Quantidade de solicitações por método de acesso")
            print("3 - Quantidade de solicitações com sucesso")
            print("4 - Horários com maior número de acesso")
            print("5 - Sair")
            
            opção = int(input("> "))

            if opção == 1:
                processar_os()
            if opção == 2:
                processar_mtd()
            if opção == 3:
                processar_cd()
            if opção == 4:
                processar_acc()
            elif opção == 5:
                print("Saindo do programa...")
                break
            else:
                print("Opção invalida!!!")
    
    menu2()  


#-------------------------------------------------------------------------------------
def menu():
    dic = {'Host': [], 'Os': [],  'Method': [], 'Access': [], 'Code': [], 'Byte': []}
    
    while True:
        
        print("1 - Ler e processar aquivo LOG")
        print("2 - Sair")
        
        opção = int(input("> "))

        if opção == 1:
            processar(dic)
        elif opção == 2:
            print("Saindo do programa...")
            break
        else:
            print("Opção invalida!!!")



menu()
