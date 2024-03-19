from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Text, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Define your engine globally, so it's available for import
engine = create_engine('sqlite:///health_fitness_app.db', echo=False)

# Optionally define Session globally as well
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, CheckConstraint("gender IN ('Male', 'Female', 'Other')"), nullable=False)
    height = Column(Float, nullable=False)  # Stored in centimeters
    weight = Column(Float, nullable=False)  # Stored in kilograms
    goal = Column(Text, nullable=False)
    workouts = relationship("Workout", back_populates="user")
    nutrition_logs = relationship("Nutrition", back_populates="user")
    sleep_records = relationship("Sleep", back_populates="user")
    health_metrics = relationship("HealthMetrics", back_populates="user")

class Workout(Base):
    __tablename__ = 'Workouts'
    workout_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)  # Stored in minutes
    intensity = Column(String, CheckConstraint("intensity IN ('Low', 'Medium', 'High')"), nullable=False)
    user = relationship("User", back_populates="workouts")

class Nutrition(Base):
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
    __tablename__ = 'Sleep'
    sleep_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('Users.user_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    duration = Column(Float, nullable=False)  # Stored in hours
    quality = Column(String, CheckConstraint("quality IN ('Poor', 'Fair', 'Good', 'Excellent')"), nullable=False)
    user = relationship("User", back_populates="sleep_records")

class HealthMetrics(Base):
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
    Base.metadata.create_all(engine)
