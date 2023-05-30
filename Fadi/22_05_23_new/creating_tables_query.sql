-- Active: 1684842887178@@127.0.0.1@3306@training_coucht_22_05_23
CREATE TABLE Person (
  person_id INT PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  date_of_birth DATE,
  gender VARCHAR(10),
  desired_goal VARCHAR(100)
);

CREATE TABLE TrainingUnit (
  training_unit_id INT PRIMARY KEY,
  person_id INT,
  intensity VARCHAR(20),
  FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

CREATE TABLE Measurement (
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
  
);

CREATE TABLE TrainingLog (
  training_log_id INT PRIMARY KEY,
  person_id INT,
  notes TEXT,
  FOREIGN KEY (person_id) REFERENCES Person(person_id)
  
  
);

CREATE TABLE Goal (
  goal_id INT PRIMARY KEY,
  person_id INT,
  goal_description TEXT,
  FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

CREATE TABLE Exercise (
  exercise_id INT PRIMARY KEY,
  exercise_name VARCHAR(100),
  muscle_group VARCHAR(50),
  description TEXT,
  demonstration_link VARCHAR(200)
);

CREATE TABLE WorkoutPlan (
  workout_plan_id INT PRIMARY KEY,
  person_id INT,
  start_date DATE,
  end_date DATE,
  description TEXT,
  exercise_id INT,
  FOREIGN KEY (person_id) REFERENCES Person(person_id),
  FOREIGN KEY (exercise_id) REFERENCES Exercise(exercise_id)
);

CREATE TABLE TrainingSession (
  training_session_id INT PRIMARY KEY,
  person_id INT,
  date DATE,
  duration TIME,
  intensity VARCHAR(20),
  calorie_burn FLOAT,
  workout_plan_id INT,
  FOREIGN KEY (person_id) REFERENCES Person(person_id),
  FOREIGN KEY (workout_plan_id) REFERENCES WorkoutPlan(workout_plan_id)
);


 --     DROP TABLE IF EXISTS TrainingSession;
   --   DROP TABLE IF EXISTS WorkoutPlan;
      DROP TABLE IF EXISTS Exercise;
      DROP TABLE IF EXISTS Goal;
      DROP TABLE IF EXISTS TrainingLog;
      DROP TABLE IF EXISTS Measurement;
      DROP TABLE IF EXISTS TrainingUnit;
      DROP TABLE IF EXISTS Person;
