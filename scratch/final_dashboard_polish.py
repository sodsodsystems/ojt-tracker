import re
import os

file_path = r"c:\Users\admin\Documents\OJT\OJT PROJECTS\OJT-TRACKER\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up CSS block (remove extra braces and duplicate media queries)
# Let's just find the whole <style> block and replace it with a clean version.
# This is safer than many regexes.

style_start = content.find('<style>')
style_end = content.find('</style>')
if style_start != -1 and style_end != -1:
    clean_style = """<style>
  :root {
    --bg-color: #030014;
    --text-primary: #f5f5f7;
    --text-muted: #86868b;
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.1);
    --surface: rgba(255, 255, 255, 0.02);
    --surface-hover: rgba(255, 255, 255, 0.05);
    --accent: #0071e3;
    --accent-glow: rgba(0, 113, 227, 0.2);
    --success: #30d158;
    --error: #ff453a;
    --warning: #ffd60a;
    --radius: 24px;
    --radius-sm: 12px;
    --blur: 40px;
  }

  @media (prefers-color-scheme: light) {
    :root {
      --bg-color: #f5f5f7;
      --text-primary: #1d1d1f;
      --text-muted: #86868b;
      --glass-bg: rgba(255, 255, 255, 0.7);
      --glass-border: rgba(0, 0, 0, 0.05);
      --surface: rgba(0, 0, 0, 0.02);
      --surface-hover: rgba(0, 0, 0, 0.04);
      --accent-glow: rgba(0, 113, 227, 0.15);
    }
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { -webkit-text-size-adjust: 100%; scroll-behavior: smooth; }

  body {
    position: relative;
    font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'SF Pro Display', 'Helvetica Neue', Arial, sans-serif;
    background: var(--bg-color);
    color: var(--text-primary);
    min-height: 100vh;
    padding: 20px 0 40px;
    overflow-x: hidden;
    overflow-y: auto;
    -webkit-font-smoothing: antialiased;
  }

  .blob-bg { position: fixed; inset: 0; z-index: -1; overflow: hidden; background: var(--bg-color); }
  .blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.4; animation: move 25s infinite alternate ease-in-out; }
  @media (prefers-color-scheme: light) { .blob { opacity: 0.15; filter: blur(120px); } }
  .blob-1 { width: 600px; height: 600px; background: linear-gradient(135deg, #5e17eb, #0071e3); top: -10%; left: -10%; }
  .blob-2 { width: 700px; height: 700px; background: linear-gradient(135deg, #0071e3, #30d158); bottom: -15%; right: -10%; animation-duration: 30s; animation-delay: -5s; }
  .blob-3 { width: 500px; height: 500px; background: linear-gradient(135deg, #8e2de2, #ff453a); top: 30%; right: 5%; animation-duration: 20s; animation-delay: -2s; }

  @keyframes move {
    0% { transform: translate(0, 0) scale(1) rotate(0deg); }
    33% { transform: translate(100px, 50px) scale(1.1) rotate(120deg); }
    66% { transform: translate(-50px, 120px) scale(0.9) rotate(240deg); }
    100% { transform: translate(0, 0) scale(1) rotate(360deg); }
  }

  /* DASHBOARD LAYOUT */
  .app-container {
    max-width: 1440px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 1fr 380px;
    grid-template-rows: auto auto;
    gap: 16px;
    padding: 0 24px;
  }

  header { 
    grid-column: 1 / -1; 
    display: flex; align-items: center; justify-content: space-between; 
    padding: 12px 0;
  }
  .brand { display: flex; align-items: center; gap: 12px; }
  .brand-icon { width: 40px; height: 40px; background: linear-gradient(135deg, var(--accent), #1d6fbd); border-radius: 10px; display: grid; place-items: center; font-size: 20px; color: #fff; box-shadow: 0 4px 12px var(--accent-glow); }
  .brand-text h1 { font-size: 1.4rem; font-weight: 700; letter-spacing: -0.02em; }
  .brand-text p { font-size: 0.75rem; color: var(--text-muted); }

  .header-actions { display: flex; gap: 8px; }
  .export-btn { 
    display: flex; align-items: center; gap: 8px; padding: 8px 16px; 
    background: var(--glass-bg); border: 1px solid var(--glass-border); border-radius: 10px;
    color: var(--text-primary); font-size: 0.8rem; font-weight: 600; cursor: pointer;
    backdrop-filter: blur(var(--blur)); transition: all 0.2s;
  }
  .export-btn:hover { background: var(--surface-hover); transform: translateY(-1px); }
  .btn-secondary { background: var(--surface); }
  .btn-accent { background: rgba(142, 45, 226, 0.08); border-color: rgba(142, 45, 226, 0.2); color: #d8b4fe; }

  /* CARDS */
  .glass-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius);
    backdrop-filter: blur(var(--blur));
    -webkit-backdrop-filter: blur(var(--blur));
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
  }

  .progress-section { 
    grid-column: 1 / -1; padding: 20px 28px; 
    display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 32px;
  }
  .progress-info { display: flex; flex-direction: column; }
  .progress-label { font-size: 0.7rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; }
  .progress-nums { font-family: ui-monospace, monospace; margin-top: 2px; }
  .progress-nums .done { font-size: 1.8rem; font-weight: 700; }
  .progress-nums .total { font-size: 1rem; color: var(--text-muted); }
  
  .progress-bar-wrap { background: var(--surface); border-radius: 99px; height: 10px; overflow: hidden; padding: 2px; flex: 1; }
  .progress-bar-fill { height: 100%; border-radius: 99px; background: linear-gradient(90deg, var(--accent), #5e17eb); transition: width 0.4s cubic-bezier(.34,1.56,.64,1); box-shadow: 0 0 10px var(--accent-glow); }
  .progress-pct { font-family: ui-monospace, monospace; font-size: 1rem; color: var(--accent); font-weight: 700; width: 60px; text-align: right; }

  .stats-compact { display: flex; gap: 16px; margin-top: 0; }
  .stat-item { display: flex; align-items: center; gap: 8px; background: var(--surface); padding: 8px 16px; border-radius: 12px; border: 1px solid var(--glass-border); }
  .stat-item .val { font-family: ui-monospace, monospace; font-weight: 700; font-size: 1.1rem; }
  .stat-item .lbl { font-size: 0.65rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }

  /* MAIN CONTENT */
  .log-section { grid-column: 1; display: flex; flex-direction: column; overflow: hidden; height: calc(100vh - 200px); }
  .log-header { padding: 16px 24px; border-bottom: 1px solid var(--glass-border); display: flex; align-items: center; justify-content: space-between; }
  .log-header h2 { font-size: 1rem; font-weight: 600; display: flex; align-items: center; gap: 10px; }
  .log-count { background: var(--surface); padding: 4px 12px; border-radius: 99px; font-size: 0.7rem; color: var(--text-muted); font-family: ui-monospace, monospace; }

  .table-wrap { flex: 1; overflow-y: auto; padding: 0; }
  table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
  thead th { position: sticky; top: 0; background: var(--bg-color); z-index: 10; color: var(--text-muted); font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.1em; padding: 12px 20px; text-align: left; border-bottom: 1px solid var(--glass-border); }
  tbody tr { border-bottom: 1px solid var(--glass-border); transition: background 0.2s; }
  tbody tr:hover { background: var(--surface-hover); }
  tbody td { padding: 12px 20px; vertical-align: middle; }
  .td-hours { font-family: ui-monospace, monospace; font-weight: 700; color: var(--success); }

  /* FORM */
  .form-card { grid-column: 2; padding: 20px !important; }
  .form-card h2 { font-size: 1rem; margin-bottom: 16px; display: flex; align-items: center; gap: 10px; }
  
  .session-block { background: var(--surface); border: 1px solid var(--glass-border); border-radius: 12px; padding: 14px; margin-bottom: 12px; }
  .session-title { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 10px; display: flex; align-items: center; justify-content: space-between; }
  .session-title.morning { color: var(--accent); }
  .session-title.afternoon { color: var(--warning); }
  
  .field { display: flex; flex-direction: column; gap: 4px; margin-bottom: 10px; }
  .field:last-child { margin-bottom: 0; }
  .field label { font-size: 0.6rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; }
  .field input, .field select { background: var(--bg-color); border: 1px solid var(--glass-border); border-radius: 10px; color: var(--text-primary); padding: 8px 12px; font-size: 0.85rem; min-height: 40px; outline: none; transition: all 0.2s; }
  .field input:focus, .field select:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-glow); }
  
  select option { background: #1d1d1f; color: #f5f5f7; }
  @media (prefers-color-scheme: light) { select option { background: #ffffff; color: #1d1d1f; } }

  .add-btn { width: 100%; justify-content: center; background: var(--accent); color: #fff; border: none; border-radius: 12px; padding: 12px; font-weight: 600; font-size: 0.9rem; cursor: pointer; transition: all 0.2s; box-shadow: 0 4px 12px var(--accent-glow); display: flex; align-items: center; gap: 8px; }
  .add-btn:hover { transform: translateY(-1px); box-shadow: 0 6px 16px var(--accent-glow); opacity: 0.9; }

  .total-row { display: flex; align-items: center; justify-content: space-between; margin: 12px 0 16px; background: var(--surface); padding: 8px 12px; border-radius: 10px; }
  .total-label { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); }
  .computed-hours { font-family: ui-monospace, monospace; font-weight: 700; color: var(--success); font-size: 1rem; }

  .toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%) translateY(100px); background: var(--success); color: #000; border-radius: 12px; padding: 12px 24px; font-size: 0.85rem; font-weight: 700; opacity: 0; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); z-index: 1000; box-shadow: 0 8px 24px rgba(48, 209, 88, 0.3); }
  .toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }

  .mini-btn { background: var(--surface-hover); color: var(--text-primary); border: 1px solid var(--glass-border); border-radius: 6px; padding: 4px 8px; font-size: 0.6rem; font-weight: 700; cursor: pointer; }

  @media(max-width: 1150px) {
    .app-container { grid-template-columns: 1fr; }
    .log-section, .form-card { grid-column: 1; height: auto; }
    .form-card { order: -1; }
  }
</style>"""
    content = content[:style_start] + clean_style + content[style_end+len('</style>'):]

# 2. Update HTML to match new compact classes
content = content.replace('class="progress-section"', 'class="progress-section glass-card"')
content = content.replace('class="form-card"', 'class="form-card glass-card"')
content = content.replace('class="log-section"', 'class="log-section glass-card"')

# Add the progress wrapper for horizontal layout
content = content.replace('<div class="progress-top">', '<div class="progress-info">\n<div class="progress-label">Overall Progress</div>')
content = content.replace('<div>\n      <div class="progress-label">Overall Progress</div>\n      <div class="progress-nums">', '<div class="progress-nums">')
content = content.replace('<div id="pctBadge" class="progress-pct">0.00%</div>\n  </div>', '</div>\n</div>\n<div id="pctBadge" class="progress-pct">0.00%</div>')

# Refactor stats to stats-compact
content = content.replace('<div class="stats-row">', '<div class="stats-compact">')
content = content.replace('<div class="stat-box">', '<div class="stat-item">')
content = content.replace('<div class="stat-val"', '<div class="stat-val val"')
content = content.replace('<div class="stat-lbl"', '<div class="stat-lbl lbl"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Final compact dashboard layout complete.")
