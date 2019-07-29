def list_to_csv(data_list):
    import csv

    with open('data_file.csv', 'a') as myfile:
        w = csv.writer(myfile, quoting=csv.QUOTE_ALL, lineterminator='\n')
        w.writerow(data_list)
        w.writerow(data_time_list)

    with open('data_file.csv', 'a') as myfile:
        w = csv.writer(myfile, quoting=csv.QUOTE_ALL, lineterminator='\n')

    return


data_list = []
data_time_list = []

import genetic
for x in range(4):
    data = genetic.main()
    print(x, ":", data[0], "time:", data[1])
    data_list.append(data[0])
    data_time_list.append(data[1])

list_to_csv(data_list)