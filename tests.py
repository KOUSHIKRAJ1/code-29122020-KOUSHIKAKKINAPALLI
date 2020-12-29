import unittest #i am using unittest module which has built in testing framework which consists of set of rules to be followed while building test cases and
#test runner for running test cases automatically
#i have taken three json files present in json folder for testing
import BMI_Calculator
#design test class which inherits the properties from TestCase class
class Test_BMI_Calculator(unittest.TestCase):
    def test_bmi(self):
        #get bmi details of all three files
        files=["json_files/person_data1.json","json_files/person_data2.json","json_files/person_data3.json"]
        expected_result=[1,2,2]
        #list comprehension is used for loading data from multiple json files
        person_details=[BMI_Calculator.load_json_data(file) for file in files]
        for i in range(len(person_details)):
            bmi_details=BMI_Calculator.CalculateBMI(person_details[i])
            self.assertEqual(BMI_Calculator.count_overweight_persons(bmi_details),expected_result[i]) #testing count of overweight persons with expected result
if __name__=="__main__":
    unittest.main() #execute the test cases by calling test_bmi() from the above class
        
