# Run Streamlit App

import subprocess

#file = "app.py"
#file = "app_plots.py"
#file = "app_profiler.py"
#file = "app_profiler_menus.py"
#file = "app_profiler_napo.py"
#file = "app_profiler_napo2.py"
file = "app_profiler_napo3.py"
#file = "napo_profile.py"
#file = "dog_life.py"



subprocess.Popen(
    ["streamlit", "run", file], shell=True
)