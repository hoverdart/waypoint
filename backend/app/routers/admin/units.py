from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import require_admin
from app.models.user import User
from app.schemas.admin import AdminUnitCreate, AdminUnitUpdate
from app.schemas.subject import UnitRead
from app.services.admin import curriculum_service

router = APIRouter(prefix="/admin/units", tags=["admin"])


@router.get("", response_model=list[UnitRead])
def list_units(subject_id: int, db: Session = Depends(get_db), _admin: User = Depends(require_admin)):
    return curriculum_service.list_units(db, subject_id)


@router.post("", response_model=UnitRead)
def create_unit(
    subject_id: int,
    payload: AdminUnitCreate,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    unit = curriculum_service.create_unit(db, subject_id, payload)
    db.commit()
    db.refresh(unit)
    return unit


@router.patch("/{unit_id}", response_model=UnitRead)
def update_unit(
    unit_id: int,
    payload: AdminUnitUpdate,
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    unit = curriculum_service.update_unit(db, unit_id, payload)
    db.commit()
    db.refresh(unit)
    return unit
