import pandas as pd
import os

# Use absolute paths for Windows stability
BASE_DIR = r"C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system\data"

def audit_gold_gaps(file_path, metric_cols, name):
    print(f"\n{'='*20} AUDIT: {name} {'='*20}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    
    df = pd.read_csv(file_path, low_memory=False)
    total_rows = len(df)
    
    print(f"[1] METRIC QUALITY (Total Records: {total_rows:,})")
    for col in metric_cols:
        zeros = (df[col] == 0).sum()
        nulls = df[col].isna().sum()
        print(f"Column '{col:15}': Zeros={zeros:8,} ({ (zeros/total_rows)*100:6.2f}%) | Nulls={nulls:8,} ({ (nulls/total_rows)*100:6.2f}%)")
    
    # Coverage check
    if 'year_be' in df.columns:
        print(f"\n[2] TEMPORAL RANGE: {df['year_be'].min()} - {df['year_be'].max()}")
        
    if 'location_id' in df.columns:
        p_codes = df['location_id'].astype(str).str.zfill(8).str[:2].unique()
        print(f"[3] SPATIAL COVERAGE: {len(p_codes)} Provinces represented.")

def audit_tei_pilot(file_path, name):
    print(f"\n{'='*20} AUDIT: TEI PILOT ({name}) {'='*20}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
        
    df = pd.read_csv(file_path)
    print(f"Total Provinces in Pilot: {len(df['province_name_th'].unique())}")
    
    # Check for name alignment issues (e.g. Krung Thep)
    bkk_variants = df[df['province_name_th'].str.contains('กรุงเทพ', na=False)]['province_name_th'].unique()
    print(f"Bangkok naming variant in Pilot: {bkk_variants}")

def main():
    impact_path = os.path.join(BASE_DIR, '2_gold', 'fact_impact.csv')
    relief_path = os.path.join(BASE_DIR, '2_gold', 'fact_relief.csv')
    tei_casualties = os.path.join(BASE_DIR, '0_bronze', 'tei_pilot', 'casualties_by_hazard_2559_2566.csv')
    tei_relief = os.path.join(BASE_DIR, '0_bronze', 'tei_pilot', 'relief_by_hazard_2559_2566.csv')

    audit_gold_gaps(impact_path, ['deaths', 'affected'], "GOLD FACT IMPACT")
    audit_gold_gaps(relief_path, ['amount_approved_baht'], "GOLD FACT RELIEF")
    
    audit_tei_pilot(tei_casualties, "Casualties")
    audit_tei_pilot(tei_relief, "Relief")

if __name__ == "__main__":
    main()
