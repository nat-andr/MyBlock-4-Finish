import pandas as pd
# Встроенные ср-ва Python
def my_text():
    #Extract
    f=open("10_file_inTXT.txt", "r", encoding='utf-8')
    s=f.read()
    print(s)
    #Transform
    s=s.replace("Счет ","")
    print(s)
    #lOAD
    f=open("10_file_inTXT_Out.txt", "w", encoding='utf-8')
    f.write(s)
    f.close()
# With Pandas
def my_pandas():
    # Extract
    df=pd.read_csv("10_Invoices.csv", sep=',')
    print(df)
    # Transform
    cnt=df[df.columns[0]].count()
    print(cnt)         # кол-во строк

    for i in range(cnt):
        df.iat[i, 1] = df.iat[i, 1].replace("Запись на ", "")
        df.iat[i,1] = df.iat[i,1].replace("Сделка по заявке ", "")
        df.iat[i,1] = df.iat[i,1].replace("курс", "Курс")
    print(df)
    # lOAD
    df.to_csv("10_my_file_out.csv",sep=';',encoding='utf-8',index=False)

def main():
    my_text()
    my_pandas()
    return(0)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
