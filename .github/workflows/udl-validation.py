#!/usr/bin/env python3
import glob
import sys
from lxml import etree

# Allowed attributes differences for WordsStyle elements.
ALLOWED_ATTRIBUTES = ['fgColor', 'bgColor', 'colorStyle', 'fontStyle']

def normalize(element):
    """
    For each <WordsStyle> element, remove the allowed differing attributes.
    Recursively process children.
    """
    if element.tag == "WordsStyle":
        for attr in ALLOWED_ATTRIBUTES:
            if attr in element.attrib:
                del element.attrib[attr]
    for child in element:
        normalize(child)

def compare_elements(elem1, elem2, file_ref, file_compare):
    """
    Recursively compare two XML elements. If a mismatch is found,
    print an error using the GitHub annotation syntax.
    """
    # Check element tags.
    if elem1.tag != elem2.tag:
        print(f"::error file={file_compare},line={elem2.sourceline}::Tag mismatch: expected <{elem1.tag}> but found <{elem2.tag}>")
        return False

    # Compare attributes (after normalizing allowed WordsStyle differences).
    if elem1.attrib != elem2.attrib:
        print(f"::error file={file_compare},line={elem2.sourceline}::Attributes mismatch in <{elem1.tag}>: expected {elem1.attrib} but found {elem2.attrib}")
        return False

    # Compare text (ignoring surrounding whitespace).
    if (elem1.text or "").strip() != (elem2.text or "").strip():
        print(f"::error file={file_compare},line={elem2.sourceline}::Text mismatch in <{elem1.tag}>: expected '{elem1.text}' but found '{elem2.text}'")
        return False

    # Check that both have the same number of children.
    if len(elem1) != len(elem2):
        print(f"::error file={file_compare},line={elem2.sourceline}::Children count mismatch in <{elem1.tag}>: expected {len(elem1)} but found {len(elem2)}")
        return False

    # Recursively compare child elements.
    for child1, child2 in zip(elem1, elem2):
        if not compare_elements(child1, child2, file_ref, file_compare):
            return False
    return True

def main():
    files = glob.glob("./src/*.xml")
    if not files:
        print("No XML files found in ./src")
        sys.exit(0)

    normalized_trees = {}
    # Parse and normalize each XML file.
    for f in files:
        try:
            parser = etree.XMLParser(remove_blank_text=True)
            tree = etree.parse(f, parser)
            root = tree.getroot()
        except Exception as e:
            print(f"::error file={f}::XML parsing error: {e}")
            sys.exit(1)
        normalize(root)
        normalized_trees[f] = root

    # Use the first file as reference.
    ref_file = files[0]
    ref_root = normalized_trees[ref_file]

    valid = True
    # Compare each subsequent file to the reference.
    for f in files[1:]:
        if not compare_elements(ref_root, normalized_trees[f], ref_file, f):
            valid = False

    if not valid:
        sys.exit(1)
    else:
        print("All XML files are valid and consistent (aside from allowed WordsStyle differences).")

if __name__ == "__main__":
    main()
