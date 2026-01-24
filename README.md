# For Nepali App

## 1. Environment Variables
- Railway automatically sets the `PORT` environment variable. Update your app to use this port if available.

## 2. Procfile
- The included `Procfile` tells Railway how to start your app: `web: python app.py`

## 3. railway.json
- The included `railway.json` configures Python version and build/start commands.

## 4. Flask App Port
- Modify your Flask app to use the `PORT` environment variable if set (see below).

## 5. Deploy
- Push this repo to Railway and it will auto-deploy.

---

### Flask Port Update Example

Replace:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```
With:
```python
import os
port = int(os.environ.get("PORT", 5000))
app.run(debug=False, host='0.0.0.0', port=port)
```

---

For more, see Railway docs: https://docs.railway.app/deploy/deployments/python
