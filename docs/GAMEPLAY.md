# Gameplay and implementation

The game is a DOS-era graphical take on the endless-runner format, implemented in a single x86 assembly source file.

## Controls

- **Space** or **Up Arrow** — jump
- **Down Arrow** — crouch
- **Left/Right Arrow** — move the dinosaur horizontally
- Mouse — navigate the menu

## Game systems

- Day and night presentation modes
- Multiple obstacle types, including ground hurdles and birds
- Collision detection based on screen-coordinate regions
- Five-life health system
- Score, elapsed-time, and high-score tracking
- Heart, 2×, and 5× score bonuses
- Player-name and score-file handling through DOS services

## Technical structure

`src/main.asm` uses the MASM small memory model and BIOS/DOS interrupts for graphics, input, timing, sound, and file operations. Coordinate arrays encode the dinosaur, scenery, menu, and obstacle shapes. The source is intentionally preserved in its original implementation form.
