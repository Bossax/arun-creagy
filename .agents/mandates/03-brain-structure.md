# Mandate: The ψ Directory Structure

This mandate defines the standardized architecture of the documentation system.

## The 8 Root Directories of ψ/

1. **inbox/**: Intake for system logs, reported issues, and received skills.
2. **memory/**: Categorized data, including identity files, patterns/learnings, retrospectives, and audit logs.
3. **incubate/**: Project-specific development space for drafts and sources.
4. **writing/**: Drafts, reports, and working documents.
5. **lab/**: Skill development. Contains project-based development folders (e.g., `ψ/lab/<project-slug>/`).
6. **learn/**: Reference materials and study resources.
7. **archive/**: Completed and versioned files, preserving project history. Treat the files as superseded.
8. **outbox/**: Finalized updates and deployments.

## Structure Rules
- **Directory Integrity**: The 8 root folders must always be present.
- **Persistence**: Data must be preserved; move completed items to `archive/` rather than deleting.
- **Isolation**: New skills or projects under development must reside in their own `ψ/lab/` subfolder.
