from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from chatbot_app.bot import build_bot, train_bot


def _get_chatbot_history(request: HttpRequest) -> list[dict[str, str]]:
    return request.session.get("chatbot_history", [])


def _save_chatbot_history(request: HttpRequest, history: list[dict[str, str]]) -> None:
    request.session["chatbot_history"] = history
    request.session.modified = True


def chat_view(request: HttpRequest) -> HttpResponse:
    """Render the small browser UI and keep a short message history in session."""
    history = _get_chatbot_history(request)
    bot = build_bot()
    train_bot(bot)

    if request.method == "POST":
        user_message = request.POST.get("message", "").strip()
        if user_message:
            bot_reply = str(bot.get_response(user_message))
            history.append({"role": "user", "text": user_message})
            history.append({"role": "bot", "text": bot_reply})
            _save_chatbot_history(request, history)
        return redirect("chat-home")

    return render(
        request,
        "chatbot_app/index.html",
        {"history": history},
    )
