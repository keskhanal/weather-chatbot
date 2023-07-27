# Weather Bot based on Rasa

Welcome to the Weather Bot based on Rasa! This chatbot is designed to provide real-time weather information for various cities. It utilizes the Rasa framework for natural language understanding (NLU) and interactive conversation handling.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Weather Bot is a language model powered by Rasa, which enables it to understand natural language queries about the weather and respond with accurate weather data for specified locations.

## Getting Started
Create conda environment and activate the environment
```bash
#create environment
conda create -n weatherbot python=3.8

#activate environment
conda activate weatherbot
```

1. Clone the Weather Bot repository:
```bash
git clone https://github.com/keskhanal/weather-chatbot.git
cd weather-chatbot
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Train the Rasa model:
```bash
rasa train
```

4. Start the Rasa action server:
```bash
rasa run actions
```

5. Start the chatbot server:
```bash
rasa shell
```
Now, you can interact with the Weather Bot and ask for weather information for different cities!

## Usage
The Weather Bot is capable of providing current weather conditions, temperature, humidity, and forecasts for various cities worldwide. You can interact with the bot using natural language input to inquire about the weather.

## Customization
You can customize the Weather Bot to add more features or tailor it to specific weather services. For instance, you can extend its capabilities to provide weather alerts, historical weather data, or weather-related recommendations.

To customize the chatbot, you can edit the `data/nlu.yml`, `data/rules.yml`, and `domain.yml` files. After making changes, retrain the model using `rasa train` to apply the updates.

## Contributing
We welcome contributions from the community to improve and enhance the Weather Bot. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License
The Weather Bot is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

---
Thank you for using the Weather Bot! We hope it helps you stay informed about the weather conditions in different locations. If you have any questions or need assistance, feel free to ask!

