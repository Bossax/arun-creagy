"""Post-process a DOCX to improve Thai text layout in Microsoft Word.

This script updates WordprocessingML defaults so Thai text is assigned a Thai
language tag and an explicit Thai-capable font instead of generic Office theme
fonts. That usually improves Thai line breaking, spacing, and paragraph flow
for DOCX files generated from Markdown via Pandoc.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"

ET.register_namespace("w", W_NS)
ET.register_namespace("a", A_NS)


def w_tag(name: str) -> str:
    return f"{{{W_NS}}}{name}"


def a_tag(name: str) -> str:
    return f"{{{A_NS}}}{name}"


def ensure_child(parent: ET.Element, tag: str) -> ET.Element:
    child = parent.find(tag)
    if child is None:
        child = ET.SubElement(parent, tag)
    return child


def set_fonts_and_language(r_pr: ET.Element, font_name: str, lang: str) -> None:
    r_fonts = ensure_child(r_pr, w_tag("rFonts"))
    for attr in [
        f"{{{W_NS}}}asciiTheme",
        f"{{{W_NS}}}hAnsiTheme",
        f"{{{W_NS}}}eastAsiaTheme",
        f"{{{W_NS}}}cstheme",
    ]:
        r_fonts.attrib.pop(attr, None)
    r_fonts.set(f"{{{W_NS}}}ascii", font_name)
    r_fonts.set(f"{{{W_NS}}}hAnsi", font_name)
    r_fonts.set(f"{{{W_NS}}}eastAsia", font_name)
    r_fonts.set(f"{{{W_NS}}}cs", font_name)

    lang_el = ensure_child(r_pr, w_tag("lang"))
    lang_el.set(f"{{{W_NS}}}val", lang)
    lang_el.set(f"{{{W_NS}}}eastAsia", lang)
    lang_el.set(f"{{{W_NS}}}bidi", lang)


def update_styles(xml_bytes: bytes, font_name: str, lang: str) -> bytes:
    root = ET.fromstring(xml_bytes)

    doc_defaults = ensure_child(root, w_tag("docDefaults"))
    r_pr_default = ensure_child(doc_defaults, w_tag("rPrDefault"))
    r_pr = ensure_child(r_pr_default, w_tag("rPr"))
    set_fonts_and_language(r_pr, font_name, lang)

    for style in root.findall(w_tag("style")):
        style_type = style.get(f"{{{W_NS}}}type")
        if style_type not in {"paragraph", "character", "table"}:
            continue
        style_r_pr = ensure_child(style, w_tag("rPr"))
        set_fonts_and_language(style_r_pr, font_name, lang)

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def update_settings(xml_bytes: bytes, lang: str) -> bytes:
    root = ET.fromstring(xml_bytes)
    theme_font_lang = ensure_child(root, w_tag("themeFontLang"))
    theme_font_lang.set(f"{{{W_NS}}}val", lang)
    theme_font_lang.set(f"{{{W_NS}}}eastAsia", lang)
    theme_font_lang.set(f"{{{W_NS}}}bidi", lang)
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def update_theme(xml_bytes: bytes, font_name: str) -> bytes:
    root = ET.fromstring(xml_bytes)
    for family_name in ["majorFont", "minorFont"]:
        family = root.find(f".//{a_tag(family_name)}")
        if family is None:
            continue

        thai_font = None
        for font in family.findall(a_tag("font")):
            if font.get("script") == "Thai":
                thai_font = font
                break

        if thai_font is None:
            thai_font = ET.SubElement(family, a_tag("font"))
            thai_font.set("script", "Thai")

        thai_font.set("typeface", font_name)

    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def fix_docx(input_path: Path, output_path: Path, font_name: str, lang: str) -> None:
    with tempfile.TemporaryDirectory() as tmp_dir:
        temp_output = Path(tmp_dir) / output_path.name

        with zipfile.ZipFile(input_path, "r") as source_zip, zipfile.ZipFile(
            temp_output, "w", compression=zipfile.ZIP_DEFLATED
        ) as target_zip:
            for info in source_zip.infolist():
                data = source_zip.read(info.filename)

                if info.filename == "word/styles.xml":
                    data = update_styles(data, font_name, lang)
                elif info.filename == "word/settings.xml":
                    data = update_settings(data, lang)
                elif info.filename == "word/theme/theme1.xml":
                    data = update_theme(data, font_name)

                target_zip.writestr(info, data)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(temp_output, output_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fix Thai font and language defaults inside a DOCX file."
    )
    parser.add_argument("input", type=Path, help="Input DOCX path")
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        help="Output DOCX path (default: sibling file with .thai.docx suffix)",
    )
    parser.add_argument(
        "--font",
        default="Angsana New",
        help="Thai-capable font name to set in the document (default: Angsana New)",
    )
    parser.add_argument(
        "--lang",
        default="th-TH",
        help="Word language tag to assign (default: th-TH)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input
    output_path = args.output or input_path.with_name(f"{input_path.stem}.thai.docx")

    if not input_path.exists():
        raise FileNotFoundError(f"Input DOCX not found: {input_path}")

    fix_docx(input_path, output_path, args.font, args.lang)
    print(f"Wrote fixed DOCX to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
