import re
import shutil

# Make a backup first
shutil.copyfile('index.html', 'index.html.bak')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Head: Fonts and Typography
font_links = """  <!-- Google Fonts: Prompt & Plus Jakarta Sans for High-Legibility Thai & English -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Prompt:wght@300;400;500;600;700&display=swap" rel="stylesheet">
"""

if 'family=Prompt' not in content:
    content = content.replace('<!-- Tailwind CSS -->', font_links + '\n  <!-- Tailwind CSS -->')

# Update font family in style
font_style = """
    body {
      font-family: 'Prompt', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      letter-spacing: 0.01em;
    }
    .katex {
      font-size: 1.05em !important;
    }
    .katex-display {
      margin: 0.75em 0 !important;
      overflow-x: auto;
      overflow-y: hidden;
      padding: 0.25em 0;
    }
"""
content = content.replace('.flashcard { perspective: 1000px; }', font_style + '    .flashcard { perspective: 1000px; }')

# Split at script tag
script_idx = content.rfind('<script>')
html_part = content[:script_idx]
script_part = content[script_idx:]

# 2. Fix delimiters in script_part
katex_config_str = """delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "\\\\[", right: "\\\\]", display: true},
            {left: "\\\\(", right: "\\\\)", display: false}
          ],
          throwOnError: false"""

# Replace all occurrences of delimiters in script_part
script_part = re.sub(r'delimiters:\s*\[[\s\S]*?\](?:\s*,\s*throwOnError:\s*\w+)?', katex_config_str, script_part)

# Also ensure renderMathInElement calls have options
# Line with `if (window.renderMathInElement) window.renderMathInElement(content);`
script_part = script_part.replace(
    'if (window.renderMathInElement) window.renderMathInElement(content);',
    'if (window.renderMathInElement) window.renderMathInElement(content, { ' + katex_config_str + ' });'
)
script_part = script_part.replace(
    'if (window.renderMathInElement) window.renderMathInElement(alertEl);',
    'if (window.renderMathInElement) window.renderMathInElement(alertEl, { ' + katex_config_str + ' });'
)
script_part = script_part.replace(
    'if (window.renderMathInElement) window.renderMathInElement(regimeCard);',
    'if (window.renderMathInElement) window.renderMathInElement(regimeCard, { ' + katex_config_str + ' });'
)
script_part = script_part.replace(
    "window.renderMathInElement(document.getElementById('fcFrontText'));",
    "window.renderMathInElement(document.getElementById('fcFrontText'), { " + katex_config_str + " });"
)
script_part = script_part.replace(
    "window.renderMathInElement(document.getElementById('fcBackText'));",
    "window.renderMathInElement(document.getElementById('fcBackText'), { " + katex_config_str + " });"
)

# 3. Escape all LaTeX commands in script_part
latex_commands = [
    r'\(', r'\)', r'\[', r'\]',
    'text', 'frac', 'vec', 'omega', 'theta', 'times', 'cdot', 'lambda',
    'zeta', 'Delta', 'sin', 'rightleftharpoons', 'rightarrow', 'xrightarrow',
    'AA', 'mathbf', 'approx', 'mu', 'eta', 'varepsilon', 'sigma', 'pi',
    'implies', 'to', 'ge', 'le', 'nu', 'propto', 'quad', 'downarrow', 'uparrow',
    'circ', 'gamma'
]

for cmd in latex_commands:
    if cmd in [r'\(', r'\)', r'\[', r'\]']:
        char = cmd[1]
        pattern = r'(?<!\\)\\' + re.escape(char)
        script_part = re.sub(pattern, r'\\\\' + char, script_part)
    else:
        pattern = r'(?<!\\)\\' + re.escape(cmd) + r'(?![a-zA-Z])'
        script_part = re.sub(pattern, r'\\\\' + cmd, script_part)

# 4. Improve typography & spacing in subjective answers & cards
# In subjective modelAnswer:
script_part = script_part.replace(
    'text-xs md:text-sm leading-relaxed text-slate-800 dark:text-slate-200',
    'text-sm md:text-[15px] leading-relaxed md:leading-loose text-slate-800 dark:text-slate-200'
)
script_part = script_part.replace(
    '<ul class="list-disc ml-5 mt-1 space-y-1">',
    '<ul class="list-disc ml-5 mt-2 space-y-2.5">'
)

# Reassemble
new_content = html_part + script_part

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("index.html updated successfully!")
