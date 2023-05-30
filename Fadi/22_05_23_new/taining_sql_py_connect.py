import mysql.connector

class DatabaseManager:
    def __init__(self, host="localhost", user="root", password="", database="training_coucht_22_05_23"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connectionect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def disconnectionect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            
    def drop_table(self, table_name):
        self.connectionect()
        cursor = self.connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        self.connection.commit()
        self.disconnectionect()
        print(f"Table '{table_name}' dropped successfully.")

    # def delete_tables(self):
    #     self.cursor.execute("DROP TABLE IF EXISTS TrainingSession")
    #     self.cursor.execute("DROP TABLE IF EXISTS WorkoutPlan")
    #     self.cursor.execute("DROP TABLE IF EXISTS Exercise")
    #     self.cursor.execute("DROP TABLE IF EXISTS Goal")
    #     self.cursor.execute("DROP TABLE IF EXISTS TrainingLog")
    #     self.cursor.execute("DROP TABLE IF EXISTS Measurement")
    #     self.cursor.execute("DROP TABLE IF EXISTS TrainingUnit")
    #     self.cursor.execute("DROP TABLE IF EXISTS Person")
    #     self.connection.commit()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Person (
            person_id INT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            date_of_birth DATE,
            gender VARCHAR(10),
            desired_goal VARCHAR(100)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TrainingUnit (
            training_unit_id INT PRIMARY KEY,
            person_id INT,
            intensity VARCHAR(20),
            FOREIGN KEY (person_id) REFERENCES Person(person_id)
        )''')
        
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TrainingLog (
            training_log_id INT PRIMARY KEY,
            person_id INT,
            notes TEXT,
            FOREIGN KEY (person_id) REFERENCES Person(person_id)
        )''')
        

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Measurement (
            measurement_id INT PRIMARY KEY,
            person_id INT,
            training_log_id INT,
            weight FLOAT,
            height FLOAT,
            body_fat_percentage FLOAT,
            resting_heart_rate INT,
            waist INT,
            event_timestamp TIMESTAMP,
            maximum_heart_rate INT,
            FOREIGN KEY (person_id) REFERENCES Person(person_id),
            FOREIGN KEY (training_log_id) REFERENCES TrainingLog(training_log_id)
        )''')

        

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Goal (
            goal_id INT PRIMARY KEY,
            person_id INT,
            goal_description TEXT,
            FOREIGN KEY (person_id) REFERENCES Person(person_id)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Exercise (
            exercise_id INT PRIMARY KEY,
            exercise_name VARCHAR(100),
            muscle_group VARCHAR(50),
            description TEXT,
            demonstration_link VARCHAR(200)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS WorkoutPlan (
            workout_plan_id INT PRIMARY KEY,
            person_id INT,
            start_date DATE,
            end_date DATE,
            description TEXT,
            exercise_id INT,
            FOREIGN KEY (person_id) REFERENCES Person(person_id),
            FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id)
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS TrainingSession (
            training_session_id INT PRIMARY KEY,
            person_id INT,
            date DATE,
            duration TIME,
            intensity VARCHAR(20),
            calorie_burn FLOAT,
            workout_plan_id INT,
            FOREIGN KEY (person_id) REFERENCES Person(person_id),
            FOREIGN KEY (workout_plan_id) REFERENCES WorkoutPlan(workout_plan_id)
        )''')
        self.connection.commit()

db_manager = DatabaseManager()
# connectionect to the database
db_manager.connectionect()

# Delete existing tables
#db_manager.delete_tables()

# Create new tables
#db_manager.create_tables()

db_manager.drop_table("person")

# Disconnectionect from the database
db_manager.disconnectionect()


