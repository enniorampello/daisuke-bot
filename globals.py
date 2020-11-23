from numpy.core.numeric import NaN
import pandas as pd

lectures = [] #list of lists (1 per day) of tuples in the format (lecture_name, lecture_duration (in minutes), lecture_color, is_uploaded)
subject_paths = {
        'sap': '/html/body/div[3]/div[1]/div[1]/div[3]/div/table/tbody/tr[3]/td[2]/a',
        'os': '/html/body/div[3]/div[1]/div[1]/div[3]/div/table/tbody/tr[5]/td[2]/a',
        'estm': '/html/body/div[3]/div[1]/div[1]/div[3]/div/table/tbody/tr[7]/td[2]/a',
        'cn': '/html/body/div[3]/div[1]/div[1]/div[3]/div/table/tbody/tr[8]/td[2]/a'
    }

#each row is a day of week Mon-Sat. To access it use schedule.iloc[i].dropna()
schedule = pd.DataFrame([
    {'cn': (4, 2), 'estm': (3, 1), 'sap': (4, 1)},
    {'cn': (4, 2), 'estm': (4, 1)},
    {'estm': (2, 1), 'sap': (5, 1), 'sap': (6, 1)},
    {'cn': (3, 2), 'sap': (3, 1)},
    {'sap': (2, 1), 'estm': (3, 1), 'os': (3, 1)},
    {'os': (3, 1), 'estm': (3, 2)}
])