from app.config.db import SessionLocal
from app.models.shared_bid import SharedBid
from app.models.pricing import Pricing
from app.models.term import Term
from app.models.ready_event import ReadyEvent
from tabulate import tabulate
class Utils:

    @staticmethod
    def clear_db():
        db = SessionLocal()
        db.query(SharedBid).delete()
        db.query(Pricing).delete()
        db.query(Term).delete()
        db.query(ReadyEvent).delete()
        db.commit()
        db.close()
        print(f"All DB are cleared before use!")

    @staticmethod
    def print_final_investments(typer):
        session = SessionLocal()
        try:
            # Getting prices and shares from company
            pricing_data = {p.company_name: {"price": p.price, "shares": p.shares} for p in
                            session.query(Pricing).all()}

            # Group bids by company
            bids = session.query(SharedBid.company_name, SharedBid.bid).all()
            bid_summary = {}
            for company, bid in bids:
                bid_summary.setdefault(company, 0)
                bid_summary[company] += bid

            headers = ["", *pricing_data.keys()]
            shares_row = ["Shares Bid For:"]
            capital_row = ["Capital Raised:"]
            sub_row = ["Subscription:"]

            max_bids = 0
            most_bid_company = None

            for company in pricing_data:
                price = pricing_data[company]["price"]
                available_shares = pricing_data[company]["shares"]
                bid_shares = bid_summary.get(company, 0)

                shares_row.append(f"{bid_shares:,}")

                if bid_shares > max_bids:
                    max_bids = bid_shares
                    most_bid_company = company

                if bid_shares <= available_shares:
                    capital = bid_shares * price
                    capital_row.append(f"{capital:,}")
                    sub_row.append("Under" if bid_shares < available_shares else "Exact")
                else:
                    capital_row.append("Allocate")
                    sub_row.append("Over")

            typer.echo(tabulate([shares_row, capital_row, sub_row], headers=headers, tablefmt="fancy_grid"))

            typer("\nWhich company received the most bids from investors?")
            typer(f">>> \033[1m{most_bid_company}\033[0m")
        finally:
            session.close()