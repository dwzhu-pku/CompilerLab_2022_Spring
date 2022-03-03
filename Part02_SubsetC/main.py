import myparser
import os

testcase = os.listdir("../test_subsetc")
with open("../test_subsetc/basic_04_var_list", 'r', encoding="utf-8") as fin:
    s = fin.read()
    result = myparser.cparser.parse(s)
    if result is not None:
        result.show(0)