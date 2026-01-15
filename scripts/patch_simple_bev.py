#!/usr/bin/env python3
import argparse
from pathlib import Path
import re


def patch_vox(repo_root: Path) -> bool:
    path = repo_root / "utils" / "vox.py"
    if not path.exists():
        raise FileNotFoundError(f"vox.py not found at: {path}")
    text = path.read_text(encoding="utf-8")

    replacements = {
        "-self.XMIN-vox_size_X/2.0": "float(-self.XMIN-vox_size_X/2.0)",
        "-self.YMIN-vox_size_Y/2.0": "float(-self.YMIN-vox_size_Y/2.0)",
        "-self.ZMIN-vox_size_Z/2.0": "float(-self.ZMIN-vox_size_Z/2.0)",
        "1./vox_size_X": "float(1./vox_size_X)",
        "1./vox_size_Y": "float(1./vox_size_Y)",
        "1./vox_size_Z": "float(1./vox_size_Z)",
    }

    changed = False
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
            changed = True

    if changed:
        path.write_text(text, encoding="utf-8")
    return changed


def patch_vis(repo_root: Path) -> bool:
    path = repo_root / "vis_nuscenes.py"
    if not path.exists():
        raise FileNotFoundError(f"vis_nuscenes.py not found at: {path}")
    text = path.read_text(encoding="utf-8")

    new_text = re.sub(
        r"^(\s*)poly_names, line_names, lmap = fetch_nusc_map2.*",
        r"\1poly_names, line_names, lmap = [], [], None",
        text,
        flags=re.MULTILINE,
    )
    new_text = re.sub(
        r"^(\s*)draw_occ_map_custom.*",
        r"\1pass",
        new_text,
        flags=re.MULTILINE,
    )

    changed = new_text != text
    if changed:
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        default="simple_bev",
        help="Path to the cloned simple_bev repository",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo).resolve()
    if not repo_root.exists():
        raise FileNotFoundError(f"Repo path does not exist: {repo_root}")

    vox_changed = patch_vox(repo_root)
    vis_changed = patch_vis(repo_root)

    print(f"vox.py patched: {vox_changed}")
    print(f"vis_nuscenes.py patched: {vis_changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
