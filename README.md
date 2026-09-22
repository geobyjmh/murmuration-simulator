# Moving Icon

A small Pygame app with a friendly icon that moves around the window.

## Project structure

```text
murmuration-simulator/
├── main.py                 # Starts the game
├── requirements.txt        # Python dependencies
├── README.md
├── .gitignore
├── scripts/
│   └── install_pygame.bat  # Windows setup script
└── game/
    ├── __init__.py
    ├── settings.py         # Window size, colors, and speed
    ├── player.py           # Moving icon
    └── game.py             # Main game loop
```

## Run

Install the dependency:

```powershell
python -m pip install -r requirements.txt
```

On Windows, you can also double-click `scripts\install_pygame.bat`.

Start the app:

```powershell
python main.py
```

Use the **arrow keys** or **WASD** to move the icon. Close the window to exit.
