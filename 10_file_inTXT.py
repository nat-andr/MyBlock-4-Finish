# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Обработка текста родными средствами
def myText():
    # Extract
    f=open("H:\=00NatArnion=\Module04\Projects\Les12\10_file_inTXT.txt","r",encoding='utf-8')
    s=f.read()
    print(s)


#Вход в программу
def main():
    myText()
    return(0)
 
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
