from tkinter import Tk, Frame, Button, Label, Entry, Text, END
import mysql.connector

class Application_grid(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.title_label = Label(master, text = 'Personendatenbank')
        self.surname_label = Label(master, text = 'Nachname')
        self.givenname_label = Label(master, text = 'Vorname')
        self.surname_entry = Entry(master)
        self.givenname_entry = Entry(master)
        self.do_button = Button(master, text = 'Eintrag DB', command = self.action_do)
        self.break_button = Button(master, text = 'Abbrechen', command = self.break_do)
        self.display = Text(master)
        self.number_label = Label(master, text = 'Einträge = 0')
        self.clear_button = Button(master, text = 'Datenbank leeren', command = self.clear)

        self.title_label.grid(row = 0, column = 0, columnspan = 2)
        self.surname_label.grid(row = 1, column = 0)
        self.givenname_label.grid(row = 2, column = 0)
        self.surname_entry.grid(row = 1, column = 1)
        self.givenname_entry.grid(row = 2, column = 1)
        self.do_button.grid(row = 3, column = 0)
        self.break_button.grid(row = 3, column = 1)
        self.display.grid(row = 4, column = 0, columnspan = 2)
        self.number_label.grid(row = 5, column = 1)
        self.clear_button.grid(row = 5, column = 0)
        
        zuruck = Datenbank.select_from_table()
        self.display.delete('1.0',END)
        for zeile in zuruck:
            self.display.insert(END, zeile[1])
            self.display.insert(END, ', ')
            self.display.insert(END, zeile[0])
            self.display.insert(END, '\n')
        labelstring = 'Einträge = ' + str(Datenbank.count_table()[0][0])
        self.number_label.config(text = labelstring)

    def action_do(self):
        vorname = self.givenname_entry.get()
        nachname = self.surname_entry.get()
        Datenbank.insert_table(vorname, nachname)
        zuruck = Datenbank.print_table()
        self.display.delete('1.0',END)
        for zeile in zuruck:
            self.display.insert(END, zeile[1])
            self.display.insert(END, ', ')
            self.display.insert(END, zeile[0])
            self.display.insert(END, '\n')
        labelstring = 'Einträge = ' + str(Datenbank.count_table()[0][0])
        self.number_label.config(text = labelstring)

    def break_do(self):
        exit('Programm beendet!')

    def clear(self):
        Datenbank.datenbank_leeren()
        zuruck = Datenbank.select_from_table()
        self.display.delete('1.0',END)
        for zeile in zuruck:
            self.display.insert(END, zeile[1])
            self.display.insert(END, ', ')
            self.display.insert(END, zeile[0])
            self.display.insert(END, '\n')
        labelstring = 'Einträge = ' + str(Datenbank.count_table()[0][0])
        self.number_label.config(text = labelstring)

class Data():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            database = 'project',
            user="root",
            password="")           
        self.create_table()
        
    def create_table(self):
    

    
    # Prompt the user if they want to create a table
        accept = input("Would you like to create a table called Person? (yes/no): ")

        if accept.lower() == "yes":
        # Get the table name from the user
            table_name = input("Enter the table name: ")

        # Define the SQL query to create the table
            person =  f"CREATE TABLE {table_name} (person_id INT PRIMARY KEY,first_name VARCHAR(50),last_name VARCHAR(50),date_of_birth DATE,gender VARCHAR(10),weight DECIMAL(5, 2),height DECIMAL(5, 2),body_fat_percentage DECIMAL(5, 2),resting_heart_rate INT,desired_goal VARCHAR(100));"
        
        try:
            cursor = self.mydb.cursor()
            cursor.execute(person)
            self.mydb.commit()
           
            print(f"Table '{table_name}' created successfully!")
        except mysql.connector.ProgrammingError:
           
            print("No table created.")
            
            
            
            
            

    def insert_table(self, vorname, nachname):
        query = f"""INSERT INTO tabelle(_vorname, _nachname)
            VALUES  ('{vorname}','{nachname}');
            """
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
            self.mydb.commit()
        except mysql.connector.ProgrammingError as err:
            print('Fehler beim Einfügen')
            print(err)
        
    import mysql.connector

    def print_table():
    
    # Create a cursor object to execute SQL queries
        cursor = mydb.cursor()

    # Prompt the user to enter the table name
        table_name = input("Enter the table name: ")

    # Define the SQL query to select all fields from the table
        select_query = f"SELECT * FROM {table_name};"

    # Execute the select query
        cursor.execute(select_query)

    # Fetch all the records returned by the query
        records = cursor.fetchall()

    # Get the column names from the cursor description
        column_names = [desc[0] for desc in cursor.description]

    # Print the column names
        print(column_names)

    # Print the records
        for record in records:
         print(record)

    # Close the database connection
        mydb.close()

# Call the print_table function
    print_table()

        
    try:
            cursor = self.mydb.cursor()
            cursor.execute(person)
            self.mydb.commit()
           
            print(f"Table '{table_name}' created successfully!")
    except mysql.connector.ProgrammingError:
           
            print("No table created.")
    
    
    
    
    # def select_from_table(self):
        
        
        
    # # Prompt the user to enter the table name
    #     table_name = input("Enter the table name: ")
    #     # Define the SQL query to select all fields from the table
    #     select_query = f"SELECT * FROM {table_name};"
    #     cursor = mydb.cursor()
        
    #     # Execute the select query
    #     cursor.execute(select_query)
        
        
    # # Prompt the user to enter the field names
    #     fields = input("Enter the field names (comma-separated): ")


    # # Define the SQL query to select specific fields from the table
    #     select_query = f"SELECT {fields} FROM {table_name};"

    

   
    #     try:
    #         # Execute the select query
    #         cursor.execute(select_query)
            
    # # Fetch all the records returned by the query
    #         records = cursor.fetchall()
    #         return result
        
    #     except  mysql.connector.DataError:
    #         print('Datenfehler')
            
    def count_table(self):
        query = 'select COUNT(_vorname) FROM tabelle;'
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        
        except  mysql.connector.DataError:
            print('Datenfehler')

    def datenbank_leeren(self):
        create_query = """DELETE FROM tabelle;
            """
        try:
            cursor = self.mydb.cursor()
            cursor.execute(create_query)
            self.mydb.commit()
        except mysql.connector.ProgrammingError:
            print('Fehler beim Löschen!')


root = Tk()
Datenbank = Data()
app = Application_grid(root)
app.mainloop()