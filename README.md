# Meeting Transcriber

Privacy-first meeting transcription tool that converts spoken audio to searchable text.
Built for organisations that want full control over their data.

## Vision

A complete meeting intelligence solution that:
- Transcribes live meetings in real-time
- Works in 50+ languages with automatic detection
- Recognises and labels speakers (speaker diarization)
- Generates summaries and action items
- Runs fully privacy-compliant (no external API calls)

## Roadmap

### Phase 1: Local Transcription Engine (current)
- [x] Project structure
- [x] Faster-whisper integration
- [x] Audio file transcription (batch)
- [x] Multi-language support
- [x] JSON output with timestamps
- [x] CLI interface

### Phase 2: Enhanced Features
- [ ] Speaker diarization (who says what)
- [ ] Real-time streaming transcription
- [ ] Automatic language detection per segment
- [ ] Export formats (SRT, VTT, TXT, DOCX)

### Phase 3: Meeting Intelligence
- [ ] AI-powered summaries
- [ ] Action item extraction
- [ ] Transcript search
- [ ] Meeting analytics dashboard

### Phase 4: Scalable Deployment
- [ ] Docker containerisation
- [ ] GitHub CI/CD pipeline
- [ ] Nebius GPU cloud deployment
- [ ] REST API for integrations
- [ ] Multi-user support with queue system

## Tech Stack

| Component | Technology | Why |
|-----------|------------|-----|
| Speech-to-Text | faster-whisper | Fastest local Whisper implementation |
| Speaker Diarization | pyannote-audio | State-of-the-art speaker detection |
| Backend | Python / FastAPI | Simple, async, good ecosystem |
| Queue | Redis + Celery | Scalable job processing |
| Storage | SQLite - PostgreSQL | Local simple, cloud scalable |
| Deployment | Docker + Nebius | GPU cloud with EU data residency |

## Requirements

### Minimum (batch processing)
- Python 3.10+
- 8GB RAM
- Any modern system (Windows/Mac/Linux)

### Recommended (real-time)
- NVIDIA GPU with 4GB+ VRAM
- CUDA 11.8+
- 16GB RAM

## Quick Start

```bash
# Clone repository
git clone https://github.com/GooseWhite/meeting-transcriber.git
cd meeting-transcriber

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Transcribe an audio file
python transcribe.py path/to/meeting.mp3
```

## Output Example

```json
{
  "metadata": {
    "filename": "meeting.mp3",
    "duration_seconds": 1847,
    "language": "nl",
    "language_confidence": 0.94,
    "processed_at": "2024-12-24T10:30:00Z"
  },
  "segments": [
    {
      "start": 0.0,
      "end": 4.2,
      "text": "Good morning everyone, let us start with the agenda.",
      "speaker": "Speaker 1",
      "confidence": 0.92
    },
    {
      "start": 4.5,
      "end": 8.1,
      "text": "Thanks for joining. First item is the Q4 review.",
      "speaker": "Speaker 2",
      "confidence": 0.89
    }
  ]
}
```

## Privacy and Security

- **Zero external calls**: All processing happens locally or on your own infrastructure
- **No data retention**: Audio is not stored after processing (unless explicitly requested)
- **EU data residency**: Cloud deployment via Nebius with EU datacenters
- **Audit logging**: All actions are logged for compliance

## Licence

MIT License - See [LICENSE](LICENSE)

## Contact

Built by [Stapje Slimmer](https://stapjeslimmer.nl)
Questions? guuswitjes@gmail.com
