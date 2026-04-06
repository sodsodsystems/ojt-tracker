# OJT Hours Tracker

A lightweight, single-file web app for tracking your On-the-Job Training (OJT) hours toward the **480-hour requirement**. No installation, no server — just open the HTML file in a browser.

---

## Features

### Progress Dashboard
- Live progress bar tracking hours rendered vs. the 480-hour target
- At-a-glance stats: **Days Logged**, **Hours Remaining**, and **Average Hours/Day**
- Percentage completion badge that updates in real time

### Daily Entry Form
Log each OJT day with:
- **Date picker** — defaults to today
- **Attendance status** — Present, Half Day (AM), Half Day (PM), or Absent
- **Morning session** — Time In / Time Out (shown/hidden based on status)
- **Afternoon session** — Time In / Time Out (shown/hidden based on status)
- **Auto-computed total hours** — calculated live as you fill in the time fields
- Input validation with descriptive error toasts (e.g., missing In/Out pairs)

### Daily Log Table
- Sortable, scrollable table of all logged entries
- Displays date, status badge, morning/afternoon times, and total hours per day
- Delete any entry with a single click (Delete button)
- Entry count shown in the table header

### Export to Excel
Exports an `.xlsx` workbook with **two sheets**:

| Sheet | Contents |
|---|---|
| **DTR** | Civil Service–style Daily Time Record — 60-day grid with Morning/Afternoon In/Out columns, per-day totals, overall rendered hours, and completion percentage |
| **Attendance** | Flat log with date, status, all time fields, and a summary block (Total Rendered, Required, Remaining, Completion %) |

The file is saved as `OJT_DTR_<today's date>.xlsx`.

### UI & Visual Design
- **Dark theme** — GitHub-inspired dark color palette (`#0d1117` background)
- **Typography** — Sora (UI) + Space Mono (monospaced values)
- **Animated particle background** — canvas-based floating particles with subtle connecting lines
- **Mouse interaction** — particles react to your cursor (repulsion + parallax); toggle on/off via the **Interaction** chip in the top-right corner
- Responsive layout — adapts to tablet and mobile screen sizes

### Persistence
All entries are saved automatically to **`localStorage`**. Your data survives page refreshes and browser restarts — no account or backend required.

---

## Getting Started

1. **Download** `OJT-TRACKER.html`
2. **Open** it in any modern browser (Chrome, Edge, Firefox, Safari)
3. Start logging your OJT days!

> **No internet required after the first load** — fonts and the XLSX library are fetched from CDNs on first open, then cached by the browser.

---

## Usage Guide

### Logging a Day
1. Set the **Date** (defaults to today)
2. Choose your **Attendance Status**
   - *Present* → fill in both Morning and Afternoon times
   - *Half Day AM* → fill in Morning only
   - *Half Day PM* → fill in Afternoon only
   - *Absent* → no time fields needed; 0 hours counted
3. Enter **Time In** and **Time Out** for each active session
4. The **Total Hours** preview updates automatically
5. Click **Add Entry** — a success toast confirms the save

### Deleting an Entry
Click the **Delete** button on any row in the Daily Log table.

### Exporting
Click **Export to Excel** in the header. The `.xlsx` file downloads immediately.

---

## Configuration

The required hour target is set via a CSS variable at the top of the file and a matching JS constant:

```css
/* In <style> */
:root {
  --total: 480;
}
```

```js
// In <script>
const TOTAL_HOURS = 480;
```

Change both values to adjust the target (e.g., `240` for a shorter program).

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Vanilla HTML/CSS/JS | Core app — zero frameworks |
| [SheetJS (xlsx)](https://sheetjs.com/) `v0.18.5` | Excel export |
| [Sora + Space Mono](https://fonts.google.com/) | Typography (Google Fonts) |
| Canvas API | Animated particle background |
| localStorage | Client-side data persistence |

---

## File Structure

This is a **single-file application** — everything (HTML, CSS, JS) lives in `OJT-TRACKER.html`. No build step, no dependencies to install.

```
OJT-TRACKER.html   ← the entire app
```

---

## Notes & Limitations

- Data is stored in **localStorage** and is **browser-specific** — clearing browser data will erase entries. Export to Excel regularly as a backup.
- The DTR sheet is formatted for a **60-day grid** (rows 1–60). Entries beyond Day 60 appear in the Attendance sheet but not in the DTR grid.
- Time validation assumes the **Out** time is always after the **In** time within the same session; overnight shifts are not supported.
- The app is intended for personal tracking — it does not submit data to any server.

---

*Built for OJT students tracking the 480-hour requirement under Philippine academic and government internship programs.*
