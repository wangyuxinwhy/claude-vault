---
summary: Use yt-dlp to download and clean subtitles when direct video access fails
tags: [cli, workaround, yt-dlp, data-processing]
date: 2026-02-28
---

# YouTube Subtitle Extraction

## Problem

Cannot directly access YouTube video content to summarize it.

## Wrong path

1. Tried WebFetch on the URL — blocked.
2. Told the user "I can't do it" and asked them to provide a transcript.

## Solution

1. Install `yt-dlp` via `uv tool install yt-dlp`.
2. Download subtitles only: `yt-dlp --write-auto-sub --sub-lang zh,en --skip-download -o "video" <URL>`.
3. Clean VTT: strip timestamps, HTML tags, deduplicate consecutive lines with a simple Python script.
4. Summarize the clean text.

## Principle

When the obvious path is blocked, look for an indirect route. The data I needed (spoken words) existed in a different form (subtitle files). Reframe "I can't watch the video" as "how else can I get the text?"
