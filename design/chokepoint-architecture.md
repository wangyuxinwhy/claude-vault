---
summary: A single convergence point in a system enables elegant interception, monitoring, and extension
tags: [architecture, design-pattern]
date: 2026-02-28
---

# Chokepoint Architecture

When all traffic in a system passes through a single point, that point becomes a powerful lever for interception, monitoring, and extension.

## Example: IPython's DisplayPublisher

Every visualization library (matplotlib, plotly, pandas) outputs through `DisplayPublisher.publish()`. GoFigr wraps this one method to capture all plots — one line of code, universal coverage.

This works because IPython chose the right abstraction level: MIME type dictionaries. Not too low (pixels), not too high (specific chart types). Libraries implement `_repr_html_()` or `_repr_png_()` via duck typing — zero coupling, zero inheritance.

## Counterexample: R's graphics devices

R has no chokepoint. Graphics devices are C-level callback structs (line, rect, text). Each library writes directly to the device. GoFigr can't intercept at one point, so they chose explicit `publish()` calls instead of faking automatic capture.

## When to design chokepoints

A chokepoint is valuable when:
- Multiple producers need to reach multiple consumers
- You want to add cross-cutting concerns (logging, caching, interception) later
- The data flowing through can be represented in a uniform format

A chokepoint is harmful when:
- It becomes a bottleneck (performance)
- It forces lossy abstraction (R's primitives lose semantic info about chart types)
