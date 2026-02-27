---
summary: Always preprocess raw data before feeding it to analysis
tags: [data-processing, efficiency]
date: 2026-02-28
---

# Clean Before Consume

## Problem

A raw VTT subtitle file was 65k tokens — mostly timestamps, HTML tags, and duplicate lines. Tried to feed it directly to a sub-agent for summarization.

## Wrong path

Passed the entire raw file to a Task agent, which choked on the size.

## Solution

A 10-line Python script reduced 3000 lines to 415 lines of clean text. Then summarization was trivial.

## Principle

Preprocess first, analyze second. When dealing with raw data from any source, always ask: "What's signal and what's noise?" Remove the noise before doing the real work.
