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
    else:
        total_calories = sum([cal.total_calories for cal in calories])
        average_calories = total_calories / len(calories)
        print(f"Average daily calories over the last {days} days: {average_calories}")

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

    # Output sleep quality analysis.
    if not sleep_quality:
        print(f"No sleep data found for user {user_id} in the last {days} days.")
    for quality in sleep_quality:
        print(f"Quality: {quality.quality}, Count: {quality.count}")

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
