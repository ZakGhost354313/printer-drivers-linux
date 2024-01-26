import os
import sys
import tempfile as temp
import shutil
import urllib.request as req

baseURL="https://www.openprinting.org/download/PPD/"
driverDir="/etc/"

"""
brother
canon
dell
epson
genicom
gestetner
hp
infoprint
infotec
konica_minolta
kyocera
lanier
lexmark
nrg
oce
oki
ricoh
samsung
savin
sharp
toshiba
utax
xerox
"""

brands = {
    "brother": ["","","",""],
    "canon": []
}

def donwload(url):
    tmp1 = temp.NamedTemporaryFile(delete=False)
    shutil.copyfileobj(req.urlopen(url),tmp1)
    return tmp
def install(brand):
    match brand:
        case "brother":
            for fn in brands["brother"]:
                download(baseURL+"Brother/"+fn)
            break
        case "canon":
            break
        case "dell":
            break
        case "epson":
            break
        case "infoprint":
            break
        case "infotec":
            break
        case "konica" || "konica_minolta":
            break
        case "kyocera":
            break
        case "lanier":
            break
        case "lexmark":
            break
        case "nrg":
            break
        case "oce":
            break
        case "oki":
            break
        case "ricoh":
            break
        case "samsung":
            break
        case "savin":
            break
        case "sharp":
            break
        case "toshiba":
            break
        case "utax":
            break
        case "xerox":
            break


def install_all():
    install("brother")
    install("canon")
    install("dell")
    install("epson")
    install("genicom")
    install("gestetner")
    install("hp")
    install("infoprint")
    install("infotec")
    install("konica")
if __name__ == "__main__": 
    if sys.argv[1] =! "all": install(args[1])
    else: install_all()
