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
# Tehtävä HTTavoiteKirjasto.py
import sys
import datetime
import numpy
import math
class TIEDOT:   #Olio johon varastoidaan kaikki LUE aliohjelmassa luetut tiedot
    aikaleima = str
    opiskelija = ""
    tehtava = ""
class DATA:     #Olio johon varastoidaan kaikki Analyysi aliohjelmassa luetut tiedot
    tehtava = ""
    maara = 0

def LUE(Luettu):
    Luettu.clear() # Tyhjennetään lista johon luettu tieto laitetaan, jotta ohjelman uudelleen ajo onnistuu.
    tiedot2 = []
    tiedostoLue = input("Anna luettavan tiedoston nimi: ")
    try:
        LueTieto = open(tiedostoLue, 'r')
        k=0
        LueTieto.readline() #Luetaan ensimmäinen turha rivi pois
        while (True):
            rivi = LueTieto.readline()
            if (len(rivi)==0):
                break
            else:
                k=k+1
                tiedot = rivi.split(';')
                tiedot2.clear()
                for i in tiedot:
                    tiedot2.append(i.strip())
                data = TIEDOT()
                data.aikaleima = tiedot2[0]
                data.opiskelija = tiedot2[1]
                data.tehtava = tiedot2[2]
                Luettu.append(data)
        print("Tiedostosta '"+tiedostoLue+"' luettiin listaan",str(k),"datarivin tiedot.")
        LueTieto.close()
    except Exception:
        print("Tiedoston '"+tiedostoLue+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return Luettu

def analyysi(Luettu,analyysi):
    analyysi.clear() # Tyhjennetään analyysi lista.
    lista2 = []
    for data in Luettu:
        lista2.append(data.tehtava)
    nk=0
    counter = 0 
    ak = lista2[0]
    for k in lista2:
        nk=nk+1
        if (k != ak):
            data3 = DATA()
            data3.tehtava = ak
            data3.maara = counter
            analyysi.append(data3)
            counter = 0
            ak=k
        if (nk==len(lista2)):
            data3 = DATA()
            data3.tehtava = k
            data3.maara = counter+1 #Lisätään counteriin +1, jotta otetaan viimeinen listan elementti huomioon.
            analyysi.append(data3)
        else:
            ak = k
            counter = counter + 1
            continue
    te = ("Analysoitu {0} palautusta {1} eri tehtävään.").format(len(Luettu),len(analyysi))
    print(te)
    print("Tilastotiedot analysoitu.")
    lista2.clear()
    return analyysi

def pienin_suurin(analyysi,aariarvot):
    aariarvot.clear() # Tyhjennetään aariarvot lista.
    for data3 in analyysi:
        suuri = data3.maara
        pieni = data3.maara
        pienin = data3.tehtava
        suurin = data3.tehtava
        break
    for data3 in analyysi:
        a = data3.maara
        if (suuri > a):
            continue
        else:
            suurin = data3.tehtava
            suuri = a
    for data3 in analyysi:
        a = data3.maara
        if (pieni < a):
            continue
        else:
            pienin = data3.tehtava
            pieni = a
    aariarvot = [suuri,suurin,pieni,pienin]
    return aariarvot

def tallenna(analyysi, Luettu, aariarvot):
    tiedostoKir = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        KirTieto = open(tiedostoKir, 'w')
        yhteensa = 0
        for data3 in analyysi:
            yhteensa += data3.maara
        keskimaara = int(yhteensa/len(analyysi))
        v = ("Palautuksia tuli yhteensä {0}, {1} eri tehtävään.").format(len(Luettu), len(analyysi))
        g = ("Viikkotehtäviin tuli keskimäärin {0} palautusta.").format(keskimaara)
        m = ("Eniten palautuksia, {0}, tuli viikkotehtävään {1}.").format(aariarvot[0],aariarvot[1])
        n = ("Vähiten palautuksia, {0}, tuli viikkotehtävään {1}.").format(aariarvot[2], aariarvot[3])
        ck = ("{0}\n{1}\n{2}\n{3}").format(v,g,m,n)    
        KirTieto.write(ck)
        KirTieto.write("\n")
        KirTieto.write("\nTehtävä;Lukumäärä\n")
        print(ck)
        print("\nTehtävä;Lukumäärä")
        for data3 in analyysi:
            o = ("{0};{1}\n").format(data3.tehtava,data3.maara)
            o1 = ("{0};{1}").format(data3.tehtava,data3.maara)
            print(o1)
            KirTieto.write(o)
        print("Tulokset tallennettu tiedostoon '"+tiedostoKir+"'.")
        KirTieto.close()
    except Exception:
        print("Tiedoston '"+tiedostoKir+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    return None

def palautusmaara(Luettu,sanak):
    palautus1 = {}
    plista = []
    avain = []
    arvot = []
    palautus1.clear()
    for data in Luettu:
        plista.append(data.opiskelija)
    for n in plista:  # Luodaan sanakirja jossa on opiskelijoiden tehtyjen tehtävien määrä.
        if n not in palautus1:
            palautus1[n] = 1
        else:
            palautus1[n] += 1
    plista2 = list(palautus1.values()) # Tehdään lista missä on kaikki opiskelija kohtaiset palautus määrät.
    # Tehdään uusi sanakirja jossa on pistemäärä ja niiden opiskelijoiden määrä joilla oli kyseinen pistemäärä.
    avain = list(range(0,61)) # 60 tehtävää
    arvot = [0]*61 #60 tehtävää joiden alku arvo on 0
    zip_1 = zip(avain, arvot) 
    sanak = dict(zip_1)
    for i in plista2:
        if i in sanak:
            sanak[i] += 1
    print("Tehtäväkohtaiset pisteet analysoitu.")
    # Tyhjennetään listat joita analyysin tekemiseen käytettiin.
    palautus1.clear()
    plista.clear()
    avain.clear()
    arvot.clear()
    return sanak

def tulostuskirjoitus(sanak):
    tied1 = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        wtied = open(tied1, 'w')
        wtied.write("Pistemäärä;Opiskelijoita\n")
        for k in sanak:
            a = ("{0};{1}\n").format(k, sanak[k])
            wtied.write(a)
        wtied.close()
        print("Tulokset tallennettu tiedostoon '"+tied1+"'.")
    except Exception:
        print("Tiedoston '"+tied1+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    sanak.clear() # Tyhjennetään sanakirja tallennuksen jälkeen
    return sanak
            
def tuntikirjoitus(matriisiA,RIVEJA,SARAKKEITA):
    tied2 = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        wtied6 = open(tied2, 'w')
        nk = 0
        for rivi in range(RIVEJA):
            wtied6.write('Tunti;')
            for sarake in range(SARAKKEITA):
                nk = nk + 1
                if (nk==SARAKKEITA):
                    ba = ("{0}").format(matriisiA[rivi][sarake])
                    wtied6.writelines(ba)
                else:
                    ba = ("{0};").format(matriisiA[rivi][sarake])
                    wtied6.writelines(ba)
            wtied6.write('\n')
            break
        nk = 0
        for rivi1 in range(RIVEJA-1):
            wtied6.write('Vko '+str(rivi1+1)+(';'))
            for sarake1 in range(SARAKKEITA):
                nk = nk + 1
                if (nk==SARAKKEITA):
                    ab = ("{0}").format(matriisiA[rivi1+1][sarake1])
                    wtied6.writelines(ab)
                    nk = 0
                else:
                    ab = ("{0};").format(matriisiA[rivi1+1][sarake1])
                    wtied6.writelines(ab)
            wtied6.write('\n')
        print("Tulokset tallennettu tiedostoon '"+tied2+"'.")
        wtied6.close()
    except Exception:
        print("Tiedoston '"+tied2+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    # Tuhotaan matriisi käytön jälkeen
    matriisiA = numpy.delete(matriisiA, numpy.s_[:], None)
    return matriisiA

def tuntianalyysi(Luettu,matriisiA):
    lista5 = list(range(0,24))
    tunti = []
    vko = []
    matriisiA[0, :] = lista5
    for data in Luettu: #Otetaan tarvittavat tiedot oliosta.
        aika1 = datetime.datetime.strptime(data.aikaleima,'%d-%m-%Y %H:%M:%S')
        tunti.append(int(aika1.strftime("%H")))
        vko.append(int(data.tehtava[1:3])) # Otetaan viikko numero tehtävän numerosta.
    for n in vko:
        for i in tunti:
            matriisiA[n,i] += 1
            tunti.remove(i)
            break
    print("Tuntikohtaiset palautukset analysoitu.")
    # Tyhjennetään analyysissä käytetyt listat.
    tunti.clear()
    vko.clear()
    lista5.clear()
    return matriisiA

def aikavalikirjoitus(matriisiB,RIVI,SARAKE):
    tied2 = input("Anna kirjoitettavan tiedoston nimi: ")
    try:
        wtied5 = open(tied2, 'w')
        # Valitaan mikä tahansa tiistai jotta saadaan sen avulla tulostettu viikonpäivät
        x = ("1.11.2021") 
        jk = 0
        y = datetime.datetime.strptime(x, "%d.%m.%Y")
        for rivi in range(RIVI):
            wtied5.write('Aikaväli;')
            for p in range(SARAKE):
                jk = jk + 1
                d = y-datetime.timedelta(days=-p-1)
                if (jk==SARAKE):
                    ba = ("{0} 06:00").format(d.strftime("%a"))
                    wtied5.writelines(ba)
                else:
                    ba = ("{0} 06:00;").format(d.strftime("%a"))
                    wtied5.writelines(ba)
            wtied5.write('\n')
            break
        jk = 0
        for rivi1 in range(RIVI):
            wtied5.write('Vko '+str(rivi1+1)+(';'))
            for sarake1 in range(SARAKE):
                jk = jk + 1
                if (jk==SARAKE):
                    ab = ("{0}").format(matriisiB[rivi1][sarake1])
                    wtied5.writelines(ab)
                    jk = 0
                else:
                    ab = ("{0};").format(matriisiB[rivi1][sarake1])
                    wtied5.writelines(ab)
            wtied5.write('\n')
        print("Tulokset tallennettu tiedostoon '"+tied2+"'.")
        wtied5.close()
    except Exception:
        print("Tiedoston '"+tied2+"' käsittelyssä virhe, lopetetaan.")
        sys.exit(0)
    # Tuhotaan matriisi käytön jälkeen
    matriisiB = numpy.delete(matriisiB, numpy.s_[:], None)
    return matriisiB

def aikavalianalyysi(Luettu,matriisiB):
    vko1 = []
    ajat = []
    for data in Luettu: #Otetaan tarvittavat tiedot oliosta.
        kek = datetime.datetime.strptime(data.aikaleima,'%d-%m-%Y %H:%M:%S')
        ajat.append(kek)
        vko1.append(int(data.tehtava[1:3])) # Otetaan viikko numero tehtävän numerosta.
    # Tehdään muuttuja ensimmäisestä palautus ajankohdasta
    ensimmainen = datetime.datetime.strptime('01.09.2020 06:00:00','%d.%m.%Y %H:%M:%S')
    # Tehdään kaikkien välien ensimmäiset palautusajat
    for n in vko1:
        for i in ajat:
            if (n<8):
                palautusaika = ensimmainen + datetime.timedelta(days=+(7*(n-1)))
            # Tehdään ehto, koska viikolla 7 palautusaika oli 2 viikkoa.
            else:
                palautusaika = ensimmainen + datetime.timedelta(days=+(7*(n)))
            paiva = i - palautusaika
            #Tehdään poikkeus viikko 7
            paiva = paiva.days
            if (n==7):
                paiva = paiva/2
                paiva = math.floor(paiva)
                matriisiB[n-1,paiva] += 1
            else:
                matriisiB[n-1,paiva] += 1
            ajat.remove(i)
            break
    print("Aikavälikohtaiset palautukset analysoitu.")
    # Tyhjennetään listat joita analyysissä käytettiin.
    vko1.clear()
    ajat.clear()
    return matriisiB

#eof
