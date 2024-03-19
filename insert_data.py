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
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

def generate_users(n=10):
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
    generate_users(10)  # Generate 10 sample users
    generate_workouts(50)  # Generate 50 workouts per user
    generate_nutrition_logs(150)  # Generate 150 nutrition logs per user
    generate_sleep_records(100)  # Generate 100 sleep records per user
    generate_health_metrics(50)  # Generate 50 health metrics records per user
