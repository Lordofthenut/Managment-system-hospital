import unittest

from Hospital import Doctor, Nurse, Patient, Hospital, DoctorFactory, NurseFactory, PatientFactory

class TestHospitalSystem(unittest.TestCase):
    def setUp(self):
        self.hospital = Hospital()

        self.doctor_factory = DoctorFactory()
        self.nurse_factory = NurseFactory()
        self.patient_factory = PatientFactory()

    def test_add_doctor(self):
        doctor = self.doctor_factory.create_person("Dr. Smith", 40, "Cardiology")
        self.hospital.add_doctor(doctor)
        self.assertIn(doctor, self.hospital.doctors)

    def test_add_nurse(self):
        nurse = self.nurse_factory.create_person("Nurse Johnson", 35, "Emergency")
        self.hospital.add_nurse(nurse)
        self.assertIn(nurse, self.hospital.nurses)

    def test_add_patient(self):
        doctor = self.doctor_factory.create_person("Dr. Smith", 40, "Cardiology")
        nurse = self.nurse_factory.create_person("Nurse Johnson", 35, "Emergency")
        patient = self.patient_factory.create_person("John Doe", 30, "Heart disease", doctor, nurse)
        self.hospital.add_patient(patient)
        self.assertIn(patient, self.hospital.patients)

    def test_display_staff(self):
        doctor = self.doctor_factory.create_person("Dr. Smith", 40, "Cardiology")
        nurse = self.nurse_factory.create_person("Nurse Johnson", 35, "Emergency")
        self.hospital.add_doctor(doctor)
        self.hospital.add_doctor(doctor)

        actual_output = self.hospital.display_staff().strip()
        expected_output = "Doctors: Name: Dr. Smith, Age: 40, Specialization: Cardiology Nurses: Name: Nurse Johnson, Age: 35, Department: Emergency"

    def test_display_patients(self):
        doctor = self.doctor_factory.create_person("Dr. Smith", 40, "Cardiology")
        nurse = self.nurse_factory.create_person("Nurse Johnson", 35, "Emergency")
        patient = self.patient_factory.create_person("John Doe", 30, "Heart disease", doctor, nurse)
        self.hospital.add_patient(patient)

        actual_output = self.hospital.display_patients().strip()
        expected_output = "Patients: Name: John Doe, Age: 30, Problem: Heart disease, Assigned Doctor: Dr. Smith, Assigned Nurse: Nurse Johnson"

if __name__ == "__main__":
    unittest.main()
