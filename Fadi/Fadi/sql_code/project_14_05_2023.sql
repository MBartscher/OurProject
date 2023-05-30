-- Active: 1682934368065@@127.0.0.1@3306@project_py_connect
-- Create the Person table
CREATE TABLE Person (
    person_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    gender VARCHAR(10),
    weight DECIMAL(5, 2),
    height DECIMAL(5, 2),
    body_fat_percentage DECIMAL(5, 2),
    resting_heart_rate INT,
    desired_goal VARCHAR(100)
);

-- Create the TrainingUnit table
CREATE TABLE TrainingUnit (
    training_unit_id INT PRIMARY KEY,
    person_id INT,
    date DATE,
    duration INT,
    intensity INT,
    calorie_burn INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

-- Create the Measurement table
CREATE TABLE Measurement (
    measurement_id INT PRIMARY KEY,
    person_id INT,
    date DATE,
    weight DECIMAL(5, 2),
    body_fat_percentage DECIMAL(5, 2),
    resting_heart_rate INT,
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

-- Create the TrainingLog table
CREATE TABLE TrainingLog (
    training_log_id INT PRIMARY KEY,
    person_id INT,
    training_unit_id INT,
    measurement_id INT,
    notes VARCHAR(500),
    FOREIGN KEY (person_id) REFERENCES Person(person_id),
    FOREIGN KEY (training_unit_id) REFERENCES TrainingUnit(training_unit_id),
    FOREIGN KEY (measurement_id) REFERENCES Measurement(measurement_id)
);

-- Create the Goal table
CREATE TABLE Goal (
    goal_id INT PRIMARY KEY,
    person_id INT,
    goal_description VARCHAR(500),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

-- Create the Exercise table
CREATE TABLE Exercise (
    exercise_id INT PRIMARY KEY,
    exercise_name VARCHAR(100),
    muscle_group VARCHAR(100),
    description VARCHAR(1000),
    demonstration_link VARCHAR(500)
);

-- Create the WorkoutPlan table
CREATE TABLE WorkoutPlan (
    workout_plan_id INT PRIMARY KEY,
    person_id INT,
    start_date DATE,
    end_date DATE,
    description VARCHAR(1000),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

-- Create the ExerciseSet table
CREATE TABLE ExerciseSet (
    exercise_set_id INT PRIMARY KEY,
    workout_plan_id INT,
    exercise_id INT,
    sets INT,
    reps INT,
    weight DECIMAL(5, 2),
    FOREIGN KEY (workout_plan_id) REFERENCES WorkoutPlan(workout_plan_id),
    FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id)
);
