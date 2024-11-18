class Pa_Med:
    """
   Birbirine atanan bir Hasta ve Tıp çifti.
     Hastanın hangi ilacı aldığını göstermek için bir listede kullanılır.
    """
    def __init__(self, PatientID, MedicineID):
        self.__PatientID = PatientID
        self.__MedicineID = MedicineID

    def get_PatientID(self):
        return self.__PatientID

    def get_MedicineID(self):
        return self.__MedicineID

    def set_PatientID(self, id):
        self.__PatientID = id

    def set_MedicineID(self, id):
        self.__MedicineID = id

class Pa_Doc:
    """
   Birbirine atanan bir çift Hasta ve Doktor.
     Hangi doktorun hangi hastaya atandığını göstermek için listede kullanılır.
    """
    def __init__(self, PatientID, DoctorID):
        self.__PatientID = PatientID
        self.__DoctorID = DoctorID

    def get_PatientID(self):
        return self.__PatientID

    def get_DoctorID(self):
        return self.__DoctorID

    def set_PatientID(self, id):
        self.__PatientID = id

    def set_DoctorID(self, id):
        self.__DoctorID = id