# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


class JcVideotalkDd(models.Model):
    talk_dd = models.CharField(max_length=50, blank=True, null=True)
    talk_bh = models.CharField(max_length=100, blank=True, null=True)
    server_ip = models.CharField(max_length=100, blank=True, null=True)
    server_td = models.CharField(max_length=100, blank=True, null=True)
    server_username = models.CharField(max_length=100, blank=True, null=True)
    server_pwd = models.CharField(max_length=50, blank=True, null=True)
    talk_ip = models.CharField(max_length=255, blank=True, null=True)
    talk_temp1 = models.CharField(max_length=50, blank=True, null=True)
    talk_temp2 = models.CharField(max_length=50, blank=True, null=True)
    talk_temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jc_videotalk_dd'


class JcVideotalkhis(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    talk_dd = models.CharField(max_length=50, blank=True, null=True)
    talk_bh = models.CharField(max_length=50, blank=True, null=True)
    talk_type = models.CharField(max_length=50, blank=True, null=True)
    talk_starttime = models.CharField(max_length=50, blank=True, null=True)
    talk_endtime = models.CharField(max_length=50, blank=True, null=True)
    talk_record = models.CharField(max_length=200, blank=True, null=True)
    talk_pic = models.CharField(max_length=100, blank=True, null=True)
    talk_pictime = models.CharField(max_length=50, blank=True, null=True)
    talk_temp1 = models.CharField(max_length=50, blank=True, null=True)
    talk_temp2 = models.CharField(max_length=50, blank=True, null=True)
    talk_temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jc_videotalkhis'


class JsGenTable(models.Model):
    table_name = models.CharField(primary_key=True, max_length=64)
    class_name = models.CharField(max_length=100)
    comments = models.CharField(max_length=500)
    parent_table_name = models.CharField(max_length=64, blank=True, null=True)
    parent_table_fk_name = models.CharField(max_length=64, blank=True, null=True)
    tpl_category = models.CharField(max_length=200, blank=True, null=True)
    data_source_name = models.CharField(max_length=64, blank=True, null=True)
    package_name = models.CharField(max_length=500, blank=True, null=True)
    module_name = models.CharField(max_length=30, blank=True, null=True)
    sub_module_name = models.CharField(max_length=30, blank=True, null=True)
    function_name = models.CharField(max_length=200, blank=True, null=True)
    function_name_simple = models.CharField(max_length=50, blank=True, null=True)
    function_author = models.CharField(max_length=50, blank=True, null=True)
    gen_base_dir = models.CharField(max_length=1000, blank=True, null=True)
    options = models.CharField(max_length=1000, blank=True, null=True)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_gen_table'


class JsGenTableColumn(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    column_name = models.CharField(max_length=64)
    column_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    column_type = models.CharField(max_length=100)
    column_label = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=500)
    attr_name = models.CharField(max_length=200)
    attr_type = models.CharField(max_length=200)
    is_pk = models.CharField(max_length=1, blank=True, null=True)
    is_null = models.CharField(max_length=1, blank=True, null=True)
    is_insert = models.CharField(max_length=1, blank=True, null=True)
    is_update = models.CharField(max_length=1, blank=True, null=True)
    is_list = models.CharField(max_length=1, blank=True, null=True)
    is_query = models.CharField(max_length=1, blank=True, null=True)
    query_type = models.CharField(max_length=200, blank=True, null=True)
    is_edit = models.CharField(max_length=1, blank=True, null=True)
    show_type = models.CharField(max_length=200, blank=True, null=True)
    options = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_gen_table_column'


class JsJobBlobTriggers(models.Model):
    sched_name = models.OneToOneField('JsJobTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True, related_name='JsJobBlobTriggers_sched_name')  # Field name made lowercase.
    trigger_name = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='JsJobBlobTriggers_trigger_name')  # Field name made lowercase.
    trigger_group = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='JsJobBlobTriggers_trigger_group')  # Field name made lowercase.
    blob_data = models.TextField(db_column='BLOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_blob_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class JsJobCalendars(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    calendar_name = models.CharField(db_column='CALENDAR_NAME', max_length=200)  # Field name made lowercase.
    calendar = models.TextField(db_column='CALENDAR')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_calendars'
        unique_together = (('sched_name', 'calendar_name'),)


class JsJobCronTriggers(models.Model):
    sched_name = models.OneToOneField('JsJobTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True, related_name='JsJobCronTriggers_sched_name')  # Field name made lowercase.
    trigger_name = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='JsJobCronTriggers_trigger_name')  # Field name made lowercase.
    trigger_group = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='JsJobCronTriggers_trigger_group')  # Field name made lowercase.
    cron_expression = models.CharField(db_column='CRON_EXPRESSION', max_length=120)  # Field name made lowercase.
    time_zone_id = models.CharField(db_column='TIME_ZONE_ID', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_cron_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class JsJobFiredTriggers(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    entry_id = models.CharField(db_column='ENTRY_ID', max_length=95)  # Field name made lowercase.
    trigger_name = models.CharField(db_column='TRIGGER_NAME', max_length=200)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=200)  # Field name made lowercase.
    fired_time = models.BigIntegerField(db_column='FIRED_TIME')  # Field name made lowercase.
    sched_time = models.BigIntegerField(db_column='SCHED_TIME')  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY')  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=16)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    job_group = models.CharField(db_column='JOB_GROUP', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_nonconcurrent = models.CharField(db_column='IS_NONCONCURRENT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    requests_recovery = models.CharField(db_column='REQUESTS_RECOVERY', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_fired_triggers'
        unique_together = (('sched_name', 'entry_id'),)


class JsJobJobDetails(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    job_name = models.CharField(db_column='JOB_NAME', max_length=200)  # Field name made lowercase.
    job_group = models.CharField(db_column='JOB_GROUP', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    job_class_name = models.CharField(db_column='JOB_CLASS_NAME', max_length=250)  # Field name made lowercase.
    is_durable = models.CharField(db_column='IS_DURABLE', max_length=1)  # Field name made lowercase.
    is_nonconcurrent = models.CharField(db_column='IS_NONCONCURRENT', max_length=1)  # Field name made lowercase.
    is_update_data = models.CharField(db_column='IS_UPDATE_DATA', max_length=1)  # Field name made lowercase.
    requests_recovery = models.CharField(db_column='REQUESTS_RECOVERY', max_length=1)  # Field name made lowercase.
    job_data = models.TextField(db_column='JOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_job_details'
        unique_together = (('sched_name', 'job_name', 'job_group'),)


class JsJobLocks(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    lock_name = models.CharField(db_column='LOCK_NAME', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_locks'
        unique_together = (('sched_name', 'lock_name'),)


class JsJobPausedTriggerGrps(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_paused_trigger_grps'
        unique_together = (('sched_name', 'trigger_group'),)


class JsJobSchedulerState(models.Model):
    sched_name = models.CharField(db_column='SCHED_NAME', primary_key=True, max_length=120)  # Field name made lowercase.
    instance_name = models.CharField(db_column='INSTANCE_NAME', max_length=200)  # Field name made lowercase.
    last_checkin_time = models.BigIntegerField(db_column='LAST_CHECKIN_TIME')  # Field name made lowercase.
    checkin_interval = models.BigIntegerField(db_column='CHECKIN_INTERVAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_scheduler_state'
        unique_together = (('sched_name', 'instance_name'),)


class JsJobSimpleTriggers(models.Model):
    sched_name = models.OneToOneField('JsJobTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True, related_name='JsJobSimpleTriggers_sched_name')  # Field name made lowercase.
    trigger_name = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='JsJobSimpleTriggers_trigger_name')  # Field name made lowercase.
    trigger_group = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='JsJobSimpleTriggers_trigger_group')  # Field name made lowercase.
    repeat_count = models.BigIntegerField(db_column='REPEAT_COUNT')  # Field name made lowercase.
    repeat_interval = models.BigIntegerField(db_column='REPEAT_INTERVAL')  # Field name made lowercase.
    times_triggered = models.BigIntegerField(db_column='TIMES_TRIGGERED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_simple_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class JsJobSimpropTriggers(models.Model):
    sched_name = models.OneToOneField('JsJobTriggers', models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True, related_name='JsJobSimpropTriggers_sched_name')  # Field name made lowercase.
    trigger_name = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_NAME', related_name='JsJobSimpropTriggers_trigger_name')  # Field name made lowercase.
    trigger_group = models.ForeignKey('JsJobTriggers', models.DO_NOTHING, db_column='TRIGGER_GROUP', related_name='JsJobSimpropTriggers_trigger_group')  # Field name made lowercase.
    str_prop_1 = models.CharField(db_column='STR_PROP_1', max_length=512, blank=True, null=True)  # Field name made lowercase.
    str_prop_2 = models.CharField(db_column='STR_PROP_2', max_length=512, blank=True, null=True)  # Field name made lowercase.
    str_prop_3 = models.CharField(db_column='STR_PROP_3', max_length=512, blank=True, null=True)  # Field name made lowercase.
    int_prop_1 = models.IntegerField(db_column='INT_PROP_1', blank=True, null=True)  # Field name made lowercase.
    int_prop_2 = models.IntegerField(db_column='INT_PROP_2', blank=True, null=True)  # Field name made lowercase.
    long_prop_1 = models.BigIntegerField(db_column='LONG_PROP_1', blank=True, null=True)  # Field name made lowercase.
    long_prop_2 = models.BigIntegerField(db_column='LONG_PROP_2', blank=True, null=True)  # Field name made lowercase.
    dec_prop_1 = models.DecimalField(db_column='DEC_PROP_1', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dec_prop_2 = models.DecimalField(db_column='DEC_PROP_2', max_digits=13, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bool_prop_1 = models.CharField(db_column='BOOL_PROP_1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bool_prop_2 = models.CharField(db_column='BOOL_PROP_2', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_simprop_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class JsJobTriggers(models.Model):
    sched_name = models.OneToOneField(JsJobJobDetails, models.DO_NOTHING, db_column='SCHED_NAME', primary_key=True)  # Field name made lowercase.
    trigger_name = models.CharField(db_column='TRIGGER_NAME', max_length=200)  # Field name made lowercase.
    trigger_group = models.CharField(db_column='TRIGGER_GROUP', max_length=200)  # Field name made lowercase.
    job_name = models.ForeignKey(JsJobJobDetails, models.DO_NOTHING, db_column='JOB_NAME', related_name='JsJobTriggers_job_name')  # Field name made lowercase.
    job_group = models.ForeignKey(JsJobJobDetails, models.DO_NOTHING, db_column='JOB_GROUP', related_name='JsJobTriggers_job_group')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=250, blank=True, null=True)  # Field name made lowercase.
    next_fire_time = models.BigIntegerField(db_column='NEXT_FIRE_TIME', blank=True, null=True)  # Field name made lowercase.
    prev_fire_time = models.BigIntegerField(db_column='PREV_FIRE_TIME', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    trigger_state = models.CharField(db_column='TRIGGER_STATE', max_length=16)  # Field name made lowercase.
    trigger_type = models.CharField(db_column='TRIGGER_TYPE', max_length=8)  # Field name made lowercase.
    start_time = models.BigIntegerField(db_column='START_TIME')  # Field name made lowercase.
    end_time = models.BigIntegerField(db_column='END_TIME', blank=True, null=True)  # Field name made lowercase.
    calendar_name = models.CharField(db_column='CALENDAR_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    misfire_instr = models.SmallIntegerField(db_column='MISFIRE_INSTR', blank=True, null=True)  # Field name made lowercase.
    job_data = models.TextField(db_column='JOB_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'js_job_triggers'
        unique_together = (('sched_name', 'trigger_name', 'trigger_group'),)


class JsSysArea(models.Model):
    area_code = models.CharField(primary_key=True, max_length=100)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    area_name = models.CharField(max_length=100)
    area_type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_area'


class JsSysCompany(models.Model):
    company_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    view_code = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    area_code = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_company'


class JsSysCompanyOffice(models.Model):
    company_code = models.CharField(primary_key=True, max_length=64)
    office_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_company_office'
        unique_together = (('company_code', 'office_code'),)


class JsSysConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    config_name = models.CharField(max_length=100)
    config_key = models.CharField(unique=True, max_length=100)
    config_value = models.CharField(max_length=1000)
    is_sys = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_config'


class JsSysDictData(models.Model):
    dict_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    dict_label = models.CharField(max_length=100)
    dict_value = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    description = models.CharField(max_length=500, blank=True, null=True)
    css_style = models.CharField(max_length=500, blank=True, null=True)
    css_class = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_data'


class JsSysDictData1(models.Model):
    dict_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    dict_label = models.CharField(max_length=100)
    dict_value = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    description = models.CharField(max_length=500, blank=True, null=True)
    css_style = models.CharField(max_length=500, blank=True, null=True)
    css_class = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_data-1'


class JsSysDictData2(models.Model):
    dict_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    dict_label = models.CharField(max_length=100)
    dict_value = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    description = models.CharField(max_length=500, blank=True, null=True)
    css_style = models.CharField(max_length=500, blank=True, null=True)
    css_class = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_data-2'




class JsSysDictData5(models.Model):
    dict_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    dict_label = models.CharField(max_length=100)
    dict_value = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    description = models.CharField(max_length=500, blank=True, null=True)
    css_style = models.CharField(max_length=500, blank=True, null=True)
    css_class = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_data5'


class JsSysDictType(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    dict_name = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_type'


class JsSysDictType1(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    dict_name = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_type-1'


class JsSysDictType2(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    dict_name = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_type-2'





class JsSysDictType5(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    dict_name = models.CharField(max_length=100)
    dict_type = models.CharField(max_length=100)
    is_sys = models.CharField(max_length=1)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_dict_type5'


class JsSysEmployee(models.Model):
    emp_code = models.CharField(primary_key=True, max_length=64)
    emp_no = models.CharField(max_length=100, blank=True, null=True)
    emp_name = models.CharField(max_length=100)
    emp_name_en = models.CharField(max_length=100, blank=True, null=True)
    office_code = models.CharField(max_length=64)
    office_name = models.CharField(max_length=100)
    company_code = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'js_sys_employee'


class JsSysEmployee1(models.Model):
    emp_code = models.CharField(primary_key=True, max_length=64)
    emp_no = models.CharField(max_length=100, blank=True, null=True)
    emp_name = models.CharField(max_length=100)
    emp_name_en = models.CharField(max_length=100, blank=True, null=True)
    office_code = models.CharField(max_length=64)
    office_name = models.CharField(max_length=100)
    company_code = models.CharField(max_length=64, blank=True, null=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'js_sys_employee-1'


class JsSysEmployeeOffice(models.Model):
    id = models.CharField(unique=True, max_length=64)
    emp_code = models.CharField(primary_key=True, max_length=64)
    office_code = models.CharField(max_length=64)
    post_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_employee_office'
        unique_together = (('emp_code', 'office_code'),)


class JsSysEmployeePost(models.Model):
    emp_code = models.CharField(primary_key=True, max_length=64)
    post_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_employee_post'
        unique_together = (('emp_code', 'post_code'),)


class JsSysFileEntity(models.Model):
    file_id = models.CharField(primary_key=True, max_length=64)
    file_md5 = models.CharField(max_length=64)
    file_path = models.CharField(max_length=1000)
    file_content_type = models.CharField(max_length=200)
    file_extension = models.CharField(max_length=100)
    file_size = models.DecimalField(max_digits=38, decimal_places=0)
    file_meta = models.CharField(max_length=255, blank=True, null=True)
    file_preview = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_file_entity'


class JsSysFileUpload(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    file_id = models.CharField(max_length=64)
    file_name = models.CharField(max_length=500)
    file_type = models.CharField(max_length=20)
    file_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    biz_key = models.CharField(max_length=64, blank=True, null=True)
    biz_type = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_file_upload'


class JsSysJob(models.Model):
    job_name = models.CharField(primary_key=True, max_length=64)
    job_group = models.CharField(max_length=64)
    description = models.CharField(max_length=100)
    invoke_target = models.CharField(max_length=1000)
    cron_expression = models.CharField(max_length=255)
    misfire_instruction = models.DecimalField(max_digits=1, decimal_places=0)
    concurrent = models.CharField(max_length=1)
    instance_name = models.CharField(max_length=64)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_job'
        unique_together = (('job_name', 'job_group'),)


class JsSysJobLog(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    job_name = models.CharField(max_length=64)
    job_group = models.CharField(max_length=64)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    job_event = models.CharField(max_length=200, blank=True, null=True)
    job_message = models.CharField(max_length=500, blank=True, null=True)
    is_exception = models.CharField(max_length=1, blank=True, null=True)
    exception_info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_job_log'


class JsSysLang(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    module_code = models.CharField(max_length=64)
    lang_code = models.CharField(max_length=500)
    lang_text = models.CharField(max_length=500)
    lang_type = models.CharField(max_length=50)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_lang'


class JsSysLog(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    log_type = models.CharField(max_length=50)
    log_title = models.CharField(max_length=500)
    create_by = models.CharField(max_length=64)
    create_by_name = models.CharField(max_length=100)
    create_date = models.DateTimeField()
    request_uri = models.CharField(max_length=500, blank=True, null=True)
    request_method = models.CharField(max_length=10, blank=True, null=True)
    request_params = models.TextField(blank=True, null=True)
    diff_modify_data = models.TextField(blank=True, null=True)
    biz_key = models.CharField(max_length=64, blank=True, null=True)
    biz_type = models.CharField(max_length=64, blank=True, null=True)
    remote_addr = models.CharField(max_length=255)
    server_addr = models.CharField(max_length=255)
    is_exception = models.CharField(max_length=1, blank=True, null=True)
    exception_info = models.TextField(blank=True, null=True)
    user_agent = models.CharField(max_length=500, blank=True, null=True)
    device_name = models.CharField(max_length=100, blank=True, null=True)
    browser_name = models.CharField(max_length=100, blank=True, null=True)
    execute_time = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'js_sys_log'


class JsSysMenu(models.Model):
    menu_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    menu_name = models.CharField(max_length=100)
    menu_type = models.CharField(max_length=1)
    menu_href = models.CharField(max_length=1000, blank=True, null=True)
    menu_target = models.CharField(max_length=20, blank=True, null=True)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    menu_color = models.CharField(max_length=50, blank=True, null=True)
    menu_title = models.CharField(max_length=100, blank=True, null=True)
    memu_title = models.CharField(max_length=100, blank=True, null=True)
    permission = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    is_show = models.CharField(max_length=1)
    sys_code = models.CharField(max_length=64)
    module_codes = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_menu'


class JsSysMenu1(models.Model):
    menu_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    menu_name = models.CharField(max_length=100)
    menu_type = models.CharField(max_length=1)
    menu_href = models.CharField(max_length=1000, blank=True, null=True)
    menu_target = models.CharField(max_length=20, blank=True, null=True)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    menu_color = models.CharField(max_length=50, blank=True, null=True)
    menu_title = models.CharField(max_length=100, blank=True, null=True)
    memu_title = models.CharField(max_length=100, blank=True, null=True)
    permission = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    is_show = models.CharField(max_length=1)
    sys_code = models.CharField(max_length=64)
    module_codes = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_menu1'


class JsSysMenu2(models.Model):
    menu_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    menu_name = models.CharField(max_length=100)
    menu_type = models.CharField(max_length=1)
    menu_href = models.CharField(max_length=1000, blank=True, null=True)
    menu_target = models.CharField(max_length=20, blank=True, null=True)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    menu_color = models.CharField(max_length=50, blank=True, null=True)
    menu_title = models.CharField(max_length=100, blank=True, null=True)
    memu_title = models.CharField(max_length=100, blank=True, null=True)
    permission = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    is_show = models.CharField(max_length=1)
    sys_code = models.CharField(max_length=64)
    module_codes = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_menu2'


class JsSysMenu5(models.Model):
    menu_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    menu_name = models.CharField(max_length=100)
    menu_type = models.CharField(max_length=1)
    menu_href = models.CharField(max_length=1000, blank=True, null=True)
    menu_target = models.CharField(max_length=20, blank=True, null=True)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    menu_color = models.CharField(max_length=50, blank=True, null=True)
    menu_title = models.CharField(max_length=100, blank=True, null=True)
    memu_title = models.CharField(max_length=100, blank=True, null=True)
    permission = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    is_show = models.CharField(max_length=1)
    sys_code = models.CharField(max_length=64)
    module_codes = models.CharField(max_length=500)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_menu5'


class JsSysModule(models.Model):
    module_code = models.CharField(primary_key=True, max_length=64)
    module_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    main_class_name = models.CharField(max_length=500, blank=True, null=True)
    current_version = models.CharField(max_length=50, blank=True, null=True)
    upgrade_info = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_module'


class JsSysMsgInner(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    msg_title = models.CharField(max_length=200)
    content_level = models.CharField(max_length=1)
    content_type = models.CharField(max_length=1, blank=True, null=True)
    msg_content = models.TextField()
    receive_type = models.CharField(max_length=1)
    receive_codes = models.TextField()
    receive_names = models.TextField()
    send_user_code = models.CharField(max_length=64)
    send_user_name = models.CharField(max_length=100)
    send_date = models.DateTimeField()
    is_attac = models.CharField(max_length=1, blank=True, null=True)
    notify_types = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_msg_inner'


class JsSysMsgInnerRecord(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    msg_inner_id = models.CharField(max_length=64)
    receive_user_code = models.CharField(max_length=64, blank=True, null=True)
    receive_user_name = models.CharField(max_length=100)
    read_status = models.CharField(max_length=1)
    read_date = models.DateTimeField(blank=True, null=True)
    is_star = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_msg_inner_record'


class JsSysMsgPush(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    msg_type = models.CharField(max_length=16)
    msg_title = models.CharField(max_length=200)
    msg_content = models.TextField()
    biz_key = models.CharField(max_length=64, blank=True, null=True)
    biz_type = models.CharField(max_length=64, blank=True, null=True)
    receive_code = models.CharField(max_length=64)
    receive_user_code = models.CharField(max_length=64)
    receive_user_name = models.CharField(max_length=100)
    send_user_code = models.CharField(max_length=64)
    send_user_name = models.CharField(max_length=100)
    send_date = models.DateTimeField()
    is_merge_push = models.CharField(max_length=1, blank=True, null=True)
    plan_push_date = models.DateTimeField(blank=True, null=True)
    push_number = models.IntegerField(blank=True, null=True)
    push_return_code = models.CharField(max_length=200, blank=True, null=True)
    push_return_msg_id = models.CharField(max_length=200, blank=True, null=True)
    push_return_content = models.TextField(blank=True, null=True)
    push_status = models.CharField(max_length=1, blank=True, null=True)
    push_date = models.DateTimeField(blank=True, null=True)
    read_status = models.CharField(max_length=1, blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_msg_push'


class JsSysMsgPushed(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    msg_type = models.CharField(max_length=16)
    msg_title = models.CharField(max_length=200)
    msg_content = models.TextField()
    biz_key = models.CharField(max_length=64, blank=True, null=True)
    biz_type = models.CharField(max_length=64, blank=True, null=True)
    receive_code = models.CharField(max_length=64)
    receive_user_code = models.CharField(max_length=64)
    receive_user_name = models.CharField(max_length=100)
    send_user_code = models.CharField(max_length=64)
    send_user_name = models.CharField(max_length=100)
    send_date = models.DateTimeField()
    is_merge_push = models.CharField(max_length=1, blank=True, null=True)
    plan_push_date = models.DateTimeField(blank=True, null=True)
    push_number = models.IntegerField(blank=True, null=True)
    push_return_content = models.TextField(blank=True, null=True)
    push_return_code = models.CharField(max_length=200, blank=True, null=True)
    push_return_msg_id = models.CharField(max_length=200, blank=True, null=True)
    push_status = models.CharField(max_length=1, blank=True, null=True)
    push_date = models.DateTimeField(blank=True, null=True)
    read_status = models.CharField(max_length=1, blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_msg_pushed'


class JsSysMsgTemplate(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    module_code = models.CharField(max_length=64, blank=True, null=True)
    tpl_key = models.CharField(max_length=100)
    tpl_name = models.CharField(max_length=100)
    tpl_type = models.CharField(max_length=16)
    tpl_content = models.TextField()
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_msg_template'


class JsSysOffice(models.Model):
    office_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    view_code = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    office_type = models.CharField(max_length=1)
    leader = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_office'





class JsSysOffice1(models.Model):
    office_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    view_code = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    office_type = models.CharField(max_length=1)
    leader = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_office1'


class JsSysPost(models.Model):
    post_code = models.CharField(primary_key=True, max_length=64)
    post_name = models.CharField(max_length=100)
    post_type = models.CharField(max_length=100, blank=True, null=True)
    post_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'js_sys_post'


class JsSysRole(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    role_name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100, blank=True, null=True)
    role_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_sys = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    data_scope = models.CharField(max_length=1, blank=True, null=True)
    biz_scope = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_role'


class JsSysRole1(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    role_name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100, blank=True, null=True)
    role_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_sys = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    data_scope = models.CharField(max_length=1, blank=True, null=True)
    biz_scope = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_role1'


class JsSysRole2(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    role_name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100, blank=True, null=True)
    role_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_sys = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    data_scope = models.CharField(max_length=1, blank=True, null=True)
    biz_scope = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_role2'


class JsSysRole5(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    role_name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100, blank=True, null=True)
    role_sort = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    is_sys = models.CharField(max_length=1, blank=True, null=True)
    user_type = models.CharField(max_length=16, blank=True, null=True)
    data_scope = models.CharField(max_length=1, blank=True, null=True)
    biz_scope = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=500, blank=True, null=True)
    extend_s3 = models.CharField(max_length=500, blank=True, null=True)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_role5'


class JsSysRoleDataScope(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_data_scope'
        unique_together = (('role_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysRoleDataScope1(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_data_scope1'
        unique_together = (('role_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysRoleDataScope2(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_data_scope2'
        unique_together = (('role_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysRoleMenu(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    menu_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_menu'
        unique_together = (('role_code', 'menu_code'),)


class JsSysRoleMenu1(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    menu_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_menu1'
        unique_together = (('role_code', 'menu_code'),)


class JsSysRoleMenu2(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    menu_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_menu2'
        unique_together = (('role_code', 'menu_code'),)


class JsSysRoleMenu5(models.Model):
    role_code = models.CharField(primary_key=True, max_length=64)
    menu_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_role_menu5'
        unique_together = (('role_code', 'menu_code'),)


class JsSysUser(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    login_code = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)
    wx_openid = models.CharField(max_length=100, blank=True, null=True)
    mobile_imei = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=16)
    ref_code = models.CharField(max_length=64, blank=True, null=True)
    ref_name = models.CharField(max_length=100, blank=True, null=True)
    mgr_type = models.CharField(max_length=1)
    pwd_security_level = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pwd_update_date = models.DateTimeField(blank=True, null=True)
    pwd_update_record = models.CharField(max_length=1000, blank=True, null=True)
    pwd_question = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_quest_update_date = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    freeze_date = models.DateTimeField(blank=True, null=True)
    freeze_cause = models.CharField(max_length=200, blank=True, null=True)
    user_weight = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=64)
    extend_s3 = models.CharField(max_length=500)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)
    recommend_code = models.CharField(max_length=64, blank=True, null=True)
    activation_status = models.IntegerField()
    islogin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_user'


class JsSysUser1(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    login_code = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)
    wx_openid = models.CharField(max_length=100, blank=True, null=True)
    mobile_imei = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=16)
    ref_code = models.CharField(max_length=64, blank=True, null=True)
    ref_name = models.CharField(max_length=100, blank=True, null=True)
    mgr_type = models.CharField(max_length=1)
    pwd_security_level = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pwd_update_date = models.DateTimeField(blank=True, null=True)
    pwd_update_record = models.CharField(max_length=1000, blank=True, null=True)
    pwd_question = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_quest_update_date = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    freeze_date = models.DateTimeField(blank=True, null=True)
    freeze_cause = models.CharField(max_length=200, blank=True, null=True)
    user_weight = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=64)
    extend_s3 = models.CharField(max_length=500)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)
    recommend_code = models.CharField(max_length=64, blank=True, null=True)
    activation_status = models.IntegerField()
    islogin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_user1'


class JsSysUser4(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    login_code = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)
    wx_openid = models.CharField(max_length=100, blank=True, null=True)
    mobile_imei = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=16)
    ref_code = models.CharField(max_length=64, blank=True, null=True)
    ref_name = models.CharField(max_length=100, blank=True, null=True)
    mgr_type = models.CharField(max_length=1)
    pwd_security_level = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pwd_update_date = models.DateTimeField(blank=True, null=True)
    pwd_update_record = models.CharField(max_length=1000, blank=True, null=True)
    pwd_question = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_quest_update_date = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    freeze_date = models.DateTimeField(blank=True, null=True)
    freeze_cause = models.CharField(max_length=200, blank=True, null=True)
    user_weight = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=64)
    extend_s3 = models.CharField(max_length=500)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)
    recommend_code = models.CharField(max_length=64, blank=True, null=True)
    activation_status = models.IntegerField()
    islogin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_user4'


class JsSysUserCopy(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    login_code = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)
    wx_openid = models.CharField(max_length=100, blank=True, null=True)
    mobile_imei = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=16)
    ref_code = models.CharField(max_length=64, blank=True, null=True)
    ref_name = models.CharField(max_length=100, blank=True, null=True)
    mgr_type = models.CharField(max_length=1)
    pwd_security_level = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    pwd_update_date = models.DateTimeField(blank=True, null=True)
    pwd_update_record = models.CharField(max_length=1000, blank=True, null=True)
    pwd_question = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_2 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_question_answer_3 = models.CharField(max_length=200, blank=True, null=True)
    pwd_quest_update_date = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=100, blank=True, null=True)
    last_login_date = models.DateTimeField(blank=True, null=True)
    freeze_date = models.DateTimeField(blank=True, null=True)
    freeze_cause = models.CharField(max_length=200, blank=True, null=True)
    user_weight = models.DecimalField(max_digits=8, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)
    corp_code = models.CharField(max_length=64)
    corp_name = models.CharField(max_length=100)
    extend_s1 = models.CharField(max_length=500, blank=True, null=True)
    extend_s2 = models.CharField(max_length=64)
    extend_s3 = models.CharField(max_length=500)
    extend_s4 = models.CharField(max_length=500, blank=True, null=True)
    extend_s5 = models.CharField(max_length=500, blank=True, null=True)
    extend_s6 = models.CharField(max_length=500, blank=True, null=True)
    extend_s7 = models.CharField(max_length=500, blank=True, null=True)
    extend_s8 = models.CharField(max_length=500, blank=True, null=True)
    extend_i1 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i2 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i3 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_i4 = models.DecimalField(max_digits=19, decimal_places=0, blank=True, null=True)
    extend_f1 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f2 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f3 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_f4 = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    extend_d1 = models.DateTimeField(blank=True, null=True)
    extend_d2 = models.DateTimeField(blank=True, null=True)
    extend_d3 = models.DateTimeField(blank=True, null=True)
    extend_d4 = models.DateTimeField(blank=True, null=True)
    recommend_code = models.CharField(max_length=64, blank=True, null=True)
    activation_status = models.IntegerField()
    islogin = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'js_sys_user_copy'


class JsSysUserDataScope(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_data_scope'
        unique_together = (('user_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysUserDataScope1(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_data_scope1'
        unique_together = (('user_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysUserDataScope2(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_data_scope2'
        unique_together = (('user_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysUserDataScopeCopy(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    ctrl_type = models.CharField(max_length=20)
    ctrl_data = models.CharField(max_length=64)
    ctrl_permi = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_data_scope_copy'
        unique_together = (('user_code', 'ctrl_type', 'ctrl_data', 'ctrl_permi'),)


class JsSysUserRole(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    role_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_role'
        unique_together = (('user_code', 'role_code'),)


class JsSysUserRole1(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    role_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_role1'
        unique_together = (('user_code', 'role_code'),)


class JsSysUserRole2(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    role_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_role2'
        unique_together = (('user_code', 'role_code'),)


class JsSysUserRole5(models.Model):
    user_code = models.CharField(primary_key=True, max_length=100)
    role_code = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'js_sys_user_role5'
        unique_together = (('user_code', 'role_code'),)


class PersonPicture(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    picture_name = models.CharField(max_length=50, blank=True, null=True)
    picture_url = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_picture'


class PersonTable1(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=100, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=100, blank=True, null=True)
    zw = models.CharField(max_length=100, blank=True, null=True)
    fxxldj = models.CharField(max_length=500, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=200, blank=True, null=True)
    zjzqk = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=200, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=200, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    zhy1 = models.CharField(max_length=100, blank=True, null=True)
    zhy2 = models.CharField(max_length=100, blank=True, null=True)
    zhy3 = models.CharField(max_length=100, blank=True, null=True)
    zhy4 = models.CharField(max_length=100, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    jba = models.CharField(max_length=50, blank=True, null=True)
    jbb = models.CharField(max_length=50, blank=True, null=True)
    jbc = models.CharField(max_length=50, blank=True, null=True)
    jbd = models.CharField(max_length=350, blank=True, null=True)
    jbe = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)
    temp11 = models.CharField(max_length=200, blank=True, null=True)
    temp12 = models.CharField(max_length=200, blank=True, null=True)
    temp13 = models.CharField(max_length=200, blank=True, null=True)
    temp14 = models.CharField(max_length=200, blank=True, null=True)
    temp15 = models.CharField(max_length=200, blank=True, null=True)
    temp16 = models.CharField(max_length=200, blank=True, null=True)
    temp17 = models.CharField(max_length=200, blank=True, null=True)
    temp18 = models.CharField(max_length=200, blank=True, null=True)
    temp19 = models.CharField(max_length=200, blank=True, null=True)
    temp20 = models.CharField(max_length=200, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)
    temp36 = models.CharField(max_length=200, blank=True, null=True)
    temp37 = models.CharField(max_length=200, blank=True, null=True)
    temp38 = models.CharField(max_length=200, blank=True, null=True)
    temp39 = models.CharField(max_length=200, blank=True, null=True)
    temp40 = models.CharField(max_length=200, blank=True, null=True)
    temp41 = models.CharField(max_length=200, blank=True, null=True)
    temp42 = models.CharField(max_length=200, blank=True, null=True)
    temp43 = models.CharField(max_length=200, blank=True, null=True)
    temp44 = models.CharField(max_length=200, blank=True, null=True)
    temp45 = models.CharField(max_length=200, blank=True, null=True)
    temp46 = models.CharField(max_length=200, blank=True, null=True)
    temp47 = models.CharField(max_length=200, blank=True, null=True)
    temp48 = models.CharField(max_length=200, blank=True, null=True)
    temp49 = models.CharField(max_length=200, blank=True, null=True)
    temp50 = models.CharField(max_length=200, blank=True, null=True)
    temp51 = models.CharField(max_length=200, blank=True, null=True)
    temp52 = models.CharField(max_length=200, blank=True, null=True)
    temp53 = models.CharField(max_length=200, blank=True, null=True)
    temp54 = models.CharField(max_length=200, blank=True, null=True)
    temp55 = models.CharField(max_length=1000, blank=True, null=True)
    temp56 = models.CharField(max_length=1000, blank=True, null=True)
    temp57 = models.CharField(max_length=1000, blank=True, null=True)
    temp58 = models.CharField(max_length=1000, blank=True, null=True)
    temp59 = models.CharField(max_length=1000, blank=True, null=True)
    temp60 = models.CharField(max_length=1000, blank=True, null=True)
    temp61 = models.CharField(max_length=200, blank=True, null=True)
    byzd1 = models.CharField(max_length=10, blank=True, null=True)
    byzd2 = models.CharField(max_length=10, blank=True, null=True)
    byzd3 = models.CharField(max_length=10, blank=True, null=True)
    byzd4 = models.CharField(max_length=10, blank=True, null=True)
    byzd5 = models.CharField(max_length=10, blank=True, null=True)
    byzd6 = models.CharField(max_length=10, blank=True, null=True)
    byzd7 = models.CharField(max_length=10, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table1'


class PersonTable11(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=200, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=200, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=200, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    bb = models.CharField(max_length=200, blank=True, null=True)
    zw = models.CharField(max_length=200, blank=True, null=True)
    fxxldj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=200, blank=True, null=True)
    zjzqk = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=200, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=200, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)
    temp11 = models.CharField(max_length=200, blank=True, null=True)
    temp12 = models.CharField(max_length=200, blank=True, null=True)
    temp13 = models.CharField(max_length=200, blank=True, null=True)
    temp14 = models.CharField(max_length=200, blank=True, null=True)
    temp15 = models.CharField(max_length=200, blank=True, null=True)
    temp16 = models.CharField(max_length=200, blank=True, null=True)
    temp17 = models.CharField(max_length=200, blank=True, null=True)
    temp18 = models.CharField(max_length=200, blank=True, null=True)
    temp19 = models.CharField(max_length=200, blank=True, null=True)
    temp20 = models.CharField(max_length=200, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table1-1'


class PersonTable12(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=200, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=200, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=200, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    bb = models.CharField(max_length=200, blank=True, null=True)
    zw = models.CharField(max_length=200, blank=True, null=True)
    fxxldj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=200, blank=True, null=True)
    zjzqk = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=200, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=200, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)
    temp11 = models.CharField(max_length=200, blank=True, null=True)
    temp12 = models.CharField(max_length=200, blank=True, null=True)
    temp13 = models.CharField(max_length=200, blank=True, null=True)
    temp14 = models.CharField(max_length=200, blank=True, null=True)
    temp15 = models.CharField(max_length=200, blank=True, null=True)
    temp16 = models.CharField(max_length=200, blank=True, null=True)
    temp17 = models.CharField(max_length=200, blank=True, null=True)
    temp18 = models.CharField(max_length=200, blank=True, null=True)
    temp19 = models.CharField(max_length=200, blank=True, null=True)
    temp20 = models.CharField(max_length=200, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table1-2'


class PersonTable10(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    csny = models.CharField(max_length=500, blank=True, null=True)
    runy = models.CharField(max_length=500, blank=True, null=True)
    xjxsj = models.CharField(max_length=500, blank=True, null=True)
    jg = models.CharField(max_length=500, blank=True, null=True)
    xl = models.CharField(max_length=500, blank=True, null=True)
    xx = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table10'


class PersonTable101(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=100, blank=True, null=True)
    csny = models.CharField(max_length=100, blank=True, null=True)
    runy = models.CharField(max_length=100, blank=True, null=True)
    xjxsj = models.CharField(max_length=100, blank=True, null=True)
    jg = models.CharField(max_length=100, blank=True, null=True)
    xl = models.CharField(max_length=100, blank=True, null=True)
    xx = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    temp1 = models.CharField(max_length=100, blank=True, null=True)
    temp2 = models.CharField(max_length=100, blank=True, null=True)
    temp3 = models.CharField(max_length=100, blank=True, null=True)
    temp4 = models.CharField(max_length=100, blank=True, null=True)
    temp5 = models.CharField(max_length=100, blank=True, null=True)
    zytype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table10-1'





class PersonTable111(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=100, blank=True, null=True)
    csny = models.CharField(max_length=100, blank=True, null=True)
    runy = models.CharField(max_length=100, blank=True, null=True)
    xjxsj = models.CharField(max_length=100, blank=True, null=True)
    jg = models.CharField(max_length=100, blank=True, null=True)
    xl = models.CharField(max_length=100, blank=True, null=True)
    xx = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    temp1 = models.CharField(max_length=100, blank=True, null=True)
    temp2 = models.CharField(max_length=100, blank=True, null=True)
    temp3 = models.CharField(max_length=100, blank=True, null=True)
    temp4 = models.CharField(max_length=100, blank=True, null=True)
    temp5 = models.CharField(max_length=100, blank=True, null=True)
    temp6 = models.CharField(max_length=100, blank=True, null=True)
    temp7 = models.CharField(max_length=100, blank=True, null=True)
    temp8 = models.CharField(max_length=100, blank=True, null=True)
    temp9 = models.CharField(max_length=100, blank=True, null=True)
    temp10 = models.CharField(max_length=100, blank=True, null=True)
    temp11 = models.CharField(max_length=100, blank=True, null=True)
    temp12 = models.CharField(max_length=100, blank=True, null=True)
    temp13 = models.CharField(max_length=100, blank=True, null=True)
    temp14 = models.CharField(max_length=100, blank=True, null=True)
    temp15 = models.CharField(max_length=100, blank=True, null=True)
    temp16 = models.CharField(max_length=100, blank=True, null=True)
    temp17 = models.CharField(max_length=100, blank=True, null=True)
    temp18 = models.CharField(max_length=100, blank=True, null=True)
    temp19 = models.CharField(max_length=100, blank=True, null=True)
    temp20 = models.CharField(max_length=100, blank=True, null=True)
    temp21 = models.CharField(max_length=100, blank=True, null=True)
    temp22 = models.CharField(max_length=100, blank=True, null=True)
    temp23 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table11-1'





class PersonTable13(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=200, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=200, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=200, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    bb = models.CharField(max_length=200, blank=True, null=True)
    zw = models.CharField(max_length=200, blank=True, null=True)
    fxxldj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=500, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=200, blank=True, null=True)
    zjzqk = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=200, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=200, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    zhy1 = models.CharField(max_length=50, blank=True, null=True)
    zhy2 = models.CharField(max_length=50, blank=True, null=True)
    zhy3 = models.CharField(max_length=50, blank=True, null=True)
    zhy4 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    jba = models.CharField(max_length=50, blank=True, null=True)
    jbb = models.CharField(max_length=50, blank=True, null=True)
    jbc = models.CharField(max_length=50, blank=True, null=True)
    jbd = models.CharField(max_length=50, blank=True, null=True)
    jbe = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)
    temp11 = models.CharField(max_length=200, blank=True, null=True)
    temp12 = models.CharField(max_length=200, blank=True, null=True)
    temp13 = models.CharField(max_length=200, blank=True, null=True)
    temp14 = models.CharField(max_length=200, blank=True, null=True)
    temp15 = models.CharField(max_length=200, blank=True, null=True)
    temp16 = models.CharField(max_length=200, blank=True, null=True)
    temp17 = models.CharField(max_length=200, blank=True, null=True)
    temp18 = models.CharField(max_length=200, blank=True, null=True)
    temp19 = models.CharField(max_length=200, blank=True, null=True)
    temp20 = models.CharField(max_length=200, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    byzd1 = models.CharField(max_length=200, blank=True, null=True)
    byzd2 = models.CharField(max_length=200, blank=True, null=True)
    byzd3 = models.CharField(max_length=200, blank=True, null=True)
    byzd4 = models.CharField(max_length=200, blank=True, null=True)
    byzd5 = models.CharField(max_length=200, blank=True, null=True)
    byzd6 = models.CharField(max_length=200, blank=True, null=True)
    byzd7 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table13'


class PersonTable15(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=200, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=200, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=200, blank=True, null=True)
    xm = models.CharField(max_length=200, blank=True, null=True)
    bb = models.CharField(max_length=200, blank=True, null=True)
    zw = models.CharField(max_length=200, blank=True, null=True)
    fxxldj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=200, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=200, blank=True, null=True)
    zjzqk = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=200, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=200, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=200, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=200, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=200, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=200, blank=True, null=True)
    bz = models.CharField(max_length=200, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    zhy1 = models.CharField(max_length=50, blank=True, null=True)
    zhy2 = models.CharField(max_length=50, blank=True, null=True)
    zhy3 = models.CharField(max_length=50, blank=True, null=True)
    zhy4 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    jba = models.CharField(max_length=50, blank=True, null=True)
    jbb = models.CharField(max_length=50, blank=True, null=True)
    jbc = models.CharField(max_length=50, blank=True, null=True)
    jbd = models.CharField(max_length=50, blank=True, null=True)
    jbe = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=500, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    temp11 = models.CharField(max_length=500, blank=True, null=True)
    temp12 = models.CharField(max_length=500, blank=True, null=True)
    temp13 = models.CharField(max_length=500, blank=True, null=True)
    temp14 = models.CharField(max_length=500, blank=True, null=True)
    temp15 = models.CharField(max_length=500, blank=True, null=True)
    temp16 = models.CharField(max_length=500, blank=True, null=True)
    temp17 = models.CharField(max_length=500, blank=True, null=True)
    temp18 = models.CharField(max_length=500, blank=True, null=True)
    temp19 = models.CharField(max_length=500, blank=True, null=True)
    temp20 = models.CharField(max_length=500, blank=True, null=True)
    temp21 = models.CharField(max_length=500, blank=True, null=True)
    temp22 = models.CharField(max_length=500, blank=True, null=True)
    temp23 = models.CharField(max_length=500, blank=True, null=True)
    temp24 = models.CharField(max_length=500, blank=True, null=True)
    temp25 = models.CharField(max_length=500, blank=True, null=True)
    temp26 = models.CharField(max_length=500, blank=True, null=True)
    temp27 = models.CharField(max_length=500, blank=True, null=True)
    temp28 = models.CharField(max_length=500, blank=True, null=True)
    temp29 = models.CharField(max_length=500, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table15'


class PersonTable2(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=500, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=500, blank=True, null=True)
    xm = models.CharField(max_length=500, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    zw = models.CharField(max_length=500, blank=True, null=True)
    fxxldj = models.CharField(max_length=500, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=500, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=500, blank=True, null=True)
    zjzqk = models.CharField(max_length=500, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=500, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=500, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=500, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=500, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=500, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=500, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=500, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=500, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=20, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=50, blank=True, null=True)
    temp6 = models.CharField(max_length=50, blank=True, null=True)
    temp7 = models.CharField(max_length=50, blank=True, null=True)
    temp8 = models.CharField(max_length=50, blank=True, null=True)
    temp9 = models.CharField(max_length=50, blank=True, null=True)
    temp10 = models.CharField(max_length=50, blank=True, null=True)
    temp11 = models.CharField(max_length=50, blank=True, null=True)
    temp12 = models.CharField(max_length=50, blank=True, null=True)
    temp13 = models.CharField(max_length=50, blank=True, null=True)
    temp14 = models.CharField(max_length=50, blank=True, null=True)
    temp15 = models.CharField(max_length=50, blank=True, null=True)
    temp16 = models.CharField(max_length=50, blank=True, null=True)
    temp17 = models.CharField(max_length=50, blank=True, null=True)
    temp18 = models.CharField(max_length=50, blank=True, null=True)
    temp19 = models.CharField(max_length=50, blank=True, null=True)
    temp20 = models.CharField(max_length=50, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)
    zhy1 = models.CharField(max_length=50, blank=True, null=True)
    zhy2 = models.CharField(max_length=50, blank=True, null=True)
    zhy3 = models.CharField(max_length=50, blank=True, null=True)
    zhy4 = models.CharField(max_length=50, blank=True, null=True)
    jba = models.CharField(max_length=50, blank=True, null=True)
    jbb = models.CharField(max_length=50, blank=True, null=True)
    jbc = models.CharField(max_length=300, blank=True, null=True)
    jbd = models.CharField(max_length=50, blank=True, null=True)
    jbe = models.CharField(max_length=300, blank=True, null=True)
    temp36 = models.CharField(max_length=200, blank=True, null=True)
    temp37 = models.CharField(max_length=200, blank=True, null=True)
    temp38 = models.CharField(max_length=200, blank=True, null=True)
    temp39 = models.CharField(max_length=200, blank=True, null=True)
    temp40 = models.CharField(max_length=200, blank=True, null=True)
    temp41 = models.CharField(max_length=200, blank=True, null=True)
    temp42 = models.CharField(max_length=200, blank=True, null=True)
    temp43 = models.CharField(max_length=200, blank=True, null=True)
    temp44 = models.CharField(max_length=200, blank=True, null=True)
    temp45 = models.CharField(max_length=200, blank=True, null=True)
    temp46 = models.CharField(max_length=200, blank=True, null=True)
    temp47 = models.CharField(max_length=200, blank=True, null=True)
    temp48 = models.CharField(max_length=200, blank=True, null=True)
    temp49 = models.CharField(max_length=200, blank=True, null=True)
    temp50 = models.CharField(max_length=200, blank=True, null=True)
    temp51 = models.CharField(max_length=200, blank=True, null=True)
    temp52 = models.CharField(max_length=200, blank=True, null=True)
    temp53 = models.CharField(max_length=200, blank=True, null=True)
    temp54 = models.CharField(max_length=200, blank=True, null=True)
    temp55 = models.CharField(max_length=200, blank=True, null=True)
    temp56 = models.CharField(max_length=200, blank=True, null=True)
    temp57 = models.CharField(max_length=200, blank=True, null=True)
    temp58 = models.CharField(max_length=200, blank=True, null=True)
    temp59 = models.CharField(max_length=200, blank=True, null=True)
    temp60 = models.CharField(max_length=1000, blank=True, null=True)
    temp61 = models.CharField(max_length=1000, blank=True, null=True)
    byzd1 = models.CharField(max_length=50, blank=True, null=True)
    byzd2 = models.CharField(max_length=50, blank=True, null=True)
    byzd3 = models.CharField(max_length=50, blank=True, null=True)
    byzd4 = models.CharField(max_length=50, blank=True, null=True)
    byzd5 = models.CharField(max_length=50, blank=True, null=True)
    byzd6 = models.CharField(max_length=50, blank=True, null=True)
    byzd7 = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table2'


class PersonTable21(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=50, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    zw = models.CharField(max_length=50, blank=True, null=True)
    fxxldj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=50, blank=True, null=True)
    zjzqk = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=50, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=50, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=20, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=50, blank=True, null=True)
    temp6 = models.CharField(max_length=50, blank=True, null=True)
    temp7 = models.CharField(max_length=50, blank=True, null=True)
    temp8 = models.CharField(max_length=50, blank=True, null=True)
    temp9 = models.CharField(max_length=50, blank=True, null=True)
    temp10 = models.CharField(max_length=50, blank=True, null=True)
    temp11 = models.CharField(max_length=50, blank=True, null=True)
    temp12 = models.CharField(max_length=50, blank=True, null=True)
    temp13 = models.CharField(max_length=50, blank=True, null=True)
    temp14 = models.CharField(max_length=50, blank=True, null=True)
    temp15 = models.CharField(max_length=50, blank=True, null=True)
    temp16 = models.CharField(max_length=50, blank=True, null=True)
    temp17 = models.CharField(max_length=50, blank=True, null=True)
    temp18 = models.CharField(max_length=50, blank=True, null=True)
    temp19 = models.CharField(max_length=50, blank=True, null=True)
    temp20 = models.CharField(max_length=50, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table2-1'


class PersonTable22(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=50, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    zw = models.CharField(max_length=50, blank=True, null=True)
    fxxldj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=50, blank=True, null=True)
    zjzqk = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=50, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=50, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=20, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=50, blank=True, null=True)
    temp6 = models.CharField(max_length=50, blank=True, null=True)
    temp7 = models.CharField(max_length=50, blank=True, null=True)
    temp8 = models.CharField(max_length=1350, blank=True, null=True)
    temp9 = models.CharField(max_length=1350, blank=True, null=True)
    temp10 = models.CharField(max_length=1350, blank=True, null=True)
    temp11 = models.CharField(max_length=50, blank=True, null=True)
    temp12 = models.CharField(max_length=50, blank=True, null=True)
    temp13 = models.CharField(max_length=50, blank=True, null=True)
    temp14 = models.CharField(max_length=50, blank=True, null=True)
    temp15 = models.CharField(max_length=50, blank=True, null=True)
    temp16 = models.CharField(max_length=50, blank=True, null=True)
    temp17 = models.CharField(max_length=50, blank=True, null=True)
    temp18 = models.CharField(max_length=50, blank=True, null=True)
    temp19 = models.CharField(max_length=50, blank=True, null=True)
    temp20 = models.CharField(max_length=50, blank=True, null=True)
    temp21 = models.CharField(max_length=200, blank=True, null=True)
    temp22 = models.CharField(max_length=200, blank=True, null=True)
    temp23 = models.CharField(max_length=200, blank=True, null=True)
    temp24 = models.CharField(max_length=200, blank=True, null=True)
    temp25 = models.CharField(max_length=200, blank=True, null=True)
    temp26 = models.CharField(max_length=200, blank=True, null=True)
    temp27 = models.CharField(max_length=200, blank=True, null=True)
    temp28 = models.CharField(max_length=200, blank=True, null=True)
    temp29 = models.CharField(max_length=200, blank=True, null=True)
    temp30 = models.CharField(max_length=200, blank=True, null=True)
    temp31 = models.CharField(max_length=200, blank=True, null=True)
    temp32 = models.CharField(max_length=200, blank=True, null=True)
    temp33 = models.CharField(max_length=200, blank=True, null=True)
    temp34 = models.CharField(max_length=200, blank=True, null=True)
    temp35 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table2-2'


class PersonTable23(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=99, blank=True, null=True)
    fjxh_fjlb = models.CharField(max_length=60, blank=True, null=True)
    fjxh_jtxh = models.CharField(max_length=60, blank=True, null=True)
    xm = models.CharField(max_length=60, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    zw = models.CharField(max_length=50, blank=True, null=True)
    fxxldj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_zsj = models.CharField(max_length=50, blank=True, null=True)
    fxsj_xsj = models.CharField(max_length=50, blank=True, null=True)
    zjzqk = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_dj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_sj = models.CharField(max_length=50, blank=True, null=True)
    lhyxjl_mc = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_sj = models.CharField(max_length=50, blank=True, null=True)
    wyrwjl_mc = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_sj = models.CharField(max_length=50, blank=True, null=True)
    sdxljl_mc = models.CharField(max_length=50, blank=True, null=True)
    jcqk_sj = models.CharField(max_length=50, blank=True, null=True)
    jcqk_mc = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=20, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=500, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    temp11 = models.CharField(max_length=500, blank=True, null=True)
    temp12 = models.CharField(max_length=500, blank=True, null=True)
    temp13 = models.CharField(max_length=500, blank=True, null=True)
    temp14 = models.CharField(max_length=500, blank=True, null=True)
    temp15 = models.CharField(max_length=500, blank=True, null=True)
    temp16 = models.CharField(max_length=500, blank=True, null=True)
    temp17 = models.CharField(max_length=500, blank=True, null=True)
    temp18 = models.CharField(max_length=500, blank=True, null=True)
    temp19 = models.CharField(max_length=500, blank=True, null=True)
    temp20 = models.CharField(max_length=500, blank=True, null=True)
    temp21 = models.CharField(max_length=500, blank=True, null=True)
    temp22 = models.CharField(max_length=500, blank=True, null=True)
    temp23 = models.CharField(max_length=500, blank=True, null=True)
    temp24 = models.CharField(max_length=500, blank=True, null=True)
    temp25 = models.CharField(max_length=500, blank=True, null=True)
    temp26 = models.CharField(max_length=500, blank=True, null=True)
    temp27 = models.CharField(max_length=500, blank=True, null=True)
    temp28 = models.CharField(max_length=500, blank=True, null=True)
    temp29 = models.CharField(max_length=500, blank=True, null=True)
    temp30 = models.CharField(max_length=500, blank=True, null=True)
    temp31 = models.CharField(max_length=500, blank=True, null=True)
    temp32 = models.CharField(max_length=500, blank=True, null=True)
    temp33 = models.CharField(max_length=500, blank=True, null=True)
    temp34 = models.CharField(max_length=500, blank=True, null=True)
    temp35 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=500, blank=True, null=True)  # Field name made lowercase.
    zhy1 = models.CharField(max_length=500, blank=True, null=True)
    zhy2 = models.CharField(max_length=500, blank=True, null=True)
    zhy3 = models.CharField(max_length=500, blank=True, null=True)
    zhy4 = models.CharField(max_length=500, blank=True, null=True)
    jba = models.CharField(max_length=500, blank=True, null=True)
    jbb = models.CharField(max_length=500, blank=True, null=True)
    jbc = models.CharField(max_length=500, blank=True, null=True)
    jbd = models.CharField(max_length=500, blank=True, null=True)
    jbe = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table2-3'


class PersonTable3(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=500, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=500, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=500, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=500, blank=True, null=True)
    zylb = models.CharField(max_length=500, blank=True, null=True)
    jtmk = models.CharField(max_length=500, blank=True, null=True)
    qtmk = models.CharField(max_length=500, blank=True, null=True)
    spsj = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=999, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table3'


class PersonTable31(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=50, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=50, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=50, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=50, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=50, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=50, blank=True, null=True)
    zylb = models.CharField(max_length=50, blank=True, null=True)
    jtmk = models.CharField(max_length=50, blank=True, null=True)
    qtmk = models.CharField(max_length=50, blank=True, null=True)
    spsj = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table3-1'


class PersonTable35(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=500, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=500, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=500, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=500, blank=True, null=True)
    zylb = models.CharField(max_length=500, blank=True, null=True)
    jtmk = models.CharField(max_length=500, blank=True, null=True)
    qtmk = models.CharField(max_length=500, blank=True, null=True)
    spsj = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=500, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table35'


class PersonTable4(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=500, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    zyly = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    xzjsj = models.CharField(max_length=500, blank=True, null=True)
    xl_jg = models.CharField(max_length=500, blank=True, null=True)
    pxjl = models.CharField(max_length=500, blank=True, null=True)
    gzjl = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=999, blank=True, null=True)
    temp7 = models.CharField(max_length=999, blank=True, null=True)
    temp8 = models.CharField(max_length=500, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table4'


class PersonTable41(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=50, blank=True, null=True)
    zyly = models.CharField(max_length=50, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=50, blank=True, null=True)
    xzjsj = models.CharField(max_length=50, blank=True, null=True)
    xl_jg = models.CharField(max_length=50, blank=True, null=True)
    pxjl = models.CharField(max_length=50, blank=True, null=True)
    gzjl = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table4-1'


class PersonTable45(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    zyly = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    xzjsj = models.CharField(max_length=500, blank=True, null=True)
    xl_jg = models.CharField(max_length=500, blank=True, null=True)
    pxjl = models.CharField(max_length=500, blank=True, null=True)
    gzjl = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=500, blank=True, null=True)
    temp9 = models.CharField(max_length=500, blank=True, null=True)
    temp10 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table45'


class PersonTable5(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    yz = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    xzjsj = models.CharField(max_length=500, blank=True, null=True)
    sl_jg = models.CharField(max_length=500, blank=True, null=True)
    pxjl = models.CharField(max_length=500, blank=True, null=True)
    gzjl = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=600, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    temp6 = models.CharField(max_length=500, blank=True, null=True)
    temp7 = models.CharField(max_length=500, blank=True, null=True)
    temp8 = models.CharField(max_length=1350, blank=True, null=True)
    temp9 = models.CharField(max_length=1350, blank=True, null=True)
    temp10 = models.CharField(max_length=1350, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table5'


class PersonTable51(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=50, blank=True, null=True)
    yz = models.CharField(max_length=50, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=50, blank=True, null=True)
    xzjsj = models.CharField(max_length=50, blank=True, null=True)
    sl_jg = models.CharField(max_length=50, blank=True, null=True)
    pxjl = models.CharField(max_length=50, blank=True, null=True)
    gzjl = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=200, blank=True, null=True)
    temp2 = models.CharField(max_length=200, blank=True, null=True)
    temp3 = models.CharField(max_length=200, blank=True, null=True)
    temp4 = models.CharField(max_length=200, blank=True, null=True)
    temp5 = models.CharField(max_length=200, blank=True, null=True)
    temp6 = models.CharField(max_length=200, blank=True, null=True)
    temp7 = models.CharField(max_length=200, blank=True, null=True)
    temp8 = models.CharField(max_length=200, blank=True, null=True)
    temp9 = models.CharField(max_length=200, blank=True, null=True)
    temp10 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table5-1'


class PersonTable6(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    lgsj = models.CharField(max_length=500, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=500, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=500, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=500, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=500, blank=True, null=True)
    zylb = models.CharField(max_length=500, blank=True, null=True)
    jtmk = models.CharField(max_length=500, blank=True, null=True)
    qtmk = models.CharField(max_length=500, blank=True, null=True)
    spsj = models.CharField(max_length=500, blank=True, null=True)
    gzz_lxfs = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table6'


class PersonTable61(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=50, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=50, blank=True, null=True)
    lgsj = models.CharField(max_length=50, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=50, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=50, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=50, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=50, blank=True, null=True)
    zylb = models.CharField(max_length=50, blank=True, null=True)
    jtmk = models.CharField(max_length=50, blank=True, null=True)
    qtmk = models.CharField(max_length=50, blank=True, null=True)
    spsj = models.CharField(max_length=50, blank=True, null=True)
    gzz_lxfs = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table6-1'


class PersonTable63(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=50, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=50, blank=True, null=True)
    lgsj = models.CharField(max_length=50, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=50, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=50, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=50, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=50, blank=True, null=True)
    zylb = models.CharField(max_length=50, blank=True, null=True)
    jtmk = models.CharField(max_length=50, blank=True, null=True)
    qtmk = models.CharField(max_length=50, blank=True, null=True)
    spsj = models.CharField(max_length=50, blank=True, null=True)
    gzz_lxfs = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table6-3'


class PersonTable65(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bzb = models.CharField(max_length=500, blank=True, null=True)
    cssj_rwsj = models.CharField(max_length=500, blank=True, null=True)
    lgsj = models.CharField(max_length=500, blank=True, null=True)
    xl_byyx_zy = models.CharField(max_length=500, blank=True, null=True)
    jszw_spsj = models.CharField(max_length=500, blank=True, null=True)
    jsdj_sj = models.CharField(max_length=500, blank=True, null=True)
    sywh_zbxh = models.CharField(max_length=500, blank=True, null=True)
    zylb = models.CharField(max_length=500, blank=True, null=True)
    jtmk = models.CharField(max_length=500, blank=True, null=True)
    qtmk = models.CharField(max_length=500, blank=True, null=True)
    spsj = models.CharField(max_length=500, blank=True, null=True)
    gzz_lxfs = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table65'


class PersonTable7(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=500, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    gw = models.CharField(max_length=500, blank=True, null=True)
    csny = models.CharField(max_length=500, blank=True, null=True)
    runy = models.CharField(max_length=500, blank=True, null=True)
    jx = models.CharField(max_length=500, blank=True, null=True)
    jg = models.CharField(max_length=500, blank=True, null=True)
    whcd = models.CharField(max_length=500, blank=True, null=True)
    sfh = models.CharField(max_length=500, blank=True, null=True)
    pxqk_zsj = models.CharField(max_length=500, blank=True, null=True)
    pxqk_fg = models.CharField(max_length=500, blank=True, null=True)
    pxqk_lj = models.CharField(max_length=500, blank=True, null=True)
    pxqk_kjh = models.CharField(max_length=500, blank=True, null=True)
    pxqk_uyt = models.CharField(max_length=500, blank=True, null=True)
    pxqk_xsj = models.CharField(max_length=500, blank=True, null=True)
    zjzqk = models.CharField(max_length=500, blank=True, null=True)
    zqk = models.CharField(max_length=500, blank=True, null=True)
    zjz = models.CharField(max_length=500, blank=True, null=True)
    qk_sj = models.CharField(max_length=500, blank=True, null=True)
    qk_mc = models.CharField(max_length=500, blank=True, null=True)
    qs = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    qk_sj1 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj2 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj3 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj4 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj5 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table7'


class PersonTable71(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    gw = models.CharField(max_length=50, blank=True, null=True)
    csny = models.CharField(max_length=50, blank=True, null=True)
    runy = models.CharField(max_length=50, blank=True, null=True)
    jx = models.CharField(max_length=50, blank=True, null=True)
    jg = models.CharField(max_length=50, blank=True, null=True)
    whcd = models.CharField(max_length=50, blank=True, null=True)
    sfh = models.CharField(max_length=50, blank=True, null=True)
    pxqk_zsj = models.CharField(max_length=50, blank=True, null=True)
    pxqk_fg = models.CharField(max_length=50, blank=True, null=True)
    pxqk_lj = models.CharField(max_length=50, blank=True, null=True)
    pxqk_kjh = models.CharField(max_length=50, blank=True, null=True)
    pxqk_uyt = models.CharField(max_length=50, blank=True, null=True)
    pxqk_xsj = models.CharField(max_length=50, blank=True, null=True)
    zjzqk = models.CharField(max_length=50, blank=True, null=True)
    zqk = models.CharField(max_length=50, blank=True, null=True)
    zjz = models.CharField(max_length=50, blank=True, null=True)
    qk_sj = models.CharField(max_length=50, blank=True, null=True)
    qk_mc = models.CharField(max_length=50, blank=True, null=True)
    qs = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    qk_sj1 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj2 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj3 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj4 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj5 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table7-1'


class PersonTable73(models.Model):
    id = models.BigAutoField(primary_key=True)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    gw = models.CharField(max_length=50, blank=True, null=True)
    csny = models.CharField(max_length=50, blank=True, null=True)
    runy = models.CharField(max_length=50, blank=True, null=True)
    jx = models.CharField(max_length=50, blank=True, null=True)
    jg = models.CharField(max_length=50, blank=True, null=True)
    whcd = models.CharField(max_length=50, blank=True, null=True)
    sfh = models.CharField(max_length=50, blank=True, null=True)
    pxqk_zsj = models.CharField(max_length=50, blank=True, null=True)
    pxqk_fg = models.CharField(max_length=50, blank=True, null=True)
    pxqk_lj = models.CharField(max_length=50, blank=True, null=True)
    pxqk_kjh = models.CharField(max_length=50, blank=True, null=True)
    pxqk_uyt = models.CharField(max_length=50, blank=True, null=True)
    pxqk_xsj = models.CharField(max_length=50, blank=True, null=True)
    zjzqk = models.CharField(max_length=50, blank=True, null=True)
    zqk = models.CharField(max_length=50, blank=True, null=True)
    zjz = models.CharField(max_length=50, blank=True, null=True)
    qk_sj = models.CharField(max_length=50, blank=True, null=True)
    qk_mc = models.CharField(max_length=50, blank=True, null=True)
    qs = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    qk_sj1 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj2 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj3 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj4 = models.CharField(max_length=50, blank=True, null=True)
    qk_sj5 = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table7-3'


class PersonTable75(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=500, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    gw = models.CharField(max_length=500, blank=True, null=True)
    csny = models.CharField(max_length=500, blank=True, null=True)
    runy = models.CharField(max_length=500, blank=True, null=True)
    jx = models.CharField(max_length=500, blank=True, null=True)
    jg = models.CharField(max_length=500, blank=True, null=True)
    whcd = models.CharField(max_length=500, blank=True, null=True)
    sfh = models.CharField(max_length=500, blank=True, null=True)
    pxqk_zsj = models.CharField(max_length=500, blank=True, null=True)
    pxqk_fg = models.CharField(max_length=500, blank=True, null=True)
    pxqk_lj = models.CharField(max_length=500, blank=True, null=True)
    pxqk_kjh = models.CharField(max_length=500, blank=True, null=True)
    pxqk_uyt = models.CharField(max_length=500, blank=True, null=True)
    pxqk_xsj = models.CharField(max_length=500, blank=True, null=True)
    zjzqk = models.CharField(max_length=500, blank=True, null=True)
    zqk = models.CharField(max_length=500, blank=True, null=True)
    zjz = models.CharField(max_length=500, blank=True, null=True)
    qk_sj = models.CharField(max_length=500, blank=True, null=True)
    qk_mc = models.CharField(max_length=500, blank=True, null=True)
    qs = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    qk_sj1 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj2 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj3 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj4 = models.CharField(max_length=500, blank=True, null=True)
    qk_sj5 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table75'


class PersonTable8(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    csny = models.CharField(max_length=500, blank=True, null=True)
    runy = models.CharField(max_length=500, blank=True, null=True)
    xjxsj = models.CharField(max_length=500, blank=True, null=True)
    jg = models.CharField(max_length=500, blank=True, null=True)
    xl = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table8'


class PersonTable81(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    csny = models.CharField(max_length=50, blank=True, null=True)
    runy = models.CharField(max_length=50, blank=True, null=True)
    xjxsj = models.CharField(max_length=50, blank=True, null=True)
    jg = models.CharField(max_length=50, blank=True, null=True)
    xl = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table8-1'


class PersonTable83(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=50, blank=True, null=True)
    xm = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=50, blank=True, null=True)
    csny = models.CharField(max_length=50, blank=True, null=True)
    runy = models.CharField(max_length=50, blank=True, null=True)
    xjxsj = models.CharField(max_length=50, blank=True, null=True)
    jg = models.CharField(max_length=50, blank=True, null=True)
    xl = models.CharField(max_length=50, blank=True, null=True)
    bz = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table8-3'


class PersonTable9(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    zytype = models.CharField(max_length=50, blank=True, null=True)
    bb = models.CharField(max_length=500, blank=True, null=True)
    csny = models.CharField(max_length=500, blank=True, null=True)
    runy = models.CharField(max_length=500, blank=True, null=True)
    xjxsj = models.CharField(max_length=500, blank=True, null=True)
    jg = models.CharField(max_length=500, blank=True, null=True)
    xl = models.CharField(max_length=500, blank=True, null=True)
    xx = models.CharField(max_length=500, blank=True, null=True)
    bz = models.CharField(max_length=500, blank=True, null=True)
    temp1 = models.CharField(max_length=500, blank=True, null=True)
    temp2 = models.CharField(max_length=500, blank=True, null=True)
    temp3 = models.CharField(max_length=500, blank=True, null=True)
    temp4 = models.CharField(max_length=500, blank=True, null=True)
    temp5 = models.CharField(max_length=500, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_table9'


class PersonTable91(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=100, blank=True, null=True)
    csny = models.CharField(max_length=100, blank=True, null=True)
    runy = models.CharField(max_length=100, blank=True, null=True)
    xjxsj = models.CharField(max_length=100, blank=True, null=True)
    jg = models.CharField(max_length=100, blank=True, null=True)
    xl = models.CharField(max_length=100, blank=True, null=True)
    xx = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    temp1 = models.CharField(max_length=100, blank=True, null=True)
    temp2 = models.CharField(max_length=100, blank=True, null=True)
    temp3 = models.CharField(max_length=100, blank=True, null=True)
    temp4 = models.CharField(max_length=100, blank=True, null=True)
    temp5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table9-1'


class PersonTable92(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    xh = models.CharField(max_length=100, blank=True, null=True)
    xm = models.CharField(max_length=100, blank=True, null=True)
    bb = models.CharField(max_length=100, blank=True, null=True)
    csny = models.CharField(max_length=100, blank=True, null=True)
    runy = models.CharField(max_length=100, blank=True, null=True)
    xjxsj = models.CharField(max_length=100, blank=True, null=True)
    jg = models.CharField(max_length=100, blank=True, null=True)
    xl = models.CharField(max_length=100, blank=True, null=True)
    xx = models.CharField(max_length=100, blank=True, null=True)
    bz = models.CharField(max_length=100, blank=True, null=True)
    temp1 = models.CharField(max_length=100, blank=True, null=True)
    temp2 = models.CharField(max_length=100, blank=True, null=True)
    temp3 = models.CharField(max_length=100, blank=True, null=True)
    temp4 = models.CharField(max_length=100, blank=True, null=True)
    temp5 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_table9-2'


class Sconfiguration(models.Model):
    dwname = models.CharField(db_column='DWNAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    sysmd5 = models.TextField(db_column='SYSMD5', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sconfiguration'


class TestData(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    test_input = models.CharField(max_length=200, blank=True, null=True)
    test_textarea = models.CharField(max_length=200, blank=True, null=True)
    test_select = models.CharField(max_length=10, blank=True, null=True)
    test_select_multiple = models.CharField(max_length=200, blank=True, null=True)
    test_radio = models.CharField(max_length=10, blank=True, null=True)
    test_checkbox = models.CharField(max_length=200, blank=True, null=True)
    test_date = models.DateTimeField(blank=True, null=True)
    test_datetime = models.DateTimeField(blank=True, null=True)
    test_user_code = models.CharField(max_length=64, blank=True, null=True)
    test_office_code = models.CharField(max_length=64, blank=True, null=True)
    test_area_code = models.CharField(max_length=64, blank=True, null=True)
    test_area_name = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_data'


class TestDataChild(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    test_sort = models.IntegerField(blank=True, null=True)
    test_data_id = models.CharField(max_length=64, blank=True, null=True)
    test_input = models.CharField(max_length=200, blank=True, null=True)
    test_textarea = models.CharField(max_length=200, blank=True, null=True)
    test_select = models.CharField(max_length=10, blank=True, null=True)
    test_select_multiple = models.CharField(max_length=200, blank=True, null=True)
    test_radio = models.CharField(max_length=10, blank=True, null=True)
    test_checkbox = models.CharField(max_length=200, blank=True, null=True)
    test_date = models.DateTimeField(blank=True, null=True)
    test_datetime = models.DateTimeField(blank=True, null=True)
    test_user_code = models.CharField(max_length=64, blank=True, null=True)
    test_office_code = models.CharField(max_length=64, blank=True, null=True)
    test_area_code = models.CharField(max_length=64, blank=True, null=True)
    test_area_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_data_child'


class TestTree(models.Model):
    tree_code = models.CharField(primary_key=True, max_length=64)
    parent_code = models.CharField(max_length=64)
    parent_codes = models.CharField(max_length=1000)
    tree_sort = models.DecimalField(max_digits=10, decimal_places=0)
    tree_sorts = models.CharField(max_length=1000)
    tree_leaf = models.CharField(max_length=1)
    tree_level = models.DecimalField(max_digits=4, decimal_places=0)
    tree_names = models.CharField(max_length=1000)
    tree_name = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    create_by = models.CharField(max_length=64)
    create_date = models.DateTimeField()
    update_by = models.CharField(max_length=64)
    update_date = models.DateTimeField()
    remarks = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_tree'


class YkFlowmeter202106(models.Model):
    flowmeter_id = models.AutoField(primary_key=True)
    flowmeter_bh = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_name = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_traffic = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_density = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_temper = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_vflow = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_atraffic = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_vtotal = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_sj = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_flowmeter_2021_06'


class YkFlowmeter202107(models.Model):
    flowmeter_id = models.AutoField(primary_key=True)
    flowmeter_bh = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_name = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_traffic = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_density = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_temper = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_vflow = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_atraffic = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_vtotal = models.CharField(max_length=50, blank=True, null=True)
    flowmeter_sj = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_flowmeter_2021_07'


class YkRefueling202107(models.Model):
    refueling_id = models.CharField(primary_key=True, max_length=50)
    refueling_oil = models.CharField(max_length=50, blank=True, null=True)
    refueling_type = models.CharField(max_length=50, blank=True, null=True)
    refueling_name = models.CharField(max_length=50, blank=True, null=True)
    refueling_balance = models.CharField(max_length=50, blank=True, null=True)
    refueling_carnum = models.CharField(max_length=50, blank=True, null=True)
    refueling_unit = models.CharField(max_length=50, blank=True, null=True)
    refueling_addtime = models.CharField(max_length=50, blank=True, null=True)
    refueling_yllb = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yk_refueling_2021_07'


class YwCommun(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    commun_dw = models.CharField(max_length=50, blank=True, null=True)
    commun_zw = models.CharField(max_length=50, blank=True, null=True)
    commun_xm = models.CharField(max_length=50, blank=True, null=True)
    commun_dh = models.CharField(max_length=50, blank=True, null=True)
    commun_sj = models.CharField(max_length=50, blank=True, null=True)
    commun_bz = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=50, blank=True, null=True)
    tboffic_code = models.CharField(db_column='tbOffic_code', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yw_commun'


class YwDdmc(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    placename = models.CharField(max_length=50, blank=True, null=True)
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yw_ddmc'


class YwDwmc(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    orgid = models.CharField(db_column='orgID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='orgName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    areaid = models.CharField(max_length=50, blank=True, null=True)
    areaname = models.CharField(max_length=50, blank=True, null=True)
    taskname = models.CharField(max_length=50, blank=True, null=True)
    tasknum = models.CharField(max_length=50, blank=True, null=True)
    groupname = models.CharField(max_length=50, blank=True, null=True)
    companyname = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    leftmark = models.CharField(max_length=50, blank=True, null=True)
    topmark = models.CharField(max_length=50, blank=True, null=True)
    leftmarkbig = models.CharField(max_length=50, blank=True, null=True)
    topmarkbig = models.CharField(max_length=50, blank=True, null=True)
    starttime = models.CharField(max_length=50, blank=True, null=True)
    endtime = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    note = models.CharField(max_length=100, blank=True, null=True)
    backup1 = models.CharField(max_length=50, blank=True, null=True)
    backup2 = models.CharField(max_length=50, blank=True, null=True)
    backup3 = models.CharField(max_length=50, blank=True, null=True)
    backup4 = models.CharField(max_length=50, blank=True, null=True)
    isshow = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yw_dwmc'


class YwNotice(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    notice_tilte = models.CharField(max_length=500, blank=True, null=True)
    notice_img = models.CharField(max_length=500, blank=True, null=True)
    notice_sj = models.CharField(max_length=50, blank=True, null=True)
    notice_nr = models.CharField(max_length=5000, blank=True, null=True)
    notice_dw = models.CharField(max_length=50, blank=True, null=True)
    notice_jb = models.CharField(max_length=50, blank=True, null=True)
    notice_ry = models.CharField(max_length=50, blank=True, null=True)
    temp1 = models.CharField(max_length=50, blank=True, null=True)
    temp2 = models.CharField(max_length=50, blank=True, null=True)
    temp3 = models.CharField(max_length=50, blank=True, null=True)
    temp4 = models.CharField(max_length=50, blank=True, null=True)
    temp5 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yw_notice'


class YwRwbs(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    areaid = models.CharField(max_length=50, blank=True, null=True)
    areaname = models.CharField(max_length=50, blank=True, null=True)
    taskname = models.CharField(max_length=50, blank=True, null=True)
    tasknum = models.CharField(max_length=50, blank=True, null=True)
    marshallnum = models.CharField(max_length=50, blank=True, null=True)
    marshallname = models.CharField(max_length=50, blank=True, null=True)
    companynum = models.CharField(max_length=50, blank=True, null=True)
    companyname = models.CharField(max_length=50, blank=True, null=True)
    troops = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)
    officer = models.CharField(max_length=50, blank=True, null=True)
    soldiers = models.CharField(max_length=50, blank=True, null=True)
    civilian = models.CharField(max_length=50, blank=True, null=True)
    instructor = models.CharField(max_length=100, blank=True, null=True)
    air = models.CharField(max_length=50, blank=True, null=True)
    team = models.CharField(max_length=50, blank=True, null=True)
    backbone = models.CharField(max_length=50, blank=True, null=True)
    talents = models.CharField(max_length=50, blank=True, null=True)
    downsizing = models.CharField(max_length=50, blank=True, null=True)
    sj = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    leader = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    task = models.CharField(max_length=50, blank=True, null=True)
    taskplan = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    backup1 = models.CharField(max_length=50, blank=True, null=True)
    backup2 = models.CharField(max_length=50, blank=True, null=True)
    backup3 = models.CharField(max_length=50, blank=True, null=True)
    backup4 = models.CharField(max_length=50, blank=True, null=True)
    isshow = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yw_rwbs'
