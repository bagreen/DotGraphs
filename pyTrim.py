with open('newFile.txt') as f:
    for line in f:
        if ("find" in line):
            with open('newerFile.txt', 'a') as file:
                file.write(line)
