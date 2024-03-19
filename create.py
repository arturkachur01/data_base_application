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