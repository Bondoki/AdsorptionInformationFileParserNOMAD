import logging
import os.path

from nomad.datamodel import EntryArchive
#from nomad.client import normalize_all, parse

from aifparser.parsers.aif_parser import AIFParser


def test_parse_file():
    parser = AIFParser()
    archive = EntryArchive()
    #parser.parse('tests/data/dut_134_scd_n2_77k.aif', archive, logging.getLogger())

    #test_file = os.path.join('tests', 'data', 'dut_134_scd_n2_77k.aif')
    #entry_archive = parse(test_file)[0]
    #normalize_all(entry_archive)
    #print(entry_archive)
    #assert entry_archive.data.aif_operator == 'test_file_SEM_01.tif' #'testSEM.tif' 
    # assert archive.workflow2.name == 'test'
