# Colab e facilidades em Pandas

## Em Pandas
```
from google.colab import data_table
from vega_datasets import data
```

carros = data.cars()
carros



carros[cars['Miles_per_Gallon'] > 20.0]

====

## No Colab
====
from google.colab import data_table
data_table.enable_dataframe_formatter()

====
from google.colab import data_table
from vega_datasets import data

carros = data.cars()
carros

====
