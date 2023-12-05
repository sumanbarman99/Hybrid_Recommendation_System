# Hybrid Recommendation System Project

## Overview

Welcome to the Hybrid Recommendation System project! This project combines both content-based and collaborative-based recommendation systems to enhance the accuracy and personalization of movie recommendations. The content-based approach utilizes CountVectorizer to convert movie metadata into a matrix of token counts, while the collaborative-based approach employs cosine similarities on user and rating data.

## Table of Contents

- [Project Description](#project-description)
- [Data Preprocessing](#data-preprocessing)
- [Feature Engineering](#feature-engineering)
- [Content-Based Recommendation](#content-based-recommendation)
- [Collaborative-Based Recommendation](#collaborative-based-recommendation)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Deployment](#deployment)

## Project Description

The goal of this project is to create a hybrid recommendation system that leverages both content-based and collaborative-based techniques to provide personalized movie recommendations. The content-based approach focuses on analyzing movie metadata using CountVectorizer to represent movies as a matrix of token counts, allowing us to measure cosine similarities between movies. The collaborative-based approach involves creating a user-item pivot table and measuring cosine similarities based on user ratings.

## Data Preprocessing

Data preprocessing involves cleaning and organizing the raw data to prepare it for analysis. In this project, we ensure that the movie metadata and user rating data are appropriately formatted and free from inconsistencies.

## Feature Engineering

Feature engineering is crucial for enhancing the quality of the input data. In this project, we engineer features by using CountVectorizer to convert the movie metadata into a matrix of token counts, including both unigram and bigram words.

## Content-Based Recommendation

The content-based recommendation system analyzes movie metadata and computes cosine similarities between movies based on their token counts. This method recommends movies similar to those a user has already shown interest in.

## Collaborative-Based Recommendation

The collaborative-based recommendation system creates a user-item pivot table and measures cosine similarities based on user ratings. This method recommends movies liked by users with similar preferences.

## Getting Started

To get started with the project, follow these instructions:

### Dependencies

Make sure you have the following dependencies installed:

- Python (>=3.6)
- Jupyter Notebook
- NumPy
- Pandas
- Scikit-learn

## Deployment
<div align="center"> <img width = "800" src = "https://github.com/sumanbarman99/Hybrid_Recommendation_System/blob/main/image/Screenshot%20(58).png"> </div>
<div align="center">Top 5 similar movies</div>
