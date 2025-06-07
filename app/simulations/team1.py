from app.services.term import TermService
from app.services.pricing import PricingService

def team1_first_project_run(typer):
    typer.echo("TEAM 1: Enter values")
    # Enter terms and values
    while True:
        term_name = typer.prompt("Enter term name (or 'done')")
        if term_name.lower() == "done":
            break
        value = typer.prompt(f"Value for '{term_name}'?")
        TermService.create_term_value(term_name, value)

    # Change terms if needed or just wait for approval
    while not TermService.all_terms_approved():
        typer.echo("\nCurrent terms:")
        TermService.print_terms(typer, False)

        choice = typer.prompt("Edit a term? (name or 'no')")
        if choice.lower() == "no":
            continue

        # Check if term exists
        check_if_exists = TermService.check_if_exists(choice)
        if not check_if_exists:
            typer.echo(f"\n\033[1mTerm with name '{choice}' not found\033[0m")
            continue

        # Edit term
        new_val = typer.prompt(f"New value for {choice}")
        TermService.update_term_value(choice, new_val)

    # That means all terms are approved by Team 2
    typer.echo("\033[1mAll terms approved by Team 2!\033[0m \nFinal terms:")
    TermService.print_terms(typer)

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