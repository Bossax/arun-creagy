import pandas as pd
import os

# Resolved path for ψ/ context
ROOT = r'C:/Users/sitth/OracleWorkspace/Arun_Creagy'
EXCEL_PATH = os.path.join(ROOT, 'ψ/incubate/DCCE/CRDB/output/03_DataInventory_DQ/260510_DCCE_CRDB_BaselineDataInventoryTOR5.3.5_v8online.xlsx')
OUTPUT_PATH = os.path.join(ROOT, 'ψ/incubate/DCCE/CRDB/output/03_DataInventory_DQ/combined_baseline_inventory.csv')

def consolidate_inventory():
    print(f"Reading: {EXCEL_PATH}")
    
    # Check if file exists
    if not os.path.exists(EXCEL_PATH):
        print(f"Error: File not found at {EXCEL_PATH}")
        return

    # Load all sheets to get names and indices
    xl = pd.ExcelFile(EXCEL_PATH)
    sheet_names = xl.sheet_names
    
    # Slice from sheet 6 (index 5) onward (skipping Ref_Lookups)
    target_sheets = sheet_names[5:]
    print(f"Targeting {len(target_sheets)} sheets: {target_sheets[0]} ... {target_sheets[-1]}")
    
    all_dfs = []
    for name in target_sheets:
        print(f"Processing sheet: {name}")
        # Note: adjust 'header=0' or 'skiprows' if the Excel has metadata at the top
        df = pd.read_excel(xl, sheet_name=name)
        # Add source sheet name for traceability (Auditor's Rule)
        df['source_sheet'] = name
        all_dfs.append(df)
    
    # Combine everything
    print("Concatenating dataframes...")
    combined_df = pd.concat(all_dfs, ignore_index=True)
    
    # Save to CSV
    combined_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    print(f"Successfully created: {OUTPUT_PATH}")

if __name__ == "__main__":
    consolidate_inventory()
