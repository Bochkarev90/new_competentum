from subfunctions.sub import excel
# from input import variables as v
import time

""" Входные данные"""
revel = 0  # 1 если REVEL, 0 если ETEXT
browser = 'chrome'
path = 'C:/work/Bauldoff.xlsx'  # Путь до excel-файла
username = 'manza2.5e.cqa.student10@mailinator.com' if revel else 'e2review1'
password = 'Password1' if revel else 'Review1234'
course_name = 'Manza_031119_TSP' if revel else 'Medical-Surgical Nursing, Clinical Reasoning in'  # Название курса
chapter_number = 46  # Номер проверяемой главы
set_number = 1  # Номер сета
lo_pos = False  # False если в excel нет Learning Objective, если есть - номер столбца, начиная с нуля

chapter_info = excel(path, chapter_number, set_number, lo_pos)


# if v.browser == 'chrome':
#     browser.quit()
