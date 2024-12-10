### Story of the Dataset

In the realm of literature, the dataset presents a rich tapestry of 10,000 books, each a doorway to different worlds and ideas. Painstakingly compiled, it catalogues a mélange of popular and classic titles, authors, and their reception among readers.

#### Overview of the Dataset

The dataset encapsulates fundamental details about each book, including identifiers, publication years, and the ratings that readers have bestowed upon them. A notable feature is its diversity, reflected in the **6,669 unique book covers** that flower throughout the collection. This hints at a myriad of genres and styles, inviting readers from various backgrounds.

#### Key Observations

1. **Vibrant Titles**: Among the featured works, classics like *To Kill a Mockingbird* by Harper Lee and modern favorites like *The Hunger Games* by Suzanne Collins coexist. Not only does this reflect the evolution of literature, but it also showcases the varying tastes of readers through different generations.

2. **Reader Engagement**: With over **4.7 million ratings** for *The Hunger Games* and *Harry Potter and the Philosopher's Stone*, these books demonstrate not just popularity but a deep engagement with their respective audiences. The frequency of ratings often correlates with the presence of a dedicated fan base and marketing efforts that keep the conversation alive.

3. **Diverse Literary Offers**: The range in average ratings across the dataset is also telling. For instance, while *Twilight* has received a notable **average rating of 3.57**, it remains a cultural phenomenon with nearly **3.9 million ratings**; contrastingly, a classic like *The Great Gatsby*, rated at **3.89**, has attracted around **2.7 million ratings**. This shows how relative the appreciation and popularity of a book can be, influenced by its time of publication and the prevailing cultural sentiments.

4. **Decades of Delight**: The chronological aspect of original publication years highlights the longevity of certain works. *The Great Gatsby* (1925) and *To Kill a Mockingbird* (1960) stand the test of time, continuing to engage new readers, a testament to their relevance and enduring appeal.

5. **International Reach**: The language code column hints at the reach of these literary gems in diverse linguistic landscapes. With most titles published in English, there remains an opportunity for translations to broaden their reach further, allowing non-English readers to experience these stories.

#### Final Insight

In summation, this dataset serves as a vibrant microcosm of the literary world, echoing the voices of myriad authors and the interpretations of countless readers. It tells us a story of popularity, engagement, and the evolution of literature over time. As readers, we are invited to explore these books, each threaded into the broader narrative of our shared cultural experience. Whether one seeks comfort in a classic or craves the thrill of a contemporary tale, this dataset highlights the significant patterns that can shape our reading journeys.# Data Analysis Report

## Numerical Summary Statistics

|       |   book_id |   goodreads_book_id |     best_book_id |         work_id |   books_count |         isbn13 |   original_publication_year |   average_rating |    ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |      ratings_4 |       ratings_5 |
|:------|----------:|--------------------:|-----------------:|----------------:|--------------:|---------------:|----------------------------:|-----------------:|-----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|---------------:|----------------:|
| count |  10000    |     10000           |  10000           | 10000           |    10000      | 9415           |                    9979     |     10000        |  10000           |      10000           |                  10000    |    10000    |    10000    |     10000   | 10000          | 10000           |
| mean  |   5000.5  |         5.2647e+06  |      5.47121e+06 |     8.64618e+06 |       75.7127 |    9.75504e+12 |                    1981.99  |         4.00219  |  54001.2         |      59687.3         |                   2919.96 |     1345.04 |     3110.89 |     11475.9 | 19965.7        | 23789.8         |
| std   |   2886.9  |         7.57546e+06 |      7.82733e+06 |     1.17511e+07 |      170.471  |    4.42862e+11 |                     152.577 |         0.254427 | 157370           |     167804           |                   6124.38 |     6635.63 |     9717.12 |     28546.4 | 51447.4        | 79768.9         |
| min   |      1    |         1           |      1           |    87           |        1      |    1.9517e+08  |                   -1750     |         2.47     |   2716           |       5510           |                      3    |       11    |       30    |       323   |   750          |   754           |
| 25%   |   2500.75 |     46275.8         |  47911.8         |     1.00884e+06 |       23      |    9.78032e+12 |                    1990     |         3.85     |  13568.8         |      15438.8         |                    694    |      196    |      656    |      3112   |  5405.75       |  5334           |
| 50%   |   5000.5  |    394966           | 425124           |     2.71952e+06 |       40      |    9.78045e+12 |                    2004     |         4.02     |  21155.5         |      23832.5         |                   1402    |      391    |     1163    |      4894   |  8269.5        |  8836           |
| 75%   |   7500.25 |         9.38223e+06 |      9.63611e+06 |     1.45177e+07 |       67      |    9.78083e+12 |                    2011     |         4.18     |  41053.5         |      45915           |                   2744.25 |      885    |     2353.25 |      9287   | 16023.5        | 17304.5         |
| max   |  10000    |         3.32886e+07 |      3.55342e+07 |     5.63996e+07 |     3455      |    9.79001e+12 |                    2017     |         4.82     |      4.78065e+06 |          4.94236e+06 |                 155254    |   456191    |   436802    |    793319   |     1.4813e+06 |     3.01154e+06 |

## Categorical Summary Statistics

|        |         isbn | authors      | original_title   | title          | language_code   | image_url                                                                                | small_image_url                                                                        |
|:-------|-------------:|:-------------|:-----------------|:---------------|:----------------|:-----------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
| count  | 9300         | 10000        | 9415             | 10000          | 8916            | 10000                                                                                    | 10000                                                                                  |
| unique | 9300         | 4664         | 9274             | 9964           | 25              | 6669                                                                                     | 6669                                                                                   |
| top    |    3.757e+08 | Stephen King |                  | Selected Poems | eng             | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |
| freq   |    1         | 60           | 5                | 4              | 6341            | 3332                                                                                     | 3332                                                                                   |

## LLM Suggested Analyses

### LLM suggests the following analyses:

Based on the summary statistics and sample data from your dataset, here are some suggested analyses and insights you could explore:

### Suggested Analyses:

1. **Correlation Analysis:**
   - Investigate the relationships between numerical features, particularly between average rating, ratings count, and work ratings count. This will help you identify which factors contribute most significantly to the perceived quality of books.

2. **Publication Year Trends:**
   - Analyze how average ratings and ratings counts have changed over time. You can plot the average rating by year to identify trends in reader preferences or changes in quality over the years.

3. **Author Analysis:**
   - Perform an analysis of the top authors based on average ratings and ratings count. You could create rankings or visualizations

## Missing Values

|                           |    0 |
|:--------------------------|-----:|
| book_id                   |    0 |
| goodreads_book_id         |    0 |
| best_book_id              |    0 |
| work_id                   |    0 |
| books_count               |    0 |
| isbn                      |  700 |
| isbn13                    |  585 |
| authors                   |    0 |
| original_publication_year |   21 |
| original_title            |  585 |
| title                     |    0 |
| language_code             | 1084 |
| average_rating            |    0 |
| ratings_count             |    0 |
| work_ratings_count        |    0 |
| work_text_reviews_count   |    0 |
| ratings_1                 |    0 |
| ratings_2                 |    0 |
| ratings_3                 |    0 |
| ratings_4                 |    0 |
| ratings_5                 |    0 |
| image_url                 |    0 |
| small_image_url           |    0 |

## Correlation Matrix

|                           |    book_id |   goodreads_book_id |   best_book_id |    work_id |   books_count |      isbn13 |   original_publication_year |   average_rating |   ratings_count |   work_ratings_count |   work_text_reviews_count |   ratings_1 |   ratings_2 |   ratings_3 |   ratings_4 |   ratings_5 |
|:--------------------------|-----------:|--------------------:|---------------:|-----------:|--------------:|------------:|----------------------------:|-----------------:|----------------:|---------------------:|--------------------------:|------------:|------------:|------------:|------------:|------------:|
| book_id                   |  1         |           0.115154  |      0.104516  |  0.113861  |    -0.263841  | -0.011291   |                  0.0498747  |      -0.0408798  |     -0.373178   |          -0.382656   |               -0.419292   | -0.239401   |  -0.345764  |  -0.413279  |  -0.407079  | -0.332486   |
| goodreads_book_id         |  0.115154  |           1         |      0.96662   |  0.929356  |    -0.164578  | -0.048246   |                  0.13379    |      -0.0248484  |     -0.073023   |          -0.0637601  |                0.118845   | -0.0383752  |  -0.0565712 |  -0.075634  |  -0.0633104 | -0.0561447  |
| best_book_id              |  0.104516  |           0.96662   |      1         |  0.899258  |    -0.15924   | -0.0472525  |                  0.131442   |      -0.021187   |     -0.0691819  |          -0.0558346  |                0.125893   | -0.0338938  |  -0.0492842 |  -0.0670141 |  -0.054462  | -0.0495245  |
| work_id                   |  0.113861  |           0.929356  |      0.899258  |  1         |    -0.109436  | -0.0393198  |                  0.107972   |      -0.0175554  |     -0.0627204  |          -0.0547121  |                0.0969853  | -0.0345903  |  -0.0513668 |  -0.0667459 |  -0.0547754 | -0.0467453  |
| books_count               | -0.263841  |          -0.164578  |     -0.15924   | -0.109436  |     1         |  0.0178649  |                 -0.321753   |      -0.0698883  |      0.324235   |           0.333664   |                0.198698   |  0.225763   |   0.334923  |   0.383699  |   0.349564  |  0.279559   |
| isbn13                    | -0.011291  |          -0.048246  |     -0.0472525 | -0.0393198 |     0.0178649 |  1          |                 -0.00461214 |      -0.0256669  |      0.00890359 |           0.00916556 |                0.00955286 |  0.00605369 |   0.0103455 |   0.0121425 |   0.0101608 |  0.00662185 |
| original_publication_year |  0.0498747 |           0.13379   |      0.131442  |  0.107972  |    -0.321753  | -0.00461214 |                  1          |       0.0156076  |     -0.0244147  |          -0.0254478  |                0.0277841  | -0.019635   |  -0.0384716 |  -0.0424592 |  -0.0257847 | -0.0153877  |
| average_rating            | -0.0408798 |          -0.0248484 |     -0.021187  | -0.0175554 |    -0.0698883 | -0.0256669  |                  0.0156076  |       1          |      0.0449904  |           0.0450416  |                0.00748112 | -0.0779966  |  -0.115875  |  -0.0652372 |   0.0361082 |  0.115412   |
| ratings_count             | -0.373178  |          -0.073023  |     -0.0691819 | -0.0627204 |     0.324235  |  0.00890359 |                 -0.0244147  |       0.0449904  |      1          |           0.995068   |                0.779635   |  0.723144   |   0.845949  |   0.935193  |   0.978869  |  0.964046   |
| work_ratings_count        | -0.382656  |          -0.0637601 |     -0.0558346 | -0.0547121 |     0.333664  |  0.00916556 |                 -0.0254478  |       0.0450416  |      0.995068   |           1          |                0.807009   |  0.718718   |   0.848581  |   0.941182  |   0.987764  |  0.966587   |
| work_text_reviews_count   | -0.419292  |           0.118845  |      0.125893  |  0.0969853 |     0.198698  |  0.00955286 |                  0.0277841  |       0.00748112 |      0.779635   |           0.807009   |                1          |  0.572007   |   0.69688   |   0.762214  |   0.817826  |  0.76494    |
| ratings_1                 | -0.239401  |          -0.0383752 |     -0.0338938 | -0.0345903 |     0.225763  |  0.00605369 |                 -0.019635   |      -0.0779966  |      0.723144   |           0.718718   |                0.572007   |  1          |   0.92614   |   0.795364  |   0.672986  |  0.597231   |
| ratings_2                 | -0.345764  |          -0.0565712 |     -0.0492842 | -0.0513668 |     0.334923  |  0.0103455  |                 -0.0384716  |      -0.115875   |      0.845949   |           0.848581   |                0.69688    |  0.92614    |   1         |   0.949596  |   0.838298  |  0.705747   |
| ratings_3                 | -0.413279  |          -0.075634  |     -0.0670141 | -0.0667459 |     0.383699  |  0.0121425  |                 -0.0424592  |      -0.0652372  |      0.935193   |           0.941182   |                0.762214   |  0.795364   |   0.949596  |   1         |   0.952998  |  0.82555    |
| ratings_4                 | -0.407079  |          -0.0633104 |     -0.054462  | -0.0547754 |     0.349564  |  0.0101608  |                 -0.0257847  |       0.0361082  |      0.978869   |           0.987764   |                0.817826   |  0.672986   |   0.838298  |   0.952998  |   1         |  0.933785   |
| ratings_5                 | -0.332486  |          -0.0561447 |     -0.0495245 | -0.0467453 |     0.279559  |  0.00662185 |                 -0.0153877  |       0.115412   |      0.964046   |           0.966587   |                0.76494    |  0.597231   |   0.705747  |   0.82555   |   0.933785  |  1          |

### Strong Positive Correlations (>= 0.75)

- **best_book_id and goodreads_book_id**: 0.97
- **ratings_2 and ratings_1**: 0.93
- **ratings_2 and ratings_count**: 0.85
- **ratings_2 and work_ratings_count**: 0.85
- **ratings_3 and ratings_1**: 0.80
- **ratings_3 and ratings_2**: 0.95
- **ratings_3 and ratings_count**: 0.94
- **ratings_3 and work_ratings_count**: 0.94
- **ratings_3 and work_text_reviews_count**: 0.76
- **ratings_4 and ratings_2**: 0.84
- **ratings_4 and ratings_3**: 0.95
- **ratings_4 and ratings_count**: 0.98
- **ratings_4 and work_ratings_count**: 0.99
- **ratings_4 and work_text_reviews_count**: 0.82
- **ratings_5 and ratings_3**: 0.83
- **ratings_5 and ratings_4**: 0.93
- **ratings_5 and ratings_count**: 0.96
- **ratings_5 and work_ratings_count**: 0.97
- **ratings_5 and work_text_reviews_count**: 0.76
- **work_id and best_book_id**: 0.90
- **work_id and goodreads_book_id**: 0.93
- **work_ratings_count and ratings_count**: 1.00
- **work_text_reviews_count and ratings_count**: 0.78
- **work_text_reviews_count and work_ratings_count**: 0.81

### Strong Negative Correlations (<= -0.2)



## Outliers

- **book_id**: 0 potential outliers
- **goodreads_book_id**: 345 potential outliers
- **best_book_id**: 357 potential outliers
- **work_id**: 601 potential outliers
- **books_count**: 844 potential outliers
- **isbn13**: 556 potential outliers
- **original_publication_year**: 1031 potential outliers
- **average_rating**: 158 potential outliers
- **ratings_count**: 1163 potential outliers
- **work_ratings_count**: 1143 potential outliers
- **work_text_reviews_count**: 1005 potential outliers
- **ratings_1**: 1140 potential outliers
- **ratings_2**: 1156 potential outliers
- **ratings_3**: 1149 potential outliers
- **ratings_4**: 1131 potential outliers
- **ratings_5**: 1158 potential outliers


## Frequency Analysis (Top 5 Values for Categorical Columns)

### Column: isbn

|       isbn |   count |
|-----------:|--------:|
|  375700455 |       1 |
|  439023483 |       1 |
|  439554934 |       1 |
|  316015849 |       1 |
| 2849659266 |       1 |

### Column: authors

| authors         |   count |
|:----------------|--------:|
| Stephen King    |      60 |
| Nora Roberts    |      59 |
| Dean Koontz     |      47 |
| Terry Pratchett |      42 |
| Agatha Christie |      39 |

### Column: original_title

| original_title   |   count |
|:-----------------|--------:|
|                  |       5 |
| The Gift         |       5 |
| Perfect          |       4 |
| Twilight         |       4 |
| Gone             |       3 |

### Column: title

| title                                     |   count |
|:------------------------------------------|--------:|
| Selected Poems                            |       4 |
| Stone Soup                                |       3 |
| The Collected Poems                       |       2 |
| One Flew Over the Cuckoo's Nest           |       2 |
| Between the Lines (Between the Lines, #1) |       2 |

### Column: language_code

| language_code   |   count |
|:----------------|--------:|
| eng             |    6341 |
| en-US           |    2070 |
| en-GB           |     257 |
| ara             |      64 |
| en-CA           |      58 |

### Column: image_url

| image_url                                                                                |   count |
|:-----------------------------------------------------------------------------------------|--------:|
| https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png |    3332 |
| https://images.gr-assets.com/books/1327872146m/18135.jpg                                 |       1 |
| https://images.gr-assets.com/books/1327132670m/6351939.jpg                               |       1 |
| https://images.gr-assets.com/books/1476942137m/116494.jpg                                |       1 |
| https://images.gr-assets.com/books/1424037542m/7613.jpg                                  |       1 |

### Column: small_image_url

| small_image_url                                                                        |   count |
|:---------------------------------------------------------------------------------------|--------:|
| https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png |    3332 |
| https://images.gr-assets.com/books/1327872146s/18135.jpg                               |       1 |
| https://images.gr-assets.com/books/1327132670s/6351939.jpg                             |       1 |
| https://images.gr-assets.com/books/1476942137s/116494.jpg                              |       1 |
| https://images.gr-assets.com/books/1424037542s/7613.jpg                                |       1 |

## Correlation Head Map 

![Correlation Head Map](/goodreads/corr_heat_map.png)

## BoxPlot 

![BoxPlot](/goodreads/boxplot.png)

## Histograms 

![Histograms](/goodreads/histograms.png)

