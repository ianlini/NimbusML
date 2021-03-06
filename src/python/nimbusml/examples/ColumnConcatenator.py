###############################################################################
# ColumnConcatenator
import numpy
from nimbusml import FileDataStream
from nimbusml.datasets import get_dataset
from nimbusml.preprocessing.schema import ColumnConcatenator

# data input (as a FileDataStream)
path = get_dataset('infert').as_filepath()

data = FileDataStream.read_csv(path, sep=',', numeric_dtype=numpy.float32)
print(data.head())
#    age  case education  induced  parity  pooled.stratum  row_num  ...
# 0  26.0   1.0    0-5yrs      1.0     6.0             3.0      1.0  ...
# 1  42.0   1.0    0-5yrs      1.0     1.0             1.0      2.0  ...
# 2  39.0   1.0    0-5yrs      2.0     6.0             4.0      3.0  ...
# 3  34.0   1.0    0-5yrs      2.0     4.0             2.0      4.0  ...
# 4  35.0   1.0   6-11yrs      1.0     3.0            32.0      5.0  ...

# transform usage
xf = ColumnConcatenator(columns={'features': ['age', 'parity', 'induced']})

# fit and transform
features = xf.fit_transform(data)

# print features
print(features.head())
# Feature is a vectory type column, when a dataset with vectortype column is
# the final output, the vector column will convert into multiple columns for
# each slot.
#    age  case education  features.age  features.induced  features.parity  ...
# 0  26.0   1.0    0-5yrs          26.0               1.0              6.0  ...
# 1  42.0   1.0    0-5yrs          42.0               1.0              1.0  ...
# 2  39.0   1.0    0-5yrs          39.0               2.0              6.0  ...
# 3  34.0   1.0    0-5yrs          34.0               2.0              4.0  ...
# 4  35.0   1.0   6-11yrs          35.0               1.0              3.0  ...
