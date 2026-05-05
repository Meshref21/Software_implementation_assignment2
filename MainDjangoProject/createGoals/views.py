from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Goal



def goal_list(request):
    goals = Goal.objects.filter(user=request.user)

    return render(request, 'goals/goal_list.html', {
        'goals': goals
    })



def create_goal(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        target_amount = request.POST.get('target_amount')
        deadline = request.POST.get('deadline')

        if name and target_amount and deadline:
            Goal.objects.create(
                user=request.user,
                name=name,
                target_amount=target_amount,
                current_amount=0,
                deadline=deadline
            )

            messages.success(request, 'Goal created successfully!')
            return redirect('goal_list')
        else:
            messages.error(request, 'Please fill all fields.')

    return render(request, 'goals/create_goal.html')



def update_goal_progress(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)

    if request.method == 'POST':
        current_amount = request.POST.get('current_amount')

        if current_amount:
            goal.current_amount = current_amount
            goal.save()

            messages.success(request, 'Goal progress updated!')
            return redirect('goal_list')
        else:
            messages.error(request, 'Please enter a current amount.')

    return render(request, 'goals/update_goal.html', {
        'goal': goal
    })