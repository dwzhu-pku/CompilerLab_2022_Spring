import myparser

with open("../test_subsetc/basic_03_param_list", 'r', encoding="utf-8") as fin:
    s = fin.read()
    result = myparser.cparser.parse(s)
    if result is not None:
        result.show(0)