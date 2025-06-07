from app.services.term import TermService
from app.services.shared_bid import SharedBidService
def team2_first_project_run(typer, gevent):
    while True:
        typer.echo("\nTEAM 2: Current terms")
        TermService.print_terms(typer)
        term = typer.prompt("Approve a term? (name or 'no')")
        if term.lower() == "no":
            gevent.sleep(2)
            continue
        check_if_exists = TermService.check_if_exists(term)
        if not check_if_exists:
            typer.echo(f"\n\033[1mTerm with name '{term}' not found\033[0m")
            continue
        TermService.change_approval_status(term)
        if TermService.all_terms_approved():
            typer.echo("\033[1mAll terms approved by Team 2!\033[0m \nFinal terms:")
            TermService.print_terms(typer)
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
