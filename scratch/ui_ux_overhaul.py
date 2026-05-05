import re
import os

file_path = r"c:\Users\admin\Documents\OJT\OJT PROJECTS\OJT-TRACKER\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Total Style Overhaul (Industry Standard Dashboard)
new_style = """<style>
  :root {
    --bg: #050508;
    --card: rgba(255, 255, 255, 0.03);
    --border: rgba(255, 255, 255, 0.08);
    --text: #f5f5f7;
    --muted: #86868b;
    --accent: #0071e3;
    --accent-glow: rgba(0, 113, 227, 0.25);
    --success: #30d158;
    --radius: 16px;
    --radius-sm: 8px;
    --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Helvetica Neue", Arial, sans-serif;
    --font-mono: ui-monospace, SFMono-Regular, SF Mono, Menlo, monospace;
  }

  @media (prefers-color-scheme: light) {
    :root {
      --bg: #f5f5f7;
      --card: #ffffff;
      --border: rgba(0, 0, 0, 0.08);
      --text: #1d1d1f;
      --muted: #86868b;
    }
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: var(--font-sans);
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden; /* Main body shouldn't scroll, inner areas will */
  }

  /* BLOB BACKGROUND */
  .blob-bg { position: fixed; inset: 0; z-index: -1; pointer-events: none; }
  .blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.15; animation: move 30s infinite alternate ease-in-out; }
  .blob-1 { width: 600px; height: 600px; background: #5e17eb; top: -100px; left: -100px; }
  .blob-2 { width: 500px; height: 500px; background: #0071e3; bottom: -100px; right: -100px; }
  @keyframes move {
    0% { transform: translate(0,0) rotate(0deg); }
    100% { transform: translate(100px, 50px) rotate(90deg); }
  }

  /* DASHBOARD LAYOUT */
  .app-layout {
    display: grid;
    grid-template-columns: 1fr 360px;
    grid-template-rows: auto 1fr;
    height: 100vh;
    max-width: 1600px;
    margin: 0 auto;
    padding: 20px;
    gap: 20px;
  }

  /* HEADER (TOP BAR) */
  header {
    grid-column: 1 / -1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
  }
  .brand { display: flex; align-items: center; gap: 12px; }
  .brand-icon { width: 32px; height: 32px; background: var(--accent); border-radius: 8px; display: grid; place-items: center; color: #fff; font-size: 18px; }
  .brand-text h1 { font-size: 1.1rem; font-weight: 600; }
  .brand-text p { font-size: 0.7rem; color: var(--muted); }
  
  .header-actions { display: flex; gap: 8px; }
  .btn {
    padding: 8px 16px; border-radius: 8px; border: 1px solid var(--border);
    background: var(--card); color: var(--text); font-size: 0.8rem; font-weight: 500;
    cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 8px;
    backdrop-filter: blur(10px);
  }
  .btn:hover { background: var(--border); }
  .btn-primary { background: var(--accent); color: #fff; border: none; }
  .btn-primary:hover { opacity: 0.9; }

  /* MAIN CONTENT (LEFT) */
  .main-content {
    grid-column: 1;
    display: flex;
    flex-direction: column;
    gap: 20px;
    overflow: hidden;
  }

  /* PROGRESS STRIP */
  .progress-card {
    background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
    padding: 20px 24px; display: flex; align-items: center; gap: 24px;
    backdrop-filter: blur(20px);
  }
  .progress-stat { display: flex; flex-direction: column; }
  .stat-label { font-size: 0.65rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.05em; font-weight: 600; }
  .stat-value { font-family: var(--font-mono); font-size: 1.4rem; font-weight: 700; }
  .stat-value span { font-size: 0.9rem; color: var(--muted); }
  
  .progress-bar-container { flex: 1; position: relative; }
  .progress-bar-bg { height: 8px; background: rgba(255,255,255,0.05); border-radius: 4px; overflow: hidden; }
  .progress-bar-fill { height: 100%; background: var(--accent); width: 0%; transition: width 0.4s ease; box-shadow: 0 0 10px var(--accent-glow); }
  .progress-percentage { position: absolute; right: 0; top: -18px; font-size: 0.75rem; font-weight: 700; color: var(--accent); }

  /* TABLE SECTION */
  .table-card {
    flex: 1; background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
    display: flex; flex-direction: column; overflow: hidden;
    backdrop-filter: blur(20px);
  }
  .table-header { padding: 16px 20px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
  .table-header h2 { font-size: 0.9rem; font-weight: 600; }
  
  .table-scroll { flex: 1; overflow-y: auto; }
  table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  th { position: sticky; top: 0; background: var(--bg); padding: 12px 20px; text-align: left; font-size: 0.7rem; color: var(--muted); text-transform: uppercase; font-weight: 600; z-index: 1; border-bottom: 1px solid var(--border); }
  td { padding: 12px 20px; border-bottom: 1px solid var(--border); }
  tr:hover { background: rgba(255,255,255,0.02); }

  /* SIDEBAR (RIGHT) */
  .sidebar {
    grid-column: 2; display: flex; flex-direction: column; gap: 20px;
    overflow-y: auto; padding-right: 4px;
  }
  .form-card {
    background: var(--card); border: 1px solid var(--border); border-radius: var(--radius);
    padding: 24px; backdrop-filter: blur(20px);
  }
  .form-card h2 { font-size: 1rem; font-weight: 600; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
  
  .field-group { margin-bottom: 16px; }
  .field-label { display: block; font-size: 0.65rem; color: var(--muted); text-transform: uppercase; font-weight: 600; margin-bottom: 6px; }
  input, select, textarea {
    width: 100%; background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 8px;
    padding: 10px 14px; color: var(--text); font-family: inherit; font-size: 0.9rem; outline: none; transition: border-color 0.2s;
  }
  input:focus, select:focus { border-color: var(--accent); }

  .session-box { background: rgba(255,255,255,0.02); border: 1px solid var(--border); border-radius: 12px; padding: 16px; margin-bottom: 16px; }
  .session-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
  .session-title { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; }
  .time-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }

  .total-display { display: flex; justify-content: space-between; align-items: center; padding: 12px 0; border-top: 1px solid var(--border); margin-top: 12px; }
  .total-val { font-family: var(--font-mono); font-weight: 700; color: var(--success); font-size: 1.1rem; }

  /* ICONS */
  .icon { width: 1.1em; height: 1.1em; stroke: currentColor; fill: none; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .icon-lg { width: 1.4em; height: 1.4em; }
  .icon-sm { width: 0.9em; height: 0.9em; }

  /* UTILS */
  .chip { position: fixed; bottom: 20px; left: 20px; z-index: 100; font-size: 0.7rem; color: var(--muted); display: flex; align-items: center; gap: 6px; }
  .toast { position: fixed; top: 20px; left: 50%; transform: translateX(-50%) translateY(-100px); background: var(--success); color: #000; padding: 12px 24px; border-radius: 99px; font-weight: 700; font-size: 0.85rem; transition: transform 0.4s cubic-bezier(0.18, 0.89, 0.32, 1.28); z-index: 1000; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
  .toast.show { transform: translateX(-50%) translateY(0); }

  /* RESPONSIVE */
  @media (max-width: 1024px) {
    .app-layout { grid-template-columns: 1fr; overflow-y: auto; height: auto; }
    .sidebar { grid-column: 1; }
    .main-content { height: auto; }
    .table-card { min-height: 400px; }
  }
</style>"""

# 2. Total HTML Structure Overhaul (Clean & Industry Standard)
new_body = """<body>
<div class="blob-bg">
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>
</div>

<div class="app-layout">
  <!-- HEADER -->
  <header>
    <div class="brand">
      <div class="brand-icon"><svg class="icon"><use href="#i-clipboard"></use></svg></div>
      <div class="brand-text">
        <h1>OJT Tracker</h1>
        <p>480-Hour Requirement</p>
      </div>
    </div>
    <div class="header-actions">
      <button class="btn" onclick="exportToExcel()">Export Excel</button>
      <button class="btn" onclick="downloadBackup()">Backup</button>
      <button class="btn" onclick="triggerImport()">Restore</button>
      <input type="file" id="backupFile" accept="application/json" style="display:none" />
    </div>
  </header>

  <!-- MAIN CONTENT (LEFT) -->
  <div class="main-content">
    <!-- PROGRESS -->
    <div class="progress-card">
      <div class="progress-stat">
        <div class="stat-label">Total Hours</div>
        <div class="stat-value"><span id="doneHours">0.00</span> <span>/ 480</span></div>
      </div>
      <div class="progress-bar-container">
        <div class="progress-percentage" id="pctBadge">0.00%</div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBar" style="width:0%"></div>
        </div>
      </div>
      <div class="progress-stat" style="text-align:right">
        <div class="stat-label">Remaining</div>
        <div class="stat-value" id="statRemain">480.00</div>
      </div>
    </div>

    <!-- TABLE -->
    <div class="table-card">
      <div class="table-header">
        <h2>Activity Log</h2>
        <span class="log-count" id="logCount" style="font-size:0.7rem; color:var(--muted)">0 entries</span>
      </div>
      <div class="table-scroll">
        <table>
          <thead>
            <tr>
              <th style="width:40px">#</th>
              <th>Date</th>
              <th>Status</th>
              <th>Morning</th>
              <th>Afternoon</th>
              <th>Total</th>
              <th style="width:80px">Action</th>
            </tr>
          </thead>
          <tbody id="logBody"></tbody>
        </table>
        <div class="empty-state" id="emptyState" style="text-align:center; padding:60px; color:var(--muted); font-size:0.9rem;">
          No entries found. Log your hours to get started.
        </div>
      </div>
    </div>
  </div>

  <!-- SIDEBAR (RIGHT) -->
  <aside class="sidebar">
    <div class="form-card">
      <h2><svg class="icon icon-lg"><use href="#i-pencil"></use></svg> New Entry</h2>
      
      <div class="field-group">
        <label class="field-label">Date</label>
        <input type="date" id="entryDate" />
      </div>
      
      <div class="field-group">
        <label class="field-label">Status</label>
        <select id="statusField" onchange="onStatusChange()">
          <option value="present">Present</option>
          <option value="halfday-am">Half Day (AM)</option>
          <option value="halfday-pm">Half Day (PM)</option>
          <option value="absent">Absent</option>
        </select>
      </div>

      <div id="timeFields">
        <div class="session-box" id="morBlock">
          <div class="session-head">
            <span class="session-title" style="color:var(--accent)">Morning Session</span>
            <button class="btn" style="padding:2px 8px; font-size:0.6rem" onclick="autofillMorning()">Autofill</button>
          </div>
          <div class="time-grid">
            <div class="field-group">
              <label class="field-label">In</label>
              <input type="time" id="morIn" oninput="onTimeInput(this.id)" />
            </div>
            <div class="field-group">
              <label class="field-label">Out</label>
              <input type="time" id="morOut" oninput="onTimeInput(this.id)" />
            </div>
          </div>
        </div>

        <div class="session-box" id="aftBlock">
          <div class="session-head">
            <span class="session-title" style="color:var(--warning)">Afternoon Session</span>
            <button class="btn" style="padding:2px 8px; font-size:0.6rem" onclick="autofillAfternoon()">Autofill</button>
          </div>
          <div class="time-grid">
            <div class="field-group">
              <label class="field-label">In</label>
              <input type="time" id="aftIn" oninput="onTimeInput(this.id)" />
            </div>
            <div class="field-group">
              <label class="field-label">Out</label>
              <input type="time" id="aftOut" oninput="onTimeInput(this.id)" />
            </div>
          </div>
        </div>
      </div>

      <div class="total-display">
        <span class="stat-label">Daily Total</span>
        <span class="total-val" id="computedHours">0.00 hrs</span>
      </div>

      <button class="btn btn-primary" id="submitBtn" onclick="submitEntry()" style="width:100%; margin-top:20px; padding:12px;">
        <span id="submitBtnText">Save Entry</span>
      </button>
      <button class="btn" id="cancelEditBtn" onclick="cancelEdit()" style="width:100%; margin-top:8px; display:none;">Cancel Edit</button>
    </div>

    <!-- MINI STATS -->
    <div class="form-card" style="padding:16px;">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
        <div>
          <div class="stat-label">Days Logged</div>
          <div class="stat-value" style="font-size:1.1rem" id="statDays">0</div>
        </div>
        <div>
          <div class="stat-label">Daily Avg</div>
          <div class="stat-value" style="font-size:1.1rem" id="statAvg">—</div>
        </div>
      </div>
    </div>
  </aside>
</div>

<div class="toast" id="toast">Entry Saved Successfully!</div>

<label class="chip">
  <input type="checkbox" id="interactionToggle" checked> Interaction
</label>

<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
  <symbol id="i-clipboard" viewBox="0 0 24 24"><path d="M9 2H15V6H9V2Z" fill="currentColor"/><path d="M19 5H17V7H7V5H5C3.89543 5 3 5.89543 3 7V19C3 20.1046 3.89543 21 5 21H19C20.1046 21 21 20.1046 21 19V7C21 5.89543 20.1046 5 19 5Z" stroke="currentColor" stroke-width="2"/></symbol>
  <symbol id="i-pencil" viewBox="0 0 24 24"><path d="M17 3L21 7L7 21H3V17L17 3Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>
  <symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2" stroke="currentColor" stroke-width="2"/><path d="M16 2V6M8 2V6M3 10H21" stroke="currentColor" stroke-width="2"/></symbol>
</svg>"""

# 3. Update JS references (Some IDs changed or structure changed)
# The `logBody` generation needs to match the new 7-column table.
# Original columns: #, Date, Status, Mor In, Mor Out, Aft In, Aft Out, Hours, Action (9 cols)
# New columns: #, Date, Status, Morning (In-Out), Afternoon (In-Out), Total, Action (7 cols)

# I need to modify the `renderEntries` function in the JS.
# First, let's replace the whole style and body.
content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
content = re.sub(r'<body>.*?<script>', new_body + '\n<script>', content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("UI/UX Overhaul complete. Proceeding to fix Javascript rendering...")
