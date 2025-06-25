from django.shortcuts import render
from datetime import date
from math import floor

QUIT_DATE = date(2025, 5, 6)
COST_PER_DAY = 17.00
GOAL = 1000  # Optional, for progress bar
BADGE_INTERVAL = 150

def dashboard(request):
    today = date.today()
    days_since = (today - QUIT_DATE).days
    money_saved = days_since * COST_PER_DAY
    percent_of_goal = min(100, round((money_saved / GOAL) * 100)) if GOAL else 0

    # 🏅 Calculate badge milestones
    badges_earned = floor(money_saved / BADGE_INTERVAL)
    earned = [i * BADGE_INTERVAL for i in range(1, badges_earned + 1)]
    upcoming = [(badges_earned + i) * BADGE_INTERVAL for i in range(1, 4)]
    last_earned = earned[-1] if earned else None

    context = {
        'quit_date': QUIT_DATE,
        'days': days_since,
        'money': money_saved,
        'goal': GOAL,
        'percent': percent_of_goal,
        'earned_badges': earned,
        'upcoming_badges': upcoming,
        'last_earned': last_earned,
    }
    return render(request, 'tracker/dashboard.html', context)
