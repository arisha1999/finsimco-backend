from app.services.term import TermService
from app.services.shared_bid import SharedBidService
from app.services.pricing import PricingService
from app.services.ready_event import ReadyEventService
from app.utils.utils import Utils
def team2_first_project_run(typer, gevent):
    # We just wait while it's gonna be approved by Team 2
    while True:
        typer.echo("TEAM 2: Current terms")
        TermService.print_terms(typer)
        term = typer.prompt("Approve a term? (name or 'no')")
        if term.lower() == "no":
            gevent.sleep(2)
            continue

        # Check if term exists
        check_if_exists = TermService.check_if_exists(term)
        if not check_if_exists:
            typer.echo(f"\n\033[1mTerm with name '{term}' not found\033[0m")
            continue

        # Change approval status
        TermService.change_approval_status(term)

        # Check if all terms are approved
        if TermService.all_terms_approved():
            typer.echo("\033[1mAll terms approved by Team 2!\033[0m \nFinal terms:")
            TermService.print_terms(typer)
            break
        gevent.sleep(1)

def team2_second_project_run(typer, gevent):
    ReadyEventService.create_team_info('team 2')
    # Print all available companies
    typer.echo("TEAM 1: This is your available companies")
    company_names = ["Company 1", "Company 2", "Company 3"]
    investors = ["Investor 1", "Investor 2", "Investor 3"]
    for company in company_names:
        typer.echo(company)

    # Getting bids from team 2
    typer.echo("TEAM 2: Enter your values")
    for company_name in company_names:
        for investor in investors:
            bid = SharedBidService.get_values(company_name, investor, typer)
            SharedBidService.create_shared_bid(company_name, investor, bid)

    typer.echo("TEAM 2: You can change your bid")
    while True:
        typer.echo("\nCurrent bids:")
        SharedBidService.print_shares_bid_table(typer)
        # Just if you want to check out team 1 info
        team_1_info = typer.prompt("Do you want to see shares and values from team 1? ('yes' or 'no')")
        if team_1_info.lower() == "yes":
            if ReadyEventService.check_if_exists('team 1'):
                PricingService.print_pricing_table(typer)
            else:
                typer.echo("Team 1 has not joined yet")
        # This one is to stop or continue
        want_to_change = typer.prompt("Do you want to edit a bid or are you done ? ('yes' for edit or 'no' for done or 'wait' to a wait for Team 1)")
        if want_to_change.lower() == "no":
            ReadyEventService.update_team_info('team 2')
            break
        elif want_to_change.lower() == "wait":
            gevent.sleep(2)
            continue
        company_name = typer.prompt("Enter a company name? (name or 'no')")
        if company_name.lower() == "no":
            continue

        investor = typer.prompt("Enter an investor? (name or 'no')")
        if investor.lower() == "no":
            continue

        # Check if share exists
        check_if_exists = SharedBidService.check_if_exists(company_name, investor)
        if not check_if_exists:
            typer.echo(f"\n\033[1mBid with company name '{company_name}' and investor '{investor}' not found\033[0m")
            continue

        # Edit share
        bid = SharedBidService.get_values(company_name, investor, typer)
        SharedBidService.update_shared_bid(company_name, investor, bid)

    # Wait for team 1 if it's joined
    while not ReadyEventService.check_if_exists('team 1'):
        typer.echo("Team 1 has not joined yet")
        gevent.sleep(1)

    # Wait for team 1 to fill all info
    while not ReadyEventService.check_if_ready('team 1'):
        typer.echo("Team 1 is not ready yet")
        gevent.sleep(1)

    typer.echo("\033[1mAll info filled by Team 1!\033[0m \nFinal info:")
    Utils.print_final_investments(typer)