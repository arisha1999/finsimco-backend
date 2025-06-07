from app.config.db import SessionLocal
from app.models.pricing import Pricing
from tabulate import tabulate

class PricingService:
    @staticmethod
    def create_pricing(company_name: str, price: int, shares: int):
        db = SessionLocal()
        pricing = Pricing(company_name=company_name, price=price, shares=shares)
        db.add(pricing)
        db.commit()
        db.close()
    @staticmethod
    def update_pricing(company_name: str, price: int, shares: int):
        db = SessionLocal()
        pricing = db.query(Pricing).filter(Pricing.company_name == company_name).first()
        pricing.price = price
        pricing.shares = shares
        db.commit()
        db.close()
    @staticmethod
    def check_if_exists(company_name: str):
        db = SessionLocal()
        pricing = db.query(Pricing).filter(Pricing.company_name == company_name).first()
        db.close()
        return True if pricing else False

    @staticmethod
    def print_pricing_table(typer):
        db = SessionLocal()
        # Get all pricings
        pricings = db.query(Pricing).order_by(Pricing.company_name).all()

        # Then sort companies
        companies = sorted(set(p.company_name for p in pricings))

        prices = {p.company_name: p.price for p in pricings}
        shares = {p.company_name: p.shares for p in pricings}
        headers = ["Pricing", *companies]

        price_row = ["Price:"] + [prices[c] for c in companies]
        shares_row = ["Shares:"] + [shares[c] for c in companies]
        table = [price_row, shares_row]

        typer.echo(tabulate(table, headers=headers, tablefmt="grid"))

    @staticmethod
    def get_values(company_name, typer):
        while True:
            price = typer.prompt(f"Price for '{company_name}'?")
            try:
                price = int(price)
                break
            except ValueError:
                typer.echo(f"\n\033[1mPrice for '{company_name}' must be a number\033[0m")

        # Getting shares till it's an integer
        while True:
            shares = typer.prompt(f"Shares for '{company_name}'?")
            try:
                shares = int(shares)
                break
            except ValueError:
                typer.echo(f"\n\033[1mShares for '{company_name}' must be a whole number\033[0m")
        return price, shares