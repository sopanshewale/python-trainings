line_number = 0
with open('men_100meter.txt', 'r', encoding='utf-8') as a_file:
    for line in a_file:
        line_number +=1
        print ("{:>4} {}".format(line_number, line.rstrip()))
        if line_number > 10:
            break


