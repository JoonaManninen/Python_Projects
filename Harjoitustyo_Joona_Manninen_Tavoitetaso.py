######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Joona Manninen
# Opiskelijanumero: 0561911
# Päivämäärä:08.12.2021
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat 
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Stackoverflow.com
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse 
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä Harjoitustyo_Joona_Manninen.py
import numpy
import sys
import HTTavoiteKirjasto
def valikko():
    print("Mitä haluat tehdä:")
    print("1) Lue tiedosto")
    print("2) Analysoi palautukset")
    print("3) Tallenna tulokset")
    print("4) Analysoi opiskelijoiden palautusmäärät")
    print("5) Analysoi tuntikohtaiset palautukset")
    print("6) Analysoi aikavälien palautukset")
    print("0) Lopeta")
    val = input("Valintasi: ")
    return val
def paaohjelma():
   analyysi = []
   Luettu = []
   RIVEJA = 15
   SARAKKEITA = 24
   SARAKE = 7
   RIVI = 14
   sanak = {}
   aariarvot = []
   while (True):
       valinta = valikko()
       try:
           valinta = int(valinta)
       except ValueError:
           print("Tuntematon valinta, yritä uudestaan.")
           continue
       if (valinta==1):
           Luettu = HTTavoiteKirjasto.LUE(Luettu)
           print("")
           print("Anna uusi valinta.")
       elif (valinta==2):
           if (len(Luettu) == 0):
               print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
               print()
               print("Anna uusi valinta.")
               continue
           analyysi = HTTavoiteKirjasto.analyysi(Luettu,analyysi)
           aariarvot = HTTavoiteKirjasto.pienin_suurin(analyysi,aariarvot) # Analysoidaan ääriarvot.
           print("")
           print("Anna uusi valinta.")
       elif (valinta==3):
           if (len(analyysi) == 0):
               print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
               print()
               print("Anna uusi valinta.")
               continue 
           HTTavoiteKirjasto.tallenna(analyysi, Luettu, aariarvot)
           analyysi.clear() # Tyhjennetään analyysi lista, jotta sitä voidaan käyttää uudelleen.
           aariarvot.clear() # Tyhjennetään aariarvot lista, jotta sitä voidaan käyttää uudelleen.
           print("")
           print("Anna uusi valinta.")
       elif (valinta==4):
           if (len(Luettu)==0):
               print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
               print('')
               print("Anna uusi valinta.")
               continue
           sanak = HTTavoiteKirjasto.palautusmaara(Luettu,sanak) 
           sanak = HTTavoiteKirjasto.tulostuskirjoitus(sanak) 
           print()
           print("Anna uusi valinta.")
       elif (valinta==5):
           if (len(Luettu)==0):
               print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
               print("")
               print("Anna uusi valinta.")
               continue
           matriisiA = numpy.zeros((RIVEJA,SARAKKEITA), int) # Luodaan matriisi, jota analyysissä ja tallennuksessa käytetään.
           matriisiA = HTTavoiteKirjasto.tuntianalyysi(Luettu,matriisiA)
           matriisiA = HTTavoiteKirjasto.tuntikirjoitus(matriisiA,RIVEJA,SARAKKEITA)
           # matriisiA palautetaan tyhjänä
           print("")
           print("Anna uusi valinta.")
       elif (valinta==6):
           if (len(Luettu)==0):
               print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
               print()
               print("Anna uusi valinta.")
               continue
           matriisiB = numpy.zeros((RIVI,SARAKKEITA), int) # Luodaan matriisi, jota analyysissä ja tallennuksessa käytetään.
           matriisiB = HTTavoiteKirjasto.aikavalianalyysi(Luettu,matriisiB)
           matriisiB = HTTavoiteKirjasto.aikavalikirjoitus(matriisiB,RIVI,SARAKE)
           # matriisiB palautetaan tyhjänä
           print()
           print("Anna uusi valinta.")
       elif (valinta==0):
           break
       else:
           print("Tuntematon valinta, yritä uudestaan.")
           print()
           print('Anna uusi valinta.')
   # Tyhjennetään kaikki tietorakenteet ohjelman lopuksi.
   analyysi.clear()
   Luettu.clear()
   sanak.clear()
   aariarvot.clear()
   print("Kiitos ohjelman käytöstä.") 
   return None
paaohjelma()
#eof
