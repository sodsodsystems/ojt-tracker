import re
import os

file_path = r"c:\Users\admin\Documents\OJT\OJT PROJECTS\OJT-TRACKER\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update renderEntries to match 7-column layout
new_render_entries = """  entries.forEach((e, i) => {
    const monday = getMondayObj(e.date);
    if (monday !== null && monday !== currentMonday) {
      weekCounter++;
      currentMonday = monday;
      html += `<tr><td colspan="7" style="background:rgba(255,255,255,0.02); color:var(--muted); font-weight:700; text-transform:uppercase; letter-spacing:1px; font-size:0.65rem; padding:8px 20px; text-align:left; border-bottom:1px solid var(--border);">Week ${weekCounter}</td></tr>`;
    }
    
    const morRange = (e.status === 'absent' || e.status === 'halfday-pm') ? '—' : `${fmt12(e.morIn)} – ${fmt12(e.morOut)}`;
    const aftRange = (e.status === 'absent' || e.status === 'halfday-am') ? '—' : `${fmt12(e.aftIn)} – ${fmt12(e.aftOut)}`;
    
    html += `
    <tr>
      <td>${i+1}</td>
      <td style="font-weight:500;">${fmtDate(e.date)}</td>
      <td><span style="font-size:0.75rem; color:var(--muted)">${statusLabel[e.status || 'present']}</span></td>
      <td style="font-family:var(--font-mono); font-size:0.75rem;">${morRange}</td>
      <td style="font-family:var(--font-mono); font-size:0.75rem;">${aftRange}</td>
      <td style="font-family:var(--font-mono); font-weight:700; color:var(--success);">${(+e.hours).toFixed(2)}</td>
      <td>
        <div style="display:flex; gap:8px;">
          <button class="btn" style="padding:4px; min-width:32px;" onclick="startEdit(${e.id})" title="Edit">${iconHtml('pencil','icon-sm')}</button>
          <button class="btn" style="padding:4px; min-width:32px; color:var(--error); border-color:rgba(255,69,58,0.2);" onclick="deleteEntry(${e.id})" title="Delete">${iconHtml('trash','icon-sm')}</button>
        </div>
      </td>
    </tr>
    `;
  });"""

content = re.sub(r'  entries\.forEach\(\(e, i\) => \{.*?  \}\);', new_render_entries, content, flags=re.DOTALL)

# 2. Fix showToast to use CSS class instead of inline styles for background
content = content.replace("t.style.background = type === 'error' ? '#b91c1c' : '#238636';",
                          "t.style.background = type === 'error' ? 'var(--error)' : 'var(--success)';")

# 3. Add 'trash' icon to SVG symbols (forgot in previous script)
trash_svg = """  <symbol id="i-trash" viewBox="0 0 24 24"><path d="M3 6h18M19 6l-1 14H6L5 6M8 6V4h8v2" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>"""
content = content.replace('</svg>', trash_svg + '\n</svg>')

# 4. Clean up the 'Interaction' chip positioning and styling
content = content.replace('<label class="chip">\n  <input type="checkbox" id="interactionToggle" checked> Interaction\n</label>',
                          '<div class="chip">\n  <input type="checkbox" id="interactionToggle" checked> <span>Interactive FX</span>\n</div>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Javascript and additional UI fixes complete.")
