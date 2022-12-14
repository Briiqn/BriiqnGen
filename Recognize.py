import os
import pathlib

import whisper


def transcribe(audio : str, model_name: str ):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio)
    return str(result["text"])

