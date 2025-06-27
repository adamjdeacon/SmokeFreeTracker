type TrackerData = {
  days: number;
  money_saved: number;
  earned_badges: number[];
  upcoming_badges: number[];
  next_badge_target: number;
  progress_percent: number;
  quit_date: string;
};

async function loadTrackerData(): Promise<void> {
  try {
    const res = await fetch("http://localhost:8000/api/tracker/");
    const data: TrackerData = await res.json();

    const stats = document.getElementById("stats");
    const progressBar = document.getElementById("progressBar") as HTMLElement;
    const badges = document.getElementById("badges");

    if (!stats || !progressBar || !badges) {
      console.error("One or more target elements are missing.");
      return;
    }

    // 🎯 Stat Cards
    stats.innerHTML = `
      <div class="col-12 col-md-4">
        <div class="p-3 border rounded bg-white shadow-sm h-100">
          <div class="fs-1 text-success">📅</div>
          <div class="fs-2 fw-bold">${data.days}</div>
          <div class="text-muted">Days Smoke-Free</div>
        </div>
      </div>
      <div class="col-12 col-md-4">
        <div class="p-3 border rounded bg-white shadow-sm h-100">
          <div class="fs-1 text-success">💷</div>
          <div class="fs-2 fw-bold">£${data.money_saved.toFixed(2)}</div>
          <div class="text-muted">Money Saved</div>
        </div>
      </div>
      <div class="col-12 col-md-4">
        <div class="p-3 border rounded bg-white shadow-sm h-100">
          <div class="fs-1 text-success">🚭</div>
          <div class="fs-5 fw-bold">${data.quit_date}</div>
          <div class="text-muted">Quit Date</div>
        </div>
      </div>
    `;

    // 📊 Progress Bar
    progressBar.style.width = `${data.progress_percent}%`;
    progressBar.textContent = `£${data.money_saved.toFixed(0)} of £${data.next_badge_target} (${data.progress_percent}%)`;

    // 🏅 Badges
    const earnedHTML = data.earned_badges.map(badge =>
      `<div class="col-6 col-md-3">
        <div class="badge bg-success w-100 p-3 fs-6 shadow-sm text-center">£${badge} 🎉</div>
      </div>`
    );

    const upcomingHTML = data.upcoming_badges.map(badge =>
      `<div class="col-6 col-md-3">
        <div class="badge bg-secondary text-light w-100 p-3 fs-6 shadow-sm opacity-50 text-center">£${badge} 🔒</div>
      </div>`
    );

    badges.innerHTML = [...earnedHTML, ...upcomingHTML].join("");
  } catch (error) {
    console.error("Failed to load tracker data:", error);
  }
}

loadTrackerData();
