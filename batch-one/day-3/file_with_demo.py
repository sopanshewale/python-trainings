with open('japanese.txt', 'r', encoding='utf-8') as a_file:
    a_file.seek(340)
    file_str = a_file.read(30)
    print (file_str)
     
