from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.exams import ExamDraftRequest, ExamFormRead, ExamSessionRead, ExamStartRequest
from app.services.exams import session_service as service

router = APIRouter(prefix='/exams', tags=['exams'])


@router.get('/subjects/{subject_id}', response_model=list[ExamFormRead])
def forms(subject_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return service.list_forms(db, subject_id)


@router.post('/start', response_model=ExamSessionRead)
def start(payload: ExamStartRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    session = service.start_exam(db, user.id, payload.subject_id, payload.form_id, payload.time_multiplier)
    result = service.read_exam(db, session)
    db.commit()
    return result


@router.get('/{session_id}', response_model=ExamSessionRead)
def read(session_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return service.read_exam(db, service.owned_exam(db, user.id, session_id))


@router.put('/{session_id}/sections/{index}/draft', response_model=ExamSessionRead)
def draft(session_id: int, index: int, payload: ExamDraftRequest,
          db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    session = service.save_draft(db, user.id, session_id, index, payload)
    result = service.read_exam(db, session)
    db.commit()
    return result


@router.post('/{session_id}/sections/{index}/start', response_model=ExamSessionRead)
def begin(session_id: int, index: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    session = service.begin_section(db, user.id, session_id, index)
    result = service.read_exam(db, session)
    db.commit()
    return result


@router.post('/{session_id}/sections/{index}/finish', response_model=ExamSessionRead)
def finish(session_id: int, index: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    session = service.finish_section(db, user.id, session_id, index)
    result = service.read_exam(db, session)
    db.commit()
    return result
