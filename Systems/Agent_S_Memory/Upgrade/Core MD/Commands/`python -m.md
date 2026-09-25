---
modified: 2026-04-23T07:26:41+03:00
---
Same fix as pytest 😄 Windows doesn't add Python scripts to PATH by default. Just prefix with `python -m`:

```bash
python -m uvicorn api.main:app --reload
```

That's it. Same pattern works for everything:

| ❌ Doesn't work | ✅ Works                                   |
| -------------- | ----------------------------------------- |
| `uvicorn ...`  | `python -m uvicorn api.main:app --reload` |
| `pytest`       | `python -m pytest tests/`                 |
| `pip`          | `python -m pip install ...`               |

**Permanent fix** (optional — so you never hit this again):

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

Restart your terminal after that, and `uvicorn`, `pytest`, etc. will all work directly without the `python -m` prefix.