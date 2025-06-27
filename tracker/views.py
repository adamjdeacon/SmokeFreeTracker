import logging
logger = logging.getLogger(__name__)

import humanize
from django.shortcuts import render
from datetime import date
from dateutil.relativedelta import relativedelta
from math import floor

QUIT_DATE = date(2025, 5, 6) # 2025-05-06
COST_PER_DAY = 17.00
BADGE_INTERVAL = 150

def dashboard(request):
    today = date.today()
    days_since = (today - QUIT_DATE).days
    money_saved = days_since * COST_PER_DAY

    # 🏅 Calculate badge milestones
    badges_earned = floor(money_saved / BADGE_INTERVAL)
    earned = [i * BADGE_INTERVAL for i in range(1, badges_earned + 1)]
    upcoming = [(badges_earned + i) * BADGE_INTERVAL for i in range(1, 4)]
    
    last_earned = earned[-1] if earned else None

    next_badge = (badges_earned +1) * BADGE_INTERVAL 

    last = last_earned or 0
    progress_percent = round(((money_saved - last) / BADGE_INTERVAL) * 100)
    
    context = {
        'quit_date': QUIT_DATE,
        'days': days_since,
        'money': money_saved,
        'progress_percent': progress_percent,
        'earned_badges': (list(reversed(earned))),
        'upcoming_badges': (list(reversed(upcoming))),
        'last_earned': last_earned,
        'next_badge_target': next_badge,
        'time_breakdown': humanize.precisedelta(today - QUIT_DATE,format=("%0.0f")),
    }
    return render(request, 'tracker/dashboard.html', context)
