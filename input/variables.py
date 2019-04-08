platform = 'e'  # 'r' - Revel, 'e' - Etext
revel = 1 if platform == 'r' else 0


browser = 'chrome'
path = 'C:/work/Manza.xlsx' if revel else 'C:/work/Bauldoff.xlsx'  # Путь до excel-файла
username = 'manza2.5e.cqa.student10@mailinator.com' if revel else 'e2review1'
password = 'Password1' if revel else 'Review1234'
book = 'Manza_031119_TSP' if revel else 'Medical-Surgical Nursing, Clinical Reasoning in'  # Название курса
chapter_number = 46  # Номер проверяемой главы
set_number = 1  # Номер сета
lo_pos = False
