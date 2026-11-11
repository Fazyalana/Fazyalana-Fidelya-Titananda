
import unittest
import importlib.util

spec = importlib.util.spec_from_file_location(
    "employee", "11_3_employee.py"
)
modul = importlib.util.module_from_spec(spec)
spec.loader.exec_module(modul)

Employee = modul.Employee


class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.karyawan = Employee("Vrysa", "Dewi", 50000)

    def test_give_default_raise(self):
        self.karyawan.give_raise()
        self.assertEqual(self.karyawan.annual_salary, 55000)

    def test_give_custom_raise(self):
        self.karyawan.give_raise(10000)
        self.assertEqual(self.karyawan.annual_salary, 60000)


if __name__ == '__main__':
    unittest.main()

