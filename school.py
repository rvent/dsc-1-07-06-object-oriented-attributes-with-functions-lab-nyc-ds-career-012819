class School():
    
    _students = {}
    
    def __init__(self, school_name=None):
        pass
    
    def add_student(self, name, grade):
        if grade not in self._students:
            self._students[grade] = [name]
        else:
             self._students[grade].append(name)
        
    def roster(self):
        return self._students
    
    def grade(self, mark):
        return self._students[mark]
    
    def sort_roster(self):
        for student_list in self._students.values():
            student_list.sort()
        return self._students