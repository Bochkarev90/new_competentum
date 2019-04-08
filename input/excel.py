import xlrd


class Excel(object):
    # Позиции в excel-файле (номер столбца)
    chapters_pos = 0
    modules_pos = 1
    breaks_pos = 2
    all_chapters = {
        1: {},
        2: {}
    }

    def __init__(self, path: str, chapter_index, set_number=1, lo_pos=3):
        self._chapter_info_excel = {
            'chapter_name': '',
            'modules_names': [],
            'breaks_names': [],
            'lo': []
        }
        self._chapter_index = chapter_index
        self._set_number = set_number
        self._path = path
        self._lo_pos = lo_pos

    def _parser(self):
        """
        Собирает данные, все строки, кроме первой, первые 5 столбцов.
        """
        sheet = xlrd.open_workbook(self._path).sheet_by_index(0)
        all_info = [sheet.row_values(rownum, 0, 5) for rownum in range(1, sheet.nrows)]

        # Убираем слово "chapter" из названия главы, если есть
        n = 0
        for i in all_info:
            if i[0]:
                first_word = i[0][:i[0].find(' ')]
                if first_word in ['chapter', 'Chapter']:
                    all_info[n][0] = i[0][i[0].find(' ')+1:]
                    all_info[n].append(first_word + ' ')
            n += 1

        return all_info

    def _break_add(self, all_info, set_number, chapter_index):
        """
        Добавляет название ScreenBreak-а в массив 'breaks' переданных главы и сета.
        """
        break_title = all_info[self.breaks_pos].strip()
        self.all_chapters[set_number][chapter_index]['breaks'].append(break_title)

    def _module_add(self, all_info, set_number, chapter_index):
        """
        Добавляет название модуля в массив 'modules' и 'breaks' переданных главы и сета.
        """
        module_title = all_info[self.modules_pos].strip()
        lo_title = all_info[self._lo_pos] if self._lo_pos else ""
        self.all_chapters[set_number][chapter_index]['modules'].append((module_title, lo_title))
        self.all_chapters[set_number][chapter_index]['breaks'].append(module_title)

    def _chapter_add(self, all_info, set_number):
        """
        Создает индекс главы из названия главы (первое слово или цифра).
        Индекс становится ключом в общем словаре, по которому можно получить всю информацию о главе.
        Добавляет название главы в созданный словарь.
        """
        title = all_info[self.chapters_pos].strip()
        chapter_index = title if title.find(' ') == -1 else title[:title.find(' ')]
        if chapter_index.find(':') != -1:
            chapter_index = int(chapter_index[:chapter_index.find(':')])
        prefix = all_info.pop()
        self.all_chapters[set_number][chapter_index] = {
            'name': all_info[self.chapters_pos],
            'modules': [],
            'breaks': [],
            'prefix': prefix
        }
        return chapter_index

    def _dictionary_create(self):
        """
        Создает большой словарь с информацией обо всех главах в книге, разбитый по сетам и индексам глав.
        """
        set_number = 1
        chapter_index = ''
        all_info = self._parser()
        count = 0
        for i in all_info:
            if i[self.chapters_pos]:
                if i[self.chapters_pos][:i[self.chapters_pos].find(' ')] in self.all_chapters[set_number]:
                    set_number = 2
                chapter_index = self._chapter_add(all_info[count], set_number)
            elif i[self.modules_pos]:
                self._module_add(all_info[count], set_number, chapter_index)
            elif i[self.breaks_pos]:
                self._break_add(all_info[count], set_number, chapter_index)
            count += 1

    def title(self):
        """
        Возвращает название главы
        """
        if not self.all_chapters[1]:
            self._dictionary_create()
        return (self.all_chapters[self._set_number][self._chapter_index]['prefix'] +
                self.all_chapters[self._set_number][self._chapter_index]['name'])

    def breaks(self):
        """
        Возвращает все breaks в главе
        """
        if not self.all_chapters[1]:
            self._dictionary_create()
        return self.all_chapters[self._set_number][self._chapter_index]['breaks']

    def modules(self):
        """
        Возвращает все модули в главе
        """
        if not self.all_chapters[1]:
            self._dictionary_create()
        return self.all_chapters[self._set_number][self._chapter_index]['modules']

    def info(self):
        """
        Возвращает информацию о переданной главе в переданном сете.
        """
        if not self.all_chapters[1]:
            self._dictionary_create()
        return self.all_chapters[self._set_number][self._chapter_index]


if __name__ == '__main__':
    """   ТЕСТ   """
    bauldoff_1 = Excel('C:/work/Bauldoff.xlsx', 46, 1, lo_pos=False)
    # print(bauldoff_1.breaks())
    assert bauldoff_1.breaks() == [
        'Introduction', '46.1 Eye Disorders', 'The Patient with Conjunctivitis', 'Nursing Care',
        'The Patient with a Corneal Disorder', 'Interprofessional Care', 'Nursing Care',
        'The Patient with a Disorder Affecting the Eyelids', 'The Patient with Eye Trauma', 'Nursing Care',
        'The Patient with Uveitis', 'The Patient with Cataracts', 'Interprofessional Care',
        'The Patient with Glaucoma', 'Interprofessional Care', 'Nursing Care', 'Case Study & Nursing Care Plan',
        'The Patient with Age-Related Macular Degeneration', 'The Patient with Diabetic Retinopathy',
        'The Patient with a Retinal Detachment', 'The Patient with Retinitis Pigmentosa', '46.2 Ear Disorders',
        'The Patient with Impacted Cerumen or a Foreign Body', 'The Patient with Otitis Media', 'Nursing Care',
        'The Patient with Acute Mastoiditis', 'The Patient with Chronic Otitis Media',
        'The Patient with an Inner Ear Disorder', 'Nursing Care', 'The Patient with a Vestibular Schwannoma',
        'The Patient with Hearing Loss', 'Interprofessional Care', 'Nursing Care', 'Chapter Highlights',
        'Test Yourself NCLEX-RN Review', 'References'
    ]

    Excel.all_chapters = {
        1: {},
        2: {}
    }
    bauldoff_2 = Excel('C:/work/Bauldoff.xlsx', 18, 1, lo_pos=False)
    # print(bauldoff_2.title())
    assert bauldoff_2.title() == 'Chapter 18: Assessing the Endocrine System'

    Excel.all_chapters = {
        1: {},
        2: {}
    }
    edwards_1 = Excel('C:/work/Edwards.xlsx', 9, 1, 4)
    # print(edwards_1.title())
    assert edwards_1.title() == '9: Campaigns and Voting Behavior'

    Excel.all_chapters = {
        1: {},
        2: {}
    }
    edwards_2 = Excel('C:/work/Edwards.xlsx', 12, set_number=2, lo_pos=4)
    # print(edwards_2.modules())
    assert edwards_2.modules() == [
        ('Introduction: Interest Groups', ''),
        ('12.1: Types of Groups', ''),
        ('12.2: Who Becomes a Lobbyist?', ''),
        ('12.3: The Impact of the Change in Party Control on Lobbying', ''),
        ('12.4: Ethics Reform', ''),
        ('Conclusion: Interest Groups', ''),
        ('Chapter 12 Quiz: Interest Groups', '')
    ]
