# Aplikacja HomeFin - baza danych do zarządzania finansami
# Prototyp

import sqlite3
import datetime
from BTCInput import *

def create_new_table():
    """
    Tworzy nową tabelę wraz z wybraną nazwą
    """
    month = input("Wprowadź nazwę miesiąca :")
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    create_table = "CREATE TABLE " + month + " (data, kategoria, nazwa, cena)"
    c.execute(create_table)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()    

def add_one():
    """
    Wybiera miesiąc i dodaje do niego jeden produkt oraz cenę
    """
    conn = sqlite3.connect('homefin.db')
    month = input("Miesiąc: ")
    name = input("Nazwa: ")
    price = input("Cena :")
    date = datetime.date.today()

    add = "INSERT INTO " + month +" VALUES (?,?,?)"
    c = conn.cursor()
    
    c.execute(add, (date, name, price))

    conn.commit()
    conn.close()

def delete_one():
    conn = sqlite3.connect('homefin.db')
    month = input("Wybierz miesiąc: ")
    id_number = input("Wprowadź nr pozycji: ")

    delete_position = "DELETE from "+month+" WHERE rowid = (?)"
    c = conn.cursor()
    c.execute(delete_position, id_number)
    
    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()


def add_many():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    month = input("Miesiąc: ")
    global category
    sel_cat = category()
    list_of_expensive = []
    date = datetime.date.today()
    i = int(input("Ile wydatków chcesz wprowadzić: "))
    for count in range(1, i+1):
        exp_name = input("Nazwa: ")
        exp_value = input("Kwota: ")
        line = date,sel_cat,exp_name,exp_value
        list_of_expensive.append(tuple(line))

    add_many_position = "INSERT INTO "+month+" VALUES (?,?,?,?)"
    c.executemany(add_many_position, (list_of_expensive))
    
    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()


def show_all():

    #Connect to database
    conn = sqlite3.connect('homefin.db')
    #Create a cursor
    c = conn.cursor()
    month = input("\nMiesiąc: ")
    show = "SELECT rowid, * FROM "+month
    #Query The Database
    c.execute(show)

    items = c.fetchall()

    for item in items:
        print(item)

    sum_price = "SELECT SUM(cena) FROM "+month
    c.execute(sum_price)
    balance = c.fetchone()
    print("---------Razem: ", balance[0],"---------\n\n")

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()

def category():
    select_category = None
    select = """Wybierz kategorię
    1. Jedzenie
    2. Czynsz i opłaty
    3. Rozrywka
    4. Inne
    Wybierz: """
    command = read_int_ranged(select, 1, 4)
    if command == 1:
        select_category = 'Jedzenie'
    elif command == 2:
        select_category = 'Opłaty'
    elif command == 3:
        select_category = 'Rozrywka'
    elif command == 4:
        select_category = 'Inne'

    return select_category
    

def category_lookup():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    month = input("\nMiesiąc: ")
    category = """\nWybierz kategorię:
    1. Jedzenie
    2. Czynsz i opłaty
    3. Rozrywka
    4. Inne
    5. Powrót
    Wybierz: """

    while(True):
        command = read_int_ranged(category, 1, 5)
        if command == 1:
            lookup = "SELECT * from "+month+" WHERE kategoria IN (?) "
            c.execute(lookup,("Jedzenie",))
            items = c.fetchall()
            for item in items:
                print(item)

            sum_price = "SELECT SUM(cena) FROM "+month+" WHERE kategoria IN (?) "
            c.execute(sum_price,("Jedzenie",))
            balance = c.fetchone()
            print("---------Razem: ", balance[0],"---------\n\n")
            
        elif command == 2:
            lookup = "SELECT * from "+month+" WHERE kategoria IN (?) "
            c.execute(lookup,("Opłaty",))
            items = c.fetchall()
            for item in items:
                print(item)

            sum_price = "SELECT SUM(cena) FROM "+month+" WHERE kategoria IN (?) "
            c.execute(sum_price,("Opłaty",))
            balance = c.fetchone()
            print("---------Razem: ", balance[0],"---------\n\n")
            
        elif command == 3:
            lookup = "SELECT * from "+month+" WHERE kategoria IN (?)"
            c.execute(lookup,("Rozrywka",))
            items = c.fetchall()
            for item in items:
                print(item)

            sum_price = "SELECT SUM(cena) FROM "+month+" WHERE kategoria IN (?) "
            c.execute(sum_price,("Rozrywka",))
            balance = c.fetchone()
            print("---------Razem: ", balance[0],"---------\n\n")
            
        elif command == 4:
            lookup = "SELECT * from "+month+" WHERE kategoria IN (?)"
            c.execute(lookup,("Inne",))
            items = c.fetchall()
            for item in items:
                print(item)

            sum_price = "SELECT SUM(cena) FROM "+month+" WHERE kategoria IN (?) "
            c.execute(sum_price,("Inne",))
            balance = c.fetchone()
            print("---------Razem: ", balance[0],"---------\n\n")
            
        elif command == 5:
            break
            # Commit out command
            conn.commit()
            # Close our connection
            conn.close()

def id_lookup():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    month = input("\nMiesiąc: ")
    id_number = input("Wprowadź numer ID: ")
    lookup = "SELECT * from "+month+" WHERE rowid = (?)"
    c.execute(lookup,(id_number,))

    items = c.fetchall()

    if len(items)==0:
        print("Brak produktu")
    else:
        for item in items:
            print(item)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()

def name_lookup():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    month = input("\nMiesiąc: ")
    name = input("Wprowadź nazwę: ")
    lookup = "SELECT * from "+month+" WHERE nazwa = (?)"
    c.execute(lookup,(name,))
    items = c.fetchall()

    if len(items)==0:
        print("Brak produktu")
    else:
        for item in items:
            print(item)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()

def date_lookup():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    month = input("\nMiesiąc: ")
    date = input("Wprowadź datę (rrrr-mm-dd) : ")
    lookup = "SELECT * from "+month+" WHERE data = (?)"
    c.execute(lookup,(date,))
    items = c.fetchall()

    if len(items)==0:
        print("Nieporawny format daty")
    else:
        for item in items:
            print(item)

    # Commit out command
    conn.commit()
    # Close our connection
    conn.close()


def main_menu():
    menu = """ ---------Aplikacja Homefin---------

1. Stwórz nowy okres rozliczeniowy
2. Wprowadź wydatki
3. Wyświetl listę wydatków
4. Wyświetl kategoriami
5. Zamknij program

Wprowadź polecenie: """

    while(True):
        command = read_int_ranged(menu, 1, 5)
        if command == 1:
            create_new_table()
        elif command == 2:
            add_many()
        elif command == 3:
            show_all()
        elif command == 4:
            category_lookup()
        elif command == 5:
            break
            




main_menu()
#month = input("Miesiąc: ")
#create_new_table(month)
#add_one()
#delete_one()
#add_many()
#show_all()
#name_lookup()
#date_lookup()



















