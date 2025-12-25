# Meeting Transcriber - Tasks

## Fase 1: Lokale MVP

### Setup & Core
- [x] Test faster-whisper installatie op Windows
- [x] Valideer GPU detectie (CUDA) - GPU niet beschikbaar, CPU fallback werkt
- [x] Test met sample audio files (NL) - Custom GPTs 01.mp4 succesvol
- [x] Test met EN audio - NEW Beginning Video.mp4 succesvol (95% confidence)
- [ ] Benchmark: snelheid vs audio lengte

### Features
- [x] Basis CLI werkt
- [x] JSON output correct
- [x] TXT export
- [x] SRT subtitle export
- [x] Language auto-detection werkt (100% confidence NL)

### Quality
- [ ] Error handling voor corrupte audio
- [x] Duidelijke error messages
- [x] Progress indicator tijdens processing

### Documentation
- [x] README setup instructies
- [ ] Example output file toevoegen

### Known Issues (24-12-2024)
- Rich library geeft encoding errors op Windows → opgelost met plain print()
- GPU mode vereist CUDA DLLs die niet aanwezig zijn → CPU mode als default
- Base model heeft fouten bij specifieke termen (ChatGPT → JetGPT, Zwitsers zakmes → Zwitserszak)
- Overweeg `small` of `medium` model voor betere accuracy

---

## Fase 2: Enhanced Features

### Speaker Diarization
- [ ] pyannote-audio integreren
- [ ] Speaker labels in output
- [ ] Test met multi-speaker audio

### Streaming
- [ ] Real-time audio capture onderzoeken
- [ ] Streaming transcriptie implementeren
- [ ] Latency meten en optimaliseren

### Export
- [ ] DOCX export
- [ ] VTT subtitle format
- [ ] Configurable timestamp format

### Containerization
- [ ] Dockerfile maken
- [ ] Docker Compose voor development
- [ ] GPU passthrough testen

---

## Fase 3: Meeting Intelligence

### AI Features
- [ ] LLM integratie voor samenvattingen
- [ ] Action item extractie prompt
- [ ] Key decisions herkenning

### Storage
- [ ] SQLite voor lokale opslag
- [ ] Search functionaliteit
- [ ] Meeting metadata

---

## Fase 4: Cloud Deployment

### Infrastructure
- [ ] Nebius account setup
- [ ] GPU instance configuratie
- [ ] Terraform/Pulumi scripts

### API
- [ ] FastAPI endpoints
- [ ] Authentication
- [ ] Rate limiting
- [ ] File upload handling

### Queue
- [ ] Redis setup
- [ ] Celery workers
- [ ] Job status tracking

### Monitoring
- [ ] Logging naar centrale plek
- [ ] Performance metrics
- [ ] Error alerting
