# Meeting Transcriber - Tasks

## Phase 1: Local MVP

### Setup and Core
- [x] Test faster-whisper installation on Windows
- [x] Validate GPU detection (CUDA) - GPU not available, CPU fallback works
- [x] Test with sample audio files (NL) - Custom GPTs 01.mp4 successful
- [x] Test with EN audio - NEW Beginning Video.mp4 successful (95% confidence)
- [ ] Benchmark: speed vs audio length

### Features
- [x] Basic CLI works
- [x] JSON output correct
- [x] TXT export
- [x] SRT subtitle export
- [x] Language auto-detection works (100% confidence NL)

### Quality
- [ ] Error handling for corrupt audio
- [x] Clear error messages
- [x] Progress indicator during processing

### Documentation
- [x] README setup instructions
- [x] GitHub repository created
- [ ] Add example output file

### Known Issues (24-12-2024)
- Rich library gives encoding errors on Windows - solved with plain print()
- GPU mode requires CUDA DLLs that are not present - CPU mode as default
- Base model has errors with specific terms (ChatGPT to JetGPT)
- Consider small or medium model for better accuracy

---

## Phase 2: Enhanced Features

### Speaker Diarization
- [ ] Integrate pyannote-audio
- [ ] Speaker labels in output
- [ ] Test with multi-speaker audio

### Streaming (priority)
- [ ] Step A: Mic capture with PyAudio
- [ ] Step A: Real-time transcription in chunks
- [ ] Step A: Test latency and accuracy
- [ ] Step B: System audio capture (virtual audio driver)
- [ ] Step B: Capture Zoom/Teams audio
- [ ] Measure and optimise latency

### Export
- [ ] DOCX export
- [ ] VTT subtitle format
- [ ] Configurable timestamp format

### Containerisation
- [ ] Create Dockerfile
- [ ] Docker Compose for development
- [ ] Test GPU passthrough

---

## Phase 3: Meeting Intelligence

### AI Features
- [ ] LLM integration for summaries
- [ ] Action item extraction prompt
- [ ] Key decisions recognition

### Storage
- [ ] SQLite for local storage
- [ ] Search functionality
- [ ] Meeting metadata

---

## Phase 4: Cloud Deployment

### Infrastructure
- [ ] Nebius account setup
- [ ] GPU instance configuration
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
- [ ] Centralised logging
- [ ] Performance metrics
- [ ] Error alerting
