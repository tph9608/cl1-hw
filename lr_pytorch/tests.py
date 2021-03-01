import unittest
import tempfile
import torch
import numpy as np

from torch.nn import BCELoss as Loss
from torch.optim import SGD as Opt

from lr_pytorch import SportsDataset, read_dataset, step, SimpleLogreg
from numpy import array


vocab = tempfile.TemporaryFile(mode='r+', encoding="utf-8", prefix="public_vocab")
vocab.write("BIAS_CONSTANT\t0\nA\t1\nB\t2\nC\t2\nD\t1")
positive = tempfile.TemporaryFile(mode='r+', encoding="utf-8", prefix="public_pos")
positive.write("A:4 B:3 C:1")
negative = tempfile.TemporaryFile(mode='r+', encoding="utf-8", prefix="public_neg")
negative.write("B:1 C:3 D:4")
positive.seek(0)
negative.seek(0)
vocab.seek(0)

class TestPublic(unittest.TestCase):
    def setUp(self):
        self.raw_data = array([[1., 4., 3., 1., 0.],
                              [0., 0., 1., 3., 4.]])
        self.data = torch.from_numpy(self.raw_data).float()

        labels = array([[1], [0]])
        self.labels = torch.from_numpy(labels).float()

        self.model = SimpleLogreg(5)

        with torch.no_grad():
            self.model.linear.bias[0] = 0.5
            self.model.linear.weight.fill_(0)
            self.model.linear.weight[0,0] = 1
            self.model.linear.weight[0,4] = -1

    def assertListAlmostEqual(self, a, b):
        self.assertEqual(len(a), len(b))
        for i in range(len(a)):
            np.testing.assert_almost_equal(a[i], b[i], decimal=5)

    def test_data(self):
        s = read_dataset(positive, negative, vocab)
        for ii in range(2):
            for jj in range(5):
                self.assertAlmostEqual(s[ii][jj], self.raw_data[ii][jj])

    def test_forward(self):
        self.assertAlmostEqual(0.817574441432952, float(self.model.forward(self.data)[0]))
        self.assertAlmostEqual(0.02931223064661026, float(self.model.forward(self.data)[1]))

    def test_step(self):
        optimizer = Opt(self.model.parameters(), lr=0.1)
        criterion = Loss()
        step(0, 0, self.model, optimizer, criterion, self.data, self.labels)

        weight, bias = list(self.model.parameters())

        true_weight = [1.009121298789978, 0.03648511320352554, 0.025898221880197525,
                       0.004724443424493074, -1.0058624744415283]
        true_bias = [0.507655680179596]

        self.assertListAlmostEqual(weight.view(-1).tolist(), true_weight)
        self.assertListAlmostEqual(bias.view(-1).tolist(), true_bias)


if __name__ == '__main__':
    unittest.main()
