# Beck Anxiety Calculator

## Requirements

- Python 3.9 or newer
- Tkinter, which is included with most Windows Python installations

## Set up on Windows

Open PowerShell in this folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, run the commands below instead:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Run

With the virtual environment activated:

```powershell
python Quiz.py
```

Without activating it:

```powershell
.\.venv\Scripts\python.exe Quiz.py
```
