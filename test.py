# Orlando Zuniga API for C.H. Robinson
# 11-28-2020 
#Performs unit tests on the shortest_path algorithm used to return a list of countries one must travel through.
# test.py
import unittest
import path_solver

'''
Tests to make sure that each list returned from shortest_path is the contains the correct list.
'''
class test_lists(unittest.TestCase):
    
    def test_equals(self):
        countries = path_solver.graph_loader('countries.json')

        can_list = ['USA', 'CAN']
        usa_list = ['USA']
        mex_list = ['USA', 'MEX']
        gtm_list = ['USA', 'MEX', 'GTM']
        blz_list = ['USA', 'MEX', 'BLZ']
        slv_list = ['USA', 'MEX', 'GTM', 'SLV']
        hnd_list = ['USA', 'MEX', 'GTM', 'HND']
        nic_list = ['USA', 'MEX', 'GTM', 'HND', 'NIC']
        cri_list = ['USA', 'MEX', 'GTM', 'HND', 'NIC', 'CRI']
        pan_list = ['USA', 'MEX', 'GTM', 'HND', 'NIC', 'CRI', 'PAN']
        
        all_lists = []
        #Creates a list of lists always starting at the USA and ending in the desired location
        for country in countries:
            route = path_solver.shortest_path(countries, start = "USA", end = country)
            all_lists.append(route)
        #Goes through each list and tests for equality
        self.assertEqual(can_list, all_lists[0])
        self.assertEqual(usa_list, all_lists[1])
        self.assertEqual(mex_list, all_lists[2])
        self.assertEqual(gtm_list, all_lists[3])
        self.assertEqual(blz_list, all_lists[4])
        self.assertEqual(slv_list, all_lists[5])
        self.assertEqual(hnd_list, all_lists[6])
        self.assertEqual(nic_list, all_lists[7])
        self.assertEqual(cri_list, all_lists[8])
        self.assertEqual(pan_list, all_lists[9])
        #Testing for when the destination is not valid should return None.
        self.assertEqual(None, path_solver.shortest_path(countries, start = "USA", end = "test"))

if __name__ == "__main__":
    unittest.main()

