#Exceptions
def print_variables(a,c):
    try:
        print('a=', a, "  b=", b, "  c=",c)
    except Exception as e:
        print(str(e))
#Конвертация списка строковых переменных, создание нового списка только чисел
def convert_list(inputs):
    new_list=""
    for my_input in inputs:
        try:
            mine=int(my_input)
            print(mine)
            new_list=new_list+str(mine)+", "
        except Exception as e:
            print(str(e))
    print("NEW LIST=",new_list)

#Попытка записи в файл, открытый на чтение
def writing(row):
    f=open("test.txt", "r", encoding='utf-8')
    s=f.read()+row
    print(s)
    try:
        f.write(s)
    except Exception as e:
        print(str(e))
    finally:
        f.close()

#Entry point

def main():
#---------------------------------------------
    a=4
    c=8
    print_variables(a,c)
#_____________________________________________
    my_input=["3","5","Hi!","7", "Bye!"]
    convert_list(my_input)
    print("")
#----------------------------------------------
    my_row="  The weather is fine!"
    writing(my_row)


    return 0

if __name__ == '__main__':
   main()


