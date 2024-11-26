import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular.checks import MixedNulls

data = pd.read_csv('heart.csv')


MixedNulls().run(data).save_as_html('mixed_null')