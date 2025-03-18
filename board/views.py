from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board, Card
from .forms import BoardForm, CardForm, AddMemberForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

@login_required
def board_list(request):
    boards = request.user.boards.all() | Board.objects.filter(owner=request.user)
    return render(request, "board/board_list.html", {"boards": boards})

@login_required
def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.user != board.owner and request.user not in board.members.all():
        return redirect("board_list")
    
    cards = board.card_set.all().order_by("-created_at")
    return render(request, "board/board_detail.html", {"board": board, "cards": cards})

@login_required
def create_board(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.owner = request.user
            board.save()
            return redirect("board_list")
    else:
        form = BoardForm()
    return render(request, "board/create_board.html", {"form": form})

@login_required
def create_card(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.user != board.owner and request.user not in board.members.all():
        return redirect("board_list")

    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.board = board
            card.author = request.user
            card.save()
            return redirect("board_detail", board_id=board.id)
    else:
        form = CardForm()
    return render(request, "board/create_card.html", {"form": form, "board": board})

@login_required
def add_member(request, board_id):
    board = get_object_or_404(Board, id=board_id, owner=request.user)

    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            user = User.objects.get(username=username)
            board.members.add(user)
            return redirect("board_detail", board_id=board.id)
    else:
        form = AddMemberForm()
    
    return render(request, "board/add_member.html", {"form": form, "board": board})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board_list')
    else:
        form = UserCreationForm()
    return render(request, 'board/signup.html', {'form': form})