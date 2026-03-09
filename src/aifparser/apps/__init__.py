from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Dashboard,
    Layout,
    Markers,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
    SearchQuantities,
    WidgetHistogram,
    WidgetScatterPlot,
)

schema = 'aifparser.schema_packages.aif_schema_package.AdsorptionInformationFile'
# schema = 'nomad_example.schema_packages.mypackage.MySchema'
aif_app_entry_point = AppEntryPoint(
    name='App AIF',
    description='App for the Adsorption Information File (AIF) database.',
    app=App(
        # Label of the App
        label='Adsorption Information File (AIF)',
        # Path used in the URL, must be unique
        path='adsorptioninformationfile',
        # Used to categorize apps in the explore menu
        category='Adsorption Information File',
        # Brief description used in the app menu
        description='Search the AIF database.',
        # Longer description that can also use markdown
        readme='This page allows you to search all AIF data within NOMAD.' +
        'The filter menu on the left and the dashboard show default columns,' +
        ' which are specifically designed for [Adsorption Information File](https://adsorptioninformationformat.com/).',
        # If you want to use quantities from a custom schema, you need to load
        # the search quantities from it first here. Note that you can use a glob
        # syntax to load the entire package, or just a single schema from a
        # package.
        search_quantities=SearchQuantities(
            include=['*#aifparser.schema_packages.aif_schema_package.AdsorptionInformationFile'],
        ),
        # Controls which columns are shown in the results table
        columns=[
            #Column(quantity='entry_id', selected=True),
            Column(quantity=f'data.aif_sample_id#{schema}', selected=True, label='Sample ID',),
            Column(quantity=f'data.aif_sample_material_id#{schema}', selected=True, label='Sample Material ID',),
            Column(quantity='mainfile', selected=True, label='File',),
            Column(quantity=f'data.aif_operator#{schema}', selected=True, label='Operator',),
            Column(quantity=f'data.aif_date#{schema}', selected=True, label='Date',),
            # Column(
            #     quantity=f'data.my_repeated_section[*].myquantity#{schema}',
            #     selected=True,
            # ),
            Column(quantity='upload_create_time', selected=True),
        ],
        # Dictionary of search filters that are always enabled for queries made
        # within this app. This is especially important to narrow down the
        # results to the wanted subset. Any available search filter can be
        # targeted here. This example makes sure that only entries that use
        # MySchema are included.
        filters_locked={'section_defs.definition_qualified_name': [schema]},
        # Controls the menu shown on the left
        menu=Menu(
            title='Material',
            items=[
                Menu(
                    title='Elements',
                    items=[
                        MenuItemPeriodicTable(
                            quantity='results.material.elements',
                        ),
                        MenuItemTerms(
                            quantity='results.material.chemical_formula_hill',
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            quantity='results.material.chemical_formula_iupac',
                            width=6,
                            options=0,
                        ),
                        MenuItemHistogram(
                            x='results.material.n_elements',
                        ),
                    ],
                ),
              #MenuItemTerms(search_quantity='authors.name', options=5),
              Menu(
                   title='Operator',
                   size='md',
                   items=[
                          MenuItemTerms(
                            width=6,
                            search_quantity=f'data.aif_operator#{schema}',
                            ),
                        ],
                  ),
              Menu(
                   title='Adsorptive',
                   size='md',
                   items=[
                          MenuItemTerms(
                            width=6,
                            search_quantity=f'data.aif_adsorptive#{schema}',
                            ),
                         ],
                  ),
              Menu(
                   title='Date',
                   size='md',
                   items=[
                          MenuItemHistogram(x=Axis(search_quantity=f'data.aif_date#{schema}')),
                         ],
                  ),
            ],
        ),
        # Controls the default dashboard shown in the search interface
        dashboard=Dashboard(
            widgets=[
                WidgetHistogram(
                    title='AIF Temperature',
                    show_input=False,
                    autorange=True,
                    nbins=30,
                    scale='linear',
                    x=Axis(search_quantity=f'data.aif_temperature#{schema}', title='Temperature', unit='kelvin'),
                    layout={'lg': Layout(minH=3, minW=3, h=4, w=12, y=0, x=0)},
                ),
                WidgetHistogram(
                    title='AIF Mass',
                    show_input=False,
                    autorange=True,
                    nbins=30,
                    scale='linear',
                    x=Axis(search_quantity=f'data.aif_sample_mass#{schema}', title='Mass', unit='milligram'),
                    layout={'lg': Layout(minH=3, minW=3, h=4, w=12, y=0, x=12)},
                ),
                WidgetScatterPlot(
                    title='Scatterplot Mass-Temperature',
                    autorange=True,
                    layout={
                        'lg': Layout(h=8, minH=3, minW=8, w=12, x=0, y=4),
                        },
                    x=Axis(search_quantity=f'data.aif_sample_mass#{schema}', title='Mass', unit='milligram'),
                    y=Axis(search_quantity=f'data.aif_temperature#{schema}', title='Temperature', unit='kelvin'),
                    markers=Markers(color=Axis(search_quantity=f'data.aif_operator#{schema}')),
                    size=1000,  # maximum number of entries loaded
                    ),
            ]
        ),
    ),
)
