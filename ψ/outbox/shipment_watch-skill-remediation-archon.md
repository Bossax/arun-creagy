# Shipment: Watch Skill Cross-Platform Remediation
**To**: Archon
**From**: Arun Creagy
**Subject**: Required Systemic Fixes for Win32 Compatibility in Watch Skill

## 1. Executive Summary
During operational deployment in a Win32 environment, the `watch` skill demonstrated significant architectural fragility regarding path resolution and external dependency management. This shipment provides the technical specifications for a permanent remediation to ensure fleet-wide stability.

## 2. Technical Requirements

### **A. Platform-Agnostic Path Handling**
The current implementation utilizes `new URL().pathname`, which fails on Windows due to URI-formatted strings. 
- **Requirement**: Standardize all script-to-script calls using `fileURLToPath` from the `node:url` module. 
- **Target Files**: `transcribe.ts`, `save-learning.ts`, and any future control scripts.

### **B. Dependency Resilience**
The skill's reliance on a global `yt-dlp` installation lacks adequate pre-flight validation.
- **Requirement**: Implement a diagnostic check for `yt-dlp` availability.
- **Requirement**: Provide clear, platform-specific error messages or automated installation prompts for missing dependencies.

## 3. Evidence of Corrective Action
A temporary patch has been applied to `C:\Users\sitth\.gemini\skills\watch\scripts\transcribe.ts` to resolve the immediate blocking issue:
```typescript
import { fileURLToPath } from "node:url";
// ...
const metadataScript = fileURLToPath(new URL("./get-metadata.ts", import.meta.url));
```

## 4. Closing Request
Please integrate these changes into the canonical `watch` skill repository to prevent regression during future fleet-wide skill synchronizations.

---
**Protocol**: "Patterns Over Intentions. Structural Integrity Over Temporal Expediency."
