#!/usr/bin/env python3
"""Fail closed when an edition is incomplete, out of sync or poorly imposed."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

import fitz

ALGORITHMS = (
    'Selection Sort', 'Insertion Sort', 'Bubble Sort', 'Merge Sort',
    'Quicksort', 'Heapsort', 'Counting Sort', 'Radix Sort',
    'Bucket Sort', 'Shellsort', 'Timsort', 'Introsort', 'Cycle Sort',
)


def normalized_words(document):
    text = ' '.join(page.get_text(sort=False) for page in document)
    return re.findall(r'[a-z0-9]+', text.casefold())


def main(manifest_path: Path):
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    expected = manifest['files']
    paths = {name: manifest_path.parent / item['path'] for name, item in expected.items()}
    for name, path in paths.items():
        if not path.is_file():
            raise RuntimeError(f'Missing {name}: {path}. Do not publish an older edition as a fallback.')
    docs = {name: fitz.open(path) for name, path in paths.items()}
    for name, document in docs.items():
        info = expected[name]
        assert len(document) == info['pages'], f'{name}: incorrect page count'
        assert not document.is_encrypted, f'{name}: encrypted'
        pictures = sum(len(page.get_images()) for page in document)
        assert pictures >= manifest['minimum_illustrations'], f'{name}: missing original illustrations ({pictures})'
        fulltext = ' '.join(page.get_text() for page in document)
        for label in ALGORITHMS:
            assert label in fulltext, f'{name}: missing chapter {label}'
        assert 'Quickselect' in fulltext, f'{name}: missing Quickselect'
        digest = hashlib.sha256(paths[name].read_bytes()).hexdigest()
        assert digest == info['sha256'], f'{name}: checksum differs from the approved edition; update manifest after review'
        print(f'{name}: {len(document)} pages, {pictures} illustrations, SHA256 {digest}')
    booklet = docs['booklet']
    assert booklet.page_count % 2 == 0, 'booklet: not complete duplex sheets'
    assert booklet.page_count // 2 == manifest['booklet_sheets'], 'booklet: wrong sheet count'
    assert all(abs(page.rect.width - 792) < 1 and abs(page.rect.height - 612) < 1 for page in booklet), 'booklet: wrong print geometry'
    assert [page.rotation for page in booklet] == [180 * (i % 2) for i in range(len(booklet))], 'booklet: wrong alternating long-edge duplex rotation'
    a, b = (normalized_words(docs[k]) for k in ('reading', 'booklet'))
    grams = lambda words: Counter(zip(words, words[1:], words[2:]))
    left, right = grams(a), grams(b)
    overlap = sum((left & right).values()) / max(sum(left.values()), sum(right.values()))
    assert overlap >= 0.75, f'reading and booklet disagree; shared 3-word sequences: {overlap:.1%}'
    print(f'Content overlap: {overlap:.1%}; edition {manifest["version"]} verified')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    args = parser.parse_args()
    main(args.manifest)
