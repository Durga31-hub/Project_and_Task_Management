from django.contrib import admin
from .models import Project, Milestone, Task, TimeLog, ProjectAssignment, TaskComment


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('meta',)
    list_display = ('name', 'code', 'status', 'start_date', 'end_date', 'owner_user_uuid', 'created_at')
    search_fields = ('name', 'code', 'status')
    list_filter = ('status', 'start_date', 'end_date')


@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'due_date', 'created_at')
    search_fields = ('title', 'status')
    list_filter = ('status', 'due_date')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'milestone', 'priority', 'status', 'due_date', 'assignee_uuid')
    search_fields = ('title', 'status', 'priority')
    list_filter = ('status', 'priority', 'due_date')


@admin.register(TimeLog)
class TimeLogAdmin(admin.ModelAdmin):
    list_display = ('task', 'user_uuid', 'start_time', 'end_time', 'minutes', 'billable', 'approved')
    list_filter = ('billable', 'approved')
    search_fields = ('task__title', 'user_uuid')


@admin.register(ProjectAssignment)
class ProjectAssignmentAdmin(admin.ModelAdmin):
    list_display = ('project', 'user_uuid', 'role', 'allocation_percent', 'start_date', 'end_date')
    search_fields = ('role',)
    list_filter = ('role', 'start_date', 'end_date')


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'author_uuid', 'created_at')
    search_fields = ('body',)
