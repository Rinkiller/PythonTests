from matrix import Matrix
import unittest

class TestCaseMatrix(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError , Matrix , None)
    
    def test_add(self):
        self.assertEqual(Matrix([[1,2],[3,4]]) + Matrix([[0,1],[2,5]]) , Matrix([[1, 3],[5, 9]]))

    def test_add_raises(self):
        with self.assertRaises(ValueError): 
            Matrix([[1,2],[3,4]]) + Matrix([[0,1],[2,5],[2,3]])
            Matrix([1,2]) + Matrix([[1,2],[2,3]])

    def test_mull(self):
        self.assertEqual(Matrix([[1,2],[3,4]]) * Matrix([[5,6],[7,8]]) , Matrix([[19, 22],[43, 50]]))

    def test_eq_matrix(self):
        self.assertTrue(Matrix([[1, 1], [1, 1]]) == Matrix([[1, 1], [1, 1]]))

    def test_gt_matrix(self):
        self.assertTrue(Matrix([[1, 1], [1, 1]]) > Matrix([[0, 1], [1, 0]]))

if __name__ == "__main__":
    unittest.main(verbosity=True)