"""Regression test for two-up signature ordering and printable sheet dimensions."""
import tempfile
import sys
from pathlib import Path

import fitz

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.impose_booklet import impose


def test_booklet():
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary)
        source = path / "source.pdf"
        destination = path / "booklet.pdf"
        document = fitz.open()
        for number in range(1, 11):
            page = document.new_page(width=396, height=612)
            page.insert_text((155, 300), f"PAGE {number}", fontsize=28)
        document.save(source)
        document.close()
        impose(source, destination, sheets_per_signature=2)
        booklet = fitz.open(destination)
        assert len(booklet) == 6
        assert all(page.rect == fitz.Rect(0, 0, 792, 612) for page in booklet)
        expected = [(8, 1), (2, 7), (6, 3), (4, 5), (9,), (10,)]
        for page, numbers in zip(booklet, expected):
            actual = page.get_text()
            for number in numbers:
                assert f"PAGE {number}" in actual, (number, actual)
            assert actual.count("PAGE") == len(numbers), (numbers, actual)
        booklet.close()


if __name__ == "__main__":
    test_booklet()
    print("Booklet signature and duplex geometry checks passed")
