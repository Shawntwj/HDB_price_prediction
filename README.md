# HDB_price_prediction
A data mining project that scrapes and feature engineer HDB variables to use for price prediction. <br>

We aim to investigate the different factors and topics that affect HDB resale prices by applying machine learning techniques to help homeowners understand the common topics that get brought up when discussing housing prices, the sentiment of the different topics, and understand the relationship of various housing features and their importance in predicting housing prices.<br>

The models used for topic modelling are LSA, LDA and BERTopic. The models used for sentiment analysis are VADER, Textblob, and Flair. The models used for price predictions are Lasso, Random Forest, Gradient Boost, XGBoost, Artificial Neural Network (ANN) and Blending

## Navigation

The folder 'HDB Housing Prediction' contains the code related to scraping, preprocessing, feature engineering and predicting HDB resale prices. <br>

The folder 'Hardwarezone Sentiment and Topic' contains the code related to scraping and preprocessing the models related to topic modelling and sentiment analysis. 

## Motivation
Getting a home has always been a huge financial decision. With many resale flats being valued above S$1 million, many Singaporeans are concerned about the affordability of housing. As roughly 80% of Singapore's population resides in HDB flats, understanding the underlying factors that affect the HDB resale prices could better equip individuals with greater decision making capabilities pertaining to purchasing resale flats. <br>

Despite the fact that the recent pandemic and global economic uncertainty have caused many future homeowners to seek resale flats as an alternative, based on PropertyGuru’s survey, 55% of Singaporeans are still unsure about future property prices due to Covid-19.  This indicates that the existing solutions are inadequate to help educate and resolve the uncertainty that Singaporeans have. Thus, by splitting the analysis pre- and post-Covid-19, we will be able to understand how an economic turndown affects the change in the factors that affect resale price. <br>

In order to understand the change, it is important to figure out what data attributes have an influence on the market value of HDB resale flats. This is where topic modelling and sentiment analysis play a huge role in our learning as finding out the topics and features that are often discussed on an online forum would give us an overview of the recent debate or engagement that the citizens are sharing. After identifying the topics and features, we will then be able to further analyse and identify those that have higher influence on the resale price. 
