import logging
import os.path
import shutil

from nomad.datamodel import EntryArchive
from nomad.client import normalize_all, parse

from aifparser.parsers.aif_parser import AIFParser


def test_parse_file():
    #parser = AIFParser()
    #archive = EntryArchive()
    #parser.parse('tests/data/dut_134_scd_n2_77k.aif', archive, logging.getLogger())
    #print(a.m_to_dict())
    
    #archives = parse('tests/data/dut_134_scd_n2_77k.aif')
    #test_file = os.path.join('tests', 'data', 'dut_134_scd_n2_77k.aif')
    test_file = os.path.join('tests', 'data', 'anie202513606-sup-0002-suppmat2/CALF-20-CO2-320K.aif')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)
    print(entry_archive.m_to_dict())
    # Get the 'main section' section_run as a metainfo object
    #assert entry_archive.data.aif_operator == 'test_file_SEM_01.tif' #'testSEM.tif' 
    # assert archive.workflow2.name == 'test'

