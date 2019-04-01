browser = 'chrome'
platform = 'e'  # 'r' - Revel, 'e' - Etext
revel = 1 if platform == 'r' else 0
path = 'C:/work/Manza.xlsx' if revel else 'C:/work/Madura.xlsx'  # Путь до excel-файла
username = 'manza2.5e.cqa.student10@mailinator.com' if revel else'bpetextqaV3'
password = 'Password1' if revel else 'EtextQA3'
course_name = 'Manza_031119_TSP' if revel else 'Personal Finance, 7e for QA'  # Название курса
chapter_number = 8  # Номер проверяемой главы
set_number = 1  # Номер сета
