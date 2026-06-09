# FIFA World Cup 2026 Prediction System

## Overview

A machine learning system that predicts FIFA World Cup 2026 outcomes using historical international football data, a custom Elo rating system, and Monte Carlo simulation.

## Methodology

### Custom Elo Ratings

* Tournament-weighted Elo system
* Goal difference scaling
* Home advantage adjustment
* Annual rating decay

### Feature Engineering

* Elo difference
* Recent form
* Attack rating
* Defensive rating
* Tournament importance

### Match Prediction

* XGBoost classifier trained on historical international matches
* Predicts win, draw, and loss probabilities

### Tournament Simulation

* Simulates the entire World Cup thousands of times
* Estimates probabilities of reaching the R16, QF, SF, Final, and winning the tournament

## Technologies

Python, Pandas, NumPy, Scikit-learn, XGBoost

## Results

Generated stage-wise qualification and championship probabilities for all 48 World Cup teams through 5,000+ Monte Carlo simulations.
