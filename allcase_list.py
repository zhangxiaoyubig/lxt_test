# coding=utf-8

import  sys
sys.path.append("C:\Python27\selenium\webdriver\test_case")

from test_case import *

def caselist():
    alltestnames = [
        star_addSalespersonunit.addSaleper,
        star_searchunitest.Sale,
        # newgroupunitest.Newgroup
        ]
    print  "success  read case list"

    return  alltestnames