from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def get_yyMM_range(yyMM, day_safety):
    """_summary_

    Args:
        yyMM (_type_): _description_
        day_safety (_type_): _description_

    Returns:
        _type_: _description_
    """
    yyMM = sorted(yyMM)
    if len(yyMM) == 2:
        range_yyMM = get_date_range(yyMM[0], _format='%Y-%m-%d', output='str', day_safety=day_safety)[0], \
            get_date_range(yyMM[1], _format='%Y-%m-%d', output='str', day_safety=day_safety)[1]
        return range_yyMM
    elif len(yyMM) == 1:
        range_yyMM = get_date_range(yyMM[0], _format='%Y-%m-%d', output='str', day_safety=day_safety)[0]
        return range_yyMM
    else:
        return 'Please assign a valid yyMM quantity/value to output parameter'

def get_date_range(yyMM, _format='%Y-%m-%d %H:%M:%S', output='str', day_safety=0):
    """_summary_

    Args:
        yyMM (_type_): _description_
        _format (str, optional): _description_. Defaults to '%Y-%m-%d %H:%M:%S'.
        output (str, optional): _description_. Defaults to 'str'.
        day_safety (int, optional): _description_. Defaults to 0.

    Returns:
        _type_: _description_
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

