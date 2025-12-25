# Meeting Transcriber - Project Context

## Doel
Privacy-first meeting transcriptie tool voor bedrijven die controle willen over hun gevoelige gesprekken.

## Waarom dit project
- Bestaande tools (Otter, Fireflies) sturen audio naar externe servers
- Bedrijven met gevoelige informatie willen dit niet
- Lokale/eigen-server oplossing geeft volledige controle

## Target Users
- Bedrijven met privacy-gevoelige meetings (legal, HR, finance)
- Organisaties met compliance eisen (GDPR, healthcare)
- Teams die meeting intelligence willen zonder vendor lock-in

## Technische Keuzes

### Waarom faster-whisper
- 4x sneller dan originele OpenAI Whisper
- Zelfde kwaliteit, minder resources
- Actief onderhouden, goede community
- Makkelijke Python integratie

### Waarom lokaal eerst
- Bewijst privacy-first concept
- Makkelijker te debuggen
- Geen cloud kosten tijdens development
- Later schalen naar Nebius is simpele stap

### Waarom Nebius voor cloud
- EU datacenters (GDPR compliant)
- Goede GPU pricing
- Minder vendor lock-in dan AWS/Azure
- Past bij privacy-first positionering

## Ontwikkel Fases

### Fase 1 (MVP)
Focus: Werkende transcriptie van audio files
- Input: mp3/wav file
- Output: JSON met timestamps
- CLI interface
- Multi-language support

### Fase 2 (Enhanced)
Focus: Productie-waardige features
- Speaker diarization
- Real-time streaming
- Meerdere export formaten
- Docker container

### Fase 3 (Intelligence)
Focus: Waarde toevoegen bovenop transcriptie
- AI samenvattingen
- Action item extractie
- Doorzoekbaar archief

### Fase 4 (Scale)
Focus: Multi-user, cloud deployment
- REST API
- Nebius GPU instances
- Queue systeem
- Dashboard

## Open Vragen
- [ ] Welk Whisper model size als default? (base vs small vs medium)
- [ ] Speaker diarization: pyannote-audio of alternatief?
- [ ] Hoe audio input bij live meetings? (system audio capture)
- [ ] Pricing model voor hosted versie?

## Development Log

### 24-12-2024 - MVP Proof of Concept
**Status:** Werkend op Windows met CPU

**Wat werkt:**
- faster-whisper installatie via pip
- FFmpeg geïnstalleerd via winget (Gyan.FFmpeg)
- Video transcriptie (mp4 → json)
- Nederlandse taaldetectie (100% confidence)
- CLI met JSON/TXT/SRT output formats

**Eerste test resultaat:**
- Input: Custom GPTs 01.mp4 (5 min training video)
- Processing: ~3-4 minuten op CPU
- Output: 78 segmenten, correct gestructureerde JSON
- Kwaliteit: Redelijk, maar specifieke termen worden soms verkeerd (ChatGPT → JetGPT)

**Geleerde lessen:**
- Rich library heeft encoding issues op Windows terminal → plain print() gebruiken
- GPU mode werkt niet zonder volledige CUDA toolkit → CPU als stabiele default
- Base model is snel maar mist accuracy voor jargon → test small/medium later

**Volgende sessie:**
- Test met Engels audio
- Probeer `small` model voor betere kwaliteit
- GitHub repo initialiseren

### 25-12-2024 - Engels + export formats testen
**Status:** Alle Fase 1 features gevalideerd

**Test resultaten:**
- EN transcriptie: NEW Beginning Video.mp4 (2 min, 95% confidence, 24 segmenten)
- TXT export: Werkt correct (platte tekst)
- SRT export: Werkt correct (subtitle formaat met timestamps)

**Conclusie:** MVP is feature-complete voor Fase 1

**Volgende sessie:**
- GitHub repo initialiseren
