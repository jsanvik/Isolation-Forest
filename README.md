# Implementing Isolation-Based Anomaly Detection
CPSC 4660 Fall 2026 Course Project  
Tushika Chauhan, John S. Anvik  

## Component Being Implemented
We plan to implement an anomaly detection method proposed by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou in 2012 [1]. Their method, which they call Isolation Forest, identifies anomalies by how isolated they are.  

The isolation forest is composed of a number of isolation trees. In each of these binary trees, the algorithm picks a random attribute, then splits the dataset into two subsets at a random value of the attribute. This value must be between the attribute’s minimum and maximum values. These subsets continue to be recursively split until all observations are leaf nodes.   

The researchers noted that when the dataset is split this way, the most isolated observations (the anomalies) tend to have much shorter path lengths than non-anomalies. Thus, whichever observations have the shortest average path length across many trees are 
labelled anomalies.  

The method requires only three parameters: the number of trees in the forest, subsampling 
size, and the height limit used to detect anomalies.  

## Evaluation
We will evaluate our program by testing how well it can identify anomalies in datasets that have known anomaly labels. The labels will not be given to the program while it's running. We will only use them after to assess the accuracy of our program to detect the anomalies.  

The results will be evaluated mostly using the AUC (Area Under the ROC Curve) metric, as it was also used in the original paper. A higher AUC means that the program was better at giving higher anomaly scores to actual anomalies. We will also examine the anomaly score and path lengths to determine if the result matches what we expected from Isolation Forest. For example, the path length of anomalies should be shorter, and the anomaly score should be higher than those of normal observations, in general,  

The program will also be evaluated with varying numbers of trees and varying subsampling sizes. This will enable us to understand the impact of these settings on our implementation. Since the algorithm uses random sampling and random splits, we will repeat the test when needed and compare the results. We will also evaluate the processing time required to execute the algorithm on the dataset.  

## Test Data
To evaluate the technique, we will be using two of the statistical datasets that Liu, Ting, and Zhou used in their paper: hbk and wood [2]. Both datasets can be found [here](https://gist.github.com/yohanesnuwara/fc1b9400d8db96bfc2690f7224690ce5).
 
## References
[1] Lui,F. T., Ting, K. M. and Zhou, Z, -H. 2012. Isolation-based anomaly detection. ACM Trans. Knowl. Discov. Data 6,1, Article 3(March 2012), 39 pages. DOI = 10.1145/2133360.2133363 http://doi.acm.org/10.1145/2133360.2133363  
[2] P. J. Rousseeuw and A. M. Leroy. 1987. Robust regression and outlier detection. John Wiley & Sons, Inc., USA.
