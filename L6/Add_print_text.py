# Exercise 2  messenger.py

# Создать скрипт, который записывает введенное пользователем сообщение в файл
# и выводит его обратно из файла на консоль:

# имя файла FILENAME = "messenges.txt"
# Введите сообщение
# запись сообщения в файл
# Все сообщения из файла



while True:
    inputedText = input("Input messege : ")
    if inputedText == "q":
        break
    addedText = open("messenges.txt","a+")
    addedText.write(inputedText + "\n")
    addedText.close()
    addedText = open("messenges.txt","r")
    print(addedText.read())
    addedText.close()
    
