from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def get_date_range(yyMM, _format='%Y-%m-%d %H:%M:%S', output='str', day_safety=0):
    """
    
    
    
    """
    
    if day_safety == 0:
        month_start = datetime.strptime(yyMM, '%Y%m') + relativedelta(days=0)
        month_end = month_start + relativedelta(months=1) + relativedelta(seconds=-1) + relativedelta(days=0)
    else:
        month_start_zero = datetime.strptime(yyMM, '%Y%m') + relativedelta(days=0)
        month_start = datetime.strptime(yyMM, '%Y%m') + relativedelta(days=-day_safety)
        month_end = month_start_zero + relativedelta(months=1) + relativedelta(seconds=-1) + relativedelta(days=day_safety)

    if output == 'str':
        return month_start.strftime(_format), month_end.strftime(_format)
    elif output == 'datetime':
        return month_start, month_end
    else:
        return 'Please assgn a valid value to output paremeter' 

