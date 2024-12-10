### Dataset Overview

The dataset captures various aspects of life satisfaction and well-being across 165 countries over the years, from 2005 to 2023. It includes measurements such as the "Life Ladder," which is a subjective measure of life satisfaction, along with factors like GDP per capita, social support, freedom of choice, generosity, perceptions of corruption, positive affect, and negative affect. 

### Key Insights and Trends

#### General Trends in Life Satisfaction

The "Life Ladder" represents a scale where higher values indicate greater life satisfaction. The average "Life Ladder" score across all countries is approximately 5.48, suggesting a moderate level of life satisfaction globally. Over the years, from a minimum of 1.28 in 2005 to a maximum of 8.02 in 2023, the dataset reflects a general upward trend in life satisfaction scores.

- **2005 to 2011:** There is a gradual increase in life satisfaction, suggesting improvements in various socio-economic factors as many countries were recovering from earlier economic shocks.
  
- **2012 to 2019:** The averages rise significantly, with countries enjoying better economies, more social support, and increased freedom of choice. This trend supports the idea that greater economic stability correlates with higher happiness levels.

- **2020 Onwards:** While the dataset ends in 2023, patterns may indicate impacts from global crises (like the COVID-19 pandemic) that could disrupt previous advancements in life satisfaction.

#### Economic Factors

The dataset suggests a correlation between GDP per capita and life satisfaction. The average logarithmic GDP score reflects economic wealth, suggesting that as the GDP increases, so does life satisfaction.

- Countries with higher GDP per capita tend to also report higher "Life Ladder" scores. This follows the principle that economic security can foster a better quality of life.

#### Social Support and Healthy Life Expectancy

The factors of social support and healthy life expectancy also show an interesting relationship with life satisfaction.

- **Social Support:** This averages around 0.65 in the dataset, indicating that a majority of individuals feel they have support systems available to them. Countries emphasizing community ties and healthcare systems see more stability in happiness levels.
  
- **Healthy Life Expectancy:** This factor indicates how long individuals can expect to lead a healthy life. Higher ratings here correspond with higher life ladder scores, reinforcing the importance of health as a foundation for happiness.

#### Freedom, Generosity, and Corruption Perceptions

These factors also reveal significant insights:

- **Freedom to Make Life Choices:** Countries that provide citizens with more freedom tend to see an increase in the life ladder score, indicating a strong connection between autonomy and satisfaction.

- **Generosity:** This averages around 0.26, showing room for improvement in philanthropy across the countries surveyed. However, it reinforces the idea that more generous societies tend to correlate with higher happiness levels.

- **Perceptions of Corruption:** On average, low perceptions of corruption (0.74) coincide with higher life satisfaction, suggesting that good governance and transparency can lead to greater societal trust and happiness.

### Conclusion

In summary, the dataset illustrates clear trends linking economic prosperity, social support, healthcare, and freedom with life satisfaction across multiple countries. Despite some challenging periods, the upward trajectory over the years indicates that several nations are fostering environments conducive to well-being. However, challenges remain, particularly concerning perceptions of corruption and the need for greater generosity in societal structures. Balancing these factors can potentially enhance life satisfaction worldwide, paving the way for happier and healthier communities.# Data Analysis Report

## Numerical Summary Statistics

|       |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |     Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|---------------:|----------------------------:|------------------:|------------------:|
| count | 2363       |    2363       |           2335       |      2350        |                         2300       |                    2327        | 2282           |                 2238        |       2339        |      2347         |
| mean  | 2014.76    |       5.48357 |              9.39967 |         0.809369 |                           63.4018  |                       0.750282 |    9.77213e-05 |                    0.743971 |          0.651882 |         0.273151  |
| std   |    5.05944 |       1.12552 |              1.15207 |         0.121212 |                            6.84264 |                       0.139357 |    0.161388    |                    0.184865 |          0.10624  |         0.0871311 |
| min   | 2005       |       1.281   |              5.527   |         0.228    |                            6.72    |                       0.228    |   -0.34        |                    0.035    |          0.179    |         0.083     |
| 25%   | 2011       |       4.647   |              8.5065  |         0.744    |                           59.195   |                       0.661    |   -0.112       |                    0.687    |          0.572    |         0.209     |
| 50%   | 2015       |       5.449   |              9.503   |         0.8345   |                           65.1     |                       0.771    |   -0.022       |                    0.7985   |          0.663    |         0.262     |
| 75%   | 2019       |       6.3235  |             10.3925  |         0.904    |                           68.5525  |                       0.862    |    0.09375     |                    0.86775  |          0.737    |         0.326     |
| max   | 2023       |       8.019   |             11.676   |         0.987    |                           74.6     |                       0.985    |    0.7         |                    0.983    |          0.884    |         0.705     |

## Categorical Summary Statistics

|        | Country name   |
|:-------|:---------------|
| count  | 2363           |
| unique | 165            |
| top    | Argentina      |
| freq   | 18             |

## LLM Suggested Analyses

### LLM suggests the following analyses:

Based on the summary statistics provided for the happiness dataset, there are several avenues for further analysis that could yield valuable insights. Here are some suggestions along with considerations for cluster analysis:

### Further Analyses

1. **Correlation Analysis:**
   - Investigate the relationships between different numerical variables using correlation coefficients. This can highlight which factors are strongly related to Life Ladder and thus contribute to happiness.

2. **Time Series Analysis:**
   - Analyze trends over time, particularly in Life Ladder, GDP per capita, and social support. This can help to understand how these factors have changed over the years and their impact on overall happiness.

3. **Regression Analysis:**
   - Carry out multiple regression analysis with Life Ladder as the dependent variable. This could

## Missing Values

|                                  |   0 |
|:---------------------------------|----:|
| Country name                     |   0 |
| year                             |   0 |
| Life Ladder                      |   0 |
| Log GDP per capita               |  28 |
| Social support                   |  13 |
| Healthy life expectancy at birth |  63 |
| Freedom to make life choices     |  36 |
| Generosity                       |  81 |
| Perceptions of corruption        | 125 |
| Positive affect                  |  24 |
| Negative affect                  |  16 |

## Correlation Matrix

|                                  |       year |   Life Ladder |   Log GDP per capita |   Social support |   Healthy life expectancy at birth |   Freedom to make life choices |   Generosity |   Perceptions of corruption |   Positive affect |   Negative affect |
|:---------------------------------|-----------:|--------------:|---------------------:|-----------------:|-----------------------------------:|-------------------------------:|-------------:|----------------------------:|------------------:|------------------:|
| year                             |  1         |     0.0468461 |          0.0801038   |       -0.0430737 |                          0.168026  |                       0.232974 |  0.0308644   |                  -0.0821355 |         0.0130525 |         0.207642  |
| Life Ladder                      |  0.0468461 |     1         |          0.783556    |        0.722738  |                          0.714927  |                       0.53821  |  0.177398    |                  -0.430485  |         0.515283  |        -0.352412  |
| Log GDP per capita               |  0.0801038 |     0.783556  |          1           |        0.685329  |                          0.819326  |                       0.364816 | -0.000765985 |                  -0.353893  |         0.230868  |        -0.260689  |
| Social support                   | -0.0430737 |     0.722738  |          0.685329    |        1         |                          0.597787  |                       0.404131 |  0.0652399   |                  -0.22141   |         0.424524  |        -0.454878  |
| Healthy life expectancy at birth |  0.168026  |     0.714927  |          0.819326    |        0.597787  |                          1         |                       0.375745 |  0.0151682   |                  -0.30313   |         0.217982  |        -0.15033   |
| Freedom to make life choices     |  0.232974  |     0.53821   |          0.364816    |        0.404131  |                          0.375745  |                       1        |  0.321396    |                  -0.466023  |         0.578398  |        -0.278959  |
| Generosity                       |  0.0308644 |     0.177398  |         -0.000765985 |        0.0652399 |                          0.0151682 |                       0.321396 |  1           |                  -0.270004  |         0.300608  |        -0.0719746 |
| Perceptions of corruption        | -0.0821355 |    -0.430485  |         -0.353893    |       -0.22141   |                         -0.30313   |                      -0.466023 | -0.270004    |                   1         |        -0.274208  |         0.265555  |
| Positive affect                  |  0.0130525 |     0.515283  |          0.230868    |        0.424524  |                          0.217982  |                       0.578398 |  0.300608    |                  -0.274208  |         1         |        -0.334451  |
| Negative affect                  |  0.207642  |    -0.352412  |         -0.260689    |       -0.454878  |                         -0.15033   |                      -0.278959 | -0.0719746   |                   0.265555  |        -0.334451  |         1         |

### Strong Positive Correlations (>= 0.75)

- **Healthy life expectancy at birth and Log GDP per capita**: 0.82
- **Log GDP per capita and Life Ladder**: 0.78

### Strong Negative Correlations (<= -0.2)



## Outliers

- **year**: 0 potential outliers
- **Life Ladder**: 2 potential outliers
- **Log GDP per capita**: 1 potential outliers
- **Social support**: 48 potential outliers
- **Healthy life expectancy at birth**: 20 potential outliers
- **Freedom to make life choices**: 16 potential outliers
- **Generosity**: 39 potential outliers
- **Perceptions of corruption**: 194 potential outliers
- **Positive affect**: 9 potential outliers
- **Negative affect**: 31 potential outliers


## Frequency Analysis (Top 5 Values for Categorical Columns)

### Column: Country name

| Country name   |   count |
|:---------------|--------:|
| Argentina      |      18 |
| Costa Rica     |      18 |
| Brazil         |      18 |
| Bolivia        |      18 |
| Bangladesh     |      18 |

## Correlation Head Map 

![Correlation Head Map](/happiness/corr_heat_map.png)

## BoxPlot 

![BoxPlot](/happiness/boxplot.png)

## Histograms 

![Histograms](/happiness/histograms.png)

