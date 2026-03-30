from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas

# ---------- Doctor ----------
def update_doctor(db: Session, doctor_id: int, doctor_data: schemas.DoctorUpdate):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    for key, value in doctor_data.dict().items():
        setattr(doctor, key, value)

    db.commit()
    db.refresh(doctor)
    return doctor


# ---------- Patient ----------
def update_patient(db: Session, patient_id: int, patient_data: schemas.PatientUpdate):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    for key, value in patient_data.dict().items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)
    return patient


# ---------- Appointment ----------
def update_appointment(
    db: Session,
    appointment_id: int,
    appointment_data: schemas.AppointmentUpdate
):
    appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    for key, value in appointment_data.dict().items():
        setattr(appointment, key, value)

    db.commit()
    db.refresh(appointment)
    return appointment