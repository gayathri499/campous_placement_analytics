import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    "CGPA": np.round(np.random.uniform(5, 10, n), 2),
    "Aptitude_Score": np.random.randint(40, 100, n),
    "Communication_Score": np.random.randint(40, 100, n),
    "Technical_Score": np.random.randint(40, 100, n),
    "Internships": np.random.randint(0, 4, n),
    "Projects": np.random.randint(1, 6, n),
    "Certifications": np.random.randint(0, 5, n),
    "Hackathons": np.random.randint(0, 3, n),
}

df = pd.DataFrame(data)

df["Placement_Status"] = (
    (df["CGPA"] > 7) &
    (df["Technical_Score"] > 60) &
    (df["Communication_Score"] > 55)
).astype(int)

df["Salary_LPA"] = np.where(
    df["Placement_Status"] == 1,
    np.round(np.random.uniform(4, 12, n), 2),
    0
)

df.to_csv("placement_data.csv", index=False)
print("Dataset Created Successfully!")