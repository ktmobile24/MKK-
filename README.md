# Streamlit Cloud Diagnostic Repo
- `mini_app.py` – runs basic environment checks & imports
- `tracker_app.py` – your app
- `requirements.txt` – pinned deps
- `runtime.txt` – pin Python 3.11.9

## Deploy steps
1) Create a **public** GitHub repo and upload all files to the repo root.
2) On Streamlit Cloud, set **Main file** to `mini_app.py` and deploy.
3) Verify the page shows Python version and that imports are OK.
   - If errors appear, the platform isn't using `requirements.txt` → check filename/location and try Restart/Clear cache.
4) When OK, change **Main file** to `tracker_app.py` and redeploy.
