# Setup

```bash
python3 00-setup/01_verify_installation.py
```

## Examples

- `01_verify_installation.py`
- `02_virtual_environment.py`
- `03_project_layout.py`




---

## Interview Prep

### Must-Know Concepts

- Difference between **system Python** and **virtual environment**
- `pip install` vs `pip install -r requirements.txt`
- `pyproject.toml` vs `requirements.txt` (modern vs legacy)
- Why `.venv` is added to `.gitignore`

### Theory Questions

**Q1: Why use virtual environments?**  
A: Isolate project dependencies. Project A may need Django 4.x while Project B needs Django 3.x. venv prevents version conflicts and keeps the system Python clean.

**Q2: What is `PYTHONPATH`?**  
A: Environment variable listing directories Python searches for modules. Prefer proper package structure over manipulating PYTHONPATH.

**Q3: `python` vs `python3` vs `py`?**  
A: On macOS/Linux, `python3` explicitly invokes Python 3. Windows `py` launcher selects version. In venv, `python` points to venv interpreter.

**Q4: What files define project dependencies?**  
A: `requirements.txt` (pinned list), `pyproject.toml` (PEP 518 — modern standard with build metadata), `Pipfile` (Pipenv).

## Practical Questions

**Q5: How do you set up a new Python project from scratch?**  
```bash
mkdir myapp && cd myapp
python3 -m venv .venv && source .venv/bin/activate
pip install pytest black ruff mypy
pip freeze > requirements.txt
```

**Q6: How do you check which Python is running?**  
```python
import sys
print(sys.executable, sys.version)
```

### Common Pitfalls

- Installing packages globally (`sudo pip install`) — breaks system tools
- Committing `.venv/` to git — bloats repo; use requirements.txt
- Not pinning versions in production — use `pip freeze` or tools like `poetry lock`
