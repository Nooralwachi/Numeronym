
from absl.testing import absltest
from absl.testing import parameterized
from rotate import rotate_return
class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        {
            'input': 'kubernetes',
            'want': 'k8s',
        }, {
            'input': 'cat',
            'want': 'c1t',
        })
    def testSalutations(self, input, want):
        self.assertEqual(calc_numeronym(input), want)


if __name__ == '__main__':
    absltest.main()