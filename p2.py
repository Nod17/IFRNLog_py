import pandas as pd
import csv
import re



log_file_name = "apache_logs.log"
csv_file_name = "out.csv"

host = []
os = []
access = []
method = []
code = []
byte = []

file = open(log_file_name, 'r')
with open(csv_file_name, 'w') as out:
#-------------------- Host - IP -------------------------------------
    for line in file:
        host.append(line.split(' - - ')[0])
#-------------------- METHOD ----------------------------------------
        method.append((line.split('"',1)[1]).split(' ',1)[0])
#-------------------- CODE ------------------------------------------
        code.append((line.split('" ',1)[1]).split(' ',1)[0])
#-------------------- BYTES -----------------------------------------
        byte.append(((line.split('" ',1)[-1]).split(' "',3)[0]).split(' ',1)[-1])
#-------------------- HORARIO ---------------------------------------       
        h = int(((line.split(':',1)[1])).split(':',1)[0])
        if (h >= 6 and h < 12):
            access.append('Manhã')
        elif (h >= 12 and h < 18):
            access.append('Tarde')
        elif (h > 18 or h < 6):
            access.append('Noite')
        else:
            access.append('erro')
#-------------------- SISTEMA OPERACIONAL ---------------------------                
        if re.search(r'Windows\sNT', line):
            os.append('Windows_NT')
        elif re.findall(r'Linux\s', line):
            os.append('Linux')
        elif re.findall(r'Mac\sOS', line):
            os.append('Mac_OS')
        else:
            os.append('Outro')
#---------------------------------------------------------------------       


#-------------- OPÇÕES PARA VISUALIZAÇÃO DO DATAFRAME ----------------

'''
pd.set_option('display.max_columns', 20)  # or 1000
pd.set_option('display.max_rows', 10000)  # or 1000
pd.set_option('display.max_colwidth', -1)  # or 199
'''
df = pd.DataFrame(list(zip(host,os, method, access, code, byte)), columns = ['HOST','OS', 'METHOD', 'ACCESS', 'CODE', 'BYTES'])
print(df)
df.to_csv('out.csv')

'''
Host,Os,Method,Access,Code,Bytes
83.149.9.216,Mac,GET,Manhã,200,203023
100.149.9.216,Windows,GET,Manhã,200,171717
'''
