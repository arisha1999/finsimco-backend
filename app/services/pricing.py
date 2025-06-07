from app.config.db import SessionLocal
from app.models.term import Term

class PricingService:
    @staticmethod
    def set_term_value(term_name: str, value: str):
        db = SessionLocal()
        term = db.query(Term).filter(Term.name == term_name).first()
        if term:
            term.value = value
            term.is_approved = False
        db.commit()
        db.close()

    @staticmethod
    def approve_term(term_name: str):
        db = SessionLocal()
        term = db.query(Term).filter(Term.name == term_name).first()
        if term:
            term.is_approved = True
            db.commit()
        db.close()

    @staticmethod
    def get_terms():
        db = SessionLocal()
        terms = db.query(Term).all()
        db.close()
        return terms

    @staticmethod
    def all_terms_approved():
        return all(t.is_approved for t in TermService.get_terms())