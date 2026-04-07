Place your training images in these folders:

- `dataset/malnourished/`
- `dataset/normal/`

Each image inside `malnourished` should belong to the malnourished class.
Each image inside `normal` should belong to the normal or not-malnourished class.

After adding images, run:

```powershell
.\venv\Scripts\python.exe train_model.py
```

The trained model will be saved as `malnutrition_model.keras`.
