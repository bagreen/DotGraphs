with open('all_sorted.txt') as f:
    for line in f:
        if ("find ." not in (line.lower()) and "find /" not in (line.lower())):
            with open('notDot.txt', 'a') as file:
                file.write(line)
