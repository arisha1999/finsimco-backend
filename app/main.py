import typer
import gevent
from gevent import monkey; monkey.patch_all()
from app.simulations.team1 import team1_first_project_run as run_team1_first_project
from app.simulations.team2 import team2_first_project_run as run_team2_first_project
from app.simulations.team1 import team1_second_project_run as run_team1_second_project
from app.simulations.team2 import team2_second_project_run as run_team2_second_project
app = typer.Typer()

@app.command()
def run(team: int, game: int):
    if team == 1:
        run_team1_first_project(typer) if game == 1 else run_team1_second_project(typer)
    elif team == 2:
        run_team2_first_project(typer, gevent) if game == 1 else run_team2_second_project(typer, gevent)
    else:
        typer.echo("❌ Invalid team number. Choose 1 or 2.")

if __name__ == "__main__":
    app()