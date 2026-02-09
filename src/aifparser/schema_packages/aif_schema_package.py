from typing import (
    TYPE_CHECKING,
)

import plotly.express as px
import plotly.graph_objects as go
import numpy as np

if TYPE_CHECKING:
    pass

from nomad.datamodel.data import (
    ArchiveSection,
    EntryData,
)
from nomad.datamodel.hdf5 import HDF5Reference
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    H5WebAnnotation,
)
from nomad.datamodel.metainfo.plot import (
    PlotlyFigure,
    PlotSection,
)
from nomad.metainfo import (
    Quantity,
    SchemaPackage,
    Section,
    SubSection,
)

from nomad.metainfo import (
    MSection, MCategory, Section, Quantity, Package, SubSection, MEnum,
    Datetime, constraint)

m_package = SchemaPackage()


class MyClassOne(PlotSection, EntryData):
    m_def = Section(
        a_plotly_express={
            'method': 'line',
            'x': '#my_value',
            'y': '#my_time',
            'label': 'Example Express Plot',
            'index': 0,
            'layout': {
                'title': {'text': 'Example Express Plot'},
                'xaxis': {'title': {'text': 'x axis'}},
                'yaxis': {'title': {'text': 'y axis'}},
            },
        },
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
        ),
    )

    my_value = Quantity(
        type=float,
        shape=['*'],
        unit='K',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='celsius',
        ),
    )

    my_time = Quantity(
        type=float,
        shape=['*'],
        unit='s',
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
            defaultDisplayUnit='minute',
        ),
    )
    
    aif_instrument = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label="Instrument",
            editable="False",
        ),
    )
        
    aif_instrument2 = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            label="Instrument2",
        ),
    )
        
    TGA_Mass_Subtrate = Quantity(
        type=np.float64,
        shape=["*"],
        unit='dimensionless',
        description='The measured mass at temperature in the TGA, given in percent.',
        a_eln=dict(label='AIF mass', defaultDisplayUnit = 'dimensionless'),
    )

class MyClassTwo(EntryData, ArchiveSection):
    """
    An example class
    """

    m_def = Section(
        a_plot=[
            dict(
                label='Pressure and Temperature',
                x=[
                    'my_class_one/0/my_time',
                ],
                y=[
                    'my_class_one/0/my_value',
                ],
                lines=[
                    dict(
                        mode='lines',
                        line=dict(
                            color='rgb(25, 46, 135)',
                        ),
                    ),
                    dict(
                        mode='lines',
                        line=dict(
                            color='rgb(0, 138, 104)',
                        ),
                    ),
                ],
            ),
            # dict(
            #     x='sources/0/vapor_source/power/time',
            #     y='sources/0/vapor_source/power/value',
            # ),
        ],
    )

    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
        ),
    )
        
    aif_instrument = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label="Instrument",
            editable="False",
        ),
    )

    aif_instrument2 = Quantity(
        type=str,
    )

    my_class_one = SubSection(
        section_def=MyClassOne,
        repeats=True,
    )


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
        # a_plotly_express={
        #     'method': 'line',
        #     'x': '#aif_data_adsorp_pressure',
        #     'y': '#aif_data_adsorp_loading',
        #     'label': 'Example Express Plot',
        #     'index': 0,
        #     'layout': {
        #         'title': {'text': 'Example Express Plot'},
        #         'xaxis': {'title': {'text': 'x axis'}},
        #         'yaxis': {'title': {'text': 'y axis'}},
        #     },
        # },
    )

    aif_data_experiment_type = Quantity(
        type=str,
        description='type of experiment e.g. adsorption/desorption - for displaying, only (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'experiment Type',
        },
    )

    # my_value = Quantity(
    #     type=float,
    #     shape=['*'],
    #     unit='K',
    #     a_eln=ELNAnnotation(
    #         component='NumberEditQuantity',
    #         defaultDisplayUnit='celsius',
    #     ),
    # )
    # 
    # my_time = Quantity(
    #     type=float,
    #     shape=['*'],
    #     unit='s',
    #     a_eln=ELNAnnotation(
    #         component='NumberEditQuantity',
    #         defaultDisplayUnit='minute',
    #     ),
    # )
#         
#     TGA_Mass_Subtrate = Quantity(
#         type=np.float64,
#         shape=["*"],
#         unit='dimensionless',
#         description='The measured mass at temperature in the TGA, given in percent.',
#         a_eln=dict(label='AIF mass', defaultDisplayUnit = 'dimensionless'),
#     )
    
    aif_data_pressure = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kPa',
        description='equilibrium pressure of the adsorption/desorption measurement (float)',
        a_eln={
            'label': 'Adsorption/Desorption Pressure',
            'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_data_saturation_pressure = Quantity(
        type=np.float64,
        shape=["*"],
        unit='kPa',
        description='saturation pressure of the adsorption/desorption measurement at the temperature of the experiment (float)',
        a_eln={
            'label': 'Adsorption/Desorption Saturation Pressure',
            'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_data_loading = Quantity(
        type=np.float64,
        shape=["*"],
        unit='dimensionless',
        description='amount adsorbed during the adsorption/desorption measurement (float)',
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
                    "aif_operator",
                    "aif_date",
                    "aif_instrument",
                    "aif_adsorptive",
                    "aif_adsorptive_name",
                    "aif_temperature",
                    "aif_sample_mass",
                    "aif_method",
                    "aif_isotherm_type",
                    "aif_saturation_pressure",
                    "aif_digitizer",
                    "aif_sample_id",
                    "aif_sample_material_id",
                ]
            }
        },
    )

    aif_operator = Quantity(
        type=str,
        description='name of the person who ran the experiment (string).',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Operator',
        },
    )
        
    aif_date = Quantity(
        type=Datetime,
        description='date of the experiment (string in ISO 8601 format)',
        a_eln={
            'component': 'DateTimeEditQuantity',
            'label': 'Date',
        },
    )
    
    aif_instrument = Quantity(
        type=str,
        description='instrument id used for the experiment (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Instrument',
        },
    )
    
    aif_adsorptive = Quantity(
        type=str,
        description='name of the adsorptive (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Adsorptive',
        },
    )
    
    aif_adsorptive_name = Quantity(
        type=str,
        description='name of the adsorptive - secondary identifier (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Adsorptive - sec. identifier',
        },
    )
    
    aif_temperature = Quantity(
        type=np.float64,
        unit='kelvin',
        description='temperature of the experiment (float)',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Temperature',
             'defaultDisplayUnit': 'kelvin',
        },
    )
        
    aif_method = Quantity(
        type=str,
        description='description of method used to determine amount adsorbed, eg. volumetric (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Method',
        },
    )
    
    aif_isotherm_type = Quantity(
        type=str,
        description='description of isotherm type, eg. absolute, excess, net (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Isotherm Type',
        },
    )
    
    aif_saturation_pressure = Quantity(
        type=np.float64,
        unit='kPa',
        description='saturation pressure of the experiment at the temperature of the experiment (float)',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Saturation Pressure',
             'defaultDisplayUnit': 'kPa',
        },
    )
    
    aif_digitizer = Quantity(
        type=str,
        description='name of the person who digitized the experiment (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Digitizer',
        },
    )
        
    aif_sample_mass = Quantity(
        type=np.float64,
        unit='gram',
        description='mass of the sample (float)',
        a_eln={
             'component': 'NumberEditQuantity',
             'label': 'Sample Mass',
             'defaultDisplayUnit': 'gram',
        },
    )
    
    aif_sample_id = Quantity(
        type=str,
        description='unique identifying code used by the operator (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Sample ID',
        },
    )
    
    aif_sample_material_id = Quantity(
        type=str,
        description='designated name for the material (string)',
        a_eln={
            'component': 'StringEditQuantity',
            'label': 'Sample Material ID',
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
            #print(f"Index {idx}/{(len(self.Raman_data_entries) - 1)}: {r_d_entries}")
            # Add line plots
            x1 = aif_data_entries.aif_data_pressure.to(aif_data_entries.aif_data_pressure.units).magnitude
            x2 = aif_data_entries.aif_data_saturation_pressure.to(aif_data_entries.aif_data_saturation_pressure.units).magnitude
            x= x1/x2
            y = aif_data_entries.aif_data_loading.to(aif_data_entries.aif_data_loading.units).magnitude
            
            
            # Get the Viridis color scale
            viridis_colors = px.colors.sequential.Viridis
            
            spectral_colors = px.colors.sequential.Spectral
            
            #color_index_line = int(idx / (len(self.aif_dataset)-1) * (len(viridis_colors) - 1)) if len(self.aif_dataset) > 1 else 0
            
            color_index_line = (
                int(idx / (len(self.aif_dataset) - 1) * (len(viridis_colors) - 1)) 
                if len(self.aif_dataset) > 1 and aif_data_entries.aif_data_experiment_type == 'adsorped' 
                else int(idx / (len(self.aif_dataset) - 1) * (len(spectral_colors) - 1)) if len(self.aif_dataset) > 1 
                else 0
            )

            
            fig.add_trace(go.Scatter(
                x=x,
                y=y,
                mode='lines+markers',  # 'lines+markers' to show both lines and markers
                name=f'{aif_data_entries.aif_data_experiment_type}: {idx}',
                line=dict(color=viridis_colors[color_index_line]), # int(idx / (len(self.Raman_data_entries)) * (len(viridis_colors) - 1))]),
                hovertemplate='(x: %{x}, y: %{y})<extra></extra>',
                marker=dict(size=10, symbol='circle' if aif_data_entries.aif_data_experiment_type == 'adsorped' else 'diamond')      # Marker size
            ))

        # exemply use the first entry for the units
        x_label = 'relative pressure'
        xaxis_title = f'{x_label} ({self.aif_dataset[0].aif_data_pressure.units:~}/{self.aif_dataset[0].aif_data_saturation_pressure.units:~})'#(1/cm)' the ':~' gives the short form
        
        y_label = 'amount adsorbed'
        yaxis_title = f'{y_label} ({self.aif_dataset[0].aif_data_loading_unit})'
        
        fig.update_layout(
            title=f'{y_label} over {x_label} - Adsorption Information File',
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
            xaxis=dict(
                fixedrange=False,
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
        
        fig.update_xaxes(showspikes=True,)  # <-- add this line
        fig.update_yaxes(showspikes=True)  # <-- add this line
        
        # figures.append(
        #     PlotlyFigure(
        #         label=f'{y_label}-{x_label} linear plot',
        #         #index=0,
        #         figure=fig.to_plotly_json(),
        #     ),
        # )
        
        figure_json = fig.to_plotly_json()
        figure_json['config'] = {'staticPlot': False, 'displayModeBar': True, 'scrollZoom': True, 'responsive': True, 'displaylogo': True, 'dragmode': True}
        
        figures.append(
            PlotlyFigure(
                label=f'{y_label}-{x_label} linear plot',
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

class MyClassThree(PlotSection, EntryData):
    """
    An example class
    """

    m_def = Section(
        a_plotly_graph_object=[
            {
                'label': 'shaft temperature',
                'index': 0,
                'dragmode': 'pan',
                'data': {
                    'type': 'scattergl',
                    'line': {'width': 2},
                    'marker': {'size': 6},
                    'mode': 'lines+markers',
                    'name': 'Temperature',
                    'x': '#my_time',
                    'y': '#my_value',
                },
                'layout': {
                    'title': {'text': 'Shaft Temperature'},
                    'xaxis': {
                        'showticklabels': True,
                        'fixedrange': True,
                        'ticks': '',
                        'title': {'text': 'Process time [min]'},
                        'showline': True,
                        'linewidth': 1,
                        'linecolor': 'black',
                        'mirror': True,
                    },
                    'yaxis': {
                        'showticklabels': True,
                        'fixedrange': True,
                        'ticks': '',
                        'title': {'text': 'Temperature [°C]'},
                        'showline': True,
                        'linewidth': 1,
                        'linecolor': 'black',
                        'mirror': True,
                    },
                    'showlegend': False,
                },
                'config': {
                    'displayModeBar': False,
                    'scrollZoom': False,
                    'responsive': False,
                    'displaylogo': False,
                    'dragmode': False,
                },
            },
            # {
            #     ...
            # },
        ],
    )
    name = Quantity(
        type=str,
        description="""
        Sample name.
        """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
        ),
    )
    my_value = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )

    my_time = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )


class MyClassFour(PlotSection, EntryData):
    """
    Class autogenerated from yaml schema.
    """

    my_value = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )

    my_time = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )
    my_value_bis = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )

    my_time_bis = Quantity(
        type=float,
        shape=['*'],
        a_eln=ELNAnnotation(
            component='NumberEditQuantity',
        ),
    )

    def normalize(self, archive, logger):
        # plotly figure
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=self.my_time,
                y=self.my_value,
                name='Sub Temp',
                line=dict(color='#2A4CDF', width=4),
                yaxis='y',
            ),
        )
        fig.add_trace(
            go.Scatter(
                x=self.my_time_bis,
                y=self.my_value_bis,
                name='Pyro Temp',
                line=dict(color='#90002C', width=2),
                yaxis='y',
            ),
        )
        fig.update_layout(
            template='plotly_white',
            dragmode='zoom',
            xaxis=dict(
                fixedrange=False,
                autorange=True,
                title='Process time / s',
                mirror='all',
                showline=True,
                gridcolor='#EAEDFC',
            ),
            yaxis=dict(
                fixedrange=False,
                title='Temperature / °C',
                tickfont=dict(color='#2A4CDF'),
                gridcolor='#EAEDFC',
            ),
            showlegend=True,
        )
        self.figures = [PlotlyFigure(label='my figure 1', figure=fig.to_plotly_json())]


class MyClassFive(EntryData, ArchiveSection):
    """
    An example class
    """

    name = Quantity(
        type=str,
        description="""
        Sample name.
        """,
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
        ),
    )

    reference = Quantity(
        type=MyClassOne,
        description='A reference to a NOMAD `MyClassOne` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='MyClassOne Reference',
        ),
    )


m_package.__init_metainfo__()
 
