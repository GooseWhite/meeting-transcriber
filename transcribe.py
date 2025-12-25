"""
Meeting Transcriber - Lokale speech-to-text met privacy-first aanpak

Usage:
    python transcribe.py <audio_file> [--output <output_file>] [--language <lang>]

Examples:
    python transcribe.py meeting.mp3
    python transcribe.py meeting.wav --output transcript.json
    python transcribe.py meeting.mp3 --language nl
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import click


def load_model(model_size: str = "base", force_cpu: bool = False):
    """Load the Whisper model. Downloads on first use."""
    from faster_whisper import WhisperModel

    if force_cpu:
        print("Running on CPU mode")
        return WhisperModel(model_size, device="cpu", compute_type="int8")

    # Try GPU first, fall back to CPU
    try:
        import torch
        if torch.cuda.is_available():
            model = WhisperModel(model_size, device="cuda", compute_type="float16")
            print("GPU mode enabled")
            return model
    except Exception:
        pass

    print("Running on CPU (no CUDA available)")
    return WhisperModel(model_size, device="cpu", compute_type="int8")


def transcribe_audio(audio_path: Path, language: str | None = None, force_cpu: bool = True) -> dict:
    """
    Transcribe audio file to structured output.

    Args:
        audio_path: Path to audio file (mp3, wav, m4a, etc.)
        language: Optional language code (nl, en, de, etc.). Auto-detects if None.
        force_cpu: Force CPU mode (default True for stability on Windows).

    Returns:
        Dictionary with metadata and transcript segments
    """
    print("Loading model...")
    model = load_model("base", force_cpu=force_cpu)

    print("Transcribing audio... (this may take a while)")
    segments, info = model.transcribe(
        str(audio_path),
        language=language,
        beam_size=5,
        word_timestamps=True,
    )

    # Process segments
    transcript_segments = []
    segment_count = 0
    for segment in segments:
        transcript_segments.append({
            "start": round(segment.start, 2),
            "end": round(segment.end, 2),
            "text": segment.text.strip(),
            "confidence": round(segment.avg_logprob, 2) if segment.avg_logprob else None,
        })
        segment_count += 1
        if segment_count % 10 == 0:
            print(f"  Processed {segment_count} segments...")

    return {
        "metadata": {
            "filename": audio_path.name,
            "duration_seconds": round(info.duration, 1),
            "language": info.language,
            "language_confidence": round(info.language_probability, 2),
            "processed_at": datetime.now().isoformat(),
            "model": "faster-whisper-base",
        },
        "segments": transcript_segments,
        "full_text": " ".join(s["text"] for s in transcript_segments),
    }


@click.command()
@click.argument("audio_file", type=click.Path(exists=True, path_type=Path))
@click.option(
    "--output", "-o",
    type=click.Path(path_type=Path),
    help="Output file path (default: <input_name>.json)"
)
@click.option(
    "--language", "-l",
    type=str,
    default=None,
    help="Language code (nl, en, de, etc.). Auto-detects if not specified."
)
@click.option(
    "--format", "-f",
    type=click.Choice(["json", "txt", "srt"]),
    default="json",
    help="Output format"
)
def main(audio_file: Path, output: Path | None, language: str | None, format: str):
    """Transcribe an audio file to text."""

    print(f"\n=== Meeting Transcriber ===")
    print(f"Input: {audio_file}\n")

    # Run transcription
    result = transcribe_audio(audio_file, language)

    # Determine output path
    if output is None:
        output = audio_file.with_suffix(f".{format}")

    # Write output
    if format == "json":
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    elif format == "txt":
        output.write_text(result["full_text"], encoding="utf-8")
    elif format == "srt":
        srt_content = generate_srt(result["segments"])
        output.write_text(srt_content, encoding="utf-8")

    # Summary
    print(f"\n=== Done ===")
    print(f"Language: {result['metadata']['language']} ({result['metadata']['language_confidence']:.0%} confidence)")
    print(f"Duration: {result['metadata']['duration_seconds']}s")
    print(f"Segments: {len(result['segments'])}")
    print(f"Output: {output}")


def generate_srt(segments: list[dict]) -> str:
    """Generate SRT subtitle format from segments."""
    lines = []
    for i, seg in enumerate(segments, 1):
        start = format_timestamp_srt(seg["start"])
        end = format_timestamp_srt(seg["end"])
        lines.append(f"{i}")
        lines.append(f"{start} --> {end}")
        lines.append(seg["text"])
        lines.append("")
    return "\n".join(lines)


def format_timestamp_srt(seconds: float) -> str:
    """Convert seconds to SRT timestamp format (HH:MM:SS,mmm)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


if __name__ == "__main__":
    main()
