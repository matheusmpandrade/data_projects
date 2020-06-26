def datetrick (data):
    dic = {'01': 'janeiro', '02' : 'fevereiro', '03': 'março', '04': 'abril', '05': 'maio',
           '06':'junho', '07':'julho', '08':'agosto', '09': 'setembro', '10': 'outubro',
           '11': 'novembro', '12':'dezembro'}
    dia, mes, ano =data.split(" de ")
    return print('%s/%s/%s'%(dia, list(dic.keys())[list(dic.values()).index(mes)], ano))
#print 'Data nascimento: %s/%s/%s' % (dia, mes_ext[int(mes)], ano)
data = "12 de fevereiro de 2008"

datetrick(data)
#dia, mes, ano = aniver.split("/")
#print 'Data nascimento: %s/%s/%s' % (dia, mes_ext[int(mes)], ano)