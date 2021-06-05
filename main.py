# %% [markdown]
# # Project C111
# %% [markdown]
# ## Getting Data

# %%
import statistics
import random

import pandas
import plotly.graph_objects as go
import plotly.figure_factory as ff

data_frame = pandas.read_csv("data.csv");
reading_time_data = list(data_frame["reading_time"])
reading_time_data_mean = statistics.mean(reading_time_data)

fig = ff.create_distplot([reading_time_data], ["Reading Time"])
fig.show()

population_mean = statistics.mean(reading_time_data)

print(f"Population Mean: {population_mean}")

# %% [markdown]
# ## Function for Sampling Mean

# %%
def sample_mean(counter: int, data: list):
    dataset = []

    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

# %% [markdown]
# # Getting Sample Mean

# %%
mean_list = []

for i in range(0, 100):
  mean_value = sample_mean(30, reading_time_data)
  mean_list.append(mean_value)

# %% [markdown]
# # Getting Standard Devivation Range 1-3

# %%
standard_deviation = statistics.stdev(reading_time_data)
sampled_mean = statistics.mean(mean_list)

stdev1_start, std1_end = sampled_mean - standard_deviation, sampled_mean + standard_deviation
stdev2_start, std2_end = sampled_mean - (2 * standard_deviation), sampled_mean + (2 * standard_deviation)
stdev3_start, std3_end = sampled_mean - (3 * standard_deviation), sampled_mean + (3 * standard_deviation)

# %% [markdown]
# ## Showing Chart with Standard Deviation and Sample Mean

# %%
chart = ff.create_distplot([mean_list], ["Reading Time Sample Mean"])

chart.add_trace(go.Scatter(x=[stdev1_start, stdev1_start], y=[0,0.8], mode="lines", name="Standard Devivation 1 Start"))
chart.add_trace(go.Scatter(x=[std1_end, std1_end], y=[0,0.8], mode="lines", name="Standard Devivation 1 End"))

chart.add_trace(go.Scatter(x=[stdev2_start, stdev2_start], y=[0,0.8], mode="lines", name="Standard Devivation 2 Start"))
chart.add_trace(go.Scatter(x=[std2_end, std2_end], y=[0,0.8], mode="lines", name="Standard Devivation 2 End"))

chart.add_trace(go.Scatter(x=[stdev3_start, stdev3_start], y=[0,0.8], mode="lines", name="Standard Devivation 3 Start"))
chart.add_trace(go.Scatter(x=[std3_end, std3_end], y=[0,0.8], mode="lines", name="Standard Devivation 3 End"))

chart.show()

# %% [markdown]
# ## Getting Z-Score

# %%
z_score = (sampled_mean - reading_time_data_mean) / standard_deviation
print(f"Z-Score: {z_score}")
