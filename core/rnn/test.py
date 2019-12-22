from keras.models import load_model
from os.path import join
import argparse
import numpy as np
import os
from core.utils import settings
from core.rnn.data_loader import PairTextDataset, DataLoader

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='rnn', help="models used")
parser.add_argument('--no-cuda', action='store_true', default=False, help='Disables CUDA training.')
parser.add_argument('--seed', type=int, default=37, help='Random seed.')
parser.add_argument('--epochs', type=int, default=30, help='Number of epochs to train.')
parser.add_argument('--lr', type=float, default=5e-2, help='Initial learning rate.')
parser.add_argument('--weight-decay', type=float, default=1e-3,
                    help='Weight decay (L2 loss on parameters).')
parser.add_argument('--dropout', type=float, default=0.2,
                    help='Dropout rate (1 - keep probability).')
parser.add_argument('--embedding-size', type=int, default=128,
                    help="Embeding size for LSTM layer")
parser.add_argument('--hidden-size', type=int, default=32,
                    help="Hidden size for LSTM layer")
parser.add_argument('--max-sequence-length', type=int, default=17,
                    help="Max sequence length for raw sequences")
parser.add_argument('--max-key-sequence-length', type=int, default=8,
                    help="Max key sequence length for key sequences")
parser.add_argument('--batch', type=int, default=32, help="Batch size")
parser.add_argument('--dim', type=int, default=128, help="Embedding dimension")
parser.add_argument('--instance-normalization', action='store_true', default=True,
                    help="Enable instance normalization")
parser.add_argument('--shuffle', action='store_true', default=True, help="Shuffle dataset")
parser.add_argument('--file-dir', type=str, default=settings.VENUE_DATA_DIR, help="Input file directory")
parser.add_argument('--train-ratio', type=float, default=70, help="Training ratio (0, 100)")
parser.add_argument('--test-ratio', type=float, default=30, help="Test ratio (0, 100)")
parser.add_argument('--class-weight-balanced', action='store_true', default=False,
                    help="Adjust weights inversely proportional"
                         " to class frequencies in the input data")
parser.add_argument('--multiple', type=int, default=16, help="decide how many times to multiply a scalar input")

args = parser.parse_args()

def main(args=args):
    np.random.seed(args.seed)
    dataset = PairTextDataset(args.file_dir, args.seed, args.shuffle, args.max_sequence_length,
                              args.max_key_sequence_length, args.batch, args.multiple)
    test_loader = dataset.get_test_loader()

    model = load_model(join(join(settings.OUT_DIR, 'rnn-model'), 'model.h5'))
    pred = model.predict([test_loader.data['keyword_mag'],
                            test_loader.data['keyword_aminer'],
                            test_loader.data['jaccard'],
                            test_loader.data['mag'],
                            test_loader.data['aminer'],
                            test_loader.data['inverse']], 
                            verbose=1)
    print(np.array([1 if x>0.5 else 0 for x in pred]))
    print(test_loader.data['labels'])
    score = model.evaluate([test_loader.data['keyword_mag'],
                            test_loader.data['keyword_aminer'],
                            test_loader.data['jaccard'],
                            test_loader.data['mag'],
                            test_loader.data['aminer'],
                            test_loader.data['inverse']], 
                            test_loader.data['labels'], 
                            verbose=1)
    print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

if __name__ == '__main__':
    main(args=args)
