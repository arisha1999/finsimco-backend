from app.config.db import SessionLocal
from app.models.term import Term
from sqlalchemy import asc

class TermService:
    @staticmethod
    def create_term_value(term_name: str, value: str):
        db = SessionLocal()
        term = Term(name=term_name, value=value, is_approved=False)
        db.add(term)
        db.commit()
        db.close()
    @staticmethod
    def update_term_value(term_name: str, value: str):
        db = SessionLocal()
        term = db.query(Term).filter(Term.name == term_name).first()
        term.value = value
        term.is_approved = False
        db.commit()
        db.close()
    @staticmethod
    def check_if_exists(term_name: str):
        db = SessionLocal()
        term = db.query(Term).filter(Term.name == term_name).first()
        db.close()
        return True if term else False

    @staticmethod
    def change_approval_status(term_name: str):
        db = SessionLocal()
        term = db.query(Term).filter(Term.name == term_name).first()
        if term:
            term.is_approved = not term.is_approved
            db.commit()
        db.close()

    @staticmethod
    def get_terms(is_approved=None):
        db = SessionLocal()
        query = db.query(Term)
        query = Term.filter_by_is_approved(query, is_approved).order_by(asc(Term.is_approved)).order_by(asc(Term.name))
        terms = query.all()
        db.close()
        return terms

    @staticmethod
    def all_terms_approved():
        return all(t.is_approved for t in TermService.get_terms())

    @staticmethod
    def print_terms(typer, is_approved=None):
        typer.echo("")
        for term in TermService.get_terms(is_approved):
            typer.echo(f"{term.name}: {term.value} | Approved: {'OK' if term.is_approved else 'TBD'}")
        typer.echo("")