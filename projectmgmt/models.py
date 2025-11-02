import uuid
from django.db import models

# ✅ Project Model
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    customer_uuid = models.UUIDField(null=True, blank=True)
    owner_user_uuid = models.UUIDField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default='planning')
    meta = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects_project'

    def __str__(self):
        return self.name


# ✅ Milestone Model (linked to Project)
class Milestone(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects_milestone'

    def __str__(self):
        return self.title


# ✅ Task Model (linked to Project & optionally Milestone)
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    milestone = models.ForeignKey(Milestone, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assignee_uuid = models.UUIDField(null=True, blank=True)
    reporter_uuid = models.UUIDField(null=True, blank=True)
    priority = models.CharField(max_length=20, default='normal')
    status = models.CharField(max_length=30, default='todo')
    estimate_minutes = models.IntegerField(null=True, blank=True)
    spent_minutes = models.IntegerField(default=0)
    labels = models.JSONField(default=list)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects_task'

    def __str__(self):
        return self.title


# ✅ TimeLog Model (linked to Task)
class TimeLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='timelogs', null=True, blank=True)
    user_uuid = models.UUIDField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    minutes = models.IntegerField()
    billable = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
    approved_by = models.UUIDField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects_timelog'


# ✅ Project Assignment Model (linked to Project)
class ProjectAssignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='assignments', null=True, blank=True)
    user_uuid = models.UUIDField()
    role = models.CharField(max_length=100)
    allocation_percent = models.IntegerField(default=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects_assignment'


# ✅ Task Comment Model (linked to Task & Project)
class TaskComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_comments', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    author_uuid = models.UUIDField()
    body = models.TextField()
    attachments = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'projects_comment'
