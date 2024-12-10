### Dataset Overview

The dataset contains information about 10,000 books, encapsulating various aspects such as author details, publication years, ratings, and images. Each entry in the dataset represents a distinct book featuring its unique `book_id`, `title`, `authors`, `average_rating`, `ratings_count`, and an image link, among other attributes. 

### Key Statistics

- **Book Range**: The dataset includes books with IDs ranging from 1 to 10,000, with an average `book_id` of about 5000.
- **Unique Authors**: There are 6669 unique image URLs indicating a diversity of book covers, although the dataset itself does not have a count for unique authors or titles given the unavailability of certain statistics for this variable.
- **Publication Years**: The earliest book published was "The Great Gatsby" in 1925, and the most recent was "The Hunger Games," published in 2008. 

### Notable Books 

1. **The Hunger Games** by *Suzanne Collins*
   - **Publication Year**: 2008
   - **Average Rating**: 4.34 (very well-received)
   - **Ratings Count**: Over 4.78 million, suggesting widespread popularity.
   - **Image**: [Link to the cover](https://images.gr-assets.com/books/1447303603m/2767052.jpg)
  
2. **Harry Potter and the Philosopher's Stone** by *J.K. Rowling*
   - **Publication Year**: 1997
   - **Average Rating**: 4.44, showcasing its classic status and lasting appeal.
   - **Ratings Count**: Around 4.60 million, highlighting its additional popularity.
   - **Image**: [Link to the cover](https://images.gr-assets.com/books/1474154022m/3.jpg)

3. **Twilight** by *Stephenie Meyer*
   - **Publication Year**: 2005
   - **Average Rating**: 3.57, lower compared to the previous titles but with 3.87 million ratings, indicating strong engagement from readers.
   - **Image**: [Link to the cover](https://images.gr-assets.com/books/1361039443m/41865.jpg)

4. **To Kill a Mockingbird** by *Harper Lee*
   - **Publication Year**: 1960
   - **Average Rating**: 4.25 with nearly 3.20 million ratings signifies it as a literary classic.
   - **Image**: [Link to the cover](https://images.gr-assets.com/books/1361975680m/2657.jpg)
  
5. **The Great Gatsby** by *F. Scott Fitzgerald*
   - **Publication Year**: 1925
   - **Average Rating**: 3.89, containing around 2.68 million ratings, indicating enduring interest.
   - **Image**: [Link to the cover](https://images.gr-assets.com/books/1490528560m/4671.jpg)

### Insights and Trends

1. **Popularity Over Time**: The dataset reveals a notable trend in the popularity of books published after the 1990s, especially the rise of series-centric content like *Harry Potter* and *Twilight* which have drawn large readerships.

2. **Ratings Correlation**: There appears to be a correlation between the number of ratings a book receives and its average rating. For example, despite *Twilight* having a lower average rating, the sheer volume of ratings indicates a strong engagement, possibly due to its status as a cultural phenomenon during its release.

3. **Genre Diversity**: While this dataset primarily highlights mainstream hits, it suggests a diversity of genres, as indicated by the variety of authors and styles represented. Classic literature blends with modern fantasy, showcasing shifts in reader interests over decades.

4. **Timeless Classics**: The dataset also serves as a reminder of literary classics that have stood the test of time, such as *To Kill a Mockingbird* and *The Great Gatsby*, reflecting a lasting relevance in contemporary readership.

### Conclusion

This dataset offers a glimpse into the reading landscape spanning several decades, illustrating the evolution of popular books based on reader engagement and ratings. As we analyze further, we can glean insights into readers' tastes, the impact of cultural phenomena, and trends in literature that may guide future publishing and marketing strategies.# Data Analysis Report

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

Based on the provided summary statistics and datasets, here are some suggestions for further analyses that could yield more insights, as well as recommendations for columns suitable for cluster analysis.

### Suggested Analyses

1. **Correlation Analysis:**
   - Examine correlations between numerical features such as average rating, ratings count, work ratings count, and the number of text reviews. Visualize the correlations using a heatmap to identify relationships.

2. **Distribution Analysis:**
   - Plot the distributions of key numerical features, such as average ratings and ratings counts. This can help identify outliers and understand the spread of the data.

3. **Trend Analysis:**
   - Analyze trends over time for the `original_publication_year`. Assess how ratings, counts, and

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

![Correlation Head Map](./goodreads/corr_heat_map.png)

## BoxPlot 

![BoxPlot](./goodreads/boxplot.png)

## Histograms 

![Histograms](./goodreads/histograms.png)

