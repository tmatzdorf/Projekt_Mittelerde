import nltk
import pandas as pd

# Funktion um den gesamten Datensatz in der Python Konsole anziegen zu können
pd.set_option('display.max_rows', 100000)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', 10000)
pd.set_option('display.width', None)

##Pfad der einzenen Dateien auf dem Betriebssystem
filepath_Ringe = "/Users/tonimatzdorf/Desktop/Python Projekt Mittelerde/Der Herr der Ringe.txt"
filepath_Hobbit = "/Users/tonimatzdorf/Desktop/Python Projekt Mittelerde/Der Hobbit.txt"<<<<<<<<<<<<<<<
filepath_Silmarillion = "/Users/tonimatzdorf/Desktop/Python Projekt Mittelerde/Silmarillion.txt"

#Funktion zum öffnen der Datei
Ringe = open(filepath_Ringe,encoding="utf8")
#Ersetzen der neuen Zeilen durch eine Lücke
txt_Ringe = Ringe.read().replace('\n\n\n\n', ' ')
#Ersetzen der neuen Zeilen mit einem Leefeld
txt_Ringe_n = txt_Ringe.replace('\n', ' ')
#Funktion um den Text in Kleinschreibung zu Formatieren
txt_Ringe_lower = txt_Ringe_n.lower()
#Funktion um \t mit einem Leerfeld zu ersetzten
txt_Ringe_t = txt_Ringe_lower.replace('\t', ' ')
# Tokenize den Text
Ringe_toknz = nltk.tokenize.sent_tokenize(txt_Ringe_t)


Hobbit = open(filepath_Hobbit,encoding="utf8")
txt_Hobbit = Hobbit.read().replace('\n\n\n\n', ' ')
txt_Hobbit_n = txt_Hobbit.replace('\n', ' ')
#print('############# Der Hobbit #############')
txt_Hobbit_lower = txt_Hobbit_n.lower()
txt_Hobbit_t = txt_Hobbit_lower.replace('\t', ' ')
Hobbit_toknz_sent = nltk.tokenize.sent_tokenize(txt_Hobbit_t)


Silmarillion = open(filepath_Silmarillion,encoding="utf8")
txt_Silmarillion = Silmarillion.read().replace('\n\n\n\n', ' ')
txt_Silmarillion_n = txt_Silmarillion.replace('\n', ' ')
txt_Silmarillion_lower = txt_Silmarillion_n.lower()
txt_Silmarillion_t = txt_Silmarillion_lower.replace('\t', ' ')
Silmarillion_toknz_sent = nltk.tokenize.sent_tokenize(txt_Silmarillion_t)


###################
# Alle 3 Bücher werden in einer Liste gestellt.
books = []
books = Ringe_toknz + Hobbit_toknz_sent + Silmarillion_toknz_sent
print(len(books)) # 37272 Lists
print(type(books)) # <class 'list'>
print(books)

#########################
## Laden, Lesen der Charakter und Orte Dateien aus dem Speicher des Betriebssystems ###
All_Charaktere_Mitttelerde = '/Users/tonimatzdorf/Desktop/Python Projekt Mittelerde/Charaktere_Mitttelerde_utf8.csv'
All_Orte_Mittelerde = '/Users/tonimatzdorf/Desktop/Python Projekt Mittelerde/Orte_Mittelerde_utf8.csv'

# Diese Funktion liest die Datei der Charaktere
Charaktere = pd.read_csv(All_Charaktere_Mitttelerde, encoding="utf-8", sep=';')
#Ausgabe type(Charaktere))
# Funktion um die Namen der Charaktere in die Kleinschreibung zu formatieren.
Charaktere_low = Charaktere.apply(lambda x: x.astype(str).str.lower())
Charaktere_low_n = Charaktere_low.replace('\n', '')
Charaktere_low_n_t = Charaktere_low_n.replace('\t', '')
#Ausgabe (Charaktere_low_n_t.head(5))

Orte = pd.read_csv(All_Orte_Mittelerde, encoding="utf-8", sep=';')
Orte_low = Orte.apply(lambda x: x.astype(str).str.lower())
Orte_low_n = Orte_low.replace('\n', '')
Orte_low_n_t = Orte_low_n.replace('\t', '')
#Ausgabe (Orte_low_n_t.head(5))


### Diese Funktion kreiert eine Liste aller Kombinationen zwischen Charakter und Ort der ersten Charakter und Ort Spalte, möchte man Daten aus den anderen Spalten abgleichen, müssen die Spaltennamen hier eingetragen werden.
Character = Charaktere_low_n_t['Name']
Ort = Orte_low_n_t['Orte']

character_ort = []
orte_liste = []
character_list = []
L = []
for c in Character:
    for o in Ort:
        str_c = c.strip()
        str_o = o.strip()
        L = [str_c +';'+ str_o]
        character_ort.append(L)

# Ausgabe der Liste aller Kombinationen
print(character_ort)

#### Diese Funktioniert konvertiert die Liste aller Kombinationen in ein Python Dataframe
df_c_o = pd.DataFrame(character_ort)
df_c_o.columns = ['character_ort']
df_c_o["character_ort"]= df_c_o["character_ort"].str.split(";", n=1, expand=False)

#### Ausgabe character_ort
print(df_c_o["character_ort"])
#0 [adrahil i., erui]
#1  [adrahil i., ãußere lehen]
#2  [adrahil i., ãußerer ozean]

# Ausgabe der Anzahl der Kombinationen ohne Zusatznamen and Zusatzorte 'Name: character_ort, Length: 552660'
print(df_c_o["character_ort"][3])  # 4. Reihe ['adrahil i.', 'östliche täler']

###################
# Diese Funktion Konvertiertdas den Dataframe der Character_Ort zu einer Liste von Strings
char_ort_list =[]
for i in range(len(df_c_o["character_ort"])):
    words = df_c_o["character_ort"][i]
    char_ort_list.append(words)

# Ausgabe aller Kombinationen als seperate List mit einer sepration der Wörter ( in einer Liste von Strings)
print(char_ort_list)
#['die nordmenschen', 'wolkenkopf']
print(len(char_ort_list))
# Länge der Liste 552660 Zeilen
print(type(char_ort_list))
# <class 'list'>
#########################
from datetime import datetime
start_time = datetime.now()
print(char_ort_list)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
# Duration: 0:00:00.720883

####### Wieviel Mal ist der  Charakter an welche Ort aufgetaucht?
L_c_o = char_ort_list
#L_c_o = char_ort_list[10000] # Sicherung der Liste ( ersten 10000 reihen für beide Listen (Name, Ort)


# Diese Funktion schreibt die Liste aller Kombinationen in eine .csv Datei
import csv
with open("List_Characters_Orte.csv", "w", encoding='utf-8' , newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(L_c_o)

#### Diese Funktion beschreibt den Zugang der Strings, innerhalb der Liste der Strings
L_c_o[2][0] # dritte Reihe = [2] & the Name von Name_Column [0] (Erste reihe=0 Name, Zweite Spalte=1 Orte )
L_c_o[2] #  dritte Reihe (Name, Orte) ['adrahil i.', 'baumbarts felsen']


### Eingabemaske um eine Charakter wie ### gandalf, frodo.. auszuwählen
## oder : Eingabemaske um einen ort einzugeben.
person = 'gandalf'

index_list = []
for index, value in enumerate(character_ort):
    if str(character_ort[index]).find(person) != -1:
        print(f'{index}: {value}')
        index_list.append(index)

print("for the character " + str(person) + " first index: " + str(index_list[0]) + " last index: " + str(index_list[-1]) + " in the Character Ort Combination List ")
first_index = index_list[0]
last_index = index_list[-1]
print(first_index)
print(last_index)
L_c_o = char_ort_list[first_index:last_index]
print("The Character is: " + str(L_c_o[1][0]))
# Auflistung der ausgewählten Charaktere zur Suche in Chart_ort:list
L_c_o = char_ort_list[first_index:last_index]


i = 0
result = []
for i in range(len(L_c_o)):
    l = [all(word in sentence for word in L_c_o[i]) for sentence in books]
    #Ausgabe (result[i].append(sum(l)))
    aufgetaucht = 0
    aufgetaucht = sum(l)
    if (aufgetaucht) > 1:
        print("Der Charakter: " + str(L_c_o[i][0]) + " ist in: " + str(L_c_o[i][1]) + " " + str(sum(l)) + " aufgetaucht")
        result.append([str(L_c_o[i][0]),str(L_c_o[i][1]),str(aufgetaucht)])

print(result)
df_result = pd.DataFrame(result)
df_result.columns = ['character','Orte','Aufgetaucht']

# Um das Ergebnis speichern zu können, wird durch diese Funktion eine "csv" Datei erzeugt.
file_name = str(person) + ".csv"
path = "/Users/tonimatzdorf/Desktop/neu"
file_path = path + file_name
df_result.to_csv(file_path, index = False)


###########################
####### 2. Lösung ######
##########################

# Gebe einen Charakter ein
c = input('Please enter a character A-Z:\n')
# Gebe einen Ort ein
o = input('Please enter an Ort A-Z:\n')

# i to iterate as index
i = 0

# Leere Liste um den Index der Liste der  Character matched_indexes_i[] & Ort matched_indexes_o =[] mit jeden Text_Tokenized abzuspeichern.
matched_indexes_i =[]
matched_indexes_o =[]

print(" ############ Der Herr Der Ringe ###############")
# iterate on Der Herr Der Ringe Tokenized_Text from i = 0 zur Liste der Strings (Ringe_Toknz)
while i < (len(Ringe_toknz)):
    # wenn die Phrase einen Charakter beinhaltet (variable:c) => enthält nicht den befehl FIND wird durch -1 als Ergebnis ausgegeben , ist es anders (!=) as -1 => enthält c
    if Ringe_toknz[i].find(c) != -1:
       # wenn es enthält, fügt die Funktion den Index (des Zeichens im Satz) der Liste hinzu, damit der satz gefunden werden kann
        matched_indexes_i.append(i)
       #beinhaltet der String den Ort (same i)
        if Ringe_toknz[i].find(o) != -1:
           # Ausgabe der Phrase
            print(Ringe_toknz[i]+ "\n")
           #den Index (des Ortes im Satz) der Liste hinzufügen, damit die Phrase im Text gefunden wird.
            matched_indexes_o.append(i)
    i +=1
    # add 1 to i um zum nächsten String in der Liste der  string = Tokenized Text gehen zu können

# die Anzahl der Vorkommnisse zählen = die Länge der Zeichenliste (enthält die Indizes)
times = len(matched_indexes_i)
# die Anzahl der Vorkommen zählen = die Länge der Ortsliste (enthält die Indizes)
times_per_ort = len(matched_indexes_o)
#Ausgabe des Ergebnisses c = character, str(times) die Anzahl der Zeichen in Zeichenfolge umwandeln
print(c + " is present in Der Herr der Ringe " + str(times) + " mal")
#Ausgabe des Ergebnisses c = character, str(times) die Anzahl der Zeichen in Zeichenfolge umwandeln
print(c + " im Bezug mit " + o + " "+ str(times_per_ort) + " mal" + "\n")


print("  ############ Der Hobbit ###############")
j = 0
matched_indexes_ji =[]
matched_indexes_jo =[]

while j < len(Hobbit_toknz_sent):
    if Hobbit_toknz_sent[j].find(c) != -1:
       #Ausgabe(Hobbit_toknz_sent[j]+ "\n")
       matched_indexes_ji.append(j)
       if Hobbit_toknz_sent[j].find(o) != -1:
           print(Hobbit_toknz_sent[j]+ "\n")
           matched_indexes_jo.append(j)
    j += 1
times_j = len(matched_indexes_ji)
times_per_ort_j = len(matched_indexes_jo)
print(c + " is present in Der Hobbit " + str(times_j) + " mal")
print(c + " im Bezug mit " + o + " "+ str(times_per_ort_j) + " mal")


print(" ############ Silmarillion ###############")
k = 0
matched_indexes_ki =[]
matched_indexes_ko =[]

while k < len(Silmarillion_toknz_sent):
    if Silmarillion_toknz_sent[k].find(c) != -1:
       #Ausgabe(Silmarillion_toknz_sent[k]+ "\n")
       matched_indexes_ki.append(k)
       if Silmarillion_toknz_sent[k].find(o) != -1:
           print(Silmarillion_toknz_sent[k]+ "\n")
           matched_indexes_ko.append(k)
    k += 1
times_k = len(matched_indexes_ki)
times_per_ort_k = len(matched_indexes_ko)
print(c + " is present in Silmarillion " + str(times_k) + " mal")
print(c + " im Bezug mit " + o + " "+ str(times_per_ort_k) + " mal")

