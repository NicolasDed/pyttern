from .python_processor import PythonProcessor
from .java_processor import JavaProcessor

def get_processor(lang):
    if lang == 'python':
        return PythonProcessor.get_instance()
    elif lang == 'java':
        return JavaProcessor.get_instance()
    else:
        raise ValueError(f"Unsupported language: {lang}")