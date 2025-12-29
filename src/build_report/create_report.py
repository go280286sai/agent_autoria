"""
Create report .pdf
author: Cod3W1ld01@proton.me
"""
from datetime import date
import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Table,
                                TableStyle, Paragraph, PageBreak, Image)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from src.build_report.register_fonts import RegisterFonts


class Report(RegisterFonts):
    """
    Create report pdf
    """

    def __init__(self, name: str):
        super().__init__()
        self.style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # фон заголовка
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "RobotoMono-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "RobotoMono-Regular"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),  # сетка
        ])

        self.doc = SimpleDocTemplate(f"data/out/{name}.pdf", pagesize=A4)
        self.elements = []

        # Заголовок
        styles = getSampleStyleSheet()
        data_report = date.today()
        title = Paragraph(
            f"<font name='RobotoMono-Bold' size=18>Звіт про "
            f"продаж авто на Авторіа від {data_report}</font>",
            styles["Title"])
        self.elements.append(title)

    def create_pages(self,
                     title: str,
                     groups: pd.DataFrame = None,
                     image: str = None,
                     message: str = None
                     ) -> None:
        """
        Create report pages
        :param title:
        :param groups:
        :param image:
        :param message:
        :return:
        """
        styles = getSampleStyleSheet()
        subtitle = Paragraph(
            f"<font name='RobotoMono-Bold' "
            f"size=14 color='blue'>{title}</font>", styles["Heading2"])
        self.elements.append(subtitle)
        if groups is None:
            self.elements.append(Paragraph(""))
        else:
            data = [list(groups.columns)] + groups.values.tolist()
            table = Table(data)
            table.setStyle(self.style)
            self.elements.append(table)
        if image is not None:
            self.elements.append(
                Image(
                    filename=f"data/img/{image}",
                    width=600,
                    height=600
                )
            )
        if message is not None:
            custom_style = ParagraphStyle('CustomMessage',
                                          parent=styles["Heading5"],
                                          leading=16,
                                          spaceBefore=10)
            self.elements.append(
                Paragraph(
                    f"<font name='RobotoMono-Regular' "
                    f"size=12 color='black'>{message}</font>",
                    custom_style))
        self.elements.append(
            PageBreak()
        )

    def build_report(self):
        """
        Create report pages
        :return:
        """
        self.doc.build(self.elements)
