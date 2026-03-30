from sqlalchemy.orm import Session
from fastapi import HTTPException

from app import models, schemas

#Doctor

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(
        name=doctor.name,
        specialization=doctor.specialization
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def get_doctors(db: Session):
    return db.query(models.Doctor).all()


def update_doctor(db: Session, doctor_id: int, doctor: schemas.DoctorUpdate):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db_doctor.name = doctor.name
    db_doctor.specialization = doctor.specialization
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()

    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(db_doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}

#Patient

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(
        name=patient.name,
        age=patient.age
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


def get_patients(db: Session):
    return db.query(models.Patient).all()


def update_patient(db: Session, patient_id: int, patient: schemas.PatientUpdate):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db_patient.name = patient.name
    db_patient.age = patient.age
    db.commit()
    db.refresh(db_patient)
    return db_patient


def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(db_patient)
    db.commit()
    return {"message": "Patient deleted successfully"}


#Appointment

def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(
        appointment_date=appointment.appointment_date,
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def get_appointments(db: Session):
    return db.query(models.Appointment).all()


def update_appointment(
    db: Session,
    appointment_id: int,
    appointment: schemas.AppointmentUpdate
):
    db_appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )

    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db_appointment.appointment_date = appointment.appointment_date
    db_appointment.doctor_id = appointment.doctor_id
    db_appointment.patient_id = appointment.patient_id
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


def delete_appointment(db: Session, appointment_id: int):
    db_appointment = (
        db.query(models.Appointment)
        .filter(models.Appointment.id == appointment_id)
        .first()
    )

    if not db_appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")

    db.delete(db_appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}
