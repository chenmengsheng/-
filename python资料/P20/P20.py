'''
20.	有30个男人女人和小孩同在一家饭馆进餐，共花了五十先令，其中男宾3先令，女宾2先令，小孩1先令。试编程求出男人女人小孩各多少人
'''
for man in range(0, 31):
    for woman in range(0, 31 - man):
        baby = 30 - man - woman
        if 3 * man + 5 * woman + baby == 50:
            print(man, woman, baby)
