from pydantic import BaseModel
from datetime import date

# Doctor 
class DoctorCreate(BaseModel):
    name: str
    specialization: str

class DoctorUpdate(DoctorCreate):
    pass

class DoctorResponse(DoctorCreate):
    id: int
    class Config:
        orm_mode = True


# Patient 
class PatientCreate(BaseModel):
    name: str
    age: int

class PatientUpdate(PatientCreate):
    pass

class PatientResponse(PatientCreate):
    id: int
    class Config:
        orm_mode = True


# Appointment 
class AppointmentCreate(BaseModel):
    appointment_date: date
    doctor_id: int
    patient_id: int

class AppointmentUpdate(AppointmentCreate):
    pass

class AppointmentResponse(AppointmentCreate):
    id: int
    class Config:
        orm_mode = True