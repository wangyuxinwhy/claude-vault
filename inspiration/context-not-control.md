---
summary: Give AI context to make good decisions, not rules to restrict its behavior
tags: [ai, philosophy, design]
date: 2026-02-28
---

# Context, Not Control

When AI makes mistakes, the instinct is to add constraints — specs, checklists, guardrails, formal verification. This is control.

The alternative: give better context and trust the AI to reason correctly. This is context.

Control scales poorly. Every new constraint adds maintenance burden and assumes the AI can't improve. Context scales well — as models get smarter, the same context produces better outcomes.

Examples:
- "Think twice, code once" (context) vs a 10-step pre-flight checklist (control)
- Minimal diff culture in training data (context) vs preservation property tests (control)
- Explaining why a design choice matters (context) vs lint rules enforcing it (control)

Bet on AI getting smarter. Build for context.
