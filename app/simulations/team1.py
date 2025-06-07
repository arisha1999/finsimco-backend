from app.services.term import TermService
from app.services.pricing import PricingService

def team1_first_project_run(typer):
    typer.echo("TEAM 1: Enter values")
    for term_name in ["EBITDA", "Interest Rate", "Multiple", "Factor Score"]:
        value = typer.prompt(f"{term_name}?")
        TermService.set_term_value(term_name, value)

    while not TermService.all_terms_approved():
        typer.echo("\nCurrent terms:")
        for term in TermService.get_terms():
            typer.echo(f"{term.name}: {term.value} | Approved: {term.is_approved}")

        choice = typer.prompt("Edit a term? (name or 'no')")
        if choice.lower() == "no":
            continue
        new_val = typer.prompt(f"New value for {choice}")
        TermService.set_term_value(choice, new_val)

    typer.echo("✅ All terms approved! Final terms:")
    for term in TermService.get_terms():
        typer.echo(f"{term.name}: {term.value}")

def team1_second_project_run(typer):
    typer.echo("TEAM 1: Enter values")
    for term_name in ["EBITDA", "Interest Rate", "Multiple", "Factor Score"]:
        value = typer.prompt(f"{term_name}?")
        TermService.set_term_value(term_name, value)

    while not TermService.all_terms_approved():
        typer.echo("\nCurrent terms:")
        for term in TermService.get_terms():
            typer.echo(f"{term.name}: {term.value} | Approved: {term.is_approved}")

        choice = typer.prompt("Edit a term? (name or 'no')")
        if choice.lower() == "no":
            continue
        new_val = typer.prompt(f"New value for {choice}")
        TermService.set_term_value(choice, new_val)

    typer.echo("✅ All terms approved! Final terms:")
    for term in TermService.get_terms():
        typer.echo(f"{term.name}: {term.value}")