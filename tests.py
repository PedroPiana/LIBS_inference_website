import pandas as pd

INPUT_FILE="dataset/laser266.dat"
OUTPUT_FILE="dataset/test_samples.csv"

df=pd.read_csv(INPUT_FILE,sep=";",header=None)

wavelength=df.iloc[1:,0].values
samples=df.iloc[1:,1:].values
sample_names=df.iloc[0,1:].values.astype(str)

selected_indices=[0,1,2,150,151,152]

selected_samples=samples[:,selected_indices]
selected_names=sample_names[selected_indices]

output=pd.DataFrame(
    selected_samples,
    columns=selected_names
)

output.insert(0,"wavelength",wavelength)

output.to_csv(
    OUTPUT_FILE,
    sep=";",
    index=False
)

print(f"Test dataset created successfully: {OUTPUT_FILE}")
print(f"Number of samples: {len(selected_names)}")
print("Selected samples:")

for index,name in zip(selected_indices,selected_names):
    print(f"Index {index}: {name}")