from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import schemas, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#Doctors

@router.post("/doctors", response_model=schemas.DoctorResponse)
def create_doctor(
    doctor: schemas.DoctorCreate,
    db: Session = Depends(get_db)
):
    return crud.create_doctor(db, doctor)


@router.get("/doctors", response_model=list[schemas.DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)


@router.put("/doctors/{doctor_id}", response_model=schemas.DoctorResponse)
def update_doctor(
    doctor_id: int,
    doctor: schemas.DoctorUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_doctor(db, doctor_id, doctor)


@router.delete("/doctors/{doctor_id}")
def delete_doctor(
    doctor_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_doctor(db, doctor_id)


#Patients

@router.post("/patients", response_model=schemas.PatientResponse)
def create_patient(
    patient: schemas.PatientCreate,
    db: Session = Depends(get_db)
):
    return crud.create_patient(db, patient)


@router.get("/patients", response_model=list[schemas.PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return crud.get_patients(db)


@router.put("/patients/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(
    patient_id: int,
    patient: schemas.PatientUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_patient(db, patient_id, patient)


@router.delete("/patients/{patient_id}")
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_patient(db, patient_id)


#Appointments

@router.post("/appointments", response_model=schemas.AppointmentResponse)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment)


@router.get("/appointments", response_model=list[schemas.AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return crud.get_appointments(db)


@router.put("/appointments/{appointment_id}", response_model=schemas.AppointmentResponse)
def update_appointment(
    appointment_id: int,
    appointment: schemas.AppointmentUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_appointment(db, appointment_id, appointment)


@router.delete("/appointments/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    return crud.delete_appointment(db, appointment_id)