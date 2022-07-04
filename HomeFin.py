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

def add_many():
    conn = sqlite3.connect('homefin.db')
    c = conn.cursor()
    global month
    month = month
    global category
    sel_cat = category()
    list_of_expensive = []
    date = datetime.date.today()
    i = int(input("Ile wydatków chcesz wprowadzić: "))
    for count in range(1, i+1):
        exp_name = input("Nazwa: ")
        exp_value = input("Kwota: ")
        line = date,sel_cat,exp_name,exp_value.replace(",",".")
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
    global month
    month = month
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
    global month
    month = month
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

def load_sheet():
    global month
    month = input("Wprowadź nazwę okresu rozliczeniowego: ")
    menu = """

1.Wprowadź wydatki
2.Wyświetl listę wydatków
3.Wyświetl kategoriami
4.Wróć do poprzedniego menu

Wprowadź polecene: """

    while(True):
        command = read_int_ranged(menu, 1, 4)
        if command == 1:
            add_many()
        elif command == 2:
            show_all()
        elif command == 3:
            category_lookup()
        elif command == 4:
            break


def main_menu():
    menu = """ ---------Aplikacja Homefin---------

1. Stwórz nowy okres rozliczeniowy
2. Wczytaj okres rozliczeniowy
3. Zamknij program

Wprowadź polecenie: """

    while(True):
        command = read_int_ranged(menu, 1, 3)
        if command == 1:
            create_new_table()
        elif command == 2:
            load_sheet()
        elif command == 3:
            break
            




main_menu()




















