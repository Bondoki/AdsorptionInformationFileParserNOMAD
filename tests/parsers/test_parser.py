import logging

from nomad.datamodel import EntryArchive

from aifparser.parsers.parser import AIFParser


def test_parse_file():
    parser = AIFParser()
    archive = EntryArchive()
    parser.parse('tests/data/dut_134_scd_n2_77k.aif', archive, logging.getLogger())

    assert archive.workflow2.name == 'test'
