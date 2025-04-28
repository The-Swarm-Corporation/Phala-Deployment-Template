
# Swarms 1-Click Template on Phala Cloud

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


[![GitHub stars](https://img.shields.io/github/stars/The-Swarm-Corporation/Legal-Swarm-Template?style=social)](https://github.com/The-Swarm-Corporation/Legal-Swarm-Template)
[![Swarms Framework](https://img.shields.io/badge/Built%20with-Swarms-blue)](https://github.com/kyegomez/swarms)


## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/0xshawn/Phala-Deployment-Template

# Install requirements
pip3 install -r requirements.txt

# Set your task in the .env file or pass it in the yaml file on the bottom `task:`
export WORKSPACE_DIR="agent_workspace" 
export OPENAI_API_KEY=""
export OPENAI_API_BASE=""
export MODEL_NAME=""

# Run the swarm
python3 main.py
```


## 🛡️ Running Swarms Agent in Phala TEE

Welcome! This guide will walk you through running your Swarms Agent in a Trusted Execution Environment (TEE) using Phala Cloud. This setup ensures your agent runs in a secure, isolated environment.

### 📋 Prerequisites

- A Swarms Agent code repository (or docker image)
- A Phala Cloud account
- An OpenAI API key

### 📝 Step-by-Step Guide

Firstly, you need to register a [Phala Cloud](https://cloud.phala.network/) account before you can create a new Swarms agent application.

#### 1. ⚙️ Configure Your Environment

First, prepare your `docker-compose.yaml` file. You can find an example in [docker-compose.yaml](./docker-compose.yaml). Make sure to have your OpenAI API key ready.

```yaml
services:
  swarms-agent-server:
    image: python:3.12-slim
    volumes:
      - swarms:/app
    restart: always
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    command: # Run swarms agent example
      - /bin/sh
      - -c
      - |
        # install dependencies
        apt update && apt install -y git python3-pip
        mkdir -p /app && cd /app

        git clone --depth 1 https://github.com/The-Swarm-Corporation/swarms-examples
        cd swarms-examples/
        pip install -r requirements.txt && pip install langchain-community langchain-core
        cd examples/agents/
        python o1_preview.py

        # keep container running
        sleep infinity

volumes:
  swarms:
```

#### 2. 🚀 Deploy Your Agent

1. Navigate to the [Phala Cloud dashboard](https://cloud.phala.network/dashboard)
2. Click `Deploy` button on the Phala Cloud dashboard.
3. Choose `docker-compose.yaml` and then click `Advanced` tab to paste the content of your docker-compose.yaml file.
4. Importantly, make sure to add the `OPENAI_API_KEY` in the `Encrypted Secrets` section with your own OpenAI API key.
5. Click `Create` button to create a new Swarms agent application.
   <p align="center">
   <img src="../docs/swarms_cloud/imgs/01_create_agent_on_phala_cloud.png" alt="Creating a Swarms agent on Phala Cloud" style="width: 700px;">
   </p>

#### 3. 📊 Monitor Your Deployment

1. Check the initialization logs of your agent
   <p align="center">
   <img src="../docs/swarms_cloud/imgs/02_serial_logs.png" alt="Agent initialization logs" style="width: 700px;">
   <img src="../docs/swarms_cloud/imgs/03_serial_logs.png" alt="Detailed initialization logs" style="width: 700px;">
   </p>

2. Verify your container is running
   <p align="center">
   <img src="../docs/swarms_cloud/imgs/04_swarms_agent_containers.png" alt="Swarms Agent Container Status" style="width: 700px;">
   </p>

3. Monitor your agent's output
   <p align="center">
   <img src="../docs/swarms_cloud/imgs/05_agent_output.png" alt="Swarms Agent Logs" style="width: 700px;">
   </p>

#### 4. ✅ Verify TEE Attestation

Ensure your agent is running in a secure TEE environment by checking the attestation proof on the [TEE Attestation Explorer](https://proof.t16z.com/).

<p align="center">
<img src="../docs/swarms_cloud/imgs/06_attestation.png" alt="TEE Attestation Verification" style="width: 700px;">
</p>

### 🎉 Success!

You've successfully deployed your Swarms Agent in a secure TEE environment using Phala Cloud. Your agent is now running in an isolated, trusted execution environment, ensuring enhanced security for your AI operations.

If you have any questions, please reach out to Phala on [Phala Cloud](https://cloud.phala.network/).


## 📬 Contact

Questions? Reach out:
- Phala Cloud:
    - Community: https://github.com/Phala-Network/phala-cloud-community
    - Twitter: [@PhalaNetwork](https://twitter.com/PhalaNetwork)
    - Discord: [Phala Network](https://discord.gg/phala-network)
    - Telegram: [Phala Network](https://t.me/+nbhjx1ADG9EyYmI9)
- Swarms:
    - Twitter: [@kyegomez](https://twitter.com/kyegomez)
    - Email: kye@swarms.world
