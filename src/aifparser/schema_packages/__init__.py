from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class AIFSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from aifparser.schema_packages.aif_schema_package import m_package

        return m_package


aif_schema_package_entry_point = AIFSchemaPackageEntryPoint(
    name='AIF Schema',
    description='Schema package for Adsorption Information File.',
)
