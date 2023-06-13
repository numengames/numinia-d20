from typing import List
import random
import discord
from d20_governance.utils.constants import CIRCLE_EMOJIS
from d20_governance.utils.utils import Quest

# Voting functions
majority = lambda results: max(results, key=results.get) if max(results.values()) > sum(results.values()) / 2 else None
consensus = lambda results: max(results, key=results.get) if max(results.values()) == sum(results.values()) else None

VOTING_FUNCTIONS = {"majority": majority, "consensus": consensus}

class VoteView(discord.ui.View):
    def __init__(self, ctx, timeout):
        super().__init__(timeout=timeout)
        self.ctx = ctx
        self.votes = {}

    async def on_timeout(self):
        self.stop()

    def add_option(self, label, value, emoji=None):
        option = discord.SelectOption(label=label, value=value, emoji=emoji)
        if not self.children:
            self.add_item(
                discord.ui.Select(
                    options=[option],
                    placeholder="Vote on the available options.",
                    min_values=1,
                    max_values=1,
                    custom_id="vote_select",
                )
            )
        else:
            self.children[0].options.append(option)

    @discord.ui.select(custom_id="vote_select")
    async def on_vote_select(
        self, interaction: discord.Interaction, select: discord.ui.Select
    ):
        vote = interaction.data.get("values")[0] # We enforce above that only one option can be selected
        player = interaction.user 
        if player not in self.votes or self.votes[player] != vote:
            self.votes[player] = vote
            await interaction.response.send_message(
                "Your vote has been recorded.", ephemeral=True
            )
        else:
            await interaction.response.send_message(
                "You've already voted.", ephemeral=True
            )


async def vote(
    ctx,
    quest: Quest,
    question: str = None,
    options: List[str] = [],
    decision_module: str = "majority",
    timeout: int = 60,
):
    """
    Trigger a vote
    """
    print(f"A vote has been triggered. The decision module is: {decision_module}")

    if len(options) > 10 or (not quest.solo_mode and len(options) < 2):
        await ctx.send("Error: A poll must have between 2 and 10 options.")
        return

    # Define embed
    embed = discord.Embed(
        title=f"Vote: {question}",
        description=f"Decision module: {decision_module}",
        color=discord.Color.dark_gold(),
    )

    # Create list of options with emojis
    assigned_emojis = random.sample(CIRCLE_EMOJIS, len(options))

    options_text = ""
    for i, option in enumerate(options):
        options_text += f"{assigned_emojis[i]} {option}\n"

    # Create vote view UI
    vote_view = VoteView(ctx, timeout)

    # Add options to the view dropdown select menu
    for i, option in enumerate(options):
        vote_view.add_option(label=option, value=str(i), emoji=assigned_emojis[i])

    # Send embed message and view
    await ctx.send(embed=embed, view=vote_view)
    await vote_view.wait()

    # Calculate total votes per member interaction
    results = await get_vote_results(
        ctx,
        vote_view.votes,
        options
    )

    message = get_results_message(results)
    if results:
        winning_option = VOTING_FUNCTIONS[decision_module](results)
    else:
        winning_option = None

    # Display results
    embed = discord.Embed(
        title=f"Results for: `{question}`:",
        description=message,
        color=discord.Color.dark_gold(),
    )

    await ctx.send(embed=embed)
    return winning_option


async def get_vote_results(
    results, votes, options
):
    print("Getting vote results")
    results = {}
    # for each member return results of vote
    for vote in votes.values():
        option_index = int(vote)
        option = options[option_index]
        results[option] = results.get(option, 0) + 1

    return results

def get_results_message(results):
    total_votes = sum(results.values())
    message = f"Total votes: {total_votes}\n\n"
    for option, votes in results.items():
        percentage = (votes / total_votes) * 100 if total_votes else 0
        message += f"Option `{option}` recieved `{votes}` votes ({percentage:.2f}%)\n\n"

    return message

