import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import os

# Step 1: Load CSV
df_bls = pd.read_csv("data/processed/bls_compensation.csv")  # adjust path as needed

# Step 2: Pivot to wide format
df_pivot = df_bls.pivot(index=["year", "month"], columns="series_id", values="value").reset_index()

# Step 3: Normalize series columns
scaler = StandardScaler()
series_cols = [col for col in df_pivot.columns if col not in ["year", "month"]]
scaled_data = scaler.fit_transform(df_pivot[series_cols])

# Step 4: Apply k-means clustering (can be expanded if you add more series)
kmeans = KMeans(n_clusters=2, random_state=42)
df_pivot["cluster"] = kmeans.fit_predict(scaled_data)

# Step 5: Create output directory
output_dir = "bls_reports"
os.makedirs(output_dir, exist_ok=True)

# Step 6: Generate charts per series
for series in series_cols:
    fig, ax = plt.subplots(figsize=(10, 4))
    
    # Prepare data
    series_data = df_bls[df_bls['series_id'] == series].copy()
    series_data['label'] = series_data['year'].astype(str) + "-" + series_data['month']
    
    # Plot
    ax.plot(series_data['label'], series_data['value'], marker='o')
    ax.set_title(f"{series} Trend Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.tick_params(axis='x', labelrotation=45)
    ax.grid(True)
    
    # Save
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"{series}_report.png"))
    plt.close()

print(f"Report images saved to: {output_dir}/")
