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
