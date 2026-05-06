from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Goal


@login_required


def goal_list(request):
    user = get_goal_user(request)

    if request.user.is_authenticated:
        goals = Goal.objects.filter(user=user)
    else:
        # For testing without login, show test user's goals
        goals = Goal.objects.filter(user=user)

    return render(request, 'goals.html', {
        'goals': goals
    })


def create_goal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target_amount = request.POST.get('target_amount')
        deadline = request.POST.get('deadline')

        if name and target_amount and deadline:
            user = get_goal_user(request)

            Goal.objects.create(
                user=user,
                name=name,
                target_amount=target_amount,
                current_amount=0,
                deadline=deadline
            )

            messages.success(request, 'Goal created successfully!')
            return redirect('goal_list')

        else:
            messages.error(request, 'Please fill all fields.')
            return redirect('/goals/?show=create')

    return redirect('goal_list')


def update_goal_progress(request, goal_id):
    user = get_goal_user(request)

    goal = get_object_or_404(Goal, id=goal_id, user=user)

    if request.method == 'POST':
        current_amount = request.POST.get('current_amount')

        if current_amount:
            goal.current_amount = current_amount
            goal.save()

            messages.success(request, 'Goal progress updated!')
            return redirect('goal_list')

        else:
            messages.error(request, 'Please enter a current amount.')
            return redirect('goal_list')

    return redirect('goal_list')


def delete_goal(request, goal_id):
    user = get_goal_user(request)

    goal = get_object_or_404(Goal, id=goal_id, user=user)

    if request.method == 'POST':
        goal.delete()
        messages.success(request, 'Goal deleted successfully!')

    return redirect('goal_list')