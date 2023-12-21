from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


def index(request):
    """The home page for Learning Log app."""
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    context = {"topics": topics}
    return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)

    _check_topic_owner(topic.owner, request.user)

    entries = topic.entry_set.order_by("-date_added")
    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("learning_logs:topics")

    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


def edit_topic(request, topic_id):
    """Edit an existing topic."""
    topic = get_object_or_404(Topic, id=topic_id)

    _check_topic_owner(topic.owner, request.user)

    if request.method != "POST":
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topics")

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/edit_topic.html", context)


@login_required
def delete_topic(request, topic_id):
    """Delete a topic."""
    topic = get_object_or_404(Topic, id=topic_id)
    entires = topic.entry_set.all()

    _check_topic_owner(topic.owner, request.user)

    if request.method == "POST":
        topic.delete()
        return redirect("learning_logs:topics")

    context = {"topic": topic, "entries": entires}
    return render(request, "learning_logs/delete_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id)

    _check_topic_owner(topic.owner, request.user)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id=topic_id)

    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    _check_topic_owner(topic.owner, request.user)

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


@login_required
def delete_entry(request, entry_id):
    """Delete an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id)
    topic = entry.topic

    _check_topic_owner(topic.owner, request.user)

    if request.method == "POST":
        entry.delete()
        return redirect("learning_logs:topic", topic_id=topic.id)

    context = {"entry": entry, "topic": topic}
    return render(request, "learning_logs/delete_entry.html", context)


def _check_topic_owner(owner, user):
    """Check if user is the owner of the topic."""
    if owner != user:
        raise Http404
