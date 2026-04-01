#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# This file has been taken from:
# https://github.com/PDI-Berlin/pdi-nomad-plugin/blob/main/src/pdi_nomad_plugin/utils.py
#
import json
import math
from typing import TYPE_CHECKING

#import h5py
import numpy as np
import pandas as pd
import yaml

if TYPE_CHECKING:
    pass
from nomad.datamodel.context import ClientContext

if TYPE_CHECKING:
    pass

from nomad.utils import hash

timezone = 'Europe/Berlin'



# https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database/blob/main/src/perovskite_solar_cell_database/parsers/utils.py#L17
# def get_reference(upload_id: str, entry_id: str) -> str:
#     return f'../uploads/{upload_id}/archive/{entry_id}#data'

# https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database/blob/main/src/perovskite_solar_cell_database/parsers/utils.py#L21
# def get_entry_id_from_file_name(file_name: str, archive: 'EntryArchive') -> str:
# 
#     return hash(archive.metadata.upload_id, file_name)

# https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database/blob/main/src/perovskite_solar_cell_database/parsers/utils.py#L27
# def create_archive(
#     entity: 'ArchiveSection',
#     archive: 'EntryArchive',
#     file_name: str,
# ) -> str:
#     import json
# 
#     from nomad.datamodel.context import ClientContext
# 
#     entity_entry = entity.m_to_dict(with_root_def=True)
#     if isinstance(archive.m_context, ClientContext):
#         with open(file_name, 'w') as outfile:
#             json.dump({'data': entity_entry}, outfile, indent=4)
#         return os.path.abspath(file_name)
#     if not archive.m_context.raw_path_exists(file_name):
#         with archive.m_context.raw_file(file_name, 'w') as outfile:
#             json.dump({'data': entity_entry}, outfile)
#         archive.m_context.process_updated_raw_file(file_name)
#     return get_reference(
#         archive.metadata.upload_id, get_entry_id_from_file_name(file_name, archive)
#     )
  

def clean_name(name):
    """
    Utility function used to clean the filenames of the epic log files.
    The filenames to be cleaned are found in the excel config file.
    This function can handle both strings and pandas Series.
    """
    if isinstance(name, str):
        return name.strip().replace(' ', '_').replace('.', '_')
    elif isinstance(name, pd.Series):
        return name[0].strip().replace(' ', '_').replace('.', '_')


def get_reference(upload_id, entry_id):
    return f'../uploads/{upload_id}/archive/{entry_id}'


def get_entry_id(upload_id, filename):

    return hash(upload_id, filename)


def get_hash_ref(upload_id, filename):
    return f'{get_reference(upload_id, get_entry_id(upload_id, filename))}#data'


def nan_equal(a, b):
    """
    Compare two values with NaN values.
    """
    if isinstance(a, float) and isinstance(b, float):
        return a == b or (math.isnan(a) and math.isnan(b))
    elif isinstance(a, dict) and isinstance(b, dict):
        return dict_nan_equal(a, b)
    elif isinstance(a, list) and isinstance(b, list):
        return list_nan_equal(a, b)
    else:
        return a == b


def list_nan_equal(list1, list2):
    """
    Compare two lists with NaN values.
    """
    if len(list1) != len(list2):
        return False
    for a, b in zip(list1, list2):
        if not nan_equal(a, b):
            return False
    return True


def dict_nan_equal(dict1, dict2):
    """
    Compare two dictionaries with NaN values.
    """
    if set(dict1.keys()) != set(dict2.keys()):
        return False
    for key in dict1:
        if not nan_equal(dict1[key], dict2[key]):
            return False
    return True

# https://github.com/PDI-Berlin/pdi-nomad-plugin/blob/main/src/pdi_nomad_plugin/utils.py
def create_archive(
    entry_dict, context, filename, file_type, logger, *, overwrite: bool = False
):
    # file_exists = context.raw_path_exists(filename)
    file_exists = getattr(context, 'raw_path_exists', lambda _: None)(filename)
    dicts_are_equal = None
    if isinstance(context, ClientContext):
        return None
    if file_exists:
        with context.raw_file(filename, 'r') as file:
            existing_dict = yaml.safe_load(file)
            dicts_are_equal = dict_nan_equal(existing_dict, entry_dict)
    if not file_exists or overwrite:# or dicts_are_equal:
        with context.raw_file(filename, 'w') as newfile:
            if file_type == 'json':
                json.dump(entry_dict, newfile)
            elif file_type == 'yaml':
                yaml.dump(entry_dict, newfile)
        context.upload.process_updated_raw_file(filename, allow_modify=True)
    elif file_exists and not overwrite and not dicts_are_equal:
        logger.error(
            f'{filename} archive file already exists. '
            f'You are trying to overwrite it with a different content. '
            f'To do so, remove the existing archive and click reprocess again.'
        )
    return get_hash_ref(context.upload_id, filename)



def handle_unit(dataframe, unit_header):
    unit_cell = dataframe.get(unit_header)
    unit = None
    if unit_cell is not None:
        if isinstance(unit_cell, str):
            if unit_cell == 'C':
                unit = '°C'
            elif unit_cell == 'sccm':
                unit = 'meter ** 3 / second'
            else:
                unit = unit_cell
        elif not unit_cell.empty and pd.notna(unit_cell.iloc[0]):
            if unit_cell.iloc[0] == 'C':
                unit = '°C'
            elif unit_cell.iloc[0] == 'sccm':
                unit = 'meter ** 3 / second'
            else:
                unit = unit_cell.iloc[0]
    return unit



def _not_equal(a, b) -> bool:
    comparison = a != b
    if isinstance(comparison, np.ndarray):
        return comparison.any()
    return comparison

