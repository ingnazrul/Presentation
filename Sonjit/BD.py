import pandas as pd

p = pd.DataFrame({"name": ["Nazrur", "Sonjit"], "age": [13,14], "id": [12,14]})

p["total_age"] = p["age"] + p["id"]





