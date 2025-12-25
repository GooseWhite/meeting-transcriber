# Meeting Transcriber - Project Context

## Goal
Privacy-first meeting transcription tool for organisations that want control over their sensitive conversations.

## Why This Project
- Existing tools (Otter, Fireflies) send audio to external servers
- Organisations with sensitive information do not want this
- Local/self-hosted solution gives full control

## Target Users
- Organisations with privacy-sensitive meetings (legal, HR, finance)
- Organisations with compliance requirements (GDPR, healthcare)
- Teams that want meeting intelligence without vendor lock-in

## Technical Decisions

### Why faster-whisper
- 4x faster than original OpenAI Whisper
- Same quality, fewer resources
- Actively maintained, good community
- Easy Python integration

### Why Local First
- Proves privacy-first concept
- Easier to debug
- No cloud costs during development
- Scaling to Nebius later is a simple step

### Why Nebius for Cloud
- EU datacenters (GDPR compliant)
- Good GPU pricing
- Less vendor lock-in than AWS/Azure
- Fits privacy-first positioning

## Development Phases

### Phase 1 (MVP)
Focus: Working transcription of audio files
- Input: mp3/wav file
- Output: JSON with timestamps
- CLI interface
- Multi-language support

### Phase 2 (Enhanced)
Focus: Production-ready features
- Speaker diarization
- Real-time streaming
- Multiple export formats
- Docker container

### Phase 3 (Intelligence)
Focus: Adding value on top of transcription
- AI summaries
- Action item extraction
- Searchable archive

### Phase 4 (Scale)
Focus: Multi-user, cloud deployment
- REST API
- Nebius GPU instances
- Queue system
- Dashboard

## Open Questions
- [ ] Which Whisper model size as default? (base vs small vs medium)
- [ ] Speaker diarization: pyannote-audio or alternative?
- [ ] How to capture audio input for live meetings? (system audio capture)
- [ ] Pricing model for hosted version?

## Development Log

### 24-12-2024 - MVP Proof of Concept
**Status:** Working on Windows with CPU

**What works:**
- faster-whisper installation via pip
- FFmpeg installed via winget (Gyan.FFmpeg)
- Video transcription (mp4 to json)
- Dutch language detection (100% confidence)
- CLI with JSON/TXT/SRT output formats

**First test result:**
- Input: Custom GPTs 01.mp4 (5 min training video)
- Processing: ~3-4 minutes on CPU
- Output: 78 segments, correctly structured JSON
- Quality: Decent, but specific terms sometimes wrong (ChatGPT to JetGPT)

**Lessons learned:**
- Rich library has encoding issues on Windows terminal - use plain print()
- GPU mode does not work without full CUDA toolkit - CPU mode as stable default
- Base model is fast but lacks accuracy for jargon - test small/medium later

### 25-12-2024 - English + Export Formats Testing
**Status:** All Phase 1 features validated

**Test results:**
- EN transcription: NEW Beginning Video.mp4 (2 min, 95% confidence, 24 segments)
- TXT export: Works correctly (plain text)
- SRT export: Works correctly (subtitle format with timestamps)

**Conclusion:** MVP is feature-complete for Phase 1

### 25-12-2024 - GitHub Repository
**Status:** Repository created and pushed

- GitHub CLI installed
- Initial commit with all project files
- Public repo: https://github.com/GooseWhite/meeting-transcriber
- Documentation converted to English

**Next steps:**
- Phase 2: Speaker diarization
