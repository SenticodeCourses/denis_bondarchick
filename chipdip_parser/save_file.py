def save(data):
    str_data = str(data)
    print(str_data)
    file = open("scratch", "w")
    file.write(str_data)
    file.close()
