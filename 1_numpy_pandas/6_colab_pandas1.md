# Colab e facilidades em Pandas

## Em Pandas
```py
from google.colab import data_table
from vega_datasets import data
```

```py
carros = data.cars()
carros
```

```py
carros[cars['Miles_per_Gallon'] > 20.0]
```


## No Colab
```py
from google.colab import data_table
data_table.enable_dataframe_formatter()
```

```py
from google.colab import data_table
from vega_datasets import data
```

```py
carros = data.cars()
carros
```

