from django.core.management.base import BaseCommand

from chatbot_app.bot import build_bot, train_bot


class Command(BaseCommand):
    help = "Start an interactive terminal chatbot session."

    def handle(self, *args, **options):
        bot = build_bot()
        train_bot(bot)

        self.stdout.write(self.style.SUCCESS("Chatbot is ready. Type 'exit' to quit.\n"))

        while True:
            try:
                user_input = input("user: ").strip()
            except (EOFError, KeyboardInterrupt):
                self.stdout.write("\nbot: goodbye")
                break

            if user_input.lower() in {"exit", "quit"}:
                self.stdout.write("bot: goodbye")
                break
            if not user_input:
                continue

            response = bot.get_response(user_input)
            self.stdout.write(f"bot: {response}")
