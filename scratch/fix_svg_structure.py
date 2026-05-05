import re
import os

file_path = r"c:\Users\admin\Documents\OJT\OJT PROJECTS\OJT-TRACKER\index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix the incorrectly inserted SVG symbol
# It was inserted inside the <h2> tag
content = content.replace('<h2><svg class="icon icon-lg"><use href="#i-pencil"></use>  <symbol id="i-trash" viewBox="0 0 24 24"><path d="M3 6h18M19 6l-1 14H6L5 6M8 6V4h8v2" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>\n</svg>',
                          '<h2><svg class="icon icon-lg"><use href="#i-pencil"></use></svg>')

# 2. Add the trash symbol to the PROPER location (the hidden SVG at the bottom)
trash_symbol = '<symbol id="i-trash" viewBox="0 0 24 24"><path d="M3 6h18M19 6l-1 14H6L5 6M8 6V4h8v2" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>'
# Find the hidden svg
hidden_svg_end = content.rfind('</svg>')
if hidden_svg_end != -1:
    # Make sure we're not inside the h2 we just fixed
    content = content[:hidden_svg_end] + trash_symbol + content[hidden_svg_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SVG structure fixed.")
