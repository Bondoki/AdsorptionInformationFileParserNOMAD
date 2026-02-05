from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class AIFParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from aifparser.parsers.parser import AIFParser

        return AIFParser(**self.model_dump())


parser_entry_point = AIFParserEntryPoint(
    name='AIF Parser',
    description='AIF Parser entry point configuration.',
    mainfile_name_re=r'.*\.newmainfilename',
)
