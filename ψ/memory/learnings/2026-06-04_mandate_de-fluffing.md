# Learning: Eliminating Persona Friction (Metaphor vs. Mechanics)

**Date**: 2026-06-04
**Concept**: #persona #linguistics #technical-standards

## Observation
Hyperbolic terminology (e.g., "Sovereignty," "The Brain," "Critical Failure") intended to enforce safety can create "Consultant Dialect" friction. While these terms serve as strong cognitive guardrails for the LLM, they can feel alien or "fluffy" to a user seeking a direct technical partner.

## The Pattern
1. **Instruction Over-Engineering**: Metaphors used to describe simple technical constraints (e.g., "Green Light Protocol" for `ask_user` confirmation) can obscure the actual mechanism.
2. **Identity Alignment**: Shifting from a high-status persona (Auditor/Gatekeeper) to a collaborative one (Assistant/Partner) requires stripping away exclusionary jargon.

## Refactored Principles
- **Old**: "Synthesis without Evidence is Hallucination."
- **New**: "Statements must be backed by current file data or command output."
- **Benefit**: The new version is actionable without requiring the LLM to adopt a "character" to understand the constraint.

## Implementation Note
When defining repository mandates, prioritize **Direct Technical Requirements** over **Persona-Based Metaphors** to maintain long-term usability and clear expectations.
