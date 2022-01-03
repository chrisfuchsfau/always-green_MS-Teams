# always green

Script which keeps MS Teams status green always

## How to set up
There are 2 options to run the script:
- Run the exe (*exe) _- no python environment necessary_
- Run the python script (*.pyw) directly _- lean_

## a) run script in exe
1. Download exe script
    - Download `keep-green.exe`
    - Save at your preferred location on your computer
2. Run script
    - Run `keep-green.exe` file by double-click
    - In case your firewall is blocking the script, add a exception to firewall
3. _[optional]_ Autostart 
    - Link the script in autostart folder to launch script with system start

## b) run script in python
1. Install python
    - Download a version from official website and install python _[local admin rights needed]_
    - Works with **Python2.7.x**
    - **Python3.x** should also work
2. Install necessary package
    - Install package **pyautogui** with command `pip install pyautogui` in shell
    - If using Python3.x `pip3 install pyautogui`
3. Download python script
    - Download `keep-green.pyw`
    - Save at your preferred location on your computer
4. Run script
    - Run `keep-green.pyw` file with: 
      - Open file with `pythonw.exe` _[pythonw.exe will run python scripts in background process]_
      - Or run in shell with `pythonw <UR_LOCAL_PATH_TO_FILE>/keep-green.pyw`
5. _[optional]_ Autostart 
   - Link the script in autostart folder to launch script with system start
   - Set standard program for **.pyw** files with pythonw.exe _[located in your python installation folder]_
