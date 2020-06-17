def add_min(data):
    # one large sub array
    # sum up the minimum or each sub array
    results = sum([min(x) for x in data])
    # results = sum(results)

    print(results)


add_min([[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]])
