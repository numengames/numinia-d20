
# D20 Governance Bot

## Prerequisites
- Python, pip & poetry installed or Docker.
- [Discord account](https://discord.com) with 2FA activated.
- An api key from [stability](https://stability.ai)

Important: This code has been tested only on x86-64 architectures and is not compatible with ARM architectures, including the new Apple Silicon processors (M1, M2, etc.). If you are using a device with Apple Silicon, this code may not function properly. Use Docker if you want to run it locally on that devices.

## How to run locally

1. Install poetry for managing dependencies
2. Run `poetry install`
3. Run `poetry shell`
4. Create a .env file and set DISCORD_TOKEN environment variable to your bot's token as well as STABILITY_API_KEY to your OpenAI API key.
5. Make sure the bot has been added to your server with admin permissions.
6. Run python3 d20_governance/__main__.py. The bot will create all the necessary channels in your server once it runs.
7. Try the `/solo` command in the #d20-agora channel to start a solo quest, and use -f for fast mode
8. Running tests
    Run `pytest` from project root.

## How to run locally using Docker

1. Ensure you have Docker installed on your system.
2. Build the Docker image using:
   ```bash
   docker build -t d20-governance-bot .
   ```
3. Create an .env file including the DISCORD_TOKEN and STABILITY_API_KEY tokens.
3. Run the container passing the .env file:
    ```bash
    docker run --rm -d --env-file .env --name my-d20-bot d20-governance-bot
    ```

## Creating an application for the bot

You can create and manage Discord applications (bots) via the following website:

- [Discord Developer Portal](https://discord.com/developers)

Make sure you do the following steps:

1. Ensure you have the 2FA in your account activated.
2. From the [Applications tab](https://discord.com/developers/applications), create a new application.
3. In the application (When you create a new one, you're redirected by default inside):
    1. Go to the **General Information** tab and update the App Icon and the name of the application.
    2. Go to the **Bot** tab, first, update the icon, secondly, **set all the privileged Gateway Intents** and lastly get a new token by clicking in *Reset Token*. That's the DISCORD_TOKEN you need to pass in the environment variable.
    3. Go to the **Instalation** and set the install link display to a Custom URL and set the `&scope=bot&permissions=8` at the end of the URL (as a trick to grab the URL, use the discord provided link)
4. Invite the bot to the server you want and set up a role for it.


## Overview
The d20 bot allows communities to play governance games in an LLM-mediated environment. Individuals and groups can come together to embark on a governance “quest”, where they make lightweight decisions about the community and experience varied mechanisms of decision-making. The bot moderates the governance game through different "culture modules" - playfully modifying users' messages to cultivate diverse interaction environments for participants.

[Join our discord server to try it out!](https://discord.gg/sSSRxWVuxE)

### Build A Group Voice Game

#### Stages

##### Propose a quest from the agora

Start in the #d20-agora channel and use the `/embark` command to start a new quest, specifying which quest you want to play as well as the number of players. The bot will create a new channel for the quest and direct you to it.

##### The Quest Begins

Players are welcomed and introduced to the game's objectives: deciding the group's name, main topic of interest, and way of speaking. The group explores conversational confusion and deliberates to shape the community's communication in the agora. 

##### Group Name
 
Players propose names for the group and deliberate. A random culture module may be activated during this period, affecting the conversation. After deliberation, players vote on the proposed names.

##### Group's Main Topic of Interest

Players propose and deliberate on the group's main topic of interest. After a set deliberation time, players vote on the proposed topics.

##### Group Way of Speaking

Players discuss and propose the group's way of speaking, considering formality, tone, and style.


#### After the Game

A record of the decisions made is published, summarizing the options considered and methods used. 

The "culture" of the community is generated from the group decisions. A new wildcard prompt is generated based on the decided upon community name, purpose, and goal. Players then return to #d20-agora channel where they can test out their new community culture using the `/wildcard` command. When wildcard mode is on, all language that happens in the agora will be transformed according to the community's culture.

### Culture of your community

Your culture will affect your communication. Think about what cultural environment you want in your community and how you would like that culture to impact your communication.
For example, you already experienced a culture of “eloquence” where your communication with your fellow community members was automatically transformed to be in verbose Shakespearean rhetoric. 

The culture you decide on will become a new communication constraint you can invoke in the agora channel and will become playable in subsequent Build a Community games.

### Agora 
The agora channel (#d20-agora) is a free-form Discord channel where your community can test out the various features and embark on quests. 

#### Decision Modules
- **Majority**: The Majority decision model allows for decisions when the community is not in full agreement. Majority voting aims to reach a decision even if not all players agree, more than half of the group agree. 
- **Consensus**: Consensus voting is also known as unanimous consent. It aims for full agreement through discussion. 
- **Lazy Consensus**: Lazy Consensus is a decision mechanism that assumes players to agree with the presented option unless they explicitly object to it. Decision occurs when no objections, rather than unanimous agreement. 
- **Implicit Feudalism**: Implicit Feudalism is the decision making method used by the bot to make a decision with the group is unable to reach a decision using the above decision modules.

#### Culture Modules
- **Amplify**: Transform messages to highten the sentiment of the original message.
- **Eloquence**: Transform messages to be elaborate, persuasive, and Shakespearean. 
- **Obscurity**: Transform messages text to make it obscure and hard to read.
- **Ritual**: Transform messages to be in agreement with previous messages. 
- **Values**: Check messages to see if they are aligned with the values of the community. 
- **Wildcard**: Transform messages to take on the voice of the most recent group to complete a quest.

### Values Feature 
- Propose value and definition
- Propose-values
- Revise-values 
- Decision-making about values: lazy consensus
- Check-values of messages

## Contributing

We welcome contributions! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/awesome-feature).
3. Make your changes and commit them (git commit -am 'Add an awesome feature').
4. Push the branch (git push origin feature/awesome-feature).
5. Open a pull request.

## 📜 License

Code released under the [MIT License](https://opensource.org/license/MIT).