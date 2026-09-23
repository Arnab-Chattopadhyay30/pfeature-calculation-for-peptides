import pandas as pd
import pfeature.python_scripts.pfeature_comp as pf

# Load original dataset

df = pd.read_csv(new_final.csv")

sequences = df["column_name"].astype(str)


import inspect

print(inspect.signature(pf.aac_comp))

import pandas as pd

# Your input CSV file
input_file = new_final.csv"

# Separate output TXT file
output_file =new_final.txt"

# Read CSV
df = pd.read_csv(input_file)

# Extract SEQUENCE column and save as a separate TXT file
df["Sequence"].to_csv(output_file, index=False, header=False)

print(f"Done! Sequences saved to {output_file}")


sequence_file = r"new_final.txt"

sequences.to_csv(
    sequence_file,
    index=False,
    header=False
)

pf.aac_comp(
    sequence_file,
    r"new_final_aac.csv"
)

# Performing physicochemical properties calculation

pcp_result = pf.pcp(sequence_file)

print(len(pcp_result[0]))
print(len(pcp_result[1]))

import inspect
import pfeature.python_scripts.pfeature_comp as pf

# Physicochemical properties features estimation

# Load original dataset
df = pd.read_csv(r"new_final.csv")
sequence_file = r"new_final.txt"
# Check number of sequences
print(len(df["Sequence"]))

# Store PCP features
pcp_rows = []
feature_names = None

for i, seq in enumerate(df["Sequence"].astype(str)):

    result = pf.pcp(sequence_file)

    # Get feature names from first sequence
    if feature_names is None:
        feature_names = result[0]

    # Get PCP values
    values = result[1][:len(feature_names)]

    pcp_rows.append(values)

    if (i + 1) % 100 == 0:
        print("Processed:", i + 1)

# Create PCP dataframe
pcp_df = pd.DataFrame(
    pcp_rows,
    columns=feature_names
)

# Add FRS target
pcp_df["label"] = df["label"].values

# Save
pcp_df.to_csv(
   r"new_final_pcp.csv",
    index=False
)

print("Final shape:", pcp_df.shape)

sequence_file = r"new_final.txt"

aac_file =r"new_final_aac.csv"

pf.aac_comp(sequence_file, aac_file)

import pandas as pd

aac_df = pd.read_csv(aac_file)

aac_df.shape

import pandas as pd

# 1. Read PCP file
pcp_df = pd.read_csv(
    r"new_final_pcp.csv"
)

# 2. Separate label from PCP features
pcp_features = pcp_df.drop(columns=["label"])

# 3. AAC features
aac_features = aac_df.copy()

# 4. Combine PCP + AAC features
combined_df = pd.concat(
    [pcp_features, aac_features],
    axis=1
)

# 5. Add label back
combined_df["label"] = pcp_df["label"].values

# 6. Save as a new CSV file
output_file = r"new_final_pcp_aac.csv"

combined_df.to_csv(
    output_file,
    index=False
)

# 7. Check the result
print("Combined file saved successfully!")
print("Shape:", combined_df.shape)
print("Output:", output_file)


import pandas as pd

# Original AO dataset
ao_df = pd.read_csv(r"new_final.csv")

# PCP + AAC dataset
combined_df = pd.read_csv(
   r"new_final_pcp_aac.csv"
)

# Add Sequence as the first column
combined_df.insert(0, "Sequence", ao_df["Sequence"].values)

# Save final dataset
final_file = r"new_final_pcp_aac_sequence.csv"
combined_df.to_csv(final_file, index=False)

# Check
combined_df.shape

#Binary profiling

import pandas as pd
import pfeature.python_scripts.pfeature_comp as pf

# Load dataset

df = pd.read_csv(r"Antioxidant\new_final.csv")

# Get sequences
sequences = df["Sequence"].dropna().astype(str).str.strip()

# Create Pfeature input
sequence_file = r"Antioxidant\new_final.txt"

with open(sequence_file, "w") as f:
    f.write(",".join(sequences))

# Binary profile
binary = pf.binary_profile_1(sequence_file, 0)

# Convert each profile to normal Python integers
binary_clean = [
    [int(float(value)) for value in profile]
    for profile in binary
]

# Find maximum sequence length
max_len = max(len(profile) for profile in binary_clean)

# Make all rows same length for the table
binary_table = pd.DataFrame(
    binary_clean,
    columns=[f"Binary_{i+1}" for i in range(max_len)]
)

# Add sequence
binary_table.insert(0, "Sequence", sequences.values)

# Save
output_file = r"new_final_pcp_aac_binary.csv"
binary_table.to_csv(output_file, index=False)

print(binary_table.head())
print("Shape:", binary_table.shape)
print("Saved:", output_file)

#Combined AAC+PCP+binary_features


pcpaac_df = pd.read_csv(r"new_final_pcp_aac.csv")
pcpaac_fearures = pcpaac_df.drop(columns=["label"]) 

binary_files = pd.read_csv(r"new_final_pcp_aac_binary.csv")

combined_df = pd.concat(
    [pcpaac_fearures, binary_files],
    axis=1
)
combined_df["label"] = df["label"].values
combined_df.to_csv(r"new_final_pcp_aac_binary.csv",index="false")

