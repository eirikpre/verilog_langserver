from pygls.server import LanguageServer
from pygls.types import WorkspaceSymbolParams
from pygls.features import WORKSPACE_SYMBOL

from .verilog_parser.parser import Parser



server = LanguageServer()


@server.feature(WORKSPACE_SYMBOL)
def workspace_symbols(params: WorkspaceSymbolParams):
    pass


server.start_tcp('localhost', 8080)