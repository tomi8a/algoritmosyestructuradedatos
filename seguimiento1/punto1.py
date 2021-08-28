file = open('discharge_s_1358.rtf')
data = file.read()
sex = data.index('Sex')
f = data[sex:sex+7]
print('el sexo del paciente es :',f)



