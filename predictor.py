from datetime import datetime, date, timedelta

def predict_consistency(created_at_str, completions):
    """
    Predicts future consistency based on past data.
    created_at_str: date string 'YYYY-MM-DD'
    completions: list of date strings 'YYYY-MM-DD'
    """
    if not completions:
        return "No data to predict. Start building your habit!"

    created_at = datetime.strptime(created_at_str, "%Y-%m-%d").date()
    today = date.today()
    total_days = (today - created_at).days + 1
    
    if total_days <= 0:
        total_days = 1
        
    completion_set = set(completions)
    
    # Calculate overall consistency
    overall_rate = len(completion_set) / total_days
    
    # Recency bias (last 7 days)
    last_7_days = [today - timedelta(days=i) for i in range(7)]
    recent_completions = sum(1 for d in last_7_days if d.isoformat() in completion_set)
    recent_rate = recent_completions / 7
    
    # Weighted average. Recent rate has more weight
    predicted_rate = (overall_rate * 0.4) + (recent_rate * 0.6)
    
    # Generate prediction string
    if predicted_rate >= 0.8:
        prediction_text = "Excellent! You have a high probability of maintaining this habit."
    elif predicted_rate >= 0.5:
        prediction_text = "Good. You are fairly consistent, but try to build a stronger streak!"
    elif predicted_rate > 0.0:
        prediction_text = "Needs Improvement. Your consistency is low. Try focusing on small steps."
    else:
        prediction_text = "At risk. You haven't been consistent recently. Time for a fresh start!"
        
    # Find current streak
    streak = 0
    current_date = today
    while current_date.isoformat() in completion_set:
        streak += 1
        current_date -= timedelta(days=1)
        
    return {
        "overall_rate": round(overall_rate * 100, 2),
        "recent_rate": round(recent_rate * 100, 2),
        "predicted_rate": round(predicted_rate * 100, 2),
        "current_streak": streak,
        "prediction_text": prediction_text
    }
