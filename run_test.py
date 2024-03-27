'''
Author: Donald duck tang5722917@163.com
Date: 2024-03-26 10:13:37
LastEditors: Donald duck tang5722917@163.com
LastEditTime: 2024-03-26 16:48:58
FilePath: \spice_netlist_front_end\run_test.py
Description: 
Copyright (c) 2024 by Donald duck email: tang5722917@163.com, All Rights Reserved.
'''

import sys
import pytest
import pytest_html
print("pytest version: "+pytest.__version__)
print("pytest _html version: "+pytest_html.__version__)
sys.path.append("./test")
sys.path.append("./src")
sys.path.append("./test/ptest/Base/")
pytest_html_arg = ["--html=report.html","--self-contained-html"]
retcode = pytest.main([pytest_html_arg[0],pytest_html_arg[1],"./test/ptest/Netlist/"])
