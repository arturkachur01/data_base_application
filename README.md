# Execution (MacOs)
``` 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 insert_data.py
python3 recommendations.py
python3 query_data.py
python3 -m unittest test_app.py
coverage run -m unittest test_app.py
coverage report
``` 

# Step 1: Health and Fitness Tracking App Overview

The Health and Fitness Tracking App is an advanced digital platform designed to empower users in their journey towards optimal health and fitness. With a focus on user-friendliness, the app provides a comprehensive suite of tools for tracking health metrics, logging workouts, monitoring nutrition, and analyzing sleep patterns. It stands out by offering personalized fitness recommendations and deep insights derived from sophisticated data analysis.

## Target Audience

The app serves a wide audience, from fitness aficionados and professional athletes to those just beginning their wellness journey. It's tailored to accommodate individual fitness levels and goals, such as weight management, muscle development, athletic enhancement, or overall health improvement.

## Health and Fitness Metrics Tracked

- **Workout Logs**: Detailed records of exercise sessions, including exercise type, duration, intensity, and personalized notes.
- **Nutrition Logs**: Comprehensive tracking of daily dietary intake, detailing calories, macros (proteins, fats, carbs), and micros (vitamins, minerals).
- **Sleep Patterns**: Insights into sleep quality, duration, and disturbances, crucial for understanding recovery and health impacts.
- **Health Metrics**: Regular monitoring of key health indicators like weight, BMI, heart rate, and blood pressure, providing a holistic health overview.
- **Advanced Analytics**: Leveraging data to uncover correlations between dietary habits and workout performance, and to identify health trends over time.

## Benefits to Users

- **Goal-Oriented Tracking**: Enables precise goal setting and progress monitoring, facilitating clear paths towards health and fitness objectives.
- **Data-Driven Insights**: Utilizes advanced analytics to offer personalized insights, highlighting progress and areas for improvement.
- **Motivational Support**: Encourages consistency through regular monitoring, fostering a sense of accountability and motivation.
- **Customized Recommendations**: Delivers tailored fitness and nutritional advice based on individual data, enhancing the effectiveness of health strategies.
- **Community Engagement**: Offers opportunities for user interaction and support, fostering a motivational community atmosphere.

By integrating sophisticated data analysis, the Health and Fitness Tracking App not only aids users in tracking their daily health and fitness activities but also provides actionable insights and personalized recommendations. This advanced approach ensures that users can make informed decisions, leading to more effective and satisfying health and fitness outcomes.

# Step 2: Identify Data Requirements

The effectiveness of the Health and Fitness Tracking App is contingent upon its ability to meticulously store and manage diverse data elements. These elements encompass a wide range of user-specific information, including detailed logs of physical activities, dietary intake, sleep quality, and comprehensive health metrics. The intricacies of the relationships among these data elements are pivotal for the app's capacity to provide nuanced, personalized recommendations and to accurately chart each user's journey towards their fitness aspirations.

## Key Data Elements:

- **User Data**: Critical personal information such as name, age, gender, height, weight, and specific health goals (like weight loss or muscle building). This foundational data underpins the creation of customized user profiles and the tailoring of the app's recommendations.

- **Workout Logs**: Each workout session is meticulously logged, detailing exercise type (cardio, strength, etc.), session duration, intensity level, and specific exercises performed when applicable. This information is instrumental in tracking user progress and fine-tuning fitness regimens.

- **Nutritional Intake Logs**: The app tracks daily dietary intake, capturing details such as meal timing, food types, portion sizes, and comprehensive nutritional content, including caloric and macronutrient breakdowns. This granular data is essential for assessing dietary habits and formulating dietary recommendations.

- **Sleep Data**: Insights into sleep duration, quality, and disturbances are recorded, providing a crucial lens through which to gauge recovery and overall health impacts.

- **Comprehensive Health Metrics**: Regular monitoring of key health indicators, including body weight, BMI, heart rate, and blood pressure, offers valuable insights into the user's overall health trajectory.

## Data Relationships:

- **User and Health Metrics**: A symbiotic link exists between each user's health metrics and their profile, enabling the tracking of temporal changes and the fine-tuning of health recommendations.

- **Workout Logs and User Profile**: Workout data is intricately linked to individual user profiles, ensuring fitness recommendations and progress tracking are deeply personalized.

- **Nutritional Logs and User Profile**: Dietary data is tethered to the user's profile, facilitating in-depth dietary analysis and tailored nutritional guidance.

- **Sleep Data and User Profile**: Sleep metrics are associated with the user's profile, shedding light on the interplay between sleep patterns and overall health and fitness levels.

## The Imperative of Data Capture:

The meticulous capture of these diverse data points is the linchpin of the app's functionality, enabling:

- **Tailored Recommendations**: The app personalizes fitness and nutrition recommendations to align with each user's unique health profile and aspirations.

- **Comprehensive Progress Tracking**: By monitoring shifts in health metrics, workout achievements, dietary patterns, and sleep quality, the app provides a holistic view of the user's progress.

- **Insightful Data Analysis**: The app delves into the amassed data to unveil actionable insights, highlighting progress milestones and areas ripe for improvement.

- **Informed Goal Setting**: The app aids users in setting attainable health and fitness goals, underpinned by their historical data and progress trends.

In essence, the Health and Fitness Tracking App's capacity to offer a personalized and comprehensive health and fitness overview hinges on its adept management of intricate data elements and their interrelations. This foundational data architecture not only propels personalized health interventions but also empowers users to navigate their health and fitness journey with informed precision.

# Step 3-5

See create.py, instert_data.py, query_data.py, recommendations.py, test_app.py code in the bottom of README.md file, where the detailed comments are added to justify and explain the data schema design, queries, data inserted, and unit tests.

# Advanced Database Features and Best Practices

## Data Normalization
Our database design adheres to the principles of data normalization to ensure data integrity and reduce redundancy. Specifically:

- **1NF (First Normal Form):** All tables are structured with a primary key, ensuring that each record is unique and that there is no repeating group of fields within a single record. For instance, the `Users` table has `user_id` as its primary key, uniquely identifying each user.
- **2NF (Second Normal Form):** Our design separates data into different tables to avoid partial dependency on a primary key. This is evident in how workout details, nutrition logs, and sleep records are stored in their respective tables (`Workouts`, `Nutrition`, `Sleep`), each linked to `Users` via foreign keys.
- **3NF (Third Normal Form):** We've ensured that all fields in each table are only dependent on the primary key, eliminating transitive dependency. For example, nutrition information is directly related to a meal and not indirectly through another entity.

## Indices
Indices have been implicitly created for all primary key columns to optimize query performance. For example, `user_id` in the `Users` table and `workout_id` in the `Workouts` table are indexed by default as primary keys. This setup significantly enhances the efficiency of operations like lookups, joins, and aggregations.

## Transactions
Our data insertion scripts utilize transactions to maintain database consistency and integrity. By wrapping the insert operations within a session commit in SQLAlchemy, we ensure that either all changes are successfully applied or none at all, preventing partial updates that could lead to data anomalies.

## Exceeding Requirements (Optional)
- **Advanced Query Scenarios:** We've implemented complex queries beyond basic CRUD operations, such as correlating nutrition and workout data (`correlate_nutrition_and_workout`) and analyzing health metric trends (`analyze_health_metric_trends`). These queries provide deep insights and add significant value to the application's analytical capabilities.
- **Recommendation Engine:** The addition of a recommendation engine (`get_fitness_recommendations`, `get_nutrition_recommendations`) in `recommendations.py` exceeds typical assignment expectations by offering personalized advice based on user data, enhancing the app's interactivity and user engagement.

These elements of our project not only fulfill the assignment's core requirements but also incorporate advanced database concepts and application features, showcasing a comprehensive understanding and application of database systems in a real-world project scenario.

## Step 6: Query Optimization

In the development of our Health and Fitness Tracking App, we implemented several SQL queries to extract insights from the user data. Below, we discuss the optimization strategies used and propose additional enhancements to further improve query efficiency.

### Current Optimization Techniques

1. **Use of Indexes**: Primary keys (`user_id`, `workout_id`, `meal_id`, etc.) naturally create indexes in the database, which significantly speed up query performance, especially for `JOIN` operations and where clauses.

2. **Filtering Data**: In functions like `get_user_workout_history`, we efficiently filter data by date range and `user_id` before fetching it, minimizing the amount of data processed and transferred.

3. **Aggregation Functions**: Utilizing SQL's built-in aggregation functions (`func.sum`, `func.avg`) in queries such as `get_average_daily_calories` and `correlate_nutrition_and_workout` optimizes the calculation process, leveraging the database engine's optimization.

### Proposed Enhancements

1. **Implementing More Indexes**: While primary keys are automatically indexed, adding indexes to frequently queried columns like `date` in `Workout`, `Nutrition`, `Sleep`, and `HealthMetrics` tables can further optimize query performance.

2. **Batch Processing**: For operations inserting or updating large volumes of data, consider batch processing techniques to reduce the number of transactions and improve efficiency.

3. **Query Refactoring**: Analyze complex queries with the SQL `EXPLAIN` command to identify potential bottlenecks. Refactoring these queries or breaking them down into simpler subqueries can improve execution plans and performance.

4. **Materialized Views**: For very complex queries that aggregate large amounts of data (e.g., trend analysis over time), consider using materialized views that store query results and can be refreshed periodically. This approach can significantly reduce load times for frequently accessed, computation-heavy data.

5. **Connection Pooling**: Implement connection pooling to reduce the overhead of establishing connections to the database, especially for applications expected to handle a high volume of requests.

By applying these strategies, we can enhance the performance of our Health and Fitness Tracking App, ensuring a smooth and responsive experience for our users.

# All code used in the assignment
## create.py
``` 
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Text, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Establish a connection to the SQLite database. 'echo=False' suppresses log output for clarity.
engine = create_engine('sqlite:///health_fitness_app.db', echo=False)

# Create a sessionmaker instance for database interactions.
Session = sessionmaker(bind=engine)

class User(Base):
    """
    Represents a user in the app, containing personal info and health goals.
    This table serves as the central point, linking to all other data related to a user, 
    thus enabling a holistic view of each user's health and fitness journey.
    """
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, CheckConstraint("gender IN ('Male', 'Female', 'Other')"), nullable=False)
    height = Column(Float, nullable=False)  # Stored in centimeters
    weight = Column(Float, nullable=False)  # Stored in kilograms
    goal = Column(Text, nullable=False)
    # Relationships establish links to other tables, enabling complex queries and data analysis.
    workouts = relationship("Workout", back_populates="user")
    nutrition_logs = relationship("Nutrition", back_populates="user")
    sleep_records = relationship("Sleep", back_populates="user")
    health_metrics = relationship("HealthMetrics", back_populates="user")

class Workout(Base):
    """
    Stores details of user workouts. Linked to the User table, allowing tracking of each user's exercise routines,
    critical for personalizing fitness plans and tracking progress.
    """
    __tablename__ = 'Workouts'
    workout_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # Stored in minutes
    intensity = Column(String, CheckConstraint("intensity IN ('Low', 'Medium', 'High')"), nullable=False)
    user = relationship("User", back_populates="workouts")

class Nutrition(Base):
    """
    Captures detailed nutrition logs for users. Essential for analyzing dietary habits and providing nutritional advice.
    Linked to the User table for personalized dietary recommendations.
    """
    __tablename__ = 'Nutrition'
    meal_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    type = Column(String, CheckConstraint("type IN ('Breakfast', 'Lunch', 'Dinner', 'Snack')"), nullable=False)
    calories = Column(Integer, nullable=False)
    protein = Column(Float, nullable=False)  # Stored in grams
    carbs = Column(Float, nullable=False)    # Stored in grams
    fats = Column(Float, nullable=False)     # Stored in grams
    user = relationship("User", back_populates="nutrition_logs")

class Sleep(Base):
    """
    Records user sleep data, including duration and quality. Sleep data is crucial for understanding recovery and overall health,
    thus linked to the User table for a comprehensive health analysis.
    """
    __tablename__ = 'Sleep'
    sleep_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    duration = Column(Float, nullable=False)  # Stored in hours
    quality = Column(String, CheckConstraint("quality IN ('Poor', 'Fair', 'Good', 'Excellent')"), nullable=False)
    user = relationship("User", back_populates="sleep_records")

class HealthMetrics(Base):
    """
    Stores health metrics like weight, BMI, heart rate, and blood pressure.
    This data is crucial for monitoring overall health trends and making adjustments to fitness and nutrition plans.
    The relationship with the User table allows for personalized health tracking and recommendations.
    """
    __tablename__ = 'Health_Metrics'
    metric_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)  # Stored in kilograms
    bmi = Column(Float, nullable=False)     # BMI calculated based on weight and height
    heart_rate = Column(Integer)            # Stored in beats per minute
    blood_pressure = Column(String)         # Stored as a string, e.g., "120/80"
    user = relationship("User", back_populates="health_metrics")

if __name__ == '__main__':
   # This script will create the database and tables based on the defined schema when run directly.
   Base.metadata.create_all(engine)

# Design Justification:
# The schema is designed to provide a comprehensive and holistic view of a user's health and fitness journey.
# By linking detailed workout, nutrition, sleep, and health metric data to individual user profiles,
# the app can offer personalized recommendations and insights, thereby encouraging users to make informed
# decisions about their health and fitness routines. The use of relationships and foreign keys ensures data integrity
# and facilitates complex queries that can drive the app's core features, such as progress tracking and trend analysis.
``` 
## insert_data.py
```
from create import User, Workout, Nutrition, Sleep, HealthMetrics, engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def generate_random_date(start_date, end_date):
    """
    Generates a random date between two specified dates. Used to create realistic date entries for data records.
    """
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

def generate_users(n=10):
    """
    Populates the database with sample user data. Each user has a unique set of attributes like name, age, gender, etc.
    """
    for _ in range(n):
        user = User(
            name=fake.name(),
            age=random.randint(18, 65),
            gender=random.choice(['Male', 'Female', 'Other']),
            height=round(random.uniform(150.0, 200.0), 2),
            weight=round(random.uniform(50.0, 120.0), 2),
            goal=random.choice(['Weight Loss', 'Muscle Gain', 'Improve Fitness'])
        )
        session.add(user)
    session.commit()

def generate_workouts(n=50):
    """
    Generates workout records for each user. Workouts vary by type, duration, and intensity, reflecting realistic fitness activities.
    """
    users = session.query(User).all()
    for user in users:
        for _ in range(n):
            workout = Workout(
                user_id=user.user_id,
                date=generate_random_date(datetime.now() - timedelta(days=365), datetime.now()),
                type=random.choice(['Cardio', 'Strength', 'Flexibility', 'Balance']),
                duration=random.randint(15, 120),
                intensity=random.choice(['Low', 'Medium', 'High'])
            )
            session.add(workout)
    session.commit()

def generate_nutrition_logs(n=150):
    """
    Creates detailed nutrition logs for each user, tracking daily food intake, calories, and macronutrients.
    """
    users = session.query(User).all()
    for user in users:
        for _ in range(n):
            nutrition = Nutrition(
                user_id=user.user_id,
                date=generate_random_date(datetime.now() - timedelta(days=365), datetime.now()),
                type=random.choice(['Breakfast', 'Lunch', 'Dinner', 'Snack']),
                calories=random.randint(100, 800),
                protein=round(random.uniform(0, 50), 2),
                carbs=round(random.uniform(0, 100), 2),
                fats=round(random.uniform(0, 50), 2)
            )
            session.add(nutrition)
    session.commit()

def generate_sleep_records(n=100):
    """
    Simulates sleep data for users, recording the duration and quality of sleep, to analyze its impact on health and fitness.
    """
    users = session.query(User).all()
    for user in users:
        for _ in range(n):
            sleep = Sleep(
                user_id=user.user_id,
                date=generate_random_date(datetime.now() - timedelta(days=365), datetime.now()),
                duration=round(random.uniform(4, 12), 2),
                quality=random.choice(['Poor', 'Fair', 'Good', 'Excellent'])
            )
            session.add(sleep)
    session.commit()

def generate_health_metrics(n=50):
    """
    Generates records of various health metrics for users, such as weight, BMI, heart rate, and blood pressure, to monitor health changes over time.
    """
    users = session.query(User).all()
    for user in users:
        for _ in range(n):
            weight = round(random.uniform(50.0, 120.0), 2)
            height = user.height / 100  # convert cm to m
            bmi = round(weight / (height ** 2), 2)
            health_metric = HealthMetrics(
                user_id=user.user_id,
                date=generate_random_date(datetime.now() - timedelta(days=365), datetime.now()),
                weight=weight,
                bmi=bmi,
                heart_rate=random.randint(60, 100),
                blood_pressure=f"{random.randint(100, 140)}/{random.randint(60, 90)}"
            )
            session.add(health_metric)
    session.commit()

if __name__ == '__main__':
    # Generate sample data to populate the database, ensuring a variety of user profiles and activities for testing.
    generate_users(10)  # Generate 10 sample users
    generate_workouts(50)  # Generate 50 workouts per user
    generate_nutrition_logs(150)  # Generate 150 nutrition logs per user
    generate_sleep_records(100)  # Generate 100 sleep records per user
    generate_health_metrics(50)  # Generate 50 health metrics records per user

```
## recommendations.py
```
from create import User, Workout, Nutrition, Sleep, HealthMetrics, Session
from sqlalchemy import func
from datetime import datetime, timedelta

def get_fitness_recommendations(user_id):
    """
    Generates personalized fitness recommendations based on the user's recent workout history.
    The recommendations adjust based on workout frequency and intensity to encourage balanced and consistent exercise habits.
    """
    session = Session()
    # Fetch recent workouts for the given user, focusing on the last 30 days to ensure recommendations are current and relevant.
    recent_workouts = session.query(Workout).filter(
        Workout.user_id == user_id,
        Workout.date >= datetime.now() - timedelta(days=30)
    ).order_by(Workout.date.desc()).all()

    # Default recommendation for new users or those without recent workout data.
    if not recent_workouts:
        return "We recommend starting with light cardio sessions, 15-30 minutes a day, three times a week."

    # Analyze workout intensity and frequency to tailor recommendations.
    high_intensity_count = sum(1 for workout in recent_workouts if workout.intensity == 'High')
    workout_days = {workout.date for workout in recent_workouts}

    # Provide specific advice based on the user's workout patterns.
    if len(workout_days) < 8:
        return "To achieve your goals faster, try to increase your workout frequency to at least twice a week."
    elif high_intensity_count < len(recent_workouts) / 2:
        return "Consider incorporating more high-intensity workouts into your routine to maximize your fitness gains."
    else:
        return "Great job maintaining a consistent workout routine! Try challenging yourself with varied workout types to improve all aspects of fitness."

def get_nutrition_recommendations(user_id):
    """
    Offers nutrition recommendations based on the user's recent calorie intake.
    Tailored advice helps users align their diet with health and fitness goals.
    """
    session = Session()
    # Aggregate recent nutrition logs to calculate average daily calorie intake.
    recent_nutrition_logs = session.query(
        Nutrition.date, 
        func.sum(Nutrition.calories).label('total_calories')
    ).filter(
        Nutrition.user_id == user_id,
        Nutrition.date >= datetime.now() - timedelta(days=7)
    ).group_by(Nutrition.date).all()

    # Encourage users to start tracking their nutrition if no data is available.
    if not recent_nutrition_logs:
        return "Start tracking your daily nutrition to receive personalized dietary advice."

    # Calculate the average calorie intake and provide recommendations based on it.
    average_calories = sum(log.total_calories for log in recent_nutrition_logs) / len(recent_nutrition_logs)

    # Tailored advice based on calorie intake ranges.
    if average_calories < 1500:
        return "Your calorie intake might be too low for optimal health. Consider consulting a dietitian for a personalized meal plan."
    elif average_calories > 2500:
        return "You might be consuming more calories than necessary. Focus on nutrient-dense foods and monitor portion sizes."
    else:
        return "Your average calorie intake is within a healthy range. Keep up the good work and ensure you're getting a balanced mix of nutrients."

# Separating recommendation logic into a different file (recommendations.py):
# This modular approach enhances code maintainability and readability, allowing the core querying logic to remain focused on data retrieval,
# while recommendation-specific logic can evolve independently, incorporating more complex algorithms or external services as needed.

# if __name__ == '__main__':
    # Test the recommendations for a given user ID
    # user_id = 1  # Adjust based on the database
    # fitness_advice = get_fitness_recommendations(user_id)
    # nutrition_advice = get_nutrition_recommendations(user_id)
    # print(f"Fitness Recommendation for User {user_id}: {fitness_advice}")
    # print(f"Nutrition Recommendation for User {user_id}: {nutrition_advice}")
```
## query_data.py
```
from create import User, Workout, Nutrition, Sleep, HealthMetrics, engine
from recommendations import get_fitness_recommendations, get_nutrition_recommendations
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from datetime import datetime, timedelta

# Setting up the session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()

def get_user_workout_history(user_id, days=30):
    """
    Retrieves a user's workout history over a specified period, defaulting to the last 30 days.
    This function helps users track their exercise patterns and progress over time.
    """
    # Calculate the date range for query.
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Query workouts within the date range for the specified user.
    workouts = session.query(Workout).filter(
        Workout.user_id == user_id,
        Workout.date >= start_date,
        Workout.date <= end_date
    ).all()

    # Provide feedback based on the presence of workout data.
    if not workouts:
        print(f"No workouts found for user {user_id} in the last {days} days.")
    for workout in workouts:
        print(f"Date: {workout.date}, Type: {workout.type}, Duration: {workout.duration} minutes, Intensity: {workout.intensity}")

def get_average_daily_calories(user_id, days=7):
    """
    Computes the average daily calorie intake for a user over the last 7 days.
    This insight assists users in managing their dietary habits aligned with their fitness goals.
    """
    # Define the date range for the query.
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Aggregate calorie data and compute the average.
    calories = session.query(
        Nutrition.date, 
        func.sum(Nutrition.calories).label('total_calories')
    ).filter(
        Nutrition.user_id == user_id,
        Nutrition.date >= start_date,
        Nutrition.date <= end_date
    ).group_by(Nutrition.date).all()

    # Provide feedback based on calorie data availability.
    if not calories:
        print(f"No nutrition data found for user {user_id} in the last {days} days.")
        return 0  # Return 0 if no data found
    else:
        total_calories = sum([cal.total_calories for cal in calories])
        average_calories = total_calories / len(calories)
        print(f"Average daily calories over the last {days} days: {average_calories}")
        return average_calories  # Return the calculated average

def analyze_sleep_quality(user_id, days=30):
    """
    Analyzes a user's sleep quality over the last 30 days, providing insights into their rest patterns.
    Good sleep quality is crucial for recovery and overall health, making this function valuable for wellness tracking.
    """
    # Determine the query date range.
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # Group sleep records by quality and count occurrences.
    sleep_quality = session.query(
        Sleep.quality, 
        func.count(Sleep.quality).label('count')
    ).filter(
        Sleep.user_id == user_id,
        Sleep.date >= start_date,
        Sleep.date <= end_date
    ).group_by(Sleep.quality).all()

    # Initialize a dictionary to summarize sleep quality analysis.
    sleep_quality_summary = {}

    # Output sleep quality analysis and populate the summary dictionary.
    if not sleep_quality:
        print(f"No sleep data found for user {user_id} in the last {days} days.")
        return {}  # Return an empty dict if no data found
    for quality in sleep_quality:
        print(f"Quality: {quality.quality}, Count: {quality.count}")
        sleep_quality_summary[quality.quality] = quality.count
    
    # Return the summary dictionary.
    return sleep_quality_summary

# Below functions are examples of more advanced queries that might be added to enhance the app's functionality:
# They demonstrate how the application could leverage complex SQL queries to provide deeper insights into the user's health and fitness data.

def correlate_nutrition_and_workout(user_id):
    """
    Correlates a user's nutrition (specifically protein intake) with their workout habits.
    Understanding this correlation can help in tailoring a balanced fitness and nutrition plan.
    """
    from sqlalchemy.sql import func

    # Subqueries to calculate average daily protein intake and workout duration.
    protein_intake = session.query(
        Nutrition.date,
        func.avg(Nutrition.protein).label('average_protein')
    ).filter(Nutrition.user_id == user_id).group_by(Nutrition.date).subquery()

    workout_duration = session.query(
        Workout.date,
        func.avg(Workout.duration).label('average_duration')
    ).filter(Workout.user_id == user_id).group_by(Workout.date).subquery()

    # Joining the two subqueries on date
    correlation_data = session.query(
        protein_intake.c.date,
        protein_intake.c.average_protein,
        workout_duration.c.average_duration
    ).join(workout_duration, protein_intake.c.date == workout_duration.c.date).all()

    # Display the correlation results
    for data in correlation_data:
        print(f"Date: {data.date}, Avg Protein Intake: {data.average_protein}g, Avg Workout Duration: {data.average_duration} mins")
    
    return correlation_data or []

def analyze_health_metric_trends(user_id, metric='weight'):
    """
    Analyzes trends in a specific health metric (default: weight) for a user over time.
    Tracking changes in health metrics can provide valuable feedback on the user's overall progress and health status.
    """
    # Query to get the specified health metric over time
    metrics_data = session.query(
        HealthMetrics.date,
        getattr(HealthMetrics, metric)
    ).filter(HealthMetrics.user_id == user_id).order_by(HealthMetrics.date).all()

    # Output the trend data for the specified health metric.
    print(f"Trends for {metric}:")
    for data in metrics_data:
        print(f"Date: {data.date}, {metric.capitalize()}: {getattr(data, metric)}")
    
    return metrics_data or []

if __name__ == '__main__':
    user_id = 1  # Adjust as needed based on your database data

    # Demonstrate each query function with example output.
    print(f"--- Workout History for User {user_id} ---")
    get_user_workout_history(user_id, 30)
    
    print(f"\n--- Average Daily Calories for User {user_id} ---")
    get_average_daily_calories(user_id, 7)
    
    print(f"\n--- Sleep Quality Analysis for User {user_id} ---")
    analyze_sleep_quality(user_id, 30)

    print(f"\n--- Correlation between Nutrition and Workout for User {user_id} ---")
    correlate_nutrition_and_workout(user_id)

    print(f"\n--- Trend Analysis for Health Metrics (Weight) for User {user_id} ---")
    analyze_health_metric_trends(user_id, 'weight')

    # Integrate recommendations into the data querying process.
    print(f"\n--- Fitness Recommendation for User {user_id} ---")
    fitness_recommendation = get_fitness_recommendations(user_id)
    print(fitness_recommendation)
    
    print(f"\n--- Nutrition Recommendation for User {user_id} ---")
    nutrition_recommendation = get_nutrition_recommendations(user_id)
    print(nutrition_recommendation)
```
## test_app.py
```
import unittest
from datetime import datetime, timedelta, date
from create import User, Workout, Nutrition, Sleep, HealthMetrics, engine
from query_data import (get_user_workout_history, get_average_daily_calories,
                        analyze_sleep_quality, correlate_nutrition_and_workout,
                        analyze_health_metric_trends)
from recommendations import get_fitness_recommendations, get_nutrition_recommendations
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class TestHealthFitnessApp(unittest.TestCase):

    def test_user_creation(self):
        """Test user creation and retrieval from the database."""
        new_user = User(name='John Doe', age=30, gender='Male', height=175, weight=80, goal='Muscle Gain')
        session.add(new_user)
        session.commit()
        user = session.query(User).filter_by(name='John Doe').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.age, 30)

    def test_workout_log(self):
        """Test workout logging and retrieval."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        new_workout = Workout(user_id=user_id, date=datetime.now(), type='Cardio', duration=60, intensity='High')
        session.add(new_workout)
        session.commit()
        workout_log = session.query(Workout).filter_by(user_id=user_id).first()
        self.assertIsNotNone(workout_log)
        self.assertEqual(workout_log.type, 'Cardio')
        self.assertEqual(workout_log.intensity, 'High')

    def test_nutrition_log(self):
        """Test nutrition logging and average calorie calculation."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        new_nutrition_log = Nutrition(user_id=user_id, date=datetime.now(), type='Lunch', calories=700, protein=30, carbs=100, fats=20)
        session.add(new_nutrition_log)
        session.commit()
        avg_calories = get_average_daily_calories(user_id, 1)
        self.assertGreaterEqual(avg_calories, 700)

    def test_sleep_quality_analysis(self):
        """Test sleep quality logging and analysis."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        new_sleep_log = Sleep(user_id=user_id, date=datetime.now(), duration=8, quality='Good')
        session.add(new_sleep_log)
        session.commit()
        sleep_quality_summary = analyze_sleep_quality(user_id, 1)
        self.assertIn('Good', sleep_quality_summary.keys())
        self.assertGreaterEqual(sleep_quality_summary.get('Good', 0), 1)

    def test_fitness_recommendations(self):
        """Test generation of fitness recommendations based on user workout history."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        fitness_advice = get_fitness_recommendations(user_id)
        self.assertIsInstance(fitness_advice, str)
        self.assertNotEqual(fitness_advice, "")

    def test_nutrition_recommendations(self):
        """Test generation of nutrition recommendations based on user calorie intake."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        nutrition_advice = get_nutrition_recommendations(user_id)
        self.assertIsInstance(nutrition_advice, str)
        self.assertNotEqual(nutrition_advice, "")

    def test_correlate_nutrition_and_workout(self):
        """Test the correlation between nutrition and workout."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        correlations = correlate_nutrition_and_workout(user_id)
        self.assertTrue(len(correlations) > 0)  # Ensure the list is not empty
        for date_item, avg_protein, avg_duration in correlations:
            self.assertIsInstance(date_item, date)  # Check the first item is a date
            self.assertIsInstance(avg_protein, float)  # Check the second item is a float (avg protein intake)
            self.assertIsInstance(avg_duration, float)  # Check the third item is a float (avg workout duration)

    def test_health_metric_trends(self):
        """Test the analysis of health metric trends."""
        user_id = session.query(User).filter_by(name='John Doe').first().user_id
        trends = analyze_health_metric_trends(user_id, 'weight')
        self.assertTrue(len(trends) > 0)  # Ensure the list is not empty
        for date_item, weight in trends:
            self.assertIsInstance(date_item, date)  # Check the first item is a date
            self.assertIsInstance(weight, float)  # Check the second item is a float (weight)

if __name__ == '__main__':
    unittest.main()
```