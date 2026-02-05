import logging

from nomad.datamodel import EntryArchive

from aifparser.parsers.parser import AIFParser


def test_parse_file():
    parser = AIFParser()
    archive = EntryArchive()
    parser.parse('tests/data/example.out', archive, logging.getLogger())

    assert archive.workflow2.name == 'test'
