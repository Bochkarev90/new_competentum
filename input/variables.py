platform = 'e'  # 'r' - Revel, 'e' - Etext
revel = 1 if platform == 'r' else 0


browser = 'f'  # 'c' - chrome, 'f' - firefox
path = 'C:/work/Manza.xlsx' if revel else 'C:/work/Price.xlsx'  # Путь до excel-файла
username = 'manza2.5e.cqa.student10@mailinator.com' if revel else 'e2review'
password = ''
book = 'Manza_031119_TSP' if revel else 'Globalization and Diversity: Geography of a Changing World, 6e'  # Название курса
chapter_number = 10  # Номер проверяемой главы
set_number = 1  # Номер сета
lo_pos = False
