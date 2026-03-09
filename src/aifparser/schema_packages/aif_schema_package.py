from typing import (
    TYPE_CHECKING,
)

import numpy as np
import plotly.express as px
import plotly.graph_objects as go

if TYPE_CHECKING:
    pass

from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.metainfo.plot import (
    PlotlyFigure,
    PlotSection,
)
from nomad.metainfo import (
    Datetime,
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

m_package = SchemaPackage()

#class AdsorptionInformationFileData(PlotSection, EntryData):
class AdsorptionInformationFileData(EntryData):
    m_def = Section(
        label_quantity='aif_data_experiment_type',
        a_eln={
            # "overview": False,
            # "hide": [
            #     "name",
            #     "lab_id",
            #     "method",
            #     "samples",
            #     "measurement_identifiers"
            # ],
            "properties": {
                "order": [
                    "aif_data_experiment_type",
                    "aif_data_loading_unit",
                ]
            }
        },
    )

    aif_data_experiment_type = Quantity(
        type=str,
        description='type of experiment e.g. adsorption/desorption - for displaying, only (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'experiment Type',
        },
    )
    
    aif_data_pressure = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kPa',
        description='Equilibrium pressure of the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Pressure',
            'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_data_fugacity = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kPa',
        description='Fugacity of the adsorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Fugacity',
            'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_data_saturation_pressure = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kPa',
        description='Saturation pressure of the adsorption/desorption measurement at the temperature of the experiment (float)',
        a_eln={
            'label': 'Adsorption/Desorption Saturation Pressure',
            'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_data_amount = Quantity(
        type=np.float64,
        shape=["*"],
        # unit='centimeter**3',
        # description='Amount adsorbed during the adsorption/desorption measurement (float)',
        # a_eln={
        #     'label': 'Adsorption/Desorption Amount (Loading)',
        #     'defaultDisplayUnit': 'centimeter**3',
        # },
        unit='dimensionless',
        description='Amount adsorbed during the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Amount (Loading)',
            'defaultDisplayUnit': 'dimensionless',
        },
    )
        
    aif_data_loading_unit = Quantity(
        type=str,
        description='units of amount adsorbed - for displaying, only (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Loading Unit',
        },
    )
    
    aif_data_amount_excess = Quantity(
        type=np.float64,
        shape=["*"],
        unit='dimensionless',
        description='Excess amount adsorbed during the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Excess Amount (Loading)',
            'defaultDisplayUnit': 'dimensionless',
        },
    )
    
    aif_data_amount_absolute = Quantity(
        type=np.float64,
        shape=["*"],
        unit='dimensionless',
        description='Absolute amount adsorbed during the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Absolute Amount (Loading)',
            'defaultDisplayUnit': 'dimensionless',
        },
    )
    
    aif_data_amount_net = Quantity(
        type=np.float64,
        shape=["*"],
        unit='dimensionless',
        description='Net amount adsorbed during the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Net Amount (Loading)',
            'defaultDisplayUnit': 'dimensionless',
        },
    )
        
    aif_data_enthalpy = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kJ/mole',
        description='Enthalpy of adsorption/desorption at infinite dilution and low loading (float)',
        a_eln={
            'label': 'Adsorption/Desorption Enthalpy',
            'defaultDisplayUnit': 'kJ/mole',
        },
    )
    

class AdsorptionInformationFile(PlotSection, EntryData, ArchiveSection):
    """
    A class for the AIF file format
    """

    m_def = Section(
        a_eln={
            "overview": True,
            "hide": [
                #"name",
                #"lab_id",
                #"method",
                #"samples",
                #"measurement_identifiers"
            ],
            "properties": {
                "order": [
                    "aif_version",
                    "aif_citation_doi",
                    "aif_citation_source",
                    "aif_operator",
                    "aif_date",
                    "aif_instrument",
                    "aif_adsorptive",
                    "aif_adsorptive_name",
                    "aif_temperature",
                    "aif_sample_mass",
                    "aif_sample_density",
                    "aif_method",
                    "aif_isotherm_type",
                    "aif_saturation_pressure",
                    "aif_digitizer",
                    "aif_sample_id",
                    "aif_sample_material_id",
                    "aif_info",
                    "aif_hashkey",
                    "aif_degas_summary",
                    "aif_degas_temperature",
                    "aif_degas_time",
                    "aif_simltn_code",
                    "aif_simltn_date",
                    "aif_simltn_size",
                    "aif_simltn_forcefield_adsorptive",
                    "aif_simltn_forcefield_adsorbent",
                    "aif_simltn_input_files",
                    "aif_simltn_sampling",
                    "aif_simltn_lot",
                ]
            }
        },
    )
    
    
    aif_version = Quantity(
        type=str,
        description='Version of AIF data names (Github commit hash).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Version',
        },
    )
        
    aif_citation_doi = Quantity(
        type=str,
        description='The digital object identifier (DOI) of the cited work (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'DOI',
        },
    )
    aif_citation_source = Quantity(
        type=str,
        description='Source of the cited work (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Source',
        },
    )

    aif_operator = Quantity(
        type=str,
        description='Name of the person who ran the experiment (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Operator',
        },
    )
        
    aif_date = Quantity(
        type=Datetime,
        description='Date of the experiment (string in ISO 8601 format).',
        a_eln={
            'component': 'DateTimeEditQuantity',
            'label': 'Date',
        },
    )
    
    aif_instrument = Quantity(
        type=str,
        description='Instrument id used for the experiment (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Instrument',
        },
    )
    
    aif_adsorptive = Quantity(
        type=str,
        description='Name of the adsorptive (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Adsorptive',
        },
    )
    
    aif_adsorptive_name = Quantity(
        type=str,
        description='Name of the adsorptive - secondary identifier (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Adsorptive - sec. identifier',
        },
    )
    
    aif_temperature = Quantity(
        type=np.float64,
        unit='kelvin',
        description='Temperature of the experiment (float)',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Temperature',
             'defaultDisplayUnit': 'kelvin',
        },
    )
        
    aif_method = Quantity(
        type=str,
        description='Description of method used to determine amount adsorbed, e.g. volumetric (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Method',
        },
    )
    
    aif_isotherm_type = Quantity(
        type=str,
        description='Description of isotherm type, eg. absolute, excess, net (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Isotherm Type',
        },
    )
    
    aif_saturation_pressure = Quantity(
        type=np.float64,
        unit='kPa',
        description='Saturation pressure of the experiment at the temperature of the experiment (float).',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Saturation Pressure',
             'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_digitizer = Quantity(
        type=str,
        description='Name of the person who digitized the experiment (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Digitizer',
        },
    )
        
    aif_sample_mass = Quantity(
        type=np.float64,
        unit='gram',
        description='Mass of the sample (float).',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Sample Mass',
             'defaultDisplayUnit': 'gram',
        },
    )
    
    aif_sample_density = Quantity(
        type=np.float64,
        unit='gram/centimeter**3',
        description='Density of the sample (float).',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Sample Density',
             'defaultDisplayUnit': 'gram/centimeter**3',
        },
    )
    
    aif_sample_id = Quantity(
        type=str,
        description='Unique identifying code used by the operator (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Sample ID',
        },
    )
    
    aif_sample_material_id = Quantity(
        type=str,
        description='Designated name for the material (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Sample Material ID',
        },
    )
    
    aif_info = Quantity(
        type=str,
        description='Secondary identifier (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Info',
        },
    )
    
    aif_hashkey = Quantity(
        type=str,
        description='Secondary identifier (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Hashkey',
        },
    )
    
    aif_degas_summary = Quantity(
        type=str,
        description='Summary of degas conditions (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Degas Conditions',
        },
    )
    
    aif_degas_temperature = Quantity(
        type=np.float64,
        unit='kelvin',
        description='Degas temperature (float).',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Degas Temperature',
             'defaultDisplayUnit': 'kelvin',
        },
    )
    
    aif_degas_time = Quantity(
        type=np.float64,
        description='Degas time (float).',
        unit='hour',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Degas Time',
             'defaultDisplayUnit': 'hour',
        },
    )
    
    aif_simltn_code = Quantity(
        type=str,
        description='Secondary identifier (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Code',
        },
    )
    
    aif_simltn_date = Quantity(
        type=Datetime,
        description='Date of the simulation (string in ISO 8601 format).',
        a_eln={
            'component': 'DateTimeEditQuantity',
            'label': 'Simulation Date',
        },
    )
    
    aif_simltn_size = Quantity(
        type=str,
        description='Num of unit cells, sample mass, etc. (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Size',
        },
    )
    
    aif_simltn_forcefield_adsorptive = Quantity(
        type=str,
        description='Adsorptive model details (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Forcefield Adsorptive',
        },
    )
    
    aif_simltn_forcefield_adsorbent = Quantity(
        type=str,
        description='Adsorbent model details (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Forcefield Adsorbent',
        },
    )
    
    aif_simltn_input_files = Quantity(
        type=str,
        description='Depository link to input files and other codes used in the simulation (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Input Files',
        },
    )
    
    aif_simltn_sampling = Quantity(
        type=str,
        description='Phase space sampling algorithm (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Sampling algorithm',
        },
    )
    
    aif_simltn_lot = Quantity(
        type=str,
        description='Level of theory used in calculation, e.g. DFT, MLP, classical etc. (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Simulation Level of Theory',
        },
    )
    
    
    aif_dataset = SubSection(
        section_def=AdsorptionInformationFileData,
        repeats=True,
    )
    
    def generate_plots(self) -> list[PlotlyFigure]:
        """
        Generate the plotly figures for the `MeasurementCV` section.

        Returns:
            list[PlotlyFigure]: The plotly figures.
        """
        figures = []
        # Create the figure
        fig = go.Figure()
        
        for idx, aif_data_entries in enumerate(self.aif_dataset):
          if aif_data_entries.aif_data_pressure is not None: # sometimes there are no desorption data
            #print(f"Index {idx}/{(len(self.Raman_data_entries) - 1)}: {r_d_entries}")
            # Add line plots
            #print("DATA PRESSURE: "+ aif_data_entries.aif_data_pressure.units)
            x1 = aif_data_entries.aif_data_pressure.to(aif_data_entries.aif_data_pressure.units).magnitude
            x= x1
            
            # if saturation pressure exist, then use it
            if aif_data_entries.aif_data_saturation_pressure is not None:
              x2 = aif_data_entries.aif_data_saturation_pressure.to(aif_data_entries.aif_data_saturation_pressure.units).magnitude
              x = x1/x2
            
            
            y = aif_data_entries.aif_data_amount.to('dimensionless').magnitude
            #y = aif_data_entries.aif_data_amount.to(aif_data_entries.aif_data_amount.units).magnitude
            
            
            # Get the Viridis color scale
            viridis_colors = px.colors.sequential.Viridis
            
            #spectral_colors = px.colors.sequential.Spectral
            
            turbo_colors = px.colors.sequential.Aggrnyl # Turbo
            
            #color_index_line = int(idx / (len(self.aif_dataset)-1) * (len(viridis_colors) - 1)) if len(self.aif_dataset) > 1 else 0
            
#             color_index_line = (
#                 int(idx / (len(self.aif_dataset) - 1) * (len(viridis_colors) - 1)) 
#                 if len(self.aif_dataset) > 1 and aif_data_entries.aif_data_experiment_type == 'adsorped' 
#                 else int(idx / (len(self.aif_dataset) - 1) * (len(spectral_colors) - 1)) if len(self.aif_dataset) > 1 
#                 else 0
#             )
# 
#             
#             fig.add_trace(go.Scatter(
#                 x=x,
#                 y=y,
#                 mode='lines+markers',  # 'lines+markers' to show both lines and markers
#                 name=f'{aif_data_entries.aif_data_experiment_type}: {idx}',
#                 line=dict(color=viridis_colors[color_index_line]), # int(idx / (len(self.Raman_data_entries)) * (len(viridis_colors) - 1))]),
#                 hovertemplate='(x: %{x}, y: %{y})<extra></extra>',
#                 marker=dict(size=10, symbol='circle' if aif_data_entries.aif_data_experiment_type == 'adsorped' else 'diamond')      # Marker size
#             ))
            color_index_line = (
                int(idx / (len(self.aif_dataset) - 1) * (len(viridis_colors) - 1))
                if len(self.aif_dataset) > 1 and aif_data_entries.aif_data_experiment_type == 'adsorption'
                else int(idx / (len(self.aif_dataset) - 1) * (len(turbo_colors) - 1)) if len(self.aif_dataset) > 1
                else 0
            )

            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',  # 'lines+markers' to show both lines and markers
                name=f'{aif_data_entries.aif_data_experiment_type}: {idx}',
                line=dict(color=viridis_colors[color_index_line] if aif_data_entries.aif_data_experiment_type == 'adsorption' else turbo_colors[color_index_line]), # int(idx / (len(self.Raman_data_entries)) * (len(viridis_colors) - 1))]),
                hovertemplate='(x: %{x}, y: %{y})<extra></extra>',
                marker=dict(size=10, symbol='circle' if aif_data_entries.aif_data_experiment_type == 'adsorption' else 'diamond')      # Marker size
            ))


        # exemply use the first entry for the units
        x_label = 'absolute pressure'
        xaxis_title = f'{x_label} ({self.aif_dataset[0].aif_data_pressure.units:~})'#(1/cm)' the ':~' gives the short form
        
        if self.aif_dataset[0].aif_data_saturation_pressure is not None:
          x_label = 'relative pressure'
          xaxis_title = f'{x_label}' # dimensionless
          # xaxis_title = f'{x_label} ({self.aif_dataset[0].aif_data_pressure.units:~}/{self.aif_dataset[0].aif_data_saturation_pressure.units:~})'#(1/cm)' the ':~' gives the short form
        
        
        y_label = 'amount adsorbed'
        yaxis_title = f'{y_label} ({self.aif_dataset[0].aif_data_loading_unit})'
        
        fig.update_layout(
            title=f'{y_label} over {x_label} - Adsorption Information File',
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
            xaxis=dict(
                fixedrange=False,
                type='log',
            ),
            yaxis=dict(
                fixedrange=False,
            ),
            #legend=dict(yanchor='top', y=0.99, xanchor='left', x=0.01),
            template='plotly_white',
            showlegend=True,
            hovermode="closest", #"x unified",
            hoverdistance=10,
        )
        
        fig.update_xaxes(showspikes=True, exponentformat = 'power')  # <-- add this line; power notation
        fig.update_yaxes(showspikes=True)  # <-- add this line
        
        
        figure_json = fig.to_plotly_json()
        figure_json['config'] = {'staticPlot': False, 'displayModeBar': True, 'scrollZoom': True, 'responsive': True, 'displaylogo': True, 'dragmode': True}
        
        figures.append(
            PlotlyFigure(
                label=f'{y_label}-{x_label} semilog plot',
                figure=figure_json
            )
        )
        
        self.figures = figures

        return figures
    
    
    def normalize(self, archive, logger):
        
        if self.aif_dataset:
            #Otherwise create plot
            self.figures = self.generate_plots()
        
        super().normalize(archive, logger)

m_package.__init_metainfo__()
 
