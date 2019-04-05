"""
Name: Vrushali Kadam
Id: 1001514762
"""

import sqlite3

#creating a connection to the sqlite3 database
conn = sqlite3.connect("player_Data.db")

#the below piece of code creates the table player if it is not created int the database provided above
conn.execute('''
        CREATE TABLE if not exists Player
        (       

          name          TEXT        NOT NULL,
          wins          INT         NOT NULL,
          losses        INT         NOT NULL,
          ties          INT         NOT NULL,
          games         INT         NOT NULL

        )         
        ''')

#function to view player information in the players table in the database
def view_players(conn):
    query = '''SELECT name, wins, losses, ties
            FROM Player ORDER BY wins DESC '''
    cursor = conn.execute(query)
    print("{:10} {:>10} {:>10} {:>10} {:>10}".format("name", "wins", "losses", "ties", "games"))
    for row in cursor:
        print("{:10} {:>10} {:>10} {:>10} {:>10}".format(row[0], row[1], row[2], row[3], row[1] + row[2] + row[3]))

#function to add player information in the players table in the database
def add_player_info(conn):
    name = input("Enter the Player name : ")
    wins = int(input("Enter the number of wins : "))
    losses = int(input("Enter the number of losses : "))
    ties = int(input("Enter the number of ties : "))
    sql = '''INSERT INTO Player (name, wins, losses, ties) 
                 VALUES (?, ?, ?, ?)'''
    conn.execute(sql, (name, wins, losses, ties))
    conn.commit()
    print(name, "was added to the table")

#function to delete player information in the players table in the database
def del_player_info(conn):
    name = input("Enter the Player name to delete : ")
    sql = ''' DELETE FROM Player WHERE NAME = ?'''
    conn.execute(sql, (name,))
    conn.commit()
    print(name, " was deleted from the table")

#function to update player information in the players table in the database
def update_player_info(conn):
    name = input("Enter the Player name to Update : ")
    wins = int(input("Enter the new number of wins : "))
    losses = int(input("Enter  the new number of losses : "))
    ties = int(input("Enter the new number of ties : "))
    sql = '''UPDATE Player SET wins = ?, losses = ?, ties = ? 
                     WHERE name = ?'''
    conn.execute(sql, (wins, losses, ties, name))
    conn.commit()
    print(name, "was updated in the table")


#provide the user an interface to make choices for every function
choice = ""

while choice != "exit":
    print("Command Menu:")
    print("view - View players")
    print("add - Add a player")
    print("del - Delete a player")
    print("update  - Update a player")
    print("exit - Exit")
    choice = input("Enter a Command :")

    if choice.lower() == "view":
        view_players(conn)

    if choice.lower() == "add":
        add_player_info(conn)

    if choice.lower() == "del":
        del_player_info(conn)

    if choice.lower() == "update":
        update_player_info(conn)

    if choice.lower() == "exit":
        print("Bye!")
        exit()

#once the necessary functions are carried out on the database, the connection to the database is closed
conn.close()
