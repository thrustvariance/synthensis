#!/usr/bin/env python3
from pathlib import Path
import html
import re

SRC = Path('reports/XA103_adaptive_cycle_engine_report.md')
OUT = Path('reports/XA103_adaptive_cycle_engine_report.html')
CSS = Path('reports/xa103_report.css')


def convert_markdown(md: str) -> str:
    lines = md.splitlines()
    out = []
    i = 0
    in_ul = False
    in_ol = False
    in_table = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append('</ul>')
            in_ul = False
        if in_ol:
            out.append('</ol>')
            in_ol = False

    def close_table():
        nonlocal in_table
        if in_table:
            out.append('</tbody></table></div>')
            in_table = False

    while i < len(lines):
        raw = lines[i]
        s = raw.rstrip('\n')
        st = s.strip()

        if not st:
            close_lists()
            close_table()
            i += 1
            continue

        if st == '---':
            close_lists(); close_table()
            out.append('<hr/>')
            i += 1
            continue

        if st.startswith('# '):
            close_lists(); close_table()
            out.append(f"<h1>{html.escape(st[2:])}</h1>")
            i += 1
            continue
        if st.startswith('## '):
            close_lists(); close_table()
            out.append(f"<h2>{html.escape(st[3:])}</h2>")
            i += 1
            continue
        if st.startswith('### '):
            close_lists(); close_table()
            out.append(f"<h3>{html.escape(st[4:])}</h3>")
            i += 1
            continue

        if st.startswith('|') and st.endswith('|'):
            close_lists()
            row = [c.strip() for c in st.strip('|').split('|')]
            # skip alignment line
            is_align = all(re.fullmatch(r':?-{3,}:?', c) for c in row)
            if is_align:
                i += 1
                continue
            if not in_table:
                out.append('<div class="table-wrap"><table><tbody>')
                in_table = True
            cells = ''.join(f'<td>{html.escape(c)}</td>' for c in row)
            out.append(f'<tr>{cells}</tr>')
            i += 1
            continue
        else:
            close_table()

        if st.startswith('- '):
            if not in_ul:
                close_lists()
                out.append('<ul>')
                in_ul = True
            content = st[2:]
            cls = ' class="eq"' if content.startswith('Equation:') else ''
            out.append(f'<li{cls}>{html.escape(content)}</li>')
            i += 1
            continue

        m = re.match(r'^(\d+)\.\s+(.*)$', st)
        if m:
            if not in_ol:
                close_lists()
                out.append('<ol>')
                in_ol = True
            out.append(f'<li>{html.escape(m.group(2))}</li>')
            i += 1
            continue

        close_lists()
        cls = ' class="eq"' if st.startswith('Equation:') else ''
        out.append(f'<p{cls}>{html.escape(st)}</p>')
        i += 1

    close_lists(); close_table()
    return '\n'.join(out)


def main():
    md = SRC.read_text(encoding='utf-8')
    body = convert_markdown(md)
    html_doc = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>XA103 Adaptive-Cycle Engine Report</title>
  <link rel="stylesheet" href="xa103_report.css" />
</head>
<body>
  <header class="hero">
    <div class="hero-inner">
      <div class="kicker">Advanced Propulsion Engineering Brief</div>
      <h1>XA103 Adaptive-Cycle Engine Report</h1>
      <p>Technically dense assessment rendered for clean review and sharing.</p>
    </div>
  </header>
  <main class="report">{body}</main>
</body>
</html>
'''
    OUT.write_text(html_doc, encoding='utf-8')
    print(f'Wrote {OUT}')


if __name__ == '__main__':
    main()
