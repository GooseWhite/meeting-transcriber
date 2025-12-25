# Meeting Transcriber

Privacy-first meeting transcriptie tool die gesproken audio omzet naar doorzoekbare tekst.
Gebouwd voor bedrijven die controle willen over hun data.

## Visie

Een complete meeting intelligence oplossing die:
- Live meetings transcribeert in real-time
- Werkt in 50+ talen met automatische detectie
- Sprekers herkent en labelt (speaker diarization)
- Samenvattingen en action items genereert
- Volledig privacy-compliant draait (geen externe API calls)

## Roadmap

### Fase 1: Lokale Transcriptie Engine (current)
- [x] Project structuur
- [ ] Faster-whisper integratie
- [ ] Audio file transcriptie (batch)
- [ ] Multi-language support
- [ ] JSON output met timestamps
- [ ] CLI interface

### Fase 2: Enhanced Features
- [ ] Speaker diarization (wie zegt wat)
- [ ] Real-time streaming transcriptie
- [ ] Automatische taaldetectie per segment
- [ ] Export formaten (SRT, VTT, TXT, DOCX)

### Fase 3: Meeting Intelligence
- [ ] AI-powered samenvattingen
- [ ] Action item extractie
- [ ] Zoeken in transcripts
- [ ] Meeting analytics dashboard

### Fase 4: Schaalbare Deployment
- [ ] Docker containerisatie
- [ ] GitHub CI/CD pipeline
- [ ] Nebius GPU cloud deployment
- [ ] REST API voor integraties
- [ ] Multi-user support met queue systeem

## Tech Stack

| Component | Technologie | Waarom |
|-----------|-------------|--------|
| Speech-to-Text | faster-whisper | Snelste lokale Whisper implementatie |
| Speaker Diarization | pyannote-audio | State-of-the-art speaker detection |
| Backend | Python / FastAPI | Simpel, async, goed ecosysteem |
| Queue | Redis + Celery | Schaalbare job processing |
| Storage | SQLite → PostgreSQL | Lokaal simpel, cloud schaalbaar |
| Deployment | Docker + Nebius | GPU cloud met EU data residency |

## Vereisten

### Minimum (batch processing)
- Python 3.10+
- 8GB RAM
- Elk modern systeem (Windows/Mac/Linux)

### Aanbevolen (real-time)
- NVIDIA GPU met 4GB+ VRAM
- CUDA 11.8+
- 16GB RAM

## Quick Start

```bash
# Clone repository
git clone https://github.com/stapje-slimmer/meeting-transcriber.git
cd meeting-transcriber

# Setup environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Transcribeer een audio file
python transcribe.py path/to/meeting.mp3
```

## Output Voorbeeld

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
      "text": "Goedemorgen allemaal, laten we beginnen met de agenda.",
      "speaker": "Speaker 1",
      "confidence": 0.92
    },
    {
      "start": 4.5,
      "end": 8.1,
      "text": "Thanks for joining. First item is the Q4 review.",
      "speaker": "Speaker 2",
      "confidence": 0.89,
      "language": "en"
    }
  ]
}
```

## Privacy & Security

- **Zero external calls**: Alle processing gebeurt lokaal of op eigen infrastructure
- **No data retention**: Audio wordt niet opgeslagen na processing (tenzij expliciet gewenst)
- **EU data residency**: Cloud deployment via Nebius met EU datacenters
- **Audit logging**: Alle acties worden gelogd voor compliance

## Licentie

MIT License - Zie [LICENSE](LICENSE)

## Contact

Gebouwd door [Stapje Slimmer](https://stapjeslimmer.nl)
Vragen? guuswitjes@gmail.com
