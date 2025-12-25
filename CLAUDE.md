# CLAUDE.md - Meeting Transcriber

## Project Overzicht
Privacy-first meeting transcriptie tool. Lokaal draaien, geen externe API calls, volledige controle over bedrijfsdata.

## Tech Stack
- **Core:** Python 3.10+, faster-whisper
- **CLI:** Click, Rich
- **Future API:** FastAPI
- **Future Cloud:** Nebius (EU GPU instances)

## Belangrijke Files
- `transcribe.py` - Main CLI tool
- `requirements.txt` - Dependencies
- `dev-docs/context.md` - Project context en beslissingen
- `dev-docs/tasks.md` - Taken per fase

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

## Huidige Fase
**Fase 1: Lokale MVP** - Focus op werkende batch transcriptie

## Conventies
- Output altijd als JSON met metadata
- Timestamps in seconden (float)
- Language codes: ISO 639-1 (nl, en, de, etc.)
- Errors via Rich console, niet via exceptions naar user

## Privacy Principes
- Geen telemetry
- Geen externe API calls
- Audio files niet opslaan na processing (default)
- Alle processing lokaal of eigen infrastructure
