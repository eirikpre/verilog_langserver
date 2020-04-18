############################################################################
# Copyright(c) Open Law Library. All rights reserved.                      #
# See ThirdPartyNotices.txt in the project root for additional notices.    #
#                                                                          #
# Licensed under the Apache License, Version 2.0 (the "License")           #
# you may not use this file except in compliance with the License.         #
# You may obtain a copy of the License at                                  #
#                                                                          #
#     http: // www.apache.org/licenses/LICENSE-2.0                         #
#                                                                          #
# Unless required by applicable law or agreed to in writing, software      #
# distributed under the License is distributed on an "AS IS" BASIS,        #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
# See the License for the specific language governing permissions and      #
# limitations under the License.                                           #
############################################################################
import unittest
import asyncio
import os
from pathlib import Path
from threading import Thread

from pygls import features
from pygls.server import LanguageServer
from pygls.features import DOCUMENT_SYMBOL
from pygls.types import DocumentSymbolParams, InitializeParams, TextDocumentIdentifier
from pygls.workspace import Document

CALL_TIMEOUT = 2

from verilog_langserver.server import server

class TestServer(unittest.TestCase):

    def setUp(self):
        self.folder = Path(__file__).parent / 'verilog'
        # Client to Server pipe
        csr, csw = os.pipe()
        # Server to client pipe
        scr, scw = os.pipe()

        # Server
        self.server = server
        # Client
        self.client = LanguageServer(asyncio.new_event_loop())

        server_thread = Thread(target=self.server.start_io, args=(
            os.fdopen(csr, 'rb'), os.fdopen(scw, 'wb')
        ))
        server_thread.daemon = True
        server_thread.start()

        client_thread = Thread(target=self.client.start_io, args=(
            os.fdopen(scr, 'rb'), os.fdopen(csw, 'wb')))
        client_thread.daemon = True
        client_thread.start()
        # Initialize server
        self.server.lsp.bf_initialize(InitializeParams(
            process_id=1234,
            root_uri=self.folder.as_uri(),
            capabilities=None
        ))
        print("Setup done!")


    def tearDown(self):
        shutdown_response = self.client.lsp.send_request(
            features.SHUTDOWN).result(timeout=CALL_TIMEOUT)
        assert shutdown_response is None
        self.client.lsp.notify(features.EXIT)


    def test_document_symbol(self):
        items = self.client.lsp.send_request(
            DOCUMENT_SYMBOL,
            DocumentSymbolParams(
                TextDocumentIdentifier((self.folder / 'class_example.sv').as_uri())
            )).result()
        names = [i.name for i in items]

        assert "tb" in names
        assert "Packet" in names