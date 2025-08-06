import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen("https://zacarias-kingzaca.github.io/angola/")
except urllib.error.URLError :
    print("O site do Zacarias não está acessível no momento.")
else:
    print("Consegui acessar o site do Zacarias com sucesso.")