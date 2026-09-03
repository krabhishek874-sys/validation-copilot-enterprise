from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(path, summary):

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    content = [

        Paragraph(
            "Validation Executive Report",
            styles["Title"]
        ),

        Spacer(1, 20),

        Paragraph(
            summary,
            styles["BodyText"]
        )

    ]

    doc.build(content)
