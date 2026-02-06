from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.datamodel.datamodel import (
        EntryArchive,
    )

from nomad.config import config
from nomad.datamodel.metainfo.workflow import Workflow
from nomad.parsing.parser import MatchingParser
# from nomad.parsing.file_parser import Quantity
from nomad.metainfo import (
    MSection,
    Package,
    SchemaPackage,
    Quantity,
    )

from gemmi import cif
import json

from aifparser.parsers.utils import (
    create_archive,
)

from aifparser.schema_packages.aif_schema_package import (
    MyClassFive,
    MyClassOne,
    #MyClassOneHDF5,
    MyClassTwo,
    #MyClassTwoHDF5,
    AdsorptionInformationFile,
)

configuration = config.get_plugin_entry_point(
    'aifparser.parsers:aif_parser_entry_point'
)


class AIFParser(MatchingParser):
  
    def find_value(self, data, target_key):
        if isinstance(data, dict):
            for key, value in data.items():
               if key == target_key:
                    return value
               # Recursion is needed if the value is a nested dictionary
               elif isinstance(value, dict):
                   result = self.find_value(value, target_key)
                   if result is not None:
                        return result
        return None
    
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('AIFParser.parse', parameter=configuration.parameter)

        filename = mainfile.split('/')[-1]
        basic_name = filename.split('.')

        # archive.data = CatalysisCollectionParserEntry(
        #     data_file=filename,
        # )
        #archive.metadata.entry_name = f'{basic_name[0]} data file'
        
        # Read and import the aif file using gemmi
        aif = cif.read_file(str(mainfile))
        
        # Convert string to JSON
        json_data= json.loads(aif.as_json())
        
        
        
        archive.data = MyClassTwo()#AdsorptionInformationFile()
        
        # Populate the information
        #archive.data.aif_operator = self.find_value(json_data, '_exptl_operator')
        archive.data.name = self.find_value(json_data, '_exptl_operator')
        #archive.data.aif_date = self.find_value(json_data, '_exptl_date')
        archive.data.aif_instrument = self.find_value(json_data, '_exptl_instrument')
        archive.data.aif_instrument2 = self.find_value(json_data, '_exptl_instrument')
        #
        # Create JSON 
        # 
        child_archive = EntryArchive()
        # 
        # #my_name = 'And'
        filetype = 'json' # 'yaml' # "json"
        # 
        example_filename = f'{basic_name[0]}.archive.{filetype}'
        # 
        child_archive.data = MyClassTwo()
        child_archive.data.name = f'{basic_name[0]}'
        child_archive.data.aif_instrument = self.find_value(json_data, '_exptl_instrument')
        child_archive.data.aif_instrument2 = self.find_value(json_data, '_exptl_instrument')
        # # Call the function
        # #operator_value = find_value(json_data, '_exptl_operator')
        # #print(operator_value)  # Output: qc
        # 
        my_class_one_subsec = MyClassOne()
        my_class_one_subsec.name = self.find_value(json_data, '_exptl_operator')
        my_class_one_subsec.aif_instrument = self.find_value(json_data, '_exptl_instrument')
        my_class_one_subsec.aif_instrument2 = self.find_value(json_data, '_exptl_instrument')
        # #my_class_one_subsec.my_value = df_csv['ValueTwo']
        # #my_class_one_subsec.my_time = df_csv['ValueTwo2']
        # 
        # # check which args the function m_add_subsection accepts here:
        # # packages/nomad-FAIR/nomad/metainfo/metainfo.py
        # # DO NOT use list.append() to add a subsection to a section!
        child_archive.data.m_add_sub_section(
            MyClassTwo.my_class_one, my_class_one_subsec
        )
        # 
        # create_archive(
        #     child_archive.m_to_dict(with_root_def=True),
        #     archive.m_context,
        #     example_filename,
        #     filetype,
        #     logger,
        # )
        # 
        # archive.data = MyClassOne()
        
        #aif = MyClassTwo()
        #aif.name = self.find_value(json_data, '_exptl_operator')
        
        # create_archive(
        #         aif, archive, f'{basic_name}.archive.json'
        #     )
        
        create_archive(
            child_archive.m_to_dict(with_root_def=True),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )
