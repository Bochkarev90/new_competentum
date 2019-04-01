import xlrd


class Excel(object):
    # Позиции в excel-файле (номер столбца)
    chapters_pos = 0
    modules_pos = 1
    breaks_pos = 2

    def __init__(self, path: str, chapter_index, set_number=1, lo_pos=3):
        self._chapter_info_excel = {
            'chapter_name': '',
            'modules_names': [],
            'breaks_names': [],
            'lo': []
        }
        self._all_chapters = {
            1: {},
            2: {}
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
            if i[0] and (i[0][:i[0].find(' ')] in ['chapter', 'Chapter']):
                all_info[n][0] = i[0][i[0].find(' ')+1:]
            n += 1

        return all_info

    def _break_add(self, all_info, set_number, chapter_index):
        """
        Добавляет название ScreenBreak-а в массив 'breaks' переданных главы и сета.
        """
        break_title = all_info[0][self.breaks_pos].strip()
        self._all_chapters[set_number][chapter_index]['breaks'].append(break_title)

    def _module_add(self, all_info, set_number, chapter_index):
        """
        Добавляет название модуля в массив 'modules' и 'breaks' переданных главы и сета.
        """
        module_title = all_info[0][self.modules_pos].strip()
        lo_title = all_info[0][self._lo_pos] if self._lo_pos else ""
        self._all_chapters[set_number][chapter_index]['modules'].append((module_title, lo_title))
        self._all_chapters[set_number][chapter_index]['breaks'].append(module_title)

    def _chapter_add(self, all_info, set_number):
        """
        Создает индекс главы из названия главы (первое слово или цифра).
        Индекс становится ключом в общем словаре, по которому можно получить всю информацию о главе.
        Добавляет название главы в созданный словарь.
        """
        title = all_info[0][self.chapters_pos].strip()
        chapter_index = title if title.find(' ') == -1 else title[:title.find(' ')]
        if chapter_index.find(':') != -1:
            chapter_index = int(chapter_index[:chapter_index.find(':')])
        self._all_chapters[set_number][chapter_index] = {
            'name': all_info[0][self.chapters_pos],
            'modules': [],
            'breaks': []
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
                if i[self.chapters_pos][:i[self.chapters_pos].find(' ')] in self._all_chapters[set_number]:
                    set_number = 2
                chapter_index = self._chapter_add(all_info[count:], set_number)
            elif i[self.modules_pos]:
                self._module_add(all_info[count:], set_number, chapter_index)
            elif i[self.breaks_pos]:
                self._break_add(all_info[count:], set_number, chapter_index)
            count += 1

    def name(self):
        """
        Возвращает название главы
        """
        if not self._all_chapters[1]:
            self._dictionary_create()
        return self._all_chapters[self._set_number][self._chapter_index]['name']

    def breaks(self):
        """
        Возвращает все breaks в главе
        """
        if not self._all_chapters[1]:
            self._dictionary_create()
        return self._all_chapters[self._set_number][self._chapter_index]['breaks']

    def modules(self):
        """
        Возвращает все модули в главе
        """
        if not self._all_chapters[1]:
            self._dictionary_create()
        return self._all_chapters[self._set_number][self._chapter_index]['modules']

    def chapter_info(self):
        """
        Возвращает информацию о переданной главе в переданном сете.
        """
        if not self._all_chapters[1]:
            self._dictionary_create()
        return self._all_chapters[self._set_number][self._chapter_index]


if __name__ == '__main__':
    bauldoff = Excel('C:/work/Bauldoff.xlsx', 46, lo_pos=False)
    assert bauldoff.breaks() == [
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

    edwards_1 = Excel('C:/work/Edwards.xlsx', 9)
    assert edwards_1.name() == '9: Campaigns and Voting Behavior'

    edwards_2 = Excel('C:/work/Edwards.xlsx', 9, set_number=2, lo_pos=4)
    assert edwards_2.modules() == [
        ('Introduction: Voting Rights in Georgia', ''),
        ('9.1: Georgia and Discriminatory Voting Practices', ''),
        ('9.2: Georgia and the Voting Rights Act', ''),
        ('9.3: African American Office Holding in Georgia', ''),
        ('9.4: Georgia Voter Photo ID', ''),
        ('Conclusion: Voting Rights in Georgia', ''),
        ('Chapter 9 Quiz: Voting Rights in Georgia', '')]
