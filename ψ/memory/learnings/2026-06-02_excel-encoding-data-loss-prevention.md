# Learning: Excel-to-CSV Encoding Corruption Trap (Thai Characters)

**Date**: 2026-06-02
**Context**: Pillar 3 Data Inventory Hardening (DCCE CRDB)
**Status**: [HARDENED]

## 1. The Pattern (The Trap)
When exporting data from Excel to CSV on a Windows system with English/Global locale settings, the standard **"CSV (Comma delimited) (*.csv)"** option (Windows-1252 or CP874) often **destroys** non-Latin characters (like Thai).

### The "Permanent Strip" Symptom:
- The bytes are physically replaced by literal question marks (`?`) in the file.
- **Critical**: This cannot be fixed by changing the decoder in Python or Notepad++ later. The data is gone.

## 2. The Solution (The Guardrail)
To ensure data fidelity for technical systems (DGA standards, Python pandas, etc.), users must use the **UTF-8 with BOM** export path:

1.  **File > Save As**
2.  Choose **"CSV UTF-8 (Comma delimited) (*.csv)"**. 
3.  Verification: Open the CSV in a HEX editor or use a Python probe. If you see `?` instead of Thai, re-export immediately.

## 3. Implementation in Oracle
Always use the **`utf-8-sig`** encoding when reading CSVs created by Excel. This correctly skips the Byte Order Mark (BOM) while preserving the multi-byte Thai characters.

```python
# The Auditor's Standard Read
df = pd.read_csv('catalog.csv', encoding='utf-8-sig')
```

## 4. Impact on Procurement
Artifacts delivered to vendors without this hardening will fail automated ingestion tests, causing delivery delays. Standardizing on **v3** (Hardened) ensures the system is "Procurement Ready."
