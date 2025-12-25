# CLAUDE.md - Meeting Transcriber

## Project Overview
Privacy-first meeting transcription tool. Runs locally, no external API calls, full control over business data.

## Tech Stack
- **Core:** Python 3.10+, faster-whisper
- **CLI:** Click
- **Future API:** FastAPI
- **Future Cloud:** Nebius (EU GPU instances)

## Key Files
- `transcribe.py` - Main CLI tool
- `requirements.txt` - Dependencies
- `dev-docs/context.md` - Project context and decisions
- `dev-docs/tasks.md` - Tasks per phase

## Development Commands

```bash
# Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run transcription
python transcribe.py audio.mp3
python transcribe.py audio.mp3 --output result.json
python transcribe.py audio.mp3 --language nl --format srt
```

## Current Phase
**Phase 1: Local MVP** - Focus on working batch transcription

## Conventions
- Output always as JSON with metadata
- Timestamps in seconds (float)
- Language codes: ISO 639-1 (nl, en, de, etc.)
- Errors via console print, not exceptions to user

## Privacy Principles
- No telemetry
- No external API calls
- Audio files not stored after processing (default)
- All processing local or own infrastructure
