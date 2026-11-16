# Copilot instructions

- This is a uv project. Run commands from the project root with `uv run ...`.
- Start the Flask app with `uv run python3 src/index.py`. It listens on port 5001.
- Flask routes are defined in `src/app.py`; `src/index.py` starts the app.
- Run all Robot Framework acceptance tests with `uv run robot src/tests`.
- The Flask app must be running while Robot tests execute.
- Usernames and passwords are validated in `src/services/user_service.py`.
- User data is stored in memory and can be cleared through the test reset endpoint.