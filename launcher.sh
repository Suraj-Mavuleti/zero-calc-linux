#!/bin/bash
# AUTO-UPDATER: Pull latest changes from GitHub before launching
cd /home/suraj/.gemini/antigravity/scratch/zero_suite/zero-calc-linux
git pull origin main --quiet

# Launch the GUI
python3 zero_calc_gui.py
