class Ward():
    def __init__(self, name_ward, list_resident):
        self.__name_ward = name_ward
        self.__list_resident = list_resident

    def add_person(self, person):
        self.__list_resident.append(person)

    def describe_ward(self):
        print(f"Ward name: {
              self.__name_ward}, including people live in there:")
        for i in range(0, len(self.__list_resident), 1):
            self.__list_resident[i].describe()

    def count_doctor(self):
        count_doctor = 0
        for i in range(0, len(self.__list_resident), 1):
            if isinstance(self.__list_resident[i], Doctor):
                count_doctor += 1
        return f"The number of doctor in this district: {count_doctor}"

    def sort_age(self):
        sorted_list_resident = sorted(
            self.__list_resident, key=lambda x: x._year_of_birth)
        print("List people live in this district after sorting age")
        for i in range(0, len(sorted_list_resident), 1):
            sorted_list_resident[i].describe()

    def compute_average_teacher_age(self):
        sum_teacher_age = 0
        num_teacher = 0
        for i in range(0, len(self.__list_resident), 1):
            if isinstance(self.__list_resident[i], Teacher):
                sum_teacher_age += self.__list_resident[i]._year_of_birth
                num_teacher += 1
        average_teacher_age = sum_teacher_age / num_teacher
        return average_teacher_age


class Person():
    def __init__(self, name, year_of_birth):
        self._name = name
        self._year_of_birth = year_of_birth


class Student(Person):
    def __init__(self, name, year_of_birth, grade):
        super().__init__(name, year_of_birth)
        self.__grade = grade

    def describe(self):
        print(f"Student name: {self._name}, year of birth: {
              self._year_of_birth}, grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, year_of_birth, subject):
        super().__init__(name, year_of_birth)
        self.__subject = subject

    def describe(self):
        print(f"Teacher name: {self._name}, year of birth: {
              self._year_of_birth}, subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, year_of_birth, specialist):
        super().__init__(name, year_of_birth)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor name: {self._name}, year of birth: {
              self._year_of_birth}, specialist: {self.__specialist}")


student_1 = Student(name="Student A", year_of_birth=2010, grade="7")

teacher_1 = Teacher("Teacher A", 1969, "Math")

teacher_2 = Teacher("Teacher B", 1970, "Computer Science")

doctor_1 = Doctor("Doctor A", 1950, "Endocrinologist")

ward_1 = Ward(name_ward="district one", list_resident=[])
ward_1.add_person(student_1)
ward_1.add_person(teacher_1)
ward_1.add_person(teacher_2)
ward_1.add_person(doctor_1)
ward_1.describe_ward()
print(ward_1.count_doctor())

ward_1.sort_age()

print(f"Averge age of teacher in this district: {
      ward_1.compute_average_teacher_age()}")
