from app.services.term import TermService
from app.services.shared_bid import SharedBidService
def team2_first_project_run(typer, gevent):
    while True:
        typer.echo("\nTEAM 2: Current terms")
        for term in TermService.get_terms():
            typer.echo(f"{term.name}: {term.value} | Approved: {term.is_approved}")
        choice = typer.prompt("Approve a term? (name or 'no')")
        if choice.lower() == "no":
            gevent.sleep(2)
            continue
        TermService.approve_term(choice)
        if TermService.all_terms_approved():
            typer.echo("✅ All terms approved by Team 2!")
            break
        gevent.sleep(1)

def team2_second_project_run(typer, gevent):
    while True:
        typer.echo("\nTEAM 2: Current terms")
        for term in TermService.get_terms():
            typer.echo(f"{term.name}: {term.value} | Approved: {term.is_approved}")
        choice = typer.prompt("Approve a term? (name or 'no')")
        if choice.lower() == "no":
            gevent.sleep(2)
            continue
        TermService.approve_term(choice)
        if TermService.all_terms_approved():
            typer.echo("✅ All terms approved by Team 2!")
            break
        gevent.sleep(1)
