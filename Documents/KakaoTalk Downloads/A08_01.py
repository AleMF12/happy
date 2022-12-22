### YOUR CODE STARTS HERE
centers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
def load_data():
    for center in centers:
        dat = []
        with open(f"MBTI-center-{center}.txt", "rt") as fin:
            data = fin.read()

        if center == 0:
            data_splited = data.strip().split(",")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 1:
            data_splited = data.strip().split(";")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 2:
            data_splited = data.strip().split(" ")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 3:
            data_splited = data.strip().split("\t")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 4:
            data_splited = data.strip().split("\n")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ',  'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 5:
            data_splited = data.strip().split(",")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 6:
            data_splited = data.strip().split(";")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 7:
            data_splited = data.strip().split(" ")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)
        elif center == 8:
            data_splited = data.strip().split(" ")

            for x in data_splited:
                if x == 'ENXJ':
                    data_splited[data_splited.index('ENXJ')] = data_splited[data_splited.index('ENXJ')].replace('ENXJ', 'ENFJ')

            for i in data_splited:
                if i == 'ENFJ':
                    dat.append(i)

        f = open("D:\Project_Siri\Ale's Work\A08\Results.txt", "a")
        f.write(f"{center}, {len(dat)}\n")
        f.close()

        with open(f"Results.txt", "rt") as fin:
            Results = fin.read()
    return Results

print(load_data())

### YOUR CODE ENDS HERE