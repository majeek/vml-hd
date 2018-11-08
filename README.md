## VML-HD: The Historical Arabic Documents Dataset for Recognition Systems

A new database with handwritten Arabic script. It is based on five books written by different writers from the years 1088-1451\. We took 668 pages from these five books, and fully annotated them on the sub-word level. For each page we manually applied bounding boxes on the different sub-words and annotated the sequence of characters. It consists of 159,149 sub-word appearances consisted of 326,289 characters out of a vocabulary of 5,509 forms of sub-words. The database is described in detail and is designed for training and testing recognition systems for handwritten Arabic sub-words. This database is available for the purpose of research, and we encourage researchers to develop and test new methods using our database.

### Copyright and Citation

This dataset is intended for research purposes only. If you wish to use the dataset for anything besides research, you must get our explicit consent.

If you download and use the dataset in your research, you must cite our paper:  
@inproceedings{kassis2017vmlhd,  
title={VML-HD: The Historical Arabic Documents Dataset for Recognition Systems},  
author={Kassis, Majeed and Abdalhaleem, Alaa and Droby, Ahmad and Alaasam, Reem and El-Sana, Jihad}, booktitle={1st International Workshop on Arabic Script Analysis and Recognition},  
year={2017},  
organization={IEEE}

[Download Database](https://www.cs.bgu.ac.il/~vml/database/VML-HD/VML-HD.zip)  
[XML Files](https://www.cs.bgu.ac.il/~vml/database/VML-HD/xmlFiles.rar)

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png)](http://creativecommons.org/licenses/by-nc-nd/4.0/)

## Books for Alignment

Complete Manuscripts: [0207](https://www.cs.bgu.ac.il/~majeek/dataset/0207.rar) [0206](https://www.cs.bgu.ac.il/~majeek/dataset/0206.rar)  
Annotated Manuscripts: [0206 0207](https://www.cs.bgu.ac.il/~majeek/dataset/0206_0207_annotated.rar)</div>

<div class="tab-pane fade" id="recognition">

### VML-HD: The Arabic Historical Manuscripts Dataset for Recognition Systems

![](writingStyle/3249138.png) ![](writingStyle/3158466.png) ![](writingStyle/3157556.png) ![](writingStyle/3368132.png) ![](/writingStyle/3426930.png)

## Dataset Information: 5 Folds Version

The dataset contains 5 manuscripts totaling 668 pages, annotated on the subword level. These manuscripts are split to five folds named 'a','b','c,'d', and 'e'. Each fold contains randomly chosen 20% pages from each manuscripts. The recognition score will be calculated using the Mean average precision (MAP) score. Mean average precision is a widespread measure for the performance of information retrieval systems. The metric is defined as the average of the precision value obtained after each relevant word is retrieved.  

<input type="image" src="competition/dataset.png" height="150"> <input type="image" src="competition/folds.png" height="150">

Each track of the two contains the folds images and annotation information in their own format.  

## Segmentation Based Track

In this track, you will receive the documents segmented, where each image of a manuscript page is segmented to its corresponding annotation information and stored in its own folder labeled with the same name of the manuscript page image name.Along with each folder containing the subwords, the annotation data are also provided. For this track it is expected that segmentation based algorithms are used to recognize the subwords found in the dataset.  

[Data for Segmentation Based Track](http://www.cs.bgu.ac.il/~vml/database/competition/segmentation_based.zip)  

## Segmentation Free Track

In this track, you will receive the documents unsegmented, where each image will contain a complete manuscript page. Along with each page, the annotation data are also provided. For this track it is expected that segmentation free algorithms are used to recognize the subwords found in the dataset.  

[Data for Segmentation Free Track](./competition/segmentation_free.zip)  

For any inquiry please send an email to the organizers at ![](http://oldweb.cs.bgu.ac.il/image_cache/6cbce1d020c3238d0301fb48929367db)

To download of the files for each track of the two, please click [here](https://goo.gl/m4qD1E).

</div>

# Other Notes
Parsing and subword segmentation code for the VML-HD Dataset.

To acquire the complete dataset please refer [here](https://www.cs.bgu.ac.il/~majeek/#dataset).

Paper detailing the dataset can be downloaded from [here](https://www.cs.bgu.ac.il/~majeek/#publications).

For the tutorial explaining the code please refer to [here](https://majeek.github.io/tutorials/vmlHD/).
