# pylint: disable=R0201

import base64
import os
from io import BytesIO

from discord import File, Option, User
from discord.ext.commands import Bot, Cog, Context, command
from google.auth.transport.requests import Request
from firebase_admin import firestore
from google.cloud.firestore import Increment
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.document import DocumentReference

from main_node import treat_command

ENVIRONMENT = os.getenv("ENVIRONMENT")
FUNCTION_BASE_URL = "https://us-central1-archy-f06ed.cloudfunctions.net/"
LOADING_MESSAGE = "Loading..."


class Commands(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.request = Request()
        self.db = firestore.client()

    def is_active_command(self, server_id: str, command_name: str) -> bool:
        """Check if a command is active in the firestore db."""
        if (command_name.startswith(("dev_", "team_"))) and server_id == "964701887540645908":
            return True

        function_collection: CollectionReference = (
            self.db.collection("servers").document(server_id).collection("functions")
        )
        doc_ref: DocumentReference = function_collection.document(command_name)
        doc: DocumentSnapshot = doc_ref.get()

        return doc.get("active") if doc.exists else False

    def increment_command_count(self, server_id: str, command_name: str) -> None:
        function_collection: CollectionReference = (
            self.db.collection("servers").document(server_id).collection("functions")
        )
        doc_ref: DocumentReference = function_collection.document(command_name)
        if doc_ref.get().exists:
            doc_ref.update({"count": Increment(1)})

    @command(description="Nsec stats")
    async def nsec_stat(self, ctx: Context) -> None:
        if ctx.guild_id == 909917470507286568:
            my_collection = self.db.collection("fobChallenge")
            count_query = list(my_collection.get())
            message = f"Number of user that asked Archy for an instance: {len(count_query)}\n"
            message += "".join([f"- <@{doc.id}>\n" for doc in my_collection.get()])
            await ctx.respond(message)

    @command(description="go")
    async def go(self, ctx: Context) -> None:  # pylint: disable=invalid-name
        server_id = str(ctx.guild.id)
        command_name = "go"

        data = {
            "server_id": server_id,
            "channel_id": "Slash_Command",
        }
        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="Hello! :)")
    async def hello(self, ctx: Context) -> None:
        command_name = "hello"

        data = {
            "server_id": str(ctx.guild.id),
            "user_id": str(ctx.author.id),
        }
        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="Return the leaderboard")
    async def leaderboard(self, ctx: Context) -> None:
        command_name = "leaderboard"

        data = {
            "server_id": str(ctx.guild.id),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="answers your question")
    async def answer(self, ctx: Context, question: Option(str, "your question", required=True)) -> None:
        command_name = "answer"

        data = {
            "server_id": str(ctx.guild.id),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        response = f"Question: {question}\nAnswer: {await treat_command(ctx, command_name, data)}"

        await interaction.edit_original_response(content=response)

    @command(description="Request a gif")
    async def gif(self, ctx: Context, query: Option(str, "query to search", required=True)) -> None:
        command_name = "gif"

        data = {
            "server_id": str(ctx.guild.id),
            "params": str(query.split(" ")),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="Template function in Java")
    async def java(self, ctx: Context) -> None:
        command_name = "java"

        data = {
            "server_id": str(ctx.guild.id),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="Return a random froge")
    async def froge(self, ctx: Context) -> None:
        command_name = "froge"

        data = {
            "server_id": str(ctx.guild.id),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)

    @command(description="Show your level")
    async def level(self, ctx: Context, mention: Option(User, "wanna check someone else's?", required=False)) -> None:
        server_id = str(ctx.guild.id)
        command_name = "level"

        data = {
            "server_id": server_id,
            "server_name": str(ctx.guild.name),
            "user_id": str(ctx.author.id),
        }
        if mention:
            data["mentions"] = [str(mention.id)]

        interaction = await ctx.respond(LOADING_MESSAGE)
        response = await treat_command(ctx, command_name, data)
        if response.split(",")[0] == "data:image/png;base64":
            await interaction.edit_original_response(
                content=None,
                file=File(BytesIO(base64.b64decode(response.split(",")[1])), "image.png"),
            )
        else:
            await interaction.edit_original_response(content=response)

    @command(description="You give me a HTTP code, I give you something nice in return")
    async def http(self, ctx: Context, query: Option(int, "HTTP code", required=True)) -> None:
        command_name = "http"

        data = {
            "server_id": str(ctx.guild.id),
            "params": str(query.split(" ")),
        }

        interaction = await ctx.respond(LOADING_MESSAGE)
        message = await treat_command(ctx, command_name, data)
        await interaction.edit_original_response(content=message)
