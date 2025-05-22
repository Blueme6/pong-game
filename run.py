# A simple workaround that prevented pygbag to host pygame game through github codespaces.

import asyncio
import sys

from pygbag.app import main_run, set_args
from pygbag import testserver

old_run_code_server = testserver.run_code_server

def run_code_server(args, cc):
    cc["proxy"] = ""
    return old_run_code_server(args, cc)

testserver.run_code_server = run_code_server

if __name__ == "__main__":
    sys.argv.append("main")
    app_folder, mainscript = set_args("main")
    asyncio.run(main_run(app_folder, mainscript))
