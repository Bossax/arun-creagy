import pandas as pd
import os
import sys

# Define absolute paths based on Environment Context
BASE_PATH = r"C:\Users\sitth\OracleWorkspace\Arun_Creagy\ψ\incubate\DCCE\CRI\data_system"
DDPM_STAT_PATH = os.path.join(BASE_PATH, "data", "1_silver", "ddpm", "master_village_disaster_stat_2557_2567.csv")
HAZARD_DIM_PATH = os.path.join(BASE_PATH, "data", "2_gold", "dim_hazard_canonical.csv")
OUTPUT_PATH = os.path.join(BASE_PATH, "data", "1_silver", "ddpm", "tambon_climate_affected_household_aggregate_ddpm_village_stat.csv")

def main():
    print("--- DDPM Climate Filter & Aggregation ---")
    
    if not os.path.exists(DDPM_STAT_PATH):
        print(f"Error: Input file not found at {DDPM_STAT_PATH}")
        sys.exit(1)
        
    if not os.path.exists(HAZARD_DIM_PATH):
        print(f"Error: Hazard dimension file not found at {HAZARD_DIM_PATH}")
        sys.exit(1)

    print(f"Reading DDPM stats: {DDPM_STAT_PATH}")
    # Using utf-8 as sample showed correct Thai characters in shell
    try:
        df_ddpm = pd.read_csv(DDPM_STAT_PATH, encoding='utf-8')
    except UnicodeDecodeError:
        print("UTF-8 decode failed, trying cp874 (Thai Windows)...")
        df_ddpm = pd.read_csv(DDPM_STAT_PATH, encoding='cp874')

    print(f"Reading Hazard Dimension: {HAZARD_DIM_PATH}")
    df_hazard = pd.read_csv(HAZARD_DIM_PATH, encoding='utf-8')

    # 1. Map DDPM 'Disaster Type' to Canonical Hazard Names
    # DDPM names observed: ภัยแล้ง, อุทกภัย, วาตภัย, ดินโคลนถล่ม, ดินโคลนถล่ม/ดินถล่ม
    # Canonical names: ภัยแล้ง, อุทกภัย, วาตภัย, ดินถล่ม
    name_mapping = {
        'ดินโคลนถล่ม': 'ดินถล่ม',
        'ดินโคลนถล่ม/ดินถล่ม': 'ดินถล่ม'
    }
    df_ddpm['canonical_hazard_name_th_mapped'] = df_ddpm['Disaster Type'].str.strip().replace(name_mapping)

    # Join DDPM stats with dim_hazard_canonical.csv
    print("Joining with canonical hazard dimension...")
    df_joined = df_ddpm.merge(
        df_hazard,
        left_on='canonical_hazard_name_th_mapped',
        right_on='canonical_hazard_name_th',
        how='left'
    )

    # 2. Filter for climate-related hazards (Flood, Storm, Drought, Dry Spell, Landslide)
    # Based on canonical codes: FLOOD, WINDSTORM, DROUGHT, DRY_SPELL, LANDSLIDE
    climate_codes = ['FLOOD', 'WINDSTORM', 'DROUGHT', 'DRY_SPELL', 'LANDSLIDE']
    df_climate = df_joined[df_joined['canonical_hazard_code'].isin(climate_codes)].copy()
    
    initial_count = len(df_ddpm)
    filtered_count = len(df_climate)
    print(f"Filtered {filtered_count} climate-related records (from {initial_count} total).")

    # 3. Clean and Prepare for Aggregation
    # Convert 'Affected Households' to numeric, handling potential strings/commas
    if df_climate['Affected Households'].dtype == object:
        df_climate['Affected Households'] = df_climate['Affected Households'].str.replace(',', '', regex=False)
    
    df_climate['Affected Households'] = pd.to_numeric(df_climate['Affected Households'], errors='coerce').fillna(0)

    # Format 'Subdistrict Code' to canonical 6-digit string
    # Handle floats (e.g., 332204.0) by stripping '.0' and whitespace
    df_climate['subdistrict_code'] = (
        df_climate['Subdistrict Code']
        .astype(str)
        .str.replace(r'\.0$', '', regex=True)
        .str.strip()
        .str.zfill(6)
    )
    
    # Filter out invalid/dummy codes (e.g., '000000', 'nan')
    df_climate = df_climate[~df_climate['subdistrict_code'].isin(['000000', 'nan', ''] )]
    
    # Extract province_code from Subdistrict Code (first 2 digits)
    df_climate['province_code'] = df_climate['subdistrict_code'].str[:2]

    # 4. Aggregate 'Affected Households' to the canonical 6-digit 'subdistrict_code'
    # We group by province_code and subdistrict_code to ensure smooth joins in the analysis phase.
    print("Aggregating historical impact...")
    agg_df = df_climate.groupby(['province_code', 'subdistrict_code']).agg({
        'Affected Households': 'sum'
    }).reset_index()

    # Rename column for clarity in the Gold/Silver layer
    agg_df = agg_df.rename(columns={'Affected Households': 'historical_affected_households_sum'})

    # 5. Output Results
    print(f"Saving aggregate to: {OUTPUT_PATH}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Using utf-8-sig for Excel compatibility in Thai environment
    agg_df.to_csv(OUTPUT_PATH, index=False, encoding='utf-8-sig')
    
    print("Success: DDPM Climate History Prepared.")

if __name__ == "__main__":
    main()
