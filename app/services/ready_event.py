# app/services/ready_flag_service.py
from app.models.ready_event import ReadyEvent
from app.config.db import SessionLocal

class ReadyEventService:
    @staticmethod
    def create_team_info(team: str):
        session = SessionLocal()
        try:
            flag = ReadyEvent(team=team, is_ready=False)
            session.add(flag)
            session.commit()
        finally:
            session.close()

    @staticmethod
    def update_team_info(team: str):
        session = SessionLocal()
        try:
            flag = session.query(ReadyEvent).filter_by(team=team).first()
            flag.is_ready = not flag.is_ready
            session.commit()
        finally:
            session.close()

    @staticmethod
    def check_if_ready(team: str):
        session = SessionLocal()
        flag = session.query(ReadyEvent).filter_by(team=team).first()
        session.close()
        return flag.is_ready

    @staticmethod
    def check_if_exists(team: str):
        session = SessionLocal()
        flag = session.query(ReadyEvent).filter_by(team=team).first()
        session.close()
        return True if flag else False