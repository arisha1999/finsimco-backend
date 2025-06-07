# FinSimCo Backend Test

## 📜 Technical Specification (Backend)

### Simulation Game № 1

For the 1st Simulation Game - The program should ask Team 1 to input values and show outputs as soon as all values are filled in. After outputs are shown, there is always an ability to jump back to edit a particular input (selection mechanism is up to you). After changing, an updated output should be shown. Outputs should reflect the most recent TBD state from Team 2.

Team 2 should have ability to see most recent terms from Team 1 and switch the toggle of approval for each input selectively. When Team 1 changes the input, the TBD toggle triggers back to TBD state (false).

### Simulation Game № 2

For the 2nd Simulation Game – This one has the same logic of execution, except that Team 2 enters inputs too and the outputs for both teams is a combination of both teams' inputs.

### Table info for this project 

![Excel Table](https://ibb.co/whQP6sff)

## 🛠️ Technologies

- Python 3.10+
- Docker & Docker Compose
- PostgreSQL
- Gevent
- SQLAlchemy
- Typer (CLI framework)

## 🚀 How to Run the Project

```bash
# 1. Stop and remove any existing containers and volumes
docker compose down -v

# 2. Start the PostgreSQL database
docker compose up -d db

# 3. Build the Docker images
docker compose build

# 4. Initialize the database and create all tables
docker compose run --rm app python app/config/init_db.py

# 5. Run the CLI simulation for each team/project combination
# If it's Simulation Game № 1:
docker compose run --rm app python app/main.py 1 1 # Team 1
docker compose run --rm app python app/main.py 2 1 # Team 2
# If it's Simulation Game № 1:
docker compose run --rm app python app/main.py 1 2 # Team 1
docker compose run --rm app python app/main.py 2 2 # Team 2

# 6. To clear the DB run this
docker compose run --rm app python app/config/clear_db.py