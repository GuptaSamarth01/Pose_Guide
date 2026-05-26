# PoseGuide — AI Pose Recommendation Engine

## Overview

PoseGuide is an AI-powered pose recommendation and body analysis system built using Computer Vision and Machine Learning concepts.
The project analyzes a person’s body posture and proportions in real time using a webcam and provides the foundation for intelligent pose recommendations for photography and content creation.

The goal of this project is to help users:

* Understand their body posture
* Improve photo poses
* Receive pose recommendations based on body structure
* Build confidence while taking pictures

---

# Problem Statement

Many people struggle with:

* Finding the right pose while taking photos
* Understanding which angles suit them best
* Maintaining good posture in pictures
* Creating aesthetically balanced poses

Currently, pose selection is mostly based on:

* Trial and error
* Social media trends
* Manual photographer guidance

PoseGuide aims to automate and personalize this process using AI.

---

# Main Objective

The main objective of PoseGuide is to:

1. Detect human body landmarks in real time
2. Analyze body proportions and posture
3. Identify body structure and pose alignment
4. Recommend suitable poses for users
5. Build a smart AI-based pose assistant

---

# Technologies Used

## Programming Language

* Python

## Libraries & Frameworks

* OpenCV — Real-time webcam processing and visualization
* MediaPipe — Human pose landmark detection
* NumPy — Mathematical calculations and body ratio analysis

---

# Features Implemented

## Real-Time Webcam Detection

* Live webcam feed processing
* Continuous frame analysis

## Human Pose Estimation

The system detects:

* Shoulders
* Elbows
* Wrists
* Hips
* Knees
* Ankles
* Facial landmarks

## Skeleton Visualization

* Real-time body landmark rendering
* Pose connection mapping

## Body Measurement System

Current measurements include:

* Shoulder width
* Waist width estimation
* Body proportion calculations

## Body Ratio Analysis

The system is being designed to calculate ratios like:

[
\text{Shoulder-to-Waist Ratio}
]

which will later help classify body types and recommend poses accordingly.

---

# Current Project Status

The project is currently in the:

## “Computer Vision & Body Analysis Foundation Stage”

Completed:

* Pose detection pipeline
* Landmark extraction
* Real-time rendering
* Shoulder line detection
* Initial waist measurement logic

In Progress:

* Accurate waist detection
* Body ratio analysis
* Body type classification

Planned:

* AI pose recommendation system
* Pose scoring engine
* Personalized recommendations
* Dataset creation
* Frontend/UI

---

# Project Workflow

```text
Webcam Input
      ↓
Pose Detection using MediaPipe
      ↓
Landmark Extraction
      ↓
Body Measurement Calculation
      ↓
Body Ratio Analysis
      ↓
Body Type Classification
      ↓
Pose Recommendation Engine
```

---

# Folder Structure

```text
Pose_Guide/
│
├── main.py
├── pose_detector.py
├── body_analyzer.py
├── utils/
├── models/
├── datasets/
└── recommendation_engine/
```

---

# Installation Guide

## Clone the Repository

```bash
git clone <repository-link>
cd Pose_Guide
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install mediapipe==0.10.14
pip install opencv-python
pip install numpy
```

---

# Run the Project

```bash
python main.py
```

Press:

```text
Q
```

to quit the webcam window.

---

# Future Scope

Future improvements planned for PoseGuide include:

## AI-Based Pose Recommendation

* Personalized pose suggestions
* Dynamic pose generation

## Body Type Classification

* Athletic
* Rectangle
* Triangle
* Inverted Triangle
* Other body structures

## Pose Scoring System

* Evaluate pose quality
* Analyze symmetry and posture

## Smart Photography Assistant

* Camera angle suggestions
* Posture correction
* Real-time feedback

## Machine Learning Integration

* Recommendation systems
* Pose similarity models
* Personalized AI models

## Mobile/Web Application

* Cross-platform accessibility
* Real-time AI pose assistant

---

# Applications

PoseGuide can be useful for:

* Photography enthusiasts
* Social media creators
* Fashion influencers
* Fitness applications
* Virtual styling systems
* AI-assisted photography tools

---

# Why This Project Matters

PoseGuide combines:

* Artificial Intelligence
* Computer Vision
* Human Pose Estimation
* Recommendation Systems

to create a smart and personalized photography experience.

The project demonstrates how AI can be used not only for automation, but also for creativity, confidence, and user experience enhancement.

---

# Author

## Samarth Gupta

AI/ML Enthusiast | Computer Vision Learner | Backend & AI Developer

---

# License

This project is for educational and research purposes.
