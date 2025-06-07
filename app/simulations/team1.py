from app.services.term import TermService
from app.services.pricing import PricingService
from app.services.shared_bid import SharedBidService
from app.services.ready_event import ReadyEventService
from app.utils.utils import Utils

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
    typer.echo("TEAM 1: You can change your terms")
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

def team1_second_project_run(typer, gevent):
    ReadyEventService.create_team_info('team 1')
    # Print all available companies
    typer.echo("TEAM 1: This is your available companies")
    company_names = ["Company 1", "Company 2", "Company 3"]
    for company in company_names:
        typer.echo(company)
    typer.echo("TEAM 1: Enter your values")
    for company_name in company_names:
        # Getting price till it's an integer
        price, shares = PricingService.get_values(company_name, typer)
        PricingService.create_pricing(company_name, price, shares)
    while True:
        typer.echo("\nCurrent shares:")
        PricingService.print_pricing_table(typer)
        team_2_info = typer.prompt("Do you want to see bids from team 2? ('yes' or 'no')")
        if team_2_info.lower() == "yes":
            if ReadyEventService.check_if_exists('team 2'):
                SharedBidService.print_shares_bid_table(typer)
            else:
                typer.echo("Team 2 has not joined yet")
        want_to_change = typer.prompt("Do you want to edit a share and value or are you done? ('yes' for edit or 'no' for done or 'wait' to a wait for Team 2)")
        if want_to_change.lower() == "no":
            ReadyEventService.update_team_info('team 1')
            break
        elif want_to_change.lower() == "wait":
            gevent.sleep(2)
            continue
        choice = typer.prompt("Enter a company name to change values? (name or 'no')")
        if choice.lower() == "no":
            continue

        # Check if share exists
        check_if_exists = PricingService.check_if_exists(choice)
        if not check_if_exists:
            typer.echo(f"\n\033[1mShare with name '{choice}' not found\033[0m")
            continue

        # Edit share
        price, shares = PricingService.get_values(choice, typer)
        PricingService.update_pricing(choice, price, shares)

    while not ReadyEventService.check_if_exists('team 2'):
        typer.echo("Team 2 has not joined yet")
        gevent.sleep(1)

    while not ReadyEventService.check_if_ready('team 2'):
        typer.echo("Team 2 is not ready yet")
        gevent.sleep(1)

    typer.echo("\033[1mAll bids filled by Team 2!\033[0m \nFinal info:")
    Utils.print_final_investments(typer)
