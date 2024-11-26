# Step 1: Install deepchecks if you haven't already
# pip install deepchecks --upgrade

# Step 2: Import the necessary libraries
import pandas as pd
from deepchecks.tabular import Dataset
from deepchecks.tabular.suites import data_integrity
from deepchecks.tabular.checks import MixedNulls

# Step 3: Load your dataset (replace 'your_data.csv' with your actual file path)
data = pd.read_csv('heart.csv')

# Step 4: Set the label column and define the categorical features
da_col = 'HeartDisease'


# Step 5: Create a Deepchecks Dataset object
ds = Dataset(data, label=da_col)

# Step 6: Run the data integrity suite
suite = data_integrity()
suite_result = suite.run(ds)

# Step 7: Display the results (in Jupyter Notebook) or save as HTML
# Display in notebook
# suite_result.show()

# Save as HTML report
suite_result.save_as_html('data_integrity_report.html')
