# Stock-Prediction-Deep-Learning

![Alt text](imgs/img1.jpg)

## Project Overview
This project aims to develop and evaluate deep learning models for predicting stock prices of major Big Tech companies in the United States. By leveraging historical financial data, we will explore the efficacy of various architectures—LSTM, GRU, Transformer, and GAN—in capturing trends, seasonality, and market dynamics to generate accurate stock price forecasts.

## Background
Stock price prediction is a challenging task due to the inherent complexity and non-linearity of financial markets. Big Tech companies like Apple, IBM, Qualcomm, and Microsoft are major players in the market, and their stock performance significantly influences the economy. Accurate forecasting for these stocks can benefit traders, investors, and financial analysts.

Traditional methods often struggle with the highly volatile and chaotic nature of financial data. Deep learning models, with their ability to extract patterns and learn temporal dependencies, present a promising alternative. This project will focus on comparing state-of-the-art deep learning approaches to determine the most effective model for stock price prediction.

### Data
The project will use historical stock price data of Big Tech companies, including:
- Basic features like open price, close price, high, low, and volume.
- Calculated features like SMA (Simple Moving Average), EMA (Exponential Moving Average), MACD (Moving Average Convergence Divergence), RSI (Relative Strength Index), ATR (Average True Range), Bollinger Bands, and RSV (Raw Stochastic Value), with varying window sizes.
- The data was sourced from reliable platforms Yahoo Finance from 1993.

The following mathematical equations describe the financial calculated features used in the project:

1. **Simple Moving Average (SMA)**:
   $$
   \text{SMA} = \frac{1}{N} \sum_{i=1}^{N} P_i
   $$
   where $P_i$ is the price at day $i$, and $N$ is the window size.

2. **Exponential Moving Average (EMA)**:
   $$
   \text{EMA}_t = \alpha \cdot P_t + (1 - \alpha) \cdot \text{EMA}_{t-1}
   $$
   where $\alpha = \frac{2}{N+1}$ is the smoothing factor.

3. **MACD (Moving Average Convergence Divergence)**:
   $$
   \text{MACD} = \text{EMA}_{\text{short}} - \text{EMA}_{\text{long}}
   $$
   $$
   \text{Signal Line} = \text{EMA}_{\text{MACD}}
   $$

4. **Relative Strength Index (RSI)**:
   $$
   \text{RSI} = 100 - \frac{100}{1 + \frac{\text{Average Gain}}{\text{Average Loss}}}
   $$

5. **Average True Range (ATR)**:
   $$
   \text{ATR} = \frac{1}{N} \sum_{i=1}^{N} (\text{High}_i - \text{Low}_i)
   $$

6. **Bollinger Bands**:
   $$
   \text{Upper Band} = \text{SMA} + 2 \cdot \text{Standard Deviation}
   $$
   $$
   \text{Lower Band} = \text{SMA} - 2 \cdot \text{Standard Deviation}
   $$

7. **Raw Stochastic Value (RSV)**:
   $$
   \text{RSV} = \frac{P_t - P_{\text{min}}}{P_{\text{max}} - P_{\text{min}}} \cdot 100
   $$
   where $P_t$ is the current price, $P_{\text{min}}$ is the lowest price in the window, and $P_{\text{max}}$ is the highest price in the window.




