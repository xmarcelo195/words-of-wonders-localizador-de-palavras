# listas que receberão os valores
size_3 = []
size_4 = []
size_5 = []
size_6 = []
size_7 = []

# abrir o arquivo
with open('dicio.txt', 'r') as f:
    text = f.readlines()
    for line in f:
        line = line.rstrip("\n")
        if len(line) == 3:
            size_3.append(line)
        if len(line) == 4:
            size_4.append(line)
        if len(line) == 5:
            size_5.append(line)
        if len(line) == 6:
            size_6.append(line)
        if len(line) == 7:
            size_7.append(line)

#salvar 

with open('size_4.txt', 'w') as f:
    for item in size_4:
        f.write("{}\n".format(item))

with open('size_5.txt', 'w') as f:
    for item in size_5:
        f.write("{}\n".format(item))

with open('size_6.txt', 'w') as f:
    for item in size_6:
        f.write("{}\n".format(item))

with open('size_7.txt', 'w') as f:
    for item in size_7:
        f.write("{}\n".format(item))