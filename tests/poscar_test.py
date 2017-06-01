# -*- coding:utf-8 -*-
'''
PosCar单元测试
'''

import unittest

from vaspy.atomco import PosCar
from tests import abs_path


class PosCarTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = True

    def test_get_poscar_content(self):
        " Make sure we can get the correct poscar content. "
        filename = abs_path + "/testdata/POSCAR"
        poscar = PosCar(filename)

        ref_content = """Created by VASPy\n 1.000000000\n    7.29321435   -4.21073927    0.00000000\n    0.00000000    8.42147853    0.00000000\n   -0.00000000    0.00000000   16.87610843\nPt   \n   36\nSelective Dynamics\nDirect\n    0.244666665792    0.223999996980    0.135815443038F    F    F    \n    0.022444443570    0.112888885869    0.271630886077T    T    T    \n    0.133555554681    0.001777774758    0.000000000000F    F    F    \n    0.133555554681    0.001777774758    0.407446329115T    T    T    \n    0.577999999126    0.223999996980    0.135815443038F    F    F    \n    0.355777776904    0.112888885869    0.271630886077T    T    T    \n    0.466888888015    0.001777774758    0.000000000000F    F    F    \n    0.466888888015    0.001777774758    0.407446329115T    T    T    \n    0.911333332459    0.223999996980    0.135815443038F    F    F    \n    0.689111110237    0.112888885869    0.271630886077T    T    T    \n    0.800222221348    0.001777774758    0.000000000000F    F    F    \n    0.800222221348    0.001777774758    0.407446329115T    T    T    \n    0.244666665792    0.557333330313    0.135815443038F    F    F    \n    0.022444443570    0.446222219202    0.271630886077T    T    T    \n    0.133555554681    0.335111108091    0.000000000000F    F    F    \n    0.133555554681    0.335111108091    0.407446329115T    T    T    \n    0.577999999126    0.557333330313    0.135815443038F    F    F    \n    0.355777776904    0.446222219202    0.271630886077T    T    T    \n    0.466888888015    0.335111108091    0.000000000000F    F    F    \n    0.466888888015    0.335111108091    0.407446329115T    T    T    \n    0.911333332459    0.557333330313    0.135815443038F    F    F    \n    0.689111110237    0.446222219202    0.271630886077T    T    T    \n    0.800222221348    0.335111108091    0.000000000000F    F    F    \n    0.800222221348    0.335111108091    0.407446329115T    T    T    \n    0.244666665792    0.890666663647    0.135815443038F    F    F    \n    0.022444443570    0.779555552536    0.271630886077T    T    T    \n    0.133555554681    0.668444441424    0.000000000000F    F    F    \n    0.133555554681    0.668444441424    0.407446329115T    T    T    \n    0.577999999126    0.890666663647    0.135815443038F    F    F    \n    0.355777776904    0.779555552536    0.271630886077T    T    T    \n    0.466888888015    0.668444441424    0.000000000000F    F    F    \n    0.466888888015    0.668444441424    0.407446329115T    T    T    \n    0.911333332459    0.890666663647    0.135815443038F    F    F    \n    0.689111110237    0.779555552536    0.271630886077T    T    T    \n    0.800222221348    0.668444441424    0.000000000000F    F    F    \n    0.800222221348    0.668444441424    0.407446329115T    T    T    \n"""

        ret_content = poscar.get_poscar_content()

        self.assertEqual(ref_content, ret_content)

    def test_get_xyz_content(self):
        " Make sure we can get correct xyz file content from poscar. "
        filename = abs_path + "/testdata/POSCAR"
        poscar = PosCar(filename)

        ref_content = """          36\nSTEP =        1\nPt   0.244666665792   0.22399999698  0.135815443038\nPt    0.02244444357  0.112888885869  0.271630886077\nPt   0.133555554681  0.001777774758             0.0\nPt   0.133555554681  0.001777774758  0.407446329115\nPt   0.577999999126   0.22399999698  0.135815443038\nPt   0.355777776904  0.112888885869  0.271630886077\nPt   0.466888888015  0.001777774758             0.0\nPt   0.466888888015  0.001777774758  0.407446329115\nPt   0.911333332459   0.22399999698  0.135815443038\nPt   0.689111110237  0.112888885869  0.271630886077\nPt   0.800222221348  0.001777774758             0.0\nPt   0.800222221348  0.001777774758  0.407446329115\nPt   0.244666665792  0.557333330313  0.135815443038\nPt    0.02244444357  0.446222219202  0.271630886077\nPt   0.133555554681  0.335111108091             0.0\nPt   0.133555554681  0.335111108091  0.407446329115\nPt   0.577999999126  0.557333330313  0.135815443038\nPt   0.355777776904  0.446222219202  0.271630886077\nPt   0.466888888015  0.335111108091             0.0\nPt   0.466888888015  0.335111108091  0.407446329115\nPt   0.911333332459  0.557333330313  0.135815443038\nPt   0.689111110237  0.446222219202  0.271630886077\nPt   0.800222221348  0.335111108091             0.0\nPt   0.800222221348  0.335111108091  0.407446329115\nPt   0.244666665792  0.890666663647  0.135815443038\nPt    0.02244444357  0.779555552536  0.271630886077\nPt   0.133555554681  0.668444441424             0.0\nPt   0.133555554681  0.668444441424  0.407446329115\nPt   0.577999999126  0.890666663647  0.135815443038\nPt   0.355777776904  0.779555552536  0.271630886077\nPt   0.466888888015  0.668444441424             0.0\nPt   0.466888888015  0.668444441424  0.407446329115\nPt   0.911333332459  0.890666663647  0.135815443038\nPt   0.689111110237  0.779555552536  0.271630886077\nPt   0.800222221348  0.668444441424             0.0\nPt   0.800222221348  0.668444441424  0.407446329115\n"""

        ret_content = poscar.get_xyz_content()

        self.assertEqual(ref_content, ret_content)

if "__main__" == __name__: 
    suite = unittest.TestLoader().loadTestsFromTestCase(PosCarTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 

