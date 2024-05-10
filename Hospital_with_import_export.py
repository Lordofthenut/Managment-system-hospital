
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass

    def __str__(self):
        return self.display_info()

class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Specialization: {self.specialization}"

class Nurse(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Department: {self.department}"

class Patient(Person):
    def __init__(self, name, age, problem, assigned_doctor, assigned_nurse):
        super().__init__(name, age)
        self.problem = problem
        self.assigned_doctor = assigned_doctor
        self.assigned_nurse = assigned_nurse

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Problem: {self.problem}, Assigned Doctor: {self.assigned_doctor.name}, Assigned Nurse: {self.assigned_nurse.name}"

class Hospital:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.doctors = []
            cls._instance.nurses = []
            cls._instance.patients = []
        return cls._instance

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_nurse(self, nurse):
        self.nurses.append(nurse)

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_staff(self):
        staff_info = "Doctors: "
        for doctor in self.doctors:
            staff_info += doctor.display_info()
        staff_info += "Nurses: "
        for nurse in self.nurses:
            staff_info += nurse.display_info()
        return staff_info

    def display_patients(self):
        patients_info = "Patients: "
        for patient in self.patients:
            patients_info += patient.display_info()
        return patients_info

class StaffFactory(ABC):
    @abstractmethod
    def create_person(self, name, age):
        pass

class DoctorFactory(StaffFactory):
    def create_person(self, name, age, specialization):
        return Doctor(name, age, specialization)

class NurseFactory(StaffFactory):
    def create_person(self, name, age, department):
        return Nurse(name, age, department)

class PatientFactory(StaffFactory):
    def create_person(self, name, age, problem, assigned_doctor, assigned_nurse):
        return Patient(name, age, problem, assigned_doctor, assigned_nurse)

def import_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data


def export_data_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)


if __name__ == "__main__":
    imported_data = import_data_from_file("impfile.txt")
    print("Imported data:")
    print(imported_data)
    
    export_data_to_file(imported_data, "expfile.txt")
    print("Data exported to expfile.txt.")