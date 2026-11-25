import json
from pathlib import Path


def load_input_bundle(root: Path) -> dict[str, dict]:
    """Read JSON files declared by the local data contract."""
    schema = json.loads((root / "data" / "schema.json").read_text(encoding="utf-8"))
    bundle = {}
    for filename, required_keys in schema["files"].items():
        payload = json.loads((root / "data" / filename).read_text(encoding="utf-8"))
        if not isinstance(payload, dict) or not set(required_keys).issubset(payload):
            raise ValueError(f"资料结构与契约不一致: {filename}")
        bundle[filename] = payload
    return bundle
