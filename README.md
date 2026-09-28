# 🦵 Modeling Recovery after Lower-Limb Musculoskeletal Injury

Welcome to the **Advanced Machine Learning 2026/2027** project repository for **Group 14**! 🚀

In this project, we step into the shoes of data scientists to analyze longitudinal clinical data from patients recovering from lower-limb musculoskeletal injuries. We aren't just looking at the data—we are building probabilistic models, uncovering hidden patterns, and even training an AI agent to suggest the best rehabilitation interventions!

## 👥 Meet The Team (Group 14)
* **David Belykh** 
* **Matilde Quitério**
* **Ramyad Raadi**

## 🎯 Project Overview
Recovery is messy, uncertain, and varies wildly from patient to patient. To tackle this, we will progress through a series of technical milestones, moving from basic data exploration all the way to Reinforcement Learning:

* **M0: Exploratory Data Analysis (EDA)** 📊 - Uncovering the baseline stats, observing patient trajectories, and finding the hidden quirks in the dataset.
* **M1: Mixture Models** 🧩 - Clustering patient-weeks using Gaussian Mixture Models (GMMs) to find hidden recovery profiles.
* **M2 & M3: Bayesian Networks & Inference** 🕸️ - Modeling probabilistic dependencies (hand-designed) and reasoning under uncertainty using exact and approximate inference.
* **M4: Learning Bayesian Networks** 🧠 - Letting the data speak for itself by using score-based structure learning algorithms.
* **M5: Hidden Markov Models (HMM)** 🕰️ - Capturing the temporal dynamics of recovery—modeling how patients transition between latent states over time.
* **M6: Reinforcement Learning (RL)** 🤖 - Implementing Q-learning to discover the optimal sequence of interventions (Rest, Light Exercise, Intensive Therapy) to maximize long-term patient utility!

## 📂 Repository Structure
* `dataset/` - Contains the synthetic `patients.csv` (static baseline traits) and `rehabilitation.csv` (longitudinal weekly observations).
* `M0_G14.ipynb` - The original EDA milestone notebook.
* `M0_G14_improved.ipynb` - The upgraded EDA notebook (featuring KS-tests for normality, PCA for dimensionality reduction, and Z-score multivariate outlier detection!).
* `Project.pdf` - The holy grail (assignment guidelines).

## 🚀 How to Run
This project relies heavily on Python and Jupyter Notebooks. To run the analysis locally:

1. Clone this repo:
   ```bash
   git clone https://github.com/Ramyad20/Advanced-ML-patients.git
   cd Advanced-ML-patients
   ```
2. Make sure you have the usual data science stack installed (`pandas`, `numpy`, `seaborn`, `scikit-learn`, `scipy`).
3. Fire up Jupyter:
   ```bash
   jupyter notebook
   ```
4. Dive into the milestones and watch the probabilistic magic happen! ✨

---
*Disclaimer: The dataset is synthetically generated for educational purposes. Any clinical advice derived from our Reinforcement Learning agent should probably not be used on real patients... yet.* 😉