# PeerStudy 🎓
### *Streamlining Collaborative Learning through Data-Driven Insights*

[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue)](https://www.python.org/)
[![Docker: Supported](https://img.shields.io/badge/Docker-Ready-cyan)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

**PeerStudy** is a lightweight, containerized Python framework designed to facilitate and analyze peer-to-peer learning environments. Whether managing study groups or analyzing student collaboration patterns, PeerStudy provides the core infrastructure to turn educational data into actionable insights.

---
## 🖼️ Interface Gallery

<p align="center">
  <b>1. Intelligent Quiz Configuration</b><br>
  <img src="image.png" alt="Quiz Settings" width="800">
</p>

---

<p align="center">
  <b>2. Interactive Assessment Interface</b><br>
  <img src="image1.png" alt="Quiz Interface" width="800">
</p>

---

<p align="center">
  <b>3. Performance Analytics Dashboard</b><br>
  <img src="image2.png" alt="Quiz Results" width="800">
</p>
## 🚀 Key Features

- **Modular Architecture:** Built with a clean `src/` structure and `setup.py` for seamless package installation.
- **Docker Integration:** Fully containerized with a `Dockerfile`, ensuring consistent behavior across all development and production environments.
- **Scalable Design:** Designed to be easily integrated into larger educational management systems (EMS).
- **Environment Agnostic:** Pre-configured with `.gitignore` and `requirements.txt` for rapid onboarding.

---

## 🛠️ Technical Stack

- **Backend:** Python 3.x
- **Infrastructure:** Docker (for isolated environment execution)
- **Packaging:** Setuptools (for modular distribution)

---

## 📦 Getting Started

### Using Docker (Recommended)
```bash
# Build the image
docker build -t peerstudy .

# Run the container
docker run peerstudy