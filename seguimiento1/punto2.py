from gettext import find


file = open('discharge_s_1358.rtf')
data = file.read()
find1 = data.find('tracheotomy')
find2 = data.find('Tracheotomy')
find3 = data.find('tracheostomy')
find4 = data.find('Tracheostomy')
if find1 == -1 and find2 == -1 and find3 == -1 and find4 == -1:
    print('no esta la palabra traqueotomia en el archivo')
else:
    print('si esta la palabra traqueotomia en el archivo')