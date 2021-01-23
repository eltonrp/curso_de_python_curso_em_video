import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site NÃO acessível no momento')
else:
    print('Site Disponível')
    # print(site.read()) # -> Lê o site em html
