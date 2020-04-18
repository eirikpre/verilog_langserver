from pygls.server import LanguageServer
from pygls.types import WorkspaceSymbolParams, DocumentSymbolParams, TextDocumentIdentifier
from pygls.features import WORKSPACE_SYMBOL, DOCUMENT_SYMBOL, INITIALIZED
from pygls.workspace import Document
from pygls.uris import to_fs_path

from .database import Database
from .verilog_parser.workspace_symbols import parse as parse_workspace_symbols


class HdlLanguageServer(LanguageServer):
    CMD_BUILD_INDEX = 'buildIndex'

    def __init__(self):
        super().__init__()


# Initialize Server
server = HdlLanguageServer()
# Initialize Database
database = Database()


@server.feature(INITIALIZED)
def indexing(ls):
    ls.show_message("Received initialized")


@server.thread()
@server.command(server.CMD_BUILD_INDEX)
def buildIndex(ls):
    ls.show_message("Building index now!")


@server.feature(DOCUMENT_SYMBOL)
async def document_symbols(ls, params: DocumentSymbolParams):
    # TODO Not ready yet
    # doc: Document = ls.workspace.get_document(params.textDocument.uri)
    # items = parse_document_symbols(doc.source)
    path = to_fs_path(params.textDocument.uri)
    return parse_workspace_symbols(path)

@server.feature(WORKSPACE_SYMBOL)
async def workspace_symbols(ls, params: WorkspaceSymbolParams):
    query = params.query
    if database.declarations == []:
        return None
    return database.declarations
