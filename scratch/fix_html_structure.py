import re
import os

file_path = r"c:\Users\admin\Documents\OJT\OJT PROJECTS\OJT-TRACKER\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Progress Section HTML
progress_fix = """<!-- PROGRESS -->
<div class="progress-section glass-card">
  <div class="progress-info">
    <div class="progress-label">Overall Progress</div>
    <div class="progress-nums">
      <span class="done" id="doneHours">0.00</span>
      <span class="total"> / 480 hrs</span>
    </div>
  </div>
  <div class="progress-bar-wrap">
    <div class="progress-bar-fill" id="progressBar" style="width:0%"></div>
  </div>
  <div id="pctBadge" class="progress-pct">0.00%</div>
  <div class="stats-compact">
    <div class="stat-item">
      <div class="stat-val val" id="statDays">0</div>
      <div class="stat-lbl lbl">Days Logged</div>
    </div>
    <div class="stat-item">
      <div class="stat-val val" id="statRemain">480.00</div>
      <div class="stat-lbl lbl">Hours Remaining</div>
    </div>
    <div class="stat-item">
      <div class="stat-val val" id="statAvg">—</div>
      <div class="stat-lbl lbl">Avg Hrs / Day</div>
    </div>
  </div>
</div>"""
content = re.sub(r'<!-- PROGRESS -->.*?<!-- ENTRY FORM -->', progress_fix + '\n\n<!-- ENTRY FORM -->', content, flags=re.DOTALL)

# 2. Fix Form Session Blocks (remove leftover inline styles)
content = content.replace('<div id="morBlock" style="background:var(--surface2); border:1px solid var(--border); border-radius:10px; padding:14px 16px;">',
                          '<div class="session-block" id="morBlock">')
content = content.replace('<span style="display:inline-flex; align-items:center; gap:8px;">',
                          '<span>')

# 3. Fix total row and computed hours
content = content.replace('<div style="display:flex; align-items:center; gap:10px; margin-bottom:14px;">', '<div class="total-row">')
content = content.replace('<div style="font-size:0.75rem; color:var(--muted); font-weight:600; text-transform:uppercase; letter-spacing:0.6px;">Total Hours:</div>', '<div class="total-label">Total Hours:</div>')

# 4. Ensure app-container is closed
# It should close after log-section
# Current state: many </div> at the end.
# Let's clean up the end of log-section.
content = re.sub(r'  </div>\n</div>\s*</div>\s*<div class="toast"', r'  </div>\n</div>\n</div>\n\n<div class="toast"', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final HTML structure fixed.")
