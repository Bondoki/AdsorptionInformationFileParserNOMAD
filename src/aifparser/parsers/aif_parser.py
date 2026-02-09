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
from nomad.units import ureg
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
    AdsorptionInformationFileData,
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
      
    def check_pressure_unit(self, pressure: str) -> str:
        if pressure == "Torr":
            return "torr"
        elif pressure == "Pascal":
            return "pascal"
        elif pressure == "Pa":
            return "Pa"
        elif pressure == "kPa":
            return "kPa"
        return pressure # Return the value if not known None  # Return None for any other value
    
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
        
        
        
        # archive.data = MyClassTwo()#AdsorptionInformationFile()
        
        # Populate the information
        #archive.data.aif_operator = self.find_value(json_data, '_exptl_operator')
        # archive.data.name = self.find_value(json_data, '_exptl_operator')
        #archive.data.aif_date = self.find_value(json_data, '_exptl_date')
        # archive.data.aif_instrument = self.find_value(json_data, '_exptl_instrument')
        # archive.data.aif_instrument2 = self.find_value(json_data, '_exptl_instrument')
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
        child_archive.data = AdsorptionInformationFile()
        child_archive.data.aif_operator = self.find_value(json_data, '_exptl_operator') # f'{basic_name[0]}'
        child_archive.data.aif_date = self.find_value(json_data, '_exptl_date')
        child_archive.data.aif_instrument = self.find_value(json_data, '_exptl_instrument')
        child_archive.data.aif_adsorptive = self.find_value(json_data, '_exptl_adsorptive')
        child_archive.data.aif_adsorptive_name = self.find_value(json_data, '_exptl_adsorptive_name')
        
        # child_archive.data.aif_temperature = self.find_value(json_data, '_exptl_temperature')
        if (self.find_value(json_data, '_exptl_temperature')) is not None:
          child_archive.data.aif_temperature = ureg.Quantity(float(self.find_value(json_data, '_exptl_temperature')), self.find_value(json_data, '_units_temperature').upper())
        
        child_archive.data.aif_method = self.find_value(json_data, '_exptl_method')
        child_archive.data.aif_isotherm_type = self.find_value(json_data, '_exptl_isotherm_type')
        
        if (self.find_value(json_data, '_exptl_p0')) is not None:
          child_archive.data.aif_saturation_pressure = ureg.Quantity(float(self.find_value(json_data, '_exptl_p0')), self.check_pressure_unit(self.find_value(json_data, '_units_pressure')))
        
        child_archive.data.aif_digitizer = self.find_value(json_data, '_exptl_digitizer')
        
        if (self.find_value(json_data, '_exptl_sample_mass')) is not None:
          child_archive.data.aif_sample_mass = ureg.Quantity(float(self.find_value(json_data, '_exptl_sample_mass')), self.find_value(json_data, '_units_mass').lower().replace('g', 'gram'))
        
        child_archive.data.aif_sample_id = self.find_value(json_data, '_sample_id')
        child_archive.data.aif_sample_material_id = self.find_value(json_data, '_sample_material_id')
        
        # # Call the function
        # #operator_value = find_value(json_data, '_exptl_operator')
        # #print(operator_value)  # Output: qc
        # 
        # Adsorption
        aif_data_adsorption = AdsorptionInformationFileData()
        aif_data_adsorption.aif_data_experiment_type = 'adsorption'
        
        if (self.find_value(json_data, '_adsorp_pressure')) is not None:
          aif_data_adsorption.aif_data_pressure = ureg.Quantity(self.find_value(json_data, '_adsorp_pressure'), self.check_pressure_unit(self.find_value(json_data, '_units_pressure')))
        
        if (self.find_value(json_data, '_adsorp_p0')) is not None:
          aif_data_adsorption.aif_data_saturation_pressure = ureg.Quantity(self.find_value(json_data, '_adsorp_p0'), self.check_pressure_unit(self.find_value(json_data, '_units_pressure')))
        
        if (self.find_value(json_data, '_adsorp_loading')) is not None:
          aif_data_adsorption.aif_data_loading = ureg.Quantity(self.find_value(json_data, '_adsorp_loading'), 'dimensionless')
        
        aif_data_adsorption.aif_data_loading_unit = self.find_value(json_data, '_units_loading')
        
        
        # Desorption
        aif_data_desorption = AdsorptionInformationFileData()
        aif_data_desorption.aif_data_experiment_type = 'desorption'
        
        if (self.find_value(json_data, '_desorp_pressure')) is not None:
          aif_data_desorption.aif_data_pressure = ureg.Quantity(self.find_value(json_data, '_desorp_pressure'), self.check_pressure_unit(self.find_value(json_data, '_units_pressure')))
        
        if (self.find_value(json_data, '_desorp_p0')) is not None:
          aif_data_desorption.aif_data_saturation_pressure = ureg.Quantity(self.find_value(json_data, '_desorp_p0'), self.check_pressure_unit(self.find_value(json_data, '_units_pressure')))
        
        if (self.find_value(json_data, '_desorp_loading')) is not None:
          aif_data_desorption.aif_data_loading = ureg.Quantity(self.find_value(json_data, '_desorp_loading'), 'dimensionless')
        
        aif_data_desorption.aif_data_loading_unit = self.find_value(json_data, '_units_loading')
        
        
        # # check which args the function m_add_subsection accepts here:
        # # packages/nomad-FAIR/nomad/metainfo/metainfo.py
        # # DO NOT use list.append() to add a subsection to a section!
        child_archive.data.m_add_sub_section(
            AdsorptionInformationFile.aif_dataset, aif_data_adsorption
        )
        
        child_archive.data.m_add_sub_section(
            AdsorptionInformationFile.aif_dataset, aif_data_desorption
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
            # child_archive.m_to_dict(with_root_def=True),
            child_archive.m_to_dict(),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )
