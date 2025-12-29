"""
Register fonts
author: Cod3W1ld01@proton.me
"""
# pylint: disable=too-few-public-methods
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class RegisterFonts:
    """
    Register fonts
    """
    def __init__(self):
        """
        Constructor
        """
        fonts_dir = 'src/build_report/fonts/'
        self.fonts = os.listdir(fonts_dir)
        for font in self.fonts:
            font_path = os.path.join(fonts_dir, font)
            font_name = os.path.splitext(font)[0]
            pdfmetrics.registerFont(TTFont(font_name, font_path))
