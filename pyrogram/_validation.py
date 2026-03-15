# Validasi di dalam Pyrogram: hanya boleh pakai build dari memekcode/pyrogram
# File ini ditempatkan di repo https://github.com/memekcode/pyrogram

import sys

_REQUIRED_REPO = "memekcode/pyrogram"
_REQUIRED_PACKAGE = "pyrogram"


def _check_pyrogram_source():
    try:
        from importlib.metadata import distribution, PackageNotFoundError
    except ImportError:
        from importlib_metadata import distribution, PackageNotFoundError

    try:
        dist = distribution(_REQUIRED_PACKAGE)
    except PackageNotFoundError:
        print(
            f"\n[ERROR] Pyrogram tidak valid!\n"
            f"Hanya berjalan dengan Pyrogram dari:\n"
            f"  https://github.com/{_REQUIRED_REPO}\n\n"
            f"Install: pip uninstall pyrogram -y && pip install git+https://github.com/{_REQUIRED_REPO}\n"
        )
        sys.exit(1)

    install_url = ""
    try:
        if hasattr(dist, "direct_url") and dist.direct_url is not None:
            install_url = str(dist.direct_url)
        elif hasattr(dist, "origin") and dist.origin is not None:
            install_url = str(dist.origin)
        else:
            from pathlib import Path
            base = getattr(dist, "_path", None)
            if base is None and dist.files:
                try:
                    first = next(iter(dist.files))
                    base = Path(first.locate()).parent if hasattr(first, "locate") else None
                except (StopIteration, OSError):
                    pass
            if base:
                direct_url_file = Path(base) / "direct_url.json"
                if direct_url_file.exists():
                    import json
                    with open(direct_url_file, encoding="utf-8") as fp:
                        data = json.load(fp)
                    install_url = data.get("url", "")
    except Exception:
        pass

    if install_url and _REQUIRED_REPO not in install_url:
        print(
            f"\n[ERROR] Pyrogram harus dari repository {_REQUIRED_REPO}!\n"
            f"Terdeteksi: {install_url}\n\n"
            f"Install ulang: pip uninstall pyrogram pyrogram -y && pip install git+https://github.com/{_REQUIRED_REPO}\n"
        )
        sys.exit(1)
