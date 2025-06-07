from app.config.db import SessionLocal
from app.models.shared_bid import SharedBid
from tabulate import tabulate

class SharedBidService:
    @staticmethod
    def create_shared_bid(company_name: str, investor_name: str, bid: int):
        db = SessionLocal()
        shared_bid = SharedBid(investor_name=investor_name, company_name=company_name, bid=bid)
        db.add(shared_bid)
        db.commit()
        db.close()
    @staticmethod
    def update_shared_bid(company_name: str, investor_name: str, bid: int):
        db = SessionLocal()
        shared_bid = db.query(SharedBid).filter(SharedBid.investor_name == investor_name).filter(SharedBid.company_name == company_name).first()
        shared_bid.bid = bid
        db.commit()
        db.close()
    @staticmethod
    def check_if_exists(company_name: str, investor_name: str):
        db = SessionLocal()
        shared_bid = db.query(SharedBid).filter(SharedBid.investor_name == investor_name).filter(SharedBid.company_name == company_name).first()
        db.close()
        return True if shared_bid else False

    @staticmethod
    def print_shares_bid_table(typer):
        db = SessionLocal()
        # Get all bids
        bids = db.query(SharedBid).all()

        # Get unique company names and investors
        investors = sorted(set(b.investor_name for b in bids))
        companies = sorted(set(b.company_name for b in bids))
        table = []
        for investor in investors:
            row = [investor]
            for company in companies:
                bid = next((b.bid for b in bids if b.investor_name == investor and b.company_name == company), 0)
                row.append(bid)
            table.append(row)

        headers = ["Shared Bids"] + companies

        typer.echo(tabulate(table, headers=headers, tablefmt="grid"))

    @staticmethod
    def get_values(company_name, investor, typer):
        while True:
            bid = typer.prompt(f"Bid for '{company_name}' by '{investor}'?")
            try:
                bid = int(bid)
                break
            except ValueError:
                typer.echo(f"\n\033[1mBid for '{company_name}' by '{investor}' must be a number\033[0m")
        return bid