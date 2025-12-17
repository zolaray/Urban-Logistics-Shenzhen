# 📚 Literature Review: Urban Logistics & Traffic Forecasting

## 1. Introduction
This review synthesizes core research in Spatio-Temporal Graph Neural Networks (GNNs) to establish a foundation for urban logistics forecasting in **Shenzhen, China**.

## 2. Key Research Summaries

### 🏙️ T-GCN: A Temporal Graph Convolutional Network (2021)
* **Model:** GCN + Gated Recurrent Units (GRU)
* **Dataset:** **SZ-taxi** (Shenzhen Taxi GPS data)
* **Contribution:** This paper provides the foundational baseline for this project. It proves that combining spatial road topology (GCN) with temporal history (GRU) significantly outperforms standard time-series models.

### 🔍 ST-GSP: Spatio-Temporal Graph Structural Learning (2024)
* **Model:** Graph Structural Learning
* **Dataset:** Multiple Urban Datasets
* **Contribution:** This research introduces how to discover **"hidden connections"** between urban zones that aren't physically connected by a road, but still influence each other's traffic flow.

### 🚛 Multi-view GNN for Urban Logistics (2023)
* **Model:** Multi-view Spatio-Temporal GNN
* **Dataset:** Logistics & Urban Traffic Data
* **Contribution:** **Main Reference.** This paper bridges the gap between general traffic and specialized logistics. It explains how "amenities" (Points of Interest like warehouses or malls) act as features for more accurate forecasting.

## 3. Thematic Synthesis
The literature shows a clear progression from basic spatial graphs (T-GCN) to complex multi-view systems that incorporate urban amenities.
* **Innovation Point:** My project aims to simplify these complex models into a functional dashboard while maintaining the "Multi-view" accuracy suggested by the 2023 research.
