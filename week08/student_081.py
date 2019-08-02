from collections import namedtuple

Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):
    ten_creds = ["CA116", "CA117", "MS121"]

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results = '\n'.join(
            [code + ' : ' + self.mods[code].title + ' : ' + str(
                self.marks[code]) for code in sorted(self.mods.keys())])

        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, module, mark):
        self.marks[module] = mark

    def precision_mark(self):
        total = 0
        for mod, mark in self.marks.items():
            if mod in Student.ten_creds:
                weight = 1 / 6
                grade = mark / 100
                weighted_mark = grade * weight
                total += weighted_mark
            else:
                weight = 1 / 12
                grade = mark / 100
                weighted_mark = grade * weight
                total += weighted_mark
        precision_mark = total * 100
        return precision_mark

    def passed(self):
        self.failed_mods = []
        self.failed_creds = 0
        for mod, mark in self.marks.items():
            if mark < 40:
                if mod in self.ten_creds:
                    self.failed_creds += 10
                else:
                    self.failed_creds += 5
                self.failed_mods.append(mod)
        if self.failed_creds != 0:
            return False
        return True

    def passed_by_compensation(self):
        for mod in self.failed_mods:
            if self.marks[mod] < 35:
                return False
        if self.precision_mark() >= 45 and self.failed_creds / 60 <= 1 / 6:
            return True
