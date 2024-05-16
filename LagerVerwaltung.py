# LAGER VERWALTUNG  

#Classes  
class LagerHausClass:
    LagerHausId = int
    LagerHaus = [
        {"LagerHausId": 1, "Name": "Luzern"},
        {"LagerHausId": 2, "Name": "Zug"},
        {"LagerHausId": 3, "Name": "Bern"},
        {"LagerHausId": 4, "Name": "Zürich"},
        {"LagerHausId": 5, "Name": "Ebikon"},
    ]

    Platz = {
       lager["Name"]: [
           [f"Sektor {sector} on Floor {floor}" for sector in ["A", "B", "C", "D", "E", "F", "G"]]
           for floor in range(10)
       ]
       for lager in LagerHaus
    }
    def get_lagerhaus_by_id(self, LagerHaus_id):
        for lagerhaus in self.LagerHaus:
            if lagerhaus['LagerHausId'] == LagerHaus_id:
                return lagerhaus
        return 'lhid wrong'
    def get_lagerhaus_name_by_id(self, lagerhaus_id):
        for lagerhaus in self.LagerHaus:
         if lagerhaus.get('LagerHausId') == lagerhaus_id:
            return lagerhaus.get('Name', 'ihn wrong')
        return 'ihn wrong'



class ArtikelProperties:
   Properties = [
       {"ArtikelID": 1,"Grösse": "45cm","Gewicht": "3.2 Kg","Farbe": "Schwarz",},
       {"ArtikelID": 2,"Grösse": "7cm","Gewicht": "0.2 Kg","Farbe": "Rot",},
       {"ArtikelID": 3,"Grösse": "25cm","Gewicht": "1.2 Kg","Farbe": "RGB",},
       {"ArtikelID": 4,"Grösse": "30cm","Gewicht": "4.0 Kg","Farbe": "Silver",},
       {"ArtikelID": 5,"Grösse": "70cm","Gewicht": "9.4Kg","Farbe": "Schwarz",},
   ]
   def get_artikelproperties_by_id(self, artikel_id):
        for artikelproperties in self.Properties:
            if artikelproperties['ArtikelID'] == artikel_id:
                return artikelproperties
        return None


class ArtikelClass:
    Artikel = [
        {"ArtikelID": 1, "Bez": "Bildschirm", "AnzahlArtikel": 10, "LieferantID": 7, "LagerHausId": 1, "LagerPlatz": "A0",},
        {"ArtikelID": 2, "Bez": "Maus", "AnzahlArtikel": 10, "LieferantID": 10, "LagerHausId": 2, "LagerPlatz": "A5"},
        {"ArtikelID": 3, "Bez": "Tastatur", "AnzahlArtikel": 10, "LieferantID": 2, "LagerHausId": 3, "LagerPlatz": "B2"},
        {"ArtikelID": 4, "Bez": "Laptop", "AnzahlArtikel": 8, "LieferantID": 1, "LagerHausId": 4, "LagerPlatz": "B5"},
        {"ArtikelID": 5, "Bez": "Drucker", "AnzahlArtikel": 0, "LieferantID": 3, "LagerHausId": 5, "LagerPlatz": "A3"},
        {"ArtikelID": 6, "Bez": "Kopiergerät", "AnzahlArtikel": 9, "LieferantID": 4, "LagerHausId": 1, "LagerPlatz": "E1"},
        {"ArtikelID": 7, "Bez": "Festplatte", "AnzahlArtikel": 100, "LieferantID": 5, "LagerHausId": 3, "LagerPlatz": "F5"},
        {"ArtikelID": 8, "Bez": "Server", "AnzahlArtikel": 2, "LieferantID": 5, "LagerHausId": 2, "LagerPlatz": "A3"},
        {"ArtikelID": 9, "Bez": "Router", "AnzahlArtikel": 60, "LieferantID": 10, "LagerHausId": 1, "LagerPlatz": "B4"},
        {"ArtikelID": 10, "Bez": "Modems", "AnzahlArtikel": 55, "LieferantID": 2, "LagerHausId": 5, "LagerPlatz": "C2"},
        {"ArtikelID": 11, "Bez": "USB-Stick", "AnzahlArtikel": 24, "LieferantID": 5, "LagerHausId": 4, "LagerPlatz": "E4"},
        {"ArtikelID": 12, "Bez": "Kabel", "AnzahlArtikel": 87, "LieferantID": 6, "LagerHausId": 2, "LagerPlatz": "A5"},
        {"ArtikelID": 13, "Bez": "Schreibtisch", "AnzahlArtikel": 49, "LieferantID": 6, "LagerHausId": 3, "LagerPlatz": "E0"},
        {"ArtikelID": 14, "Bez": "Bürostuhl", "AnzahlArtikel": 85, "LieferantID": 2, "LagerHausId": 1, "LagerPlatz": "A3"},
        {"ArtikelID": 15, "Bez": "Regal", "AnzahlArtikel": 5, "LieferantID": 1, "LagerHausId": 5, "LagerPlatz": "B3"},
        {"ArtikelID": 16, "Bez": "Etikettendrucker", "AnzahlArtikel": 929, "LieferantID": 4, "LagerHausId": 3, "LagerPlatz": "F2"},
        {"ArtikelID": 17, "Bez": "Werkzeuge", "AnzahlArtikel": 68, "LieferantID": 3, "LagerHausId": 5, "LagerPlatz": "C4"},
        {"ArtikelID": 18, "Bez": "Maschiene", "AnzahlArtikel": 35, "LieferantID": 5, "LagerHausId": 1, "LagerPlatz": "A3"},
        {"ArtikelID": 19, "Bez": "Microphone", "AnzahlArtikel": 99, "LieferantID": 8, "LagerHausId": 2, "LagerPlatz": "B4"},
        {"ArtikelID": 20, "Bez": "iPhone", "AnzahlArtikel": 8, "LieferantID": 9, "LagerHausId": 3, "LagerPlatz": "A3"}
    ]
    def get_artikel_by_id(self, artikel_id):
        for artikel in self.Artikel:
            if artikel['ArtikelID'] == artikel_id:
                return artikel
        return None
    

class LieferantClass:
    Lieferanten = [
        {"LieferantID": 1, "Name": "Digitech"},
        {"LieferantID": 2, "Name": "Dell"},
        {"LieferantID": 3, "Name": "Amazon"},
        {"LieferantID": 4, "Name": "Intel"},
        {"LieferantID": 5, "Name": "HP"},
        {"LieferantID": 6, "Name": "Lenovo"},
        {"LieferantID": 7, "Name": "Mani"},
        {"LieferantID": 8, "Name": "Mela"},
        {"LieferantID": 9, "Name": "Acer"},
        {"LieferantID": 10,"Name": "Fasco"}
    ]
    def get_lieferant_by_id(self, lieferant_id):
        for lieferant in self.Lieferanten:
            if lieferant['LieferantID'] == lieferant_id:
                return lieferant
        return '1rong'

    def get_lieferant_name_by_id(self, lieferant_id):
        for lieferant in self.Lieferanten:
            if lieferant['LieferantID'] == lieferant_id:
                return lieferant['Name']
        return '2rong'
    




# Menu / Clear
import os 
def clear(): return os.system('cls') 

def Menuchange():
    menuchange = input("\nWollen Sie ins Menu wechseln?(Ja/Nein)")
    if menuchange.lower() == "ja":
        menu()
    else:
        exit()







#Funktionen

#Suchen
def AktionSArtikel():
    artikelnummer = input("Geben Sie die Artikel Nummer an: ")
    artikel_class = ArtikelClass()
    artikel = artikel_class.get_artikel_by_id(int(artikelnummer))
    if artikel:
        lieferant_id = artikel['LieferantID']
        lagerhaus_id = artikel["LieferantID"]
        lieferant_class = LieferantClass()
        lagerhaus_class = LagerHausClass()
        lieferant_name = lieferant_class.get_lieferant_name_by_id(lieferant_id)
        lagerhaus_name = lagerhaus_class.get_lagerhaus_name_by_id(lagerhaus_id)
        print(f"\n\nArtikel ID: {artikel['ArtikelID']} \nBez: {artikel['Bez']} \nAnzahl Artikel: {artikel['AnzahlArtikel']}")
        print(f"Lieferant: {lieferant_name}\nLagerhaus: {lagerhaus_name}\nLagerplatz: {artikel['LagerPlatz']}")
    else:
        print("Artikel nicht gefunden.")
    Menuchange()

def AktionSArtikelLagerP():
    lagerplatz = input("Geben Sie den Lager Platz an: ")
    artikel_class = ArtikelClass()
    lieferant_class = LieferantClass()
    lagerhaus_class = LagerHausClass()

    matching_articles = []

    for artikel in artikel_class.Artikel:
        if artikel.get('LagerPlatz') == lagerplatz:
            matching_articles.append(artikel)

    if matching_articles:
        print(f"Artikel mit Lager Platz '{lagerplatz}':")
        for artikel in matching_articles:
            print(f"\nArtikelID: {artikel['ArtikelID']}")
            print(f"Bez: {artikel['Bez']}")
            print(f"Anzahl Artikel: {artikel['AnzahlArtikel']}")
            
            lieferant_id = artikel.get('LieferantID')
            lieferant_name = lieferant_class.get_lieferant_name_by_id(lieferant_id)
            print(f"Lieferant: {lieferant_name}")

            lagerhaus_id = artikel.get('LagerHausId')
            lagerhaus_name = lagerhaus_class.get_lagerhaus_name_by_id(lagerhaus_id)
            print(f"LagerHaus: {lagerhaus_name}")
            
            print(f"LagerPlatz: {artikel['LagerPlatz']}")
            print()
    else:
        print(f"Keine Artikel mit Lager Platz '{lagerplatz}' gefunden.")
    Menuchange()


# Eigenschaften Anzeigen
def AktionE():
    artikelnummer = input("Geben Sie die Artikel ID an für die Sie die Eigenschaften sehen möchten: ")
    artikelproperties = ArtikelProperties()
    artikelproperty = artikelproperties.get_artikelproperties_by_id(int(artikelnummer))
    artikel_class = ArtikelClass()
    artikel = artikel_class.get_artikel_by_id(int(artikelnummer))

    if artikelproperty and artikel:
        print(f"Artikel: {artikel['Bez']}")
        print(f"Artikel ID: {artikelproperty['ArtikelID']}")
        print(f"Grösse: {artikelproperty['Grösse']}")
        print(f"Gewicht: {artikelproperty['Gewicht']}")
        print(f"Farbe: {artikelproperty['Farbe']}")
    else:
        print("Artikel nicht gefunden.")
    
    Menuchange()



# Hinzufügen
def AktionHArtikel():
    clear()
    print("1. Anzahl Artikel erhöhen")
    print("2. Neuen Artikel hinzufügen")
    auswahl = input("Geben Sie Ihre Auswahl ein (1/2): ")

    if auswahl == "1":
        artikel_id = int(input("Artikel ID: "))
        artikel_class = ArtikelClass()
        existing_article = artikel_class.get_artikel_by_id(artikel_id)

        if existing_article:
            additional_quantity = int(input("Geben Sie die zusätzliche Menge an: "))
            existing_article['AnzahlArtikel'] += additional_quantity
            print(f"Anzahl des Artikels mit ID {artikel_id} um {additional_quantity} erhöht.")
        else:
            print("Artikel mit angegebener ID nicht gefunden.")
    elif auswahl == "2":
        bez = input("Bezeichnung: ")
        anzahl = int(input("Anzahl: "))
        try:
            lieferant_id = int(input("Lieferant ID: "))
        except:
            print("Das war keine Nummer")
        lagerhaus_id = int(input("Lagerhaus ID: "))
        lagerplatz = input("Lagerplatz: ")

        next_artikel_id = max(artikel["ArtikelID"] for artikel in ArtikelClass.Artikel) + 1
        lieferant_class = LieferantClass()
        lieferant = lieferant_class.get_lieferant_name_by_id(lieferant_id)

        lagerhaus_class = LagerHausClass()
        lagerhaus_name = lagerhaus_class.get_lagerhaus_name_by_id(lagerhaus_id)

        new_article = {
            "ArtikelID": next_artikel_id,
            "Bez": bez,
            "AnzahlArtikel": anzahl,
            "LieferantID": lieferant_id,
            "Lagerhaus": lagerhaus_name,
            "LagerPlatz": lagerplatz
        }
        ArtikelClass.Artikel.append(new_article)
        print("Artikel erfolgreich hinzugefügt!")
    else:
        print("Ungültige Auswahl. Bitte geben Sie '1' oder '2' ein.")

    Menuchange()


def AktionHLieferant():
    clear()
    bez = input("Name: ")

    next_lieferant_id = max(lieferant["LieferantID"] for lieferant in LieferantClass.Lieferanten) + 1

    new_lieferant = {
        "LieferantID": next_lieferant_id,
        "Name": bez,
    }
    LieferantClass.Lieferanten.append(new_lieferant)
    print(f"Lieferant erfolgreich hinzugefügt mit neuer LieferantID {next_lieferant_id}!")
    Menuchange()


def AktionHLagerPlatz():
    clear()
    bez = input("Bezeichnung des Lagerplatzes: ")
    lagerhaus_id = int(input("Geben Sie die Lagerhaus-ID oder den Namen an, zu dem der Lagerplatz gehört: "))

    lagerhaus_class = LagerHausClass()

    lagerhaus = lagerhaus_class.get_lagerhaus_by_id(lagerhaus_id)

    if lagerhaus:
        new_lagerplatz = {
            "Platz": bez,
        }

        if lagerhaus['Name'] in lagerhaus_class.Platz:
            lagerhaus_class.Platz[lagerhaus['Name']].append(new_lagerplatz)
        else:
            lagerhaus_class.Platz[lagerhaus['Name']] = [new_lagerplatz]

        print(f"Lagerplatz erfolgreich zu Lagerhaus {lagerhaus['Name']} hinzugefügt mit Bezeichnung {bez}!")
    else:
        print(f"Lagerhaus mit ID {lagerhaus_id} oder Name '{lagerhaus_id}' nicht gefunden.")

    Menuchange()


def AktionHLagerHaus():
    clear()
    ort = input("Ort: ")

    next_lagerhaus_id = max(lagerhaus["LagerHausId"] for lagerhaus in LagerHausClass.LagerHaus) + 1

    new_lagerhaus = {
        "LagerhausID": next_lagerhaus_id,
        "Ort": ort,
    }

    LagerHausClass.LagerHaus.append(new_lagerhaus)
    print(f"Lagerhaus erfolgreich hinzugefügt im {ort}!")
    Menuchange()


def AktionHArtikelproperty():
    clear()
    ArtikelId = int(input("ArtikelId: "))
    size = input("Grösse: ")
    weight = input("Gewicht: ")
    farbe = input("Farbe: ")

    new_Artikelproperties = {
        "ArtikelID": ArtikelId,
        "Grösse": size,
        "Gewicht": weight,
        "Farbe": farbe,
    }
   
    artikelproperties = ArtikelProperties()
    artikelproperty = artikelproperties.get_artikelproperties_by_id(ArtikelId)
    if artikelproperty:
        ArtikelProperties.Properties.remove(artikelproperty)
        print(f"Artikel Eigenschaften erfolgreich entfernt für Artikel {artikelproperty['ArtikelID']}!")

    ArtikelProperties.Properties.append(new_Artikelproperties)
    print(f"Artikel Eigenschaften erfolgreich hinzugefügt für Artikel {new_Artikelproperties['ArtikelID']}!")
    Menuchange()

# Löschen
def AktionL():
    ArtikelId = int(input("Artikel Id welcher gelöscht wird: "))
    loesch_option = input("Alle Artikel löschen (ALL) / Anzahl der zu löschenden Stücke: ")
    
    found = False
    for artikel in ArtikelClass.Artikel.copy():
        if artikel['ArtikelID'] == ArtikelId:
            if loesch_option.lower() == 'all':
                ArtikelClass.Artikel.remove(artikel)
                print(f"Alle Artikel mit ID {ArtikelId} wurden gelöscht.")
            else:
                anzahl_loeschung = int(loesch_option)
                if anzahl_loeschung >= artikel['AnzahlArtikel']:
                    ArtikelClass.Artikel.remove(artikel)
                    print(f"Artikel mit ID {ArtikelId} wurde komplett gelöscht.")
                else:
                    artikel['AnzahlArtikel'] -= anzahl_loeschung
                    print(f"{anzahl_loeschung} Stück(e) des Artikels mit ID {ArtikelId} wurden gelöscht.")
            found = True
            break
    
    if not found:
        print(f"Kein Artikel mit ID {ArtikelId} gefunden.")
    Menuchange()

# Verschieben
def AktionV():
    ArtikelId = int(input("Artikel Id welche verschoben werden soll: "))
    LagerplatzId = input("Lagerplatz in welche der Artikel verschoben werden soll: ")
   
    for artikel in ArtikelClass.Artikel:
        if artikel['ArtikelID'] == ArtikelId:
            print(f"Vorheriger Lagerplatz {artikel['LagerPlatz']}")
            artikel['LagerPlatz'] = LagerplatzId
            print(f"Artikel mit ID {ArtikelId} wurde in Lagerplatz {artikel['LagerPlatz']} verschoben.")
            Menuchange()
    print(f"Kein Artikel mit ID {ArtikelId} gefunden.")

# Alle Artikel anzeigen
def AktionA():
    artikel_class = ArtikelClass()
    lieferant_class = LieferantClass()
    lagerhaus_class = LagerHausClass()
    
    for artikel in artikel_class.Artikel:
        artikel_id = artikel['ArtikelID']
        bez = artikel['Bez']
        anzahl_artikel = artikel['AnzahlArtikel']
        lieferant_id = artikel.get('LieferantID')
        lagerhaus_id = artikel.get('LagerHausId')
        lagerplatz = artikel.get('LagerPlatz')

        lieferant_name = lieferant_class.get_lieferant_name_by_id(lieferant_id)
        lagerhaus_name = lagerhaus_class.get_lagerhaus_name_by_id(lagerhaus_id)

        print(f"ArtikelID: {artikel_id}")
        print(f"Bez: {bez}")
        print(f"Anzahl Artikel: {anzahl_artikel}")
        print(f"Lieferant: {lieferant_name}")
        print(f"LagerHaus: {lagerhaus_name}")
        print(f"LagerPlatz: {lagerplatz}")
        print()

    print(f"Anzahl Artikel insgesamt: {len(artikel_class.Artikel)}")
    Menuchange()


# List Items
class ListItems():

    def list_items(self):
        print("Was möchten Sie auflisten?:")
        print("1. Artikel")
        print("2. Lieferant")
        print("3. LagerHaus")
        choice = input("Ihre Eingabe (1/2/3): ")

        if choice == "1":
            self.list_artikel()
        elif choice == "2":
            self.list_lieferant()
        elif choice == "3":
            self.list_lagerhaus()
        else:
            print("Ungültige Eingabe. bitte 1, 2, oder 3 wählen.")
        Menuchange()

    def list_artikel(self):
        print("Artikel listen:")
        artikel_class = ArtikelClass()
        for artikel in artikel_class.Artikel:
            print(f"\nArtikel ID: {artikel['ArtikelID']}")
            print(f"Bez: {artikel['Bez']}")
            print(f"Anzahl Artikel: {artikel['AnzahlArtikel']}")
            print()

    def list_lieferant(self):
        print("Listing Lieferant:")
        lieferant_class = LieferantClass()
        for lieferant in lieferant_class.Lieferanten:
            print(f"\nLieferant ID: {lieferant['LieferantID']}")
            print(f"Name: {lieferant['Name']}")
            print()

    def list_lagerhaus(self):
        print("Listing Lager Haus:")
        lagerhaus_class = LagerHausClass()
        for lagerhaus in lagerhaus_class.LagerHaus:
            print(f"\nLagerHaus ID: {lagerhaus['LagerHausId']}")
            print(f"Name: {lagerhaus['Name']}")
            print()



# Menu
def menu():
        clear()
        Aktion = " "
        print("VERWALTUNG DES LAGERS")
        print()
        print("")
        print("S - Suchen")
        print("H - Hinzufügen")
        print("L - Artikel Löschen")
        print("V - Artikel Verschieben")
        print("A - Alle Artikel anzeigen")
        print("E - Eigenschaften anzeigen")
        print("LA - Items listen")
        print("Q - Quit")

        Aktion = input("\nWählen Sie eine Aktion aus: ")

        if Aktion == "S" or Aktion == "s":
            print("\n1. Artikel \n2. Alle Artikel im Lager Platz (ALP)\n")
            AktionSearch = input("Was möchten Sie Suchen (1/2): ")
            if AktionSearch == "1":
                AktionSArtikel()
            elif AktionSearch == "2":
                AktionSArtikelLagerP()
        elif Aktion == "H" or Aktion == "h":
            print("\n1. Lagerhaus \n2. Lagerplatz \n3. Artikel \n4. Lieferant \n5. Artikelproperty\n")
            AktionAdd = input("Was möchten Sie hinzufügen (1/2/3/4/5): ")

            if AktionAdd == "1":
                AktionHLagerHaus()
            elif AktionAdd == "2":
                AktionHLagerPlatz()
            elif AktionAdd == "3":
                AktionHArtikel()
            elif AktionAdd == "4":
                AktionHLieferant()
            elif AktionAdd == "5":
                AktionHArtikelproperty()
        elif Aktion == "L" or Aktion == "l":
            AktionL()
        elif Aktion == "V" or Aktion == "v":
            AktionV()
        elif Aktion == "A" or Aktion == "a":
            AktionA()
        elif Aktion == "E" or Aktion == "e":
            AktionE()
        elif Aktion == "LA" or Aktion == "la":
            your_instance = ListItems()
            your_instance.list_items()

        elif Aktion == "Q":
            clear()
            exit()
        else:
            print("Ungültige Eingabe: Nichts wird ausgeführt")


menu()
