#!/usr/bin/env python3
from pathlib import Path
import textwrap

INPUT = Path('reports/XA103_adaptive_cycle_engine_report.md')
OUTPUT = Path('reports/XA103_adaptive_cycle_engine_report.pdf')

PAGE_W = 595
PAGE_H = 842
MARGIN = 52
LINE_H = 14
BODY_FONT = 10
TITLE_FONT = 24
H1_FONT = 15
H2_FONT = 12


def esc(s: str) -> str:
    return s.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def wrap_text(text: str, width_chars: int):
    return textwrap.wrap(text, width=width_chars, break_long_words=False, break_on_hyphens=False) or ['']


def parse_lines(md: str):
    out = []
    for raw in md.splitlines():
        if raw.startswith('# '):
            out.append(('title', raw[2:].strip()))
        elif raw.startswith('## '):
            out.append(('h1', raw[3:].strip()))
        elif raw.startswith('### '):
            out.append(('h2', raw[4:].strip()))
        elif raw.startswith('- '):
            out.append(('bullet', raw[2:].strip()))
        elif raw.strip() == '---':
            out.append(('rule', ''))
        elif raw.strip() == '':
            out.append(('blank', ''))
        else:
            out.append(('p', raw.strip()))
    return out


def make_pages(elements):
    pages = []
    content = []
    y = PAGE_H - MARGIN

    def new_page():
        nonlocal content, y
        if content:
            pages.append('\n'.join(content))
        content = []
        y = PAGE_H - MARGIN
        # aero gradient-esque top band (stacked translucent bars approximation)
        content.append('q 0.08 0.16 0.28 rg 0 790 595 52 re f Q')
        content.append('q 0.12 0.28 0.45 rg 0 780 595 10 re f Q')
        content.append('q 0.75 0.82 0.9 RG 1.2 w 52 770 m 543 770 l S Q')

    def ensure(lines=1, h=LINE_H):
        nonlocal y
        if y - lines * h < MARGIN:
            new_page()

    new_page()

    for kind, text in elements:
        if kind == 'title':
            ensure(3, 28)
            content.append('BT /F2 %d Tf 1 1 1 rg %d %d Td (%s) Tj ET' % (TITLE_FONT, MARGIN, 802, esc(text)))
            y = 748
        elif kind == 'h1':
            ensure(2, 20)
            content.append('BT /F2 %d Tf 0.08 0.16 0.28 rg %d %d Td (%s) Tj ET' % (H1_FONT, MARGIN, int(y), esc(text)))
            y -= 22
        elif kind == 'h2':
            ensure(2, 18)
            content.append('BT /F2 %d Tf 0.1 0.24 0.38 rg %d %d Td (%s) Tj ET' % (H2_FONT, MARGIN, int(y), esc(text)))
            y -= 18
        elif kind == 'rule':
            ensure(1)
            content.append('q 0.7 0.78 0.88 RG 0.8 w %d %d m %d %d l S Q' % (MARGIN, int(y), PAGE_W - MARGIN, int(y)))
            y -= 12
        elif kind == 'blank':
            y -= 7
        elif kind == 'bullet':
            lines = wrap_text(text, 92)
            ensure(len(lines))
            content.append('BT /F1 %d Tf 0.12 0.12 0.12 rg %d %d Td (\342\200\242 %s) Tj ET' % (BODY_FONT, MARGIN, int(y), esc(lines[0])))
            y -= LINE_H
            for ln in lines[1:]:
                ensure(1)
                content.append('BT /F1 %d Tf 0.12 0.12 0.12 rg %d %d Td (  %s) Tj ET' % (BODY_FONT, MARGIN + 11, int(y), esc(ln)))
                y -= LINE_H
        else:
            lines = wrap_text(text, 100)
            ensure(len(lines))
            for ln in lines:
                content.append('BT /F1 %d Tf 0.12 0.12 0.12 rg %d %d Td (%s) Tj ET' % (BODY_FONT, MARGIN, int(y), esc(ln)))
                y -= LINE_H

    if content:
        pages.append('\n'.join(content))
    return pages


def build_pdf(page_streams):
    objs = []

    def add_obj(s):
        objs.append(s)
        return len(objs)

    font1 = add_obj('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    font2 = add_obj('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>')

    page_objs = []
    content_objs = []

    for stream in page_streams:
        data = stream.encode('latin-1', errors='replace')
        content_objs.append(add_obj(f'<< /Length {len(data)} >>\nstream\n{stream}\nendstream'))

    pages_placeholder = add_obj('')

    for cobj in content_objs:
        pobj = add_obj(
            f'<< /Type /Page /Parent {pages_placeholder} 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] '
            f'/Resources << /Font << /F1 {font1} 0 R /F2 {font2} 0 R >> >> /Contents {cobj} 0 R >>'
        )
        page_objs.append(pobj)

    kids = ' '.join(f'{p} 0 R' for p in page_objs)
    objs[pages_placeholder - 1] = f'<< /Type /Pages /Kids [{kids}] /Count {len(page_objs)} >>'

    catalog = add_obj(f'<< /Type /Catalog /Pages {pages_placeholder} 0 R >>')

    out = ['%PDF-1.4\n%\xe2\xe3\xcf\xd3\n']
    offsets = [0]
    for i, obj in enumerate(objs, start=1):
        offsets.append(sum(len(part.encode("latin-1", errors='replace')) for part in out))
        out.append(f'{i} 0 obj\n{obj}\nendobj\n')

    xref_offset = sum(len(part.encode("latin-1", errors='replace')) for part in out)
    out.append(f'xref\n0 {len(objs)+1}\n')
    out.append('0000000000 65535 f \n')
    for i in range(1, len(objs)+1):
        out.append(f'{offsets[i]:010d} 00000 n \n')
    out.append(f'trailer\n<< /Size {len(objs)+1} /Root {catalog} 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n')
    return ''.join(out).encode('latin-1', errors='replace')


def main():
    text = INPUT.read_text(encoding='utf-8')
    elements = parse_lines(text)
    pages = make_pages(elements)
    pdf = build_pdf(pages)
    OUTPUT.write_bytes(pdf)
    print(f'Wrote {OUTPUT} ({len(pdf)} bytes, {len(pages)} page(s))')


if __name__ == '__main__':
    main()
