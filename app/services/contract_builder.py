from jinja2 import Environment, BaseLoader
from docx import Document
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from typing import Dict
import textwrap

# Упрощённый шаблон: заголовок + lorem ipsum
DEFAULT_TEMPLATE = """
ДОГОВОР № {{ number }}

г. {{ city }} «{{ date }}»

Заказчик: {{ customer.name }} (ИНН {{ customer.inn }}{% if customer.kpp %} / КПП {{ customer.kpp }}{% endif %})
Исполнитель: {{ contractor.name }} (ИНН {{ contractor.inn }}{% if contractor.kpp %} / КПП {{ contractor.kpp }}{% endif %})

1. Lorem ipsum
1.1. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.

2. Aliquam
2.1. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat.

3. Donec
3.1. Donec sit amet eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris fermentum dictum magna. Sed laoreet aliquam leo.

4. Fusce
4.1. Fusce convallis, mauris imperdiet gravida bibendum, nisl lorem iaculis sapien, a placerat ante felis a odio. Nullam varius, turpis et commodo pharetra, est eros bibendum elit, nec luctus magna felis sollicitudin mauris.

5. Vivamus
5.1. Vivamus fermentum semper porta. Nunc diam velit, adipiscing ut tristique vitae, sagittis vel odio. Maecenas convallis ullamcorper ultricies.

6. Реквизиты и подписи (заглушка)
Заказчик: {{ customer.name }}
Исполнитель: {{ contractor.name }}

(Отметка: статус верификации — {{ verification_status }})
"""


def render_text(context: Dict) -> str:
    """Рендерит текст договора из DEFAULT_TEMPLATE по Jinja2."""
    env = Environment(loader=BaseLoader(), autoescape=False, trim_blocks=True, lstrip_blocks=True)
    template = env.from_string(DEFAULT_TEMPLATE)
    return template.render(**context)


def text_to_docx(text: str, out_path: str) -> str:
    """Сохраняет текст в DOCX (простой построчный перенос)."""
    doc = Document()
    for para in text.split("\n\n"):
        p = doc.add_paragraph()
        for line in para.split("\n"):
            p.add_run(line)
            p.add_run("\n")
    doc.save(out_path)
    return out_path


def text_to_pdf(text: str, out_path: str) -> str:
    """Сохраняет текст в PDF (простая печать строк, перенос по ширине)."""
    c = canvas.Canvas(out_path, pagesize=A4)
    width, height = A4
    x = 40
    y = height - 40
    for paragraph in text.split("\n\n"):
        for line in paragraph.split("\n"):
            for wrapped in textwrap.wrap(line, width=95):
                c.drawString(x, y, wrapped)
                y -= 14
                if y < 40:
                    c.showPage()
                    y = height - 40
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40
    c.save()
    return out_path