# Predictive Maintenance Strategy: Telemetry Error Clustering with PySpark

## Executive Summary
This project outlines a strategic pivot from reactive repairs to a data-driven predictive maintenance model. By analyzing telemetry data from **100 industrial machines**, I engineered a **PySpark** data pipeline to identify failure patterns that contribute to operational downtime.

Using **Unsupervised Machine Learning (K-Means Clustering)**, I segmented the fleet into distinct operational categories. The analysis revealed that machine health is not uniform: a specific subset of assets (approx. 10%) drives a disproportionate volume of errors. This project demonstrates how big data technologies can be used to optimize maintenance schedules, automate risk detection, and reduce unnecessary labor costs.

## Data Source
* **Source:** Microsoft Azure Predictive Maintenance (AzureML Sample Experiments).
* **Scope:** 100 industrial machines operating 24/7 over a 12-month period.
* **Dataset:** `PdM_errors.csv` (Timestamped error logs representing non-terminal failures).

## Technical Architecture & Stack
This solution simulates a production-grade Big Data environment capable of scaling to high-velocity sensor streams.
* **Processing Engine:** **Apache Spark (PySpark)** – Chosen for distributed computing capabilities, ensuring the ETL pipeline scales from 100 to 100,000 assets without refactoring.
* **Machine Learning:** **Spark MLlib** – Utilized for scalable model training (K-Means) and feature extraction.
* **Analysis & Visualization:** **Pandas** & **Seaborn** – Used for post-processing cluster results and generating executive-level reporting.
* **Dimensionality Reduction:** **PCA (Principal Component Analysis)** – Applied to visualize high-dimensional cluster separation.

## Methodology: The Data Science Lifecycle

### 1. ETL & Feature Engineering
Raw telemetry logs are transactional streams. To model machine behavior, I transformed this stream into a structured **Machine Feature Matrix**:
* **Pivot Operation:** Aggregated 3,900+ log entries into a dataset where each row represents a unique machine's "Health Signature" (counts of specific error types).

### 2. Unsupervised Segmentation (K-Means)
Since the dataset lacked explicit "Failure/No Failure" labels for every timestamp, I used Unsupervised Learning to discover hidden structures.
* **Algorithm:** K-Means Clustering.
* **Logic:** Grouped machines based on the mathematical similarity of their error vectors.
* **Outcome:** Automated classification of machines into "Stable," "Specific Defect," and "Critical" categories.

## Visual Analysis & Strategic Insights

### Error Frequency Analysis
Understanding the distribution of failure modes is critical for inventory planning.

<p align="center">
  <img src=".assets/Distribution of Error Types.png" alt="Distribution of Error Types" width="800"/>
  <br>
  <b>Figure 1: Distribution of Error Types</b>
</p>

* **Analysis:** The distribution is non-uniform. **Error 1** and **Error 2** appear roughly twice as often as Error 5.
* **Insight:** The majority of maintenance tickets are driven by common, likely wear-and-tear issues (Error 1/2), while Error 5 represents a rare, severe failure mode. Spare parts inventory should be weighted heavily toward resolving Errors 1 and 2 to minimize downtime.

### High-Frequency Offender Identification
Aggregating error counts allows us to identify specific assets that deviate from the fleet norm.

<p align="center">
  <img src=".assets/Top 10 Machines by Error Count.png" alt="Top 10 Machines by Error Count" width="800"/>
  <br>
  <b>Figure 2: Top 10 Machines by Error Count</b>
</p>

* **Analysis:** Machine health is skewed. **Machine #22** is the primary outlier with ~60 recorded errors, followed closely by Machines #99 and #78.
* **Insight:** The drop-off in error counts after the top 10 assets indicates that instability is **localized**, not systemic. Immediate inspection of Machine #22 is required, rather than a fleet-wide overhaul.

### Machine Clustering & Segmentation
To validate the K-Means results, I applied PCA to project the 5-dimensional error data into a 2D space.

<p align="center">
  <img src=".assets/Machine Clusters.png" alt="Machine Clusters" width="800"/>
  <br>
  <b>Figure 3: Machine Clusters based on Error Profile</b>
</p>

* **Cluster A (Purple - "Baseline"):** The dense majority. These machines exhibit low, consistent error rates and represent the standard operating baseline.
* **Cluster B (Teal - "Specific Mode"):** Distinct from the baseline, suggesting a specific, repeated failure pattern (likely dominance of Error 1). These machines may share a common configuration flaw.
* **Cluster C (Yellow - "High Volatility"):** The dispersed group containing high-error outliers (like Machine #22). The wide spread indicates chaotic, multi-mode failures. This is the **high-priority intervention group**.

## Business Recommendations
Based on the analytical findings, the following actions are proposed:

1.  **Risk-Based Scheduling:** Transition from a flat schedule to a risk-weighted one. Prioritize the "Yellow Cluster" for weekly reviews while reducing inspection frequency for the "Purple Cluster" to optimize labor usage.
2.  **Root Cause Investigation:** Dispatch senior technicians to **Machine #22** and **#99**. The data indicates persistent defects requiring component replacement.
3.  **Pipeline Automation:** Deploy this PySpark script as a weekly cron job. Any machine that "migrates" from the Safe Cluster to the Risk Cluster should automatically trigger a work order, effectively catching failures before they escalate.

## Setup & Usage
**Prerequisites:** Python 3.8+, Apache Spark
```bash
# Install dependencies
pip install pyspark pandas seaborn matplotlib scikit-learn

# Run the pipeline
python predictive_maintenance_pipeline.py
