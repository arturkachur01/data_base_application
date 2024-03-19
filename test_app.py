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
